from django.shortcuts import render
from django.views.generic.base import View

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'portfolio/home.html')