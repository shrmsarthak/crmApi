from django.shortcuts import render
from rest_framework import viewsets

from .serializers import enquiryFormSerializer
from .models import enquiryForm

class enquiryFormViewSet(viewsets.ModelViewSet):
  """
  API endpoint that allows users to be viewed or edited.
  
  """
  queryset = enquiryForm.objects.all().order_by('-dateCreated')
  serializer_class = enquiryFormSerializer