from django.db import models
from django.urls import reverse
from django.utils import timezone
from django.conf import settings

class FeetBack(models.Model):
	name = models.TextField()
	text = models.TextField()
	data = models.DateTimeField(auto_now=True, 
							auto_now_add=False)

	def __unicode__(self):
		return self.name