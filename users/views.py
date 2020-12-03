from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework import permissions, status
from rest_framework.views import APIView
from .serializers import UserSerializer
from .models import Users

class UserList(APIView):
    def get_permissions(self):
        if self.request.method == 'POST':
            return [permissions.AllowAny()]
        else:
            return [permissions.IsAuthenticated()]

    def get(self, request):
        users = Users.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response({
            'success' : True,
            'data': serializer.data
        })
    
    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'success' : True,
                'msg': 'Successfully added a user',
                'data': serializer.data
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, *args, **kwargs):
        if request.data.get('id') is not None:
            user = Users.objects.get(pk=request.data.get('id'))
            if user:
                user.delete()
                return Response({
                    'success' : True,
                    'msg': f'Successfully Deleted {user.email} from SampleName'
                })

class UserDetail(APIView):
    pass