from django.views import View
from django.shortcuts import render, redirect
from .models import Job
from .models import Bio
from .models import Skills
from .models import Feedback
from .models import Projects
import os


class Main(View):
    def get(self, request):
        skills = Skills.objects.all()
        bio = Bio.objects.get(name="Шумилов Сергей")
        projects = Projects.objects.all()
        feedback = Feedback.objects.all()
        jobs = Job.objects.all()

        return render(request, 'index.html', {
            "skills":skills,
            "bio":bio,
            "projects":projects,
            "feedback":feedback,
            "jobs":jobs
        })
    


