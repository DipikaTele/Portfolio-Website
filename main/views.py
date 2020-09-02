from django.shortcuts import render
from django.conf import settings

# Create your views here.
def Index(request):
    context = {
        "name":  settings.DATA["NAME"],
        "about_me": settings.DATA["ABOUT_ME"]
    }
    return render(request, 'index.html', context)
    
def Projects(request):
    context = {
        "projects": settings.DATA["PROJECTS"]
    }
    return render(request, 'projects.html', context)
    
def Languages(request):
    context = {
        "languages" : settings.DATA[ "TECHNICAL_SKILLS"]
    }
    return render(request, 'languages.html',context)