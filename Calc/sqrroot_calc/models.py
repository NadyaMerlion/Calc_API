from django.db import models


class Number(models.Model):
    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()
    root1 = models.FloatField()
    root2 = models.FloatField()

    def __str__(self):
        return self.name
