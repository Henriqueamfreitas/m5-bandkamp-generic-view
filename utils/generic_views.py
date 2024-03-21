from rest_framework.views import APIView, Request, Response, status
from .mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin, UpdateModelMixin

class GenericView(APIView):
    serializer_class = None

class CreateAPIView(GenericView, CreateModelMixin):
    def post(self, request: Request) -> Response:
        return super().create(request)

class RetrieveAPIView(GenericView, RetrieveModelMixin):
    def get(self, request: Request, pk: int) -> Response:
        return super().retrieve(request, pk)

class DestroyAPIView(GenericView, DestroyModelMixin):
    def delete(self, request: Request, pk: int) -> Response:
        return super().destroy(request, pk)
    
class UpdateAPIView(GenericView, UpdateModelMixin):
    def patch(self, request: Request, pk: int) -> Response:
        return super().partial_update(request, pk)

class RetrieveUpdateDestroyAPIView(RetrieveAPIView, UpdateAPIView, DestroyAPIView):
    ...