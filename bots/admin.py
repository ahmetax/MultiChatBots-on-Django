from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import Bot, Category


@admin.register(Bot)
class BotAdmin(ImportExportModelAdmin):
    pass

@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    pass
