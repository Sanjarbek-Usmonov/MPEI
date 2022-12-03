from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponseBadRequest
from ads.models import Ads
from news.models import News


def index(request):
    site_logo = SiteLogo.objects.all().first()
    sociallinks = SocialLinks.objects.all().first()
    introsection = IntroSection.objects.all().first()
    contactaddress = ContactAddress.objects.all().first()
    newslettertext = JoinOurNewsletterText.objects.all().first()
    news = News.objects.all()[::-1][:6]
    
    testimonials = Testimonials.objects.all()
    whychooseus = WhyChooseUs.objects.all().first()
    ads = Ads.objects.all()[::-1][:3]
    ad_odd = ads[1]
    context = {
        'site_logo': site_logo,
        'introsection': introsection,
        'sociallinks': sociallinks,
        'contactaddress': contactaddress,
        'newslettertext': newslettertext,
        'ads': ads,
        'news': news,
        'ad_odd': ad_odd,
        'testimonials': testimonials,
        'whychooseus': whychooseus,
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

def contact_view(request):
    site_logo = SiteLogo.objects.all().first()
    sociallinks = SocialLinks.objects.all().first()
    contactaddress = ContactAddress.objects.all().first()
    newslettertext = JoinOurNewsletterText.objects.all().first()
    if request.method == 'POST':
        ReceivedMessages.objects.create(
            email=request.POST['email'],
            phone_number=request.POST['phone_number'],
            message=request.POST['message'],
        )
        return redirect('contact')
    context = {
        'site_logo': site_logo,
        'sociallinks': sociallinks,
        'contactaddress': contactaddress,
        'newslettertext': newslettertext,
    }
    return render(request, 'contact.html', context=context)
