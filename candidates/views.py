from django.shortcuts import render

# Create your views here.
def error(request):
    return render(request, '404.html')


def about(request):
    return render(request, 'about.html')


def candidatesingle(request):
    return render(request, 'candidates_single.html')


def candidateslist(request):
    return render(request, 'candidates_list.html')


def candidatessingle(request):
    return render(request, 'candidates_single.html')


def contact(request):
    return render(request, 'contact.html')


def employerlist(request):
    return render(request, 'employer_list.html')


def employersingle(request):
    return render(request, 'employer_single.html')


def how(request):
    return render(request, 'how.html')


def index(request):
    return render(request, 'index.html')


def locationsingle(request):
    return render(request, 'location_single.html')


def pricing(request):
    return render(request, 'pricing.html')


def services(request):
    return render(request, 'services.html')