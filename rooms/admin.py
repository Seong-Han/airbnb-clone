from django.contrib import admin
from . import models


@admin.register(models.RoomType, models.HouseRule, models.Facility, models.Amenity)
class ItemAdmin(admin.ModelAdmin):
    pass


# Register your models here.
@admin.register(models.Room)
class RoomAdmin(admin.ModelAdmin):

    fieldsets = (
        (
            "Basic Info",
            {"fields": ("name", "description", "country", "address", "price")},
        ),
        ("Times", {"fields": ("check_in", "check_out", "instant_book")}),
        ("Spaces", {"fields": ("guests", "beds", "bedrooms", "baths")}),
        (
            "More About the Space",
            {
                "classes": ("collapse",),
                "fields": ("amenities", "facilities", "house_rules"),
            },
        ),
        ("Last Details", {"fields": ("host",)}),
    )

    list_display = (
        "name",
        "country",
        "city",
        "price",
        "guests",
        "beds",
        "bedrooms",
        "baths",
        "check_in",
        "check_out",
        "instant_book",
    )
    list_filter = ["instant_book", "city", "country"]

    search_fields = ["=city", "^host__username"]

    filter_horizontal = ("amenity", "facility", "house_rules")
    # manytomany관계에서 사용함


@admin.register(models.Photo)
class PhotoAdmin(admin.ModelAdmin):
    pass

