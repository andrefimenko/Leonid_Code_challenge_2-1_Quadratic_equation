from django.db import models


class Equation(models.Model):
    a = models.FloatField()
    b = models.FloatField()
    c = models.FloatField()

    root1 = models.FloatField(null=True, blank=True)
    root2 = models.FloatField(null=True, blank=True)
