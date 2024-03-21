from django.shortcuts import get_object_or_404
from rest_framework.views import APIView, Request, Response, status

class CreateModelMixin:
    def create(self, request: Request) -> Response:
        """
        Registro de usuários
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()

        return Response(serializer.data, status.HTTP_201_CREATED)

class RetrieveModelMixin:
    def retrieve(self, request: Request, pk: int) -> Response:
        """
        Obtençao de usuário
        """
        obj = get_object_or_404(self.queryset, pk=pk)

        self.check_object_permissions(request, obj)

        serializer = self.serializer_class(obj)

        return Response(serializer.data)
    
class DestroyModelMixin:
    def destroy(self, request: Request, pk: int) -> Response:
        """
        Deleçao de usuário
        """
        obj = get_object_or_404(self.queryset, pk=pk)

        self.check_object_permissions(request, obj)

        obj.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)

class UpdateModelMixin:
    def partial_update(self, request: Request, pk: int) -> Response:
        """
        Atualização de usuário
        """
        obj = get_object_or_404(self.queryset, pk=pk)

        self.check_object_permissions(request, obj)

        serializer = self.serializer_class(obj, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)




