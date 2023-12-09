import os

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand
from django.core.management.commands import loaddata


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        call_command("makemigrations")
        call_command("migrate")

        call_command("loaddata", "db_user_fixture.json")
        call_command("loaddata", "db_brand_fixture.json")
        call_command("loaddata", "db_category_fixture.json")
        call_command("loaddata", "db_product_type_fixture.json")
        call_command("loaddata", "db_product_fixture.json")
        call_command("loaddata", "db_inventory_fixture.json")
        call_command("loaddata", "db_media_fixture.json")

        call_command("loaddata", "db_product_attribute_fixture.json")
        call_command("loaddata", "db_product_attribute_value_fixture.json")
        call_command("loaddata", "db_product_attribute_values_fixture.json")
