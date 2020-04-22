from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home_view(request):
    return render(request, "file.html", {})

def full_analysis(request):
    return render(request, "fullanalysis.html", {})

def sector_wise_analysis(request):
    return render(request, "sectorwise.html", {})

def prediction(request):
    return render(request, "prediction.html", {})