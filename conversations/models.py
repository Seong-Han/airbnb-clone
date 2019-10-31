from django.db import models
from core import models as core_model

# Create your models here.


class Conversation(core_model.TimeStampedModel):
    participant = models.ManyToManyField("users.User", blank=True)

    def __self__(self):
        return str(self.created)


class Message(core_model.TimeStampedModel):
    message = models.TextField()
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    conversation = models.ForeignKey("Conversation", on_delete=models.CASCADE)

    def __self__(self):
        return f"{self.user} says : {self.text}"
