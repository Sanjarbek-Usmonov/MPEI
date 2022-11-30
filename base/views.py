from django.shortcuts import render
from .models import *


def index(request):
    site_logo = SiteLogo.objects.all().first()
    sociallinks = SocialLinks.objects.all().first()
    introsection = IntroSection.objects.all()
    context = {
        'site_logo': site_logo,
        'introsection': introsection,
        'sociallinks': sociallinks,
    }
    return render(request, 'index.html', context=context)
