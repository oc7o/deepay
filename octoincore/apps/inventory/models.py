from django.conf import settings
from django.db import models
from django.utils.text import slugify
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey, TreeManyToManyField

from octoincore.apps.users.models import ExtendUser
from octoincore.models import OctoModel

################
### Managers ###
################


class ProductInventoryManager(models.Manager):
    def get_queryset(self):
        return (
            super().get_queryset().filter(is_active=True)
        )  # ProductInventoryManager, self


##############
### Models ###
##############
class Category(MPTTModel, OctoModel):
    """
    Inventory Category table implemented with MPTT
    """

    name = models.CharField(
        max_length=100,
        null=False,
        unique=False,
        blank=False,
        verbose_name=_("category name"),
        help_text=_("format: required, max-100"),
    )

    slug = models.SlugField(
        max_length=150,
        null=False,
        unique=True,
        blank=False,
        verbose_name=_("category safe URL"),
        help_text=_("format: required, letters, numbers, underscore or hyphens"),
        default=slugify(name),
    )

    is_active = models.BooleanField(default=True)

    parent = TreeForeignKey(
        "self",
        on_delete=models.PROTECT,
        related_name="children",
        null=True,
        blank=True,
        unique=False,
        verbose_name=_("parent of category"),
        help_text=_("format: not required"),
    )

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("product category")
        verbose_name_plural = _("product categories")

    def __str__(self) -> str:
        return self.name


class Product(OctoModel):
    """
    Product details table
    """

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="products"
    )

    name = models.CharField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("product name"),
        help_text=_("format: required, max-255"),
    )
    description = models.TextField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("product description"),
        help_text=_("format: required"),
    )
    category = TreeManyToManyField(Category)
    is_active = models.BooleanField(
        unique=False,
        null=False,
        blank=False,
        default=True,
        verbose_name=_("product visibility"),
        help_text=_("format: true=product visible"),
    )

    def __str__(self):
        return self.name


class ProductAttribute(OctoModel):
    """
    Product attribute table
    """

    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("product attribute name"),
        help_text=_("format: required, unique, max-255"),
    )
    description = models.TextField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("product attribute description"),
        help_text=_("format: required"),
    )

    def __str__(self):
        return self.name


class ProductType(OctoModel):
    """
    Product type table
    """

    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("type of product"),
        help_text=_("format: required, unique, max-255"),
    )

    product_type_attributes = models.ManyToManyField(
        ProductAttribute,
        related_name="product_type_attributes",
        through="ProductTypeAttribute",
    )

    def __str__(self):
        return self.name


class Brand(OctoModel):
    """
    Product brand table
    """

    name = models.CharField(
        max_length=255,
        unique=True,
        null=False,
        blank=False,
        verbose_name=_("brand name"),
        help_text=_("format: required, unique, max-255"),
    )

    def __str__(self):
        return self.name


class ProductAttributeValue(OctoModel):
    """
    Product attribute value table
    """

    product_attribute = models.ForeignKey(
        ProductAttribute,
        related_name="product_attribute",
        on_delete=models.PROTECT,
    )
    attribute_value = models.CharField(
        max_length=255,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("attribute value"),
        help_text=_("format: required, max-255"),
    )

    def __str__(self):
        return f"{self.product_attribute.name} : {self.attribute_value}"


