from rest_framework.serializers import ModelSerializer
from tasks.models import Spotlight

class SpotlightSerializer(ModelSerializer):
    class Meta:
        fields = "__all__"
        model = Spotlight