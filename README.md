### Generate Class Overview

1. `pip install django-extensions`
2. Add `django_extensions` to `INSTALLED_APPS` in `settings.py`
3. (Mac OS): `brew install graphviz`
4. `python manage.py graph_models -a --dot -o myapp_models.dot`
5. `dot -Tpng myapp_models.dot -omyapp_models.png`

### Dev

`npm run tailwind-watch`
