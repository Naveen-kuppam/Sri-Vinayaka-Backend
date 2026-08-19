from django.db import models


class Vinayaka(models.Model):
    Name = models.CharField(max_length=200)
    Amount = models.CharField(max_length=100)
    Phone = models.CharField(max_length=20)
    SenderNumber = models.CharField(max_length=20)

    updatedAt = models.DateTimeField(
        auto_now=True
    )

    def __str__(self):
        return self.Name