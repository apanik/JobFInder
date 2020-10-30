from django.shortcuts import render
from rest_framework.views import APIView
from .models import Company
from rest_framework.response import Response
from rest_framework import generics

def jobs(request):
    context = {
        'keyword': '',
        'top_categories':'',
        'top_skill':''
    }

    category = request.GET.get('category')
    skill = request.GET.get('skill')
    top_skill = request.POST.get('top-skill')
    context['category'] = category
    context['skill'] = skill
    context['top_skill'] = top_skill

    return render(request, 'job-list.html', context)
