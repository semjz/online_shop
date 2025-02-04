from rest_framework import status
from rest_framework.generics import CreateAPIView
from rest_framework.permissions import AllowAny

from rest_framework.response import Response

from authentication.serializers import (UserSignUpSerializer, CustomerSignUpSerializer,
                                        UserSerializer)



class UserSignUpView(CreateAPIView):
    serializer_class = UserSignUpSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)


class CustomerSignUpView(CreateAPIView):
    serializer_class = CustomerSignUpSerializer
    permission_classes = [AllowAny]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)





