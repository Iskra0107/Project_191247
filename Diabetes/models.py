from django.db import models
from django.db.models import Model

from django.contrib.auth.models import User
# Create your models here.

# class MyUser(models.Model):
# 	first_name= models.CharField(max_length=100)
# 	last_name = models.CharField(max_length=100)
# 	email= models.EmailField('User Email')


# 	def __str__(self):
# 		return self.first_name+" "+self.last_name


class Glucose(models.Model):
	level = models.CharField(max_length=20)
	date = models.DateTimeField('Measurement Date')
	user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
	# myUsers= models.ForeignKey(MyUser, blank=True, null=True, on_delete=models.CASCADE)


	def __str__(self):
		return self.level

# class GlucoseUser(models.Model):
# 	myUsers = models.ForeignKey(MyUser, on_delete=models.CASCADE)
# 	glucose = models.ForeignKey(Glucose, on_delete=models.CASCADE)
