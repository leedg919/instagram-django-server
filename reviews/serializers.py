from rest_framework.serializers import ModelSerializer
from .models import Review

from users.serializers import UserSerializer

class ReviewSerializer(ModelSerializer):
    user = UserSerializer()
    
    class Meta:
        model = Review
        fields = "__all__"
        # fields = ("id", "content", "like")
        depth = 1
    