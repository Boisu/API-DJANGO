from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from . models import word
from . serialiazers import wordSerializer

# Create your views here.

class wordList(APIView):
    def get(self, request):
        word1 = word.objects.all()
        serializer = wordSerializer(word1,many = True)
        return Response(serializer.data)
def post(self):
    pass

