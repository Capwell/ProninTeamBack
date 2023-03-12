from cases.models import Case
from django.contrib import admin


class CaseAdmin(admin.ModelAdmin):
    list_display = [
        'title',
        'is_on_main_page',
        'is_visible',
    ]


admin.site.register(Case, CaseAdmin)
