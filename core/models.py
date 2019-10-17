from django.db import models

# Create your models here.


class TimeStampedModel(models.Model):
    """ Time Stamped Model """

    created = models.DateTimeField(auto_now_add=True)  ## 자동으로 현재 시간을 입력해줌
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ## database로 업데이트 하지 않기 위해 만드는 것?
        abstract = True
