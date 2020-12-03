from rest_framework.views import APIView
from .models import Post
from .serializers import PostSerializer
from rest_framework.response import Response

# Create your views here.
class PostList(APIView):
    def get(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response({
            'success' : True,
            'data': serializer.data
        })