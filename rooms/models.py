from django.db import models
from django_countries.fields import CountryField
from core import models as core_models

## 원래 여기에 바로 created, updated를 만들어줬늕데 어떤 이유에서(왜 그런지 이해 못함, 4.0강의)
## core로 분리하고 클래스를 불러오는 방법을 택함
from users import models as user_models

## 모듈을 불러올 때도 순서가 있음
## python pakages => django => 내가 만든 거


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Item """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class RoomType(AbstractItem):
    pass


class Amenity(AbstractItem):
    pass


class Facility(AbstractItem):
    pass


class HouseRule(AbstractItem):
    pass


class Room(core_models.TimeStampedModel):
    """ Room Model Definitions """

    name = models.CharField(max_length=140)
    description = models.TextField()
    country = CountryField()
    city = models.CharField(max_length=80)
    price = models.IntegerField()
    address = models.CharField(max_length=140)
    guests = models.IntegerField()
    beds = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    check_in = models.TimeField()
    check_out = models.TimeField()
    instant_book = models.BooleanField(default=False)
    host = models.ForeignKey(user_models.User, on_delete=models.CASCADE)
    ## host는 다른 user과 연결되야 한다.
    room_type = models.ForeignKey(RoomType, on_delete=models.SET_NULL, null=True)
    amenity = models.ManyToManyField(Amenity)
    facility = models.ManyToManyField(Facility)
    house_rules = models.ManyToManyField(HouseRule)

    def __str__(self):
        return self.name