class ProductInventory(OctoModel):
    """
    Product inventory table
    """

    sku = models.CharField(
        max_length=20,
        unique=True,
        null=True,  # False
        blank=True,  # False
        verbose_name=_("stock keeping unit"),
        help_text=_("format: required, unique, max-20"),
    )
    upc = models.CharField(
        max_length=12,
        unique=True,
        null=True,  # False
        blank=True,  # False
        verbose_name=_("universal product code"),
        help_text=_("format: required, unique, max-12"),
    )
    product_type = models.ForeignKey(
        ProductType, related_name="inventories", on_delete=models.PROTECT
    )
    product = models.ForeignKey(
        Product, related_name="inventories", on_delete=models.PROTECT
    )
    describing_keyword = models.CharField(
        blank=True,
        null=True,
        max_length=255,
        verbose_name=_("keyword describing product"),
        help_text=_("max-255"),
    )
    brand = models.ForeignKey(
        Brand,
        related_name="inventries",
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        default=None,
    )
    attribute_values = models.ManyToManyField(
        ProductAttributeValue,
        related_name="inventories",
        through="ProductAttributeValues",
    )
    is_active = models.BooleanField(
        default=True,
        verbose_name=_("product visibility"),
        help_text=_("format: true=product visible"),
    )
    is_default = models.BooleanField(
        default=False,
        verbose_name=_("product selection"),
        help_text=_("format: true=sub product visible"),
    )
    retail_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        unique=False,
        null=True,
        blank=True,
        verbose_name=_("recommended retail price"),
        help_text=_("format: maximum price 999.99"),
        error_messages={
            "name": {
                "max_length": _("the price must be between 0 and 999.99."),
            },
        },
    )  # Preis den unsere Kunden an uns bezahlen müssen
    store_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("regular store price"),
        help_text=_("format: maximum price 999.99"),
        error_messages={
            "name": {
                "max_length": _("the price must be between 0 and 999.99."),
            },
        },
    )  # Preis den wir dafür bezahlen
    sale_price = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        unique=False,
        null=True,
        blank=True,
        verbose_name=_("sale price"),
        help_text=_("format: maximum price 999.99"),
        error_messages={
            "name": {
                "max_length": _("the price must be between 0 and 999.99."),
            },
        },
    )
    weight = models.FloatField(
        unique=False,
        null=True,
        blank=True,
        verbose_name=_("product weight"),
    )

    # products = ProductInventoryManager()

    def __str__(self):
        return f"{self.product.name}: {self.describing_keyword}"

    class Meta:
        unique_together = ("product", "describing_keyword")


class Media(OctoModel):
    """
    The product image table.
    """

    product_inventory = models.ForeignKey(
        ProductInventory,
        on_delete=models.PROTECT,
        related_name="media_files",
    )
    image = models.ImageField(
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("product image"),
        upload_to="uploads/product_images/",
        default="/static/defaults/placeholder.png",
        help_text=_("format: required, default-default.png"),
    )
    alt_text = models.CharField(
        max_length=255,
        unique=False,
        null=True,
        blank=True,
        verbose_name=_("alternative text"),
        help_text=_("format: required, max-255"),
    )
    is_feature = models.BooleanField(
        default=False,
        verbose_name=_("product default image"),
        help_text=_("format: default=false, true=default image"),
    )

    def __str__(self):
        return self.alt_text

    class Meta:
        verbose_name = _("product image")
        verbose_name_plural = _("product images")


class Stock(OctoModel):
    product_inventory = models.OneToOneField(
        ProductInventory,
        related_name="stock",
        on_delete=models.PROTECT,
    )
    last_checked = models.DateTimeField(
        unique=False,
        null=True,
        blank=True,
        verbose_name=_("inventory stock check date"),
        help_text=_("format: Y-m-d H:M:S, null-true, blank-true"),
    )
    units = models.IntegerField(
        default=0,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("units/qty of stock"),
        help_text=_("format: required, default-0"),
    )
    units_sold = models.IntegerField(
        default=0,
        unique=False,
        null=False,
        blank=False,
        verbose_name=_("units sold to date"),
        help_text=_("format: required, default-0"),
    )

    def __str__(self):
        return f"{self.product_inventory} - {self.units}"


class ProductAttributeValues(models.Model):
    """
    Product attribute values link table
    """

    attributevalues = models.ForeignKey(
        "ProductAttributeValue",
        related_name="attributevalues",
        on_delete=models.PROTECT,
    )
    productinventory = models.ForeignKey(
        ProductInventory,
        related_name="productattributevalues",
        on_delete=models.PROTECT,
    )

    def __str__(self) -> str:
        return f"{self.attributevalues} - {self.productinventory}"

    class Meta:
        unique_together = (("attributevalues", "productinventory"),)


class ProductTypeAttribute(models.Model):
    """
    Product type attributes link table
    """

    product_attribute = models.ForeignKey(
        ProductAttribute,
        related_name="productattribute",
        on_delete=models.PROTECT,
    )
    product_type = models.ForeignKey(
        ProductType,
        related_name="producttype",
        on_delete=models.PROTECT,
    )

    class Meta:
        unique_together = (("product_attribute", "product_type"),)
