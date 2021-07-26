from django.db import models

# Create your models here.
class contact(models.Model):
    sno = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    message = models.CharField(max_length=150)
    datatime = models.DateTimeField(auto_now_add=True,blank=True)


    def __str__(self):
        return 'Message from' + self.username + ' - ' + self.email