from .models import ServerSettings

default_settings = {
    ""
}

for attribute in default_settings:
    ServerSettings.objects.create(attribute=attribute, value=default_settings[attribute])