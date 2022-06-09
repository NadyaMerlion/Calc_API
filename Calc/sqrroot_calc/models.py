from django.db import models


class Number(models.Model):
    a = models.IntegerField()
    b = models.IntegerField()
    c = models.IntegerField()
    # root1 = models.IntegerField(null=True, blank=True)
    # root2 = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.name
