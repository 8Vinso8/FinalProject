from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

# redis connection
# redis = rd.Redis(host=’redis’, port=6379, db=0)

def test(request):
    return HttpResponse("This is Django")
