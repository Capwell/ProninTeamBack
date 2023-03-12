from django.contrib import admin
from offers.models import Offer


class OfferAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'communicate',
    ]


admin.site.register(Offer, OfferAdmin)
