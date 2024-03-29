from django.http import Http404, JsonResponse

from rest_framework import permissions, status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView

from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView

from .serializers import ProjectSerializer
from crafter_tracker.models import Project

class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        return token

class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class GetRoutes(APIView):
    def get(self, request):
        routes = [
        '/api/token',
        '/api/token/refresh'
    ]
        return Response(routes)

class PublicProjectsList(APIView):
    def get(self, request, format=None):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

class PublicProjectDetails(APIView):
    def get_object(self, pk):
        try:
            return Project.objects.get(id=pk)
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        project = self.get_object(pk)
        serializer = ProjectSerializer(project)
        return Response(serializer.data)

class ProjectsList(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        projects = user.project_set.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)

    def post(self, request):
        data = request.data
        project = Project.objects.create(
            name=data['name'],
            description=data['description'],
            user = request.user
        )
        serializer = ProjectSerializer(project, many=False)
        return Response(serializer.data)

class ProjectDetails(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, pk):
        user = request.user
        project = user.project_set.get(id=pk)
        serializer = ProjectSerializer(project, many=False)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        user = request.user
        project = user.project_set.get(id=pk)
        serializer = ProjectSerializer(project, data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        user = request.user
        project = user.project_set.get(id=pk)
        project.delete()
        return Response('Project deleted!')

