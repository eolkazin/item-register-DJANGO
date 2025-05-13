from django.db import models

class Login_user(models.Model):
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    def __str__(self):
        return self.username


class Item(models.Model):
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    location = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)


    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'code'], name='unique_item_name_code')
        ]

    def __str__(self):
        return self.name
