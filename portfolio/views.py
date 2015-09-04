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

def great_grand_mother(request):
    return render_to_response('great_grand_mother.html')

def ggm_2(request):
    return render_to_response('ggm_2.html')

def film(request):
    return render_to_response('film.html')

def du_fehlst(request):
    return render_to_response('du_fehlst.html')

def fourfoureight(request):
    return render_to_response('448.html')

def eighthundret(request):
    return render_to_response('800.html')

def memorial(request):
    return render_to_response('memorial.html')

def installation(request):
    return render_to_response('installation.html')

def reflecting_light(request):
    return render_to_response('reflecting_light.html')

def inside(request):
    return render_to_response('inside.html')

def soad(request):
    return render_to_response('soad.html')

def theatre(request):
    return render_to_response('theatre.html')

def blindenschrift(request):
    return render_to_response('blindenschrift.html')

def dance(request):
    return render_to_response('dance.html')

def kylma(request):
    return render_to_response('kylma.html')

def two_people(request):
    return render_to_response('two_people.html')

def ikke(request):
    return render_to_response('ikke.html')

def sd(request):
    return render_to_response('schnitzlers_dreams.html')