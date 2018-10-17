from django.db import models

class File_Model(models.Model):
    title = models.CharField(max_length=50)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/')
