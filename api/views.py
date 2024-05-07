from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from .serializers import TaskSerializer, UserRegistrationSerializer, UserLoginSerializer
from .models import Task
from rest_framework.permissions import DjangoModelPermissionsOrAnonReadOnly
from rest_framework import generics, permissions, status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate


# class ApiOverview(APIView):
#     def get(self, request):
#         api_urls = {
#             'List':'/task-list/',
#             'Detail View':'/task-detail/<str:pk>/',
#             'Create':'/task-create/',
#             'Update':'/task-update/<str:pk>/',
#             'Delete':'/task-delete/<str:pk>/',
#         }
#         return Response(api_urls)

@permission_classes((permissions.AllowAny,))
class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all().order_by('-id')  # Specify your queryset here
    serializer_class = TaskSerializer

# Create your views here.
@api_view(['GET'])
@permission_classes((permissions.AllowAny,))
def apiOverview(request):
	api_urls = {
		'List':'/task-list/',
		'Detail View':'/task-detail/<str:pk>/',
		'Create':'/task-create/',
		'Update':'/task-update/<str:pk>/',
		'Delete':'/task-delete/<str:pk>/',
		}

	return Response(api_urls)

# @api_view(['GET'])
# def taskList(request):
# 	queryset = Task.objects.all().order_by('-id')
# 	serializer = TaskSerializer(queryset, many=True)
# 	return Response(serializer.data)

@permission_classes((permissions.AllowAny,))
class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@permission_classes((permissions.AllowAny,))
class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username, password=password)
            if user:
                refresh = RefreshToken.for_user(user)
                return Response({
                    'refresh': str(refresh),
                    'access': str(refresh.access_token),
                })
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# taskList.permission_classes = [DjangoModelPermissionsOrAnonReadOnly]