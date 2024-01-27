from django.contrib import admin

from search import models as search_models

admin.site.register(search_models.Video)
