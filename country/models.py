from django.db import models
from accounts.models import CustomUser
from django.urls import reverse

class Country(models.Model):
    name=models.CharField(max_length=255, null=False, blank=True)
    author=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    desc=models.TextField()


    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('country_list')    


