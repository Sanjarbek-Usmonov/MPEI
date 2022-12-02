from django.shortcuts import render
from .models import News
from base.models import *
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q


def newsview(request):
    site_logo = SiteLogo.objects.all().first()
    sociallinks = SocialLinks.objects.all().first()
    contactaddress = ContactAddress.objects.all().first()
    newslettertext = JoinOurNewsletterText.objects.all().first()

    newss = News.objects.all()[::-1]
    page = request.GET.get('page', 1)
    paginator = Paginator(newss, 10)
    try:
        news = paginator.page(page)
    except PageNotAnInteger:
        news = paginator.page(1)
    except EmptyPage:
        news = paginator.page(paginator.num_pages)
    context = {
        'news': news,
        'site_logo': site_logo,
        'sociallinks': sociallinks,
        'contactaddress': contactaddress,
        'newslettertext': newslettertext,
    }
    return render(request, 'blog.html', context=context)