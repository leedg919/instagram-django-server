from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Feed
from users.models import User
from .serializers import FeedSerializer

# 전체 게시글 불러오는 API
class AllFeeds(APIView):
    def get(self, request):
        all_feeds = Feed.objects.all()
        serializer = FeedSerializer(
            all_feeds,
            many=True
        )
        
        return Response(serializer.data)


from rest_framework.exceptions import NotFound
from .serializers import FeedDetailSerializer
from reviews.serializers import ReviewSerializer

# 유저네임을 기반으로 특정 유저의 게시글을 불러오는 API
class FeedDetail(APIView):
	def get(self, request, username):
             print("Feed Datail")
             user = User.objects.get(username=username)
             feed = Feed.objects.filter(user_id=user.id)
             serializer = FeedDetailSerializer(feed,many=True)
             return Response(serializer.data)

from users.models import User
from .serializers import FeedSerializer
class UserAnmeFeeds(APIView):
    def get(self, request, username):
        print("username", username)
        
        user_id = User.objects.get(username=username)
        print("user_id", user_id)
        
        user_feeds = Feed.objects.filter(user_id=user_id)
        print("user_feeds", user_feeds)
        
        serializer = FeedSerializer(user_feeds, many=True)
        
        return Response(serializer.data)
    