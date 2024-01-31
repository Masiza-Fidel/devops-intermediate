from django.db import models



# models.py

class Shoe(models.Model):
    SHOE_TYPES = (
        ('loafers', 'Loafers'),
        ('sneakers', 'Sneakers'),
        ('official', 'Official'),
        ('sandals', 'Sandals'),
        ('boots', 'Boots'),
        ('casual', 'Casual'),
    )

    type = models.CharField(max_length=10, choices=SHOE_TYPES, default='loafers')
    brand = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='shoe_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.type} - {self.brand}"
