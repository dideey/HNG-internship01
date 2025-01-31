from django.utils.timezone import now
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import MyModelSerializer
from .models import MyModel

@api_view(['GET'])
def my_model_view(request):
    instance = MyModel.objects.first()
    
    if instance is None:
        return Response({"error": "No data found"}, status=404)
    
    serializer = MyModelSerializer(instance)
    data = serializer.data
    data["current_datetime"] = now().isoformat() + 'Z'
    
    return Response(data, status=200)
