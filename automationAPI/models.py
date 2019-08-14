from django.db import models

class appointments(models.Model):
    token = models.IntegerField()
    userid = models.CharField(max_length=500)
    name = models.CharField(max_length=200)
    department = models.CharField(max_length=500)
    date = models.DateField() # models.DateField(default=datetime.now)



    def __str__(self):
        return 'user_id: ' + self.userid + '\ntoken: ' + self.token + '\n' + '\nname: ' + self.name + '\n'
