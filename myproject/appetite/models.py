from django.db import models

class ShoeCategory(models.TextChoices):
    LOAFERS = 'loafers', 'Loafers'
    SNEAKERS = 'sneakers', 'Sneakers'
    OFFICIAL = 'official', 'Official'
    SANDALS = 'sandals', 'Sandals'
    BOOTS = 'boots', 'Boots'
    CASUAL = 'casual', 'Casual'

class Shoe(models.Model):
    category = models.CharField(
        max_length=20,
        choices=ShoeCategory.choices,
        default=ShoeCategory.CASUAL,
    )
    brand = models.CharField(max_length=100)
    model_name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField()
    is_featured = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.brand} {self.model_name}"

class ShoeImage(models.Model):
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='shoe_images/')

class ShoeVideo(models.Model):
    shoe = models.ForeignKey(Shoe, on_delete=models.CASCADE)
    video = models.FileField(upload_to='shoe_videos/')
