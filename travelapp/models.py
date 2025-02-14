from django.db import models
from taggit.managers import TaggableManager

class Post(models.Model):
    Postname=models.CharField(max_length=50)
    travelappphoto=models.ImageField(blank=True,null=True,upload_to="images/")
    publishedDate=models.DateTimeField(blank=True,null=True)
    modifiedDate=models.DateTimeField(blank=True,null=True)
    contents = models.TextField()
    tag = TaggableManager(blank=True)

    def __str__(self):
        return self.Postname
    
class Video(models.Model):
    caption=models.CharField(max_length=100)
    video=models.FileField(upload_to="video/")
    def __str__(self):
        return self.caption