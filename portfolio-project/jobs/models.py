from django.db import models

# Create your models here.
class Job(models.Model):
	image = models.ImageField(upload_to = 'images/')
<<<<<<< Updated upstream
	summary = models.CharField(max_length = 300)
	#name = models.CharField(max_length = 50)

	
=======
	summary = models.CharField(max_length = 64)
>>>>>>> Stashed changes
