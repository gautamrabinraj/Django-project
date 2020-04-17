from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from meetings.models import Meeting
# Create your views here.

def welcome(request):
    return render(request, "pages/welcome.html", 
        {"number_meet": Meeting.objects.count()})
def about(request):
    return HttpResponse(str(datetime.now()))