from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Review
from .serializers import ReviewSerializer

class AllReviews(APIView):
    def get(self, request):
        all_reviews = Review.objects.all()
        serializer = ReviewSerializer(
            all_reviews,
            many=True
        )
        
        return Response(serializer.data)