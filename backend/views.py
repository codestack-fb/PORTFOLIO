from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import Project
from django.views.generic import ListView , DetailView

# Create your views here.

def home(request):
    proyektlar = Project.objects.all()
    context = { 
        'proyektlar': proyektlar
    }
    return render(request , 'index.html' , context)

class Search(ListView):
    queryset = Project.objects.all()
    context_object_name = 'proyektlar'
    template_name = 'index.html'

    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get('q')
        return Project.objects.filter(name__icontains=query).order_by('id')

class ProjectDetail(DetailView):
    model = Project
    context_object_name = 'project'
    template_name = 'details.html'