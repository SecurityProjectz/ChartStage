from django.contrib.auth import get_user_model
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import View

from rest_framework.views import APIView
from rest_framework.response import Response

User = get_user_model()

class HomeView(View):
    def get(self, request, *args, **kwargs):
        return render(request, 'charts.html', {"customers": 10})



def get_data(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response
	
def get_guagedata(request, *args, **kwargs):
    data = {
        "sales": 100,
        "customers": 10,
    }
    return JsonResponse(data) # http response

def guage(request, *args, **kwargs):
    return render(request, 'guage.html', {"customers": 10})

class ChartData(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request, format=None):
        label = ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"]
        default_items = [1,3,4,3,6,7]
        data = {
            "lables": label,
            "default_items": default_items,
        }
        return Response(data)
