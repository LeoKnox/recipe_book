from django.shortcuts import render, HttpResponse

from preparations.models import Preparation

def index(request):
    prep_data = Preparation.objects.values()
    return render(request, 'preparations/index.html', {'prep_data': prep_data})