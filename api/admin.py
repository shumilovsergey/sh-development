from django.contrib import admin
from .models import Job
from .models import Bio
from .models import Skills
from .models import Feedback
from .models import Projects

admin.site.register(Job)
admin.site.register(Bio)
admin.site.register(Skills)
admin.site.register(Feedback)
admin.site.register(Projects)