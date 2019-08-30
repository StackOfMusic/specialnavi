from django.db import models

# Create your models here.


class Policeoffice(models.Model):
    police_name = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.police_name


class Guns(models.Model):
    police = models.ForeignKey(Policeoffice, on_delete=models.CASCADE)
    gun_name = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.gun_name


class Guns_detail(models.Model):
    gun = models.ForeignKey(Guns, on_delete=models.CASCADE)
    gun_type = models.CharField(max_length=5, blank=True)
    gun_owner = models.CharField(max_length=3, blank=True)
    gun_age = models.CharField(max_length=4, blank=True)

