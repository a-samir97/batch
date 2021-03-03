from django.db import models


class Batch(models.Model):
    SIZE_TYPES = (
        ('S', 'Small'),
        ('M', 'Medium'),
        ('L', 'Large'),
        ('XL', 'X Large')
    )

    COLORS_TYPES = (
        ('R', 'Red'),
        ('BE', 'Blue'),
        ('BK', 'Black'),
        ('G', 'Green')
    )

    size = models.CharField(choices=SIZE_TYPES, default='S', max_length=2)
    color = models.CharField(choices=COLORS_TYPES, default='R', max_length=2)
    quantity = models.PositiveIntegerField()