from django.db import models


class Spotlight(models.Model):
    name = models.CharField(max_length=200)
    food_image = models.ImageField(upload_to="tasks/images")
    fod_name = models.CharField(max_length=220, blank=True,null=True)
    price = models.CharField(max_length=50)


    class Meta:
        db_table = 'food_spotlights'


    def __str__(self):
        return self.name


