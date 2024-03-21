from rest_framework.views import APIView, status, Response
from .models import Album
from .serializers import AlbumSerializer
from django.shortcuts import get_object_or_404
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from utils.generic_views import CreateAPIView, RetrieveAPIView
from rest_framework.generics import ListCreateAPIView



class AlbumView(ListCreateAPIView):
    queryset = Album.objects.all()
    serializer_class = AlbumSerializer

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

