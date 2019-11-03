from django.db import models
from core import models as core_model

# Create your models here.


class Conversation(core_model.TimeStampedModel):
    participants = models.ManyToManyField(
        "users.User", related_name="converstation", blank=True
    )

    def __self__(self):
        return str(self.created)


class Message(core_model.TimeStampedModel):
    message = models.TextField()
    user = models.ForeignKey(
        "users.User", related_name="messages", on_delete=models.CASCADE
    )
    conversation = models.ForeignKey(
        "Conversation", related_name="messages", on_delete=models.CASCADE
    )

    def __self__(self):
        return f"{self.user} says : {self.text}"
