from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from base.models import *
from .models import *

@login_required
def schedule(request):
    site_logo = SiteLogo.objects.all().first()
    sociallinks = SocialLinks.objects.all().first()
    contactaddress = ContactAddress.objects.all().first()
    newslettertext = JoinOurNewsletterText.objects.all().first()

    query = Faculty.objects.all()
    context = {
        'query': query,
        'site_logo': site_logo,
        'sociallinks': sociallinks,
        'contactaddress': contactaddress,
        'newslettertext': newslettertext,
    }
    return render(request, 'schedule.html', context=context)