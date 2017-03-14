from django.db import models
import datetime
from django.contrib.auth.models import User
# Create your models here.



class Profile(models.Model):
	user = models.ForeignKey(User)
	contactno = models.CharField(max_length = 15)

	def __str__(self):
		return self.user.username
	
	
class MessageData(models.Model):
	user = models.ForeignKey(User)
	message = models.CharField(max_length = 100)
	contactno = models.CharField(max_length = 15)
	sendTime = models.DateTimeField(default = datetime.datetime.now)
	
	
	def __str__(self):
		return self.user.username+' -> '+str(self.message)
	
		
		
	