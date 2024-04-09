from django.views import View
from django.shortcuts import render
from .models import Job
from .models import Bio
from .models import Skills
from .models import Projects
from django.shortcuts import get_object_or_404
import os


class Main(View):
    def get(self, request):
        skills = Skills.objects.all()
        
        bio = get_object_or_404(Bio, name="Шумилов Сергей")
        # bio = Bio.objects.get(name="Шумилов Сергей")
        projects = Projects.objects.all()
        # feedback = Feedback.objects.all()
        jobs = Job.objects.all().order_by('-id')

        return render(request, 'index.html', {
            "skills":skills,
            "bio":bio,
            "projects":projects,
            "jobs":jobs
        })
    


