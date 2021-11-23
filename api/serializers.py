from .models import enquiryForm
from rest_framework import serializers

class enquiryFormSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = enquiryForm
        fields = ['id', 'fullName', 'email', 'mobile', 'courseInterest', 'city', 'state', 'zipcode', 'dateCreated', 'claimed_by', 'claimed']
