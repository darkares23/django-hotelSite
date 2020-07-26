from django.db import models

# Create your models here.


class ContactDetail(models.Model):
    # location =
    email = models.EmailField(null=False)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return str(self.id)
