<<<<<<< Updated upstream
from django.shortcuts import render, get_object_or_404
=======
from django.shortcuts import render
>>>>>>> Stashed changes
from .models import Job
# Create your views here.
def home(request):
	jobs = Job.objects
	return render(request,'jobs/home.html')