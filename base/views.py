from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseBadRequest
from ads.models import Ads


def index(request):
    site_logo = SiteLogo.objects.all().first()
    sociallinks = SocialLinks.objects.all().first()
    introsection = IntroSection.objects.all()
    contactaddress = ContactAddress.objects.all().first()
    newslettertext = JoinOurNewsletterText.objects.all().first()
    ads = Ads.objects.all()[::-1][:3]
    ad_odd = ads[1]
    context = {
        'site_logo': site_logo,
        'introsection': introsection,
        'sociallinks': sociallinks,
        'contactaddress': contactaddress,
        'newslettertext': newslettertext,
        'ads': ads,
        'ad_odd': ad_odd,
    }
    return render(request, 'index.html', context=context)

def newsletterformview(request):
    if request.method == "POST":
        JoinOurNewsletterForm.objects.create(
            email=request.POST['email'],
        )
        return redirect('index')
    else:
        return HttpResponseBadRequest()

def receivedmessagesview(request):
    if request.method == "POST":
        ReceivedMessages.objects.create(
            email=request.POST['email'],
            message=request.POST['message'],
        )
        return redirect('index')
    else:
        return HttpResponseBadRequest()
