from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.


@admin.register(models.User)  # decorator는 클래스 위에 있어야 작동한다.
class CustomUserAdmin(UserAdmin):
    """ Custom User Admin """

    fieldsets = UserAdmin.fieldsets + (
        (
            "Custom profile",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )
    ## UserAdmin을 적기만 하면 우리가 model에 적었던 게 반영이 안됨
    ## fieldsets라는 걸 만들어서 반영시켜줘야 한다.
    ## UserAdmin의 fieldset을 추가하기 위해 UserAdmin.fieldsets 를 해줌
