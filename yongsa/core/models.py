from django.db import models


# Create your models here.
class Hero(models.Model):
    name = models.CharField(max_length=20)
    gold = models.IntegerField(default=1000)
    atk = models.IntegerField()

    def __str__(self):
        return f"{self.name}"


class Monster(models.Model):
    name = models.CharField(max_length=50, default='몬스터')
    atk = models.IntegerField()

    def __str__(self):
        return f"{self.name} {self.atk}"
