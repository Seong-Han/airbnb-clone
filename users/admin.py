from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.User)  # decorator는 클래스 위에 있어야 작동한다.
class CustomUserAdmin(admin.ModelAdmin):
    """ Custom User Admin """

    list_display = ("username", "gender", "language", "currency", "superhost")
    # 메인 화면에 뜰 것을 정의하는 옵션
    list_filter = ("superhost",)
    ## 메인 화면에서 어떤 걸 필터링 할 것이니?
