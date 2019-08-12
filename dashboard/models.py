from django.db import models

class userdb(models.Model):
    uname = models.CharField(max_length=200)
    passwd = models.CharField(max_length=500)
    temp_key = models.CharField(max_length=500)
    def __str__(self):
        return self.uname + '\n' + self.temp_key


class noname(models.Model):
     sequence = models.ForeignKey(userdb, on_delete=models.CASCADE)
     img_urls = models.ImageField(max_length=1000, null=True, blank=True)


     def __str__(self):
         return str(self.img_urls)