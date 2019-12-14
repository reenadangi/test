from django.db import models

# Create your models here.
class showsManager(models.Manager):
    def valid_show(self,postData):
        errors={}
        if len(postData['title'])<2:
           errors["short"]="Show name should be more than 2 char"

        return errors

class shows(models.Model):
    title=models.CharField(max_length=255)
    network=models.CharField(max_length=255)
    release_date=models.DateField(auto_now=False)
    desc=models.TextField()
    poster = models.ImageField(default='default.jpg',upload_to='images')
    objects=showsManager()
