from django.conf import settings
from django_selectel_storage import storage


class StaticFilesStorage(storage.SelectelStorage):
    def __init__(self, *args, **kwargs):
        super().__init__(settings.SELECTEL_STATICFILES_STORAGE_URL)


