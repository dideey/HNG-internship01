from django.shortcuts import render
from .serializers import MyModelSerializer
from .models import MyModel
from django.utils.timezone import now 
from django.http import JsonResponse

def MyModelview(request):
    if request.method == 'GET':
        instance = MyModel.objects.first()
        serializer = MyModelSerializer(instance)
        data = serializer.data
         data = {
            "email": "dideeyndwaru@gmail.com",
            "current_datetime": now().isoformat(timespec='seconds').replace("+00:00", "Z")
        }
        return JsonResponse(data, safe=False, status=200)
