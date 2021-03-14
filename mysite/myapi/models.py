from django.db import models

# Create your models here.
class Organization(models.Model):
    name = models.CharField(max_length=60)
    county = models.CharField(max_length=60)
    ein = models.IntegerField()

    def __str__(self):
        return self.name

class Profile(models.Model):
    name = models.CharField(max_length=60)
    email = models.CharField(max_length=60)
    org = models.ForeignKey(Organization, on_delete=models.CASCADE)

    def __str__(self):
        return self.name