from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=30)
    Title = models.CharField(max_length=30)
    description = models.TextField()
    user = models.ForeignKey( on_delete=models.CASCADE)
    field_name = models.DateTimeField()
    userPic = models.Imagefield(max_length=20, null=True)

    def __str__(self):
        return self.name