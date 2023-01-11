from rest_framework.response import Response
from rest_framework.decorators import api_view

from api.v1.tasks.serializers import SpotlightSerializer
from tasks.models import Spotlight


@api_view(["GET"])
def tasks(request):
    instances = Spotlight.objects.all()
    context={
        "request":request
    }
    serializer = SpotlightSerializer(instances,many=True,context=context)
    response_data = {
        "status_code" : 3000,
        "data" : serializer.data,
    }
    return Response (response_data)


