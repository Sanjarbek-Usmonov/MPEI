from django.shortcuts import render
from base.models import SiteLogo, SocialLinks, ContactAddress, JoinOurNewsletterText
from .models import Ads, AdDetail
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.utils.translation import gettext_lazy as _
from django.db.models import Q

def ads(request):
    site_logo = SiteLogo.objects.all().first()
    sociallinks = SocialLinks.objects.all().first()
    newslettertext = JoinOurNewsletterText.objects.all().first()
    contactaddress = ContactAddress.objects.all().first()
    if request.method == 'POST' and 'search-ad' in request.POST:
        advers = Ads.objects.filter(
            Q(name__icontains=request.POST['search-ad']) | Q(area__icontains=request.POST['search-ad'])
        )[::-1]
    else:
        advers = Ads.objects.all()[::-1]
    page = request.GET.get('page', 1)
    paginator = Paginator(advers, 6)
    try:
        ads = paginator.page(page)
    except PageNotAnInteger:
        ads = paginator.page(1)
    except EmptyPage:
        ads = paginator.page(paginator.num_pages)
    ads_odd = ads[::2]
    context = {
        'site_logo': site_logo,
        'sociallinks': sociallinks,
        'contactaddress': contactaddress,
        'newslettertext': newslettertext,
        'ads': ads,
        'ads_odd': ads_odd,
    }
    return render(request, 'event.html', context=context)

def ad_detail(request, pk):
    site_logo = SiteLogo.objects.all().first()
    sociallinks = SocialLinks.objects.all().first()
    newslettertext = JoinOurNewsletterText.objects.all().first()
    contactaddress = ContactAddress.objects.all().first()
    try:
        ad = AdDetail.objects.get(ad_id=pk)
    except Exception as e:
        ad = _('Object does not find! Sorry.')
    context = {
        'site_logo': site_logo,
        'sociallinks': sociallinks,
        'contactaddress': contactaddress,
        'newslettertext': newslettertext,
        'ad': ad,
    }
    return render(request, 'event-detail.html', context=context)