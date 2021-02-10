from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


class User(models.Model):
    alphanumeric = RegexValidator(r'^[0-9A-Z]*$',
                                  'Only alphanumeric characters are allowed.')
    id = models.CharField(max_length=50, primary_key=True,
                          blank=True, validators=[alphanumeric])
    name = models.CharField(max_length=200)
    time_zone = models.CharField(max_length=200)

    def __str__(self):
        return self.id


class ActivityPeriod(models.Model):
    ID = models.ForeignKey(User,on_delete=models.CASCADE)
    login_time = models.TimeField(null=True)
    s_time = models.DateTimeField()
    e_time = models.DateTimeField()

    def __str__(self):
        return self.s_time
