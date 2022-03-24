from django.db import models
# Create your models here.


class ArchivePhoto(models.Model):
    title = models.CharField(max_length=50, null = False, blank = False)
    media = models.CharField(max_length=100, null=False, blank= False)

    def __str__(self):
        return self.title

class ArchiveVideo(models.Model):
    title = models.CharField(max_length=50, null = False, blank = False)
    media = models.CharField(max_length=100,null=False, blank= False)

    def __str__(self):
        return self.title

class ArchiveAudio(models.Model):
    title = models.CharField(max_length=50, null = False, blank = False)
    media = models.CharField(max_length=100, null=False, blank= False)

    def __str__(self):
        return self.title



