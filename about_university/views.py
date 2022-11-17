from django.shortcuts import render, HttpResponse
from .models import IntroduceMEI

def test(request):
    test = IntroduceMEI.objects.get(pk=1)
    return HttpResponse(test.text)