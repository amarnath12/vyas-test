from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.generic import View


class details(View):
    def get(self, *args, **kwargs):
        emp_details = {
            "name": "Amar"
        }
        return JsonResponse(emp_details)
