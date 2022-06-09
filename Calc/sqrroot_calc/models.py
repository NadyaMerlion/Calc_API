from django.db import models

import cmath


class Number(models.Model):
    a = models.IntegerField()
    b = models.IntegerField()
    c = models.IntegerField()
    root1 = models.CharField(max_length=20)
    root2 = models.CharField(max_length=20)

    def __str__(self):
        return self.name


# @property
# def result(self):
#     a = self.a
#     b = self.b
#     c = self.c
#     discrement = (b**2) - (4 * a*c)
#     root1 = (-b-cmath.sqrt(discrement))/(2 * a)
#     root2 = (-b + cmath.sqrt(discrement))/(2 * a)
#     root1.save()
#     root2.save()
#     return root1, root2


@property
def root1(self):
    a = self.a
    b = self.b
    c = self.c
    discrement = (b**2) - (4 * a*c)
    root1 = (-b-cmath.sqrt(discrement))/(2 * a)
    return root1

@property
def root2(self):
    a = self.a
    b = self.b
    c = self.c
    discrement = (b**2) - (4 * a*c)
    root2 = (-b + cmath.sqrt(discrement))/(2 * a)
    return root2

def save(self, *args, **kwargs):
    self.root1 = self.root1
    self.root2 = self.root2
    super(Number, self).save(*args, **kwargs)


# class Result(models.Model):
#     root1 = models.IntegerField()
#     root2 = models.IntegerField()

#     def __str__(self):
#         return self.name