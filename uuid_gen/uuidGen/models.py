from django.db import models
import uuid

# Create your models here.
class UuidGenerator(models.Model):

	timestamp = models.DateTimeField(auto_now_add=True)
	uuid = models.UUIDField(default=uuid.uuid4, editable= False)

	
	def __str__(self):

		return f'{self.timestamp} : {self.uuid}'

