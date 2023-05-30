from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response
from core import models

# Create your views here.

template = loader.get_template('home.html')

def index(request):
    return HttpResponse(template.render())


class CreateInnovate(APIView):
    def post(self,request):
        data = models.InnovateModel.objects.create(
            name=request.data.get('name'),
            email=request.data.get('email'),
            department=request.data.get('department'),
            title=request.data.get('ideaTitle'),
            description=request.data.get('description'),
            benefits=request.data.get('benefits'),
            plan=request.data.get('implementationPlan')
        )

        return data

        
