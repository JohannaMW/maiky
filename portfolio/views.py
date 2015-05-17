from django.shortcuts import render, render_to_response

# Create your views here.
def home(request):
    return render_to_response('index.html')

def news(request):
    return render_to_response('news.html')

def about(request):
    return render_to_response('about.html')

def impressum(request):
    return render_to_response('impressum.html')

def works(request):
    return render_to_response('works.html')

def opera(request):
    return render_to_response('opera.html')

def street_opera(request):
    return render_to_response('street_opera_stockholm.html')