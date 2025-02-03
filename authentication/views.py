from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from authentication.serializers import LogoutSerializer, SignUpSerializer, UserSerializer
from authentication.models import User


class getAllUsers(APIView):

    def get(self, request):
        query = User.objects.all()
        serialized_users = UserSerializer(query, many=True)  # Fix: Use many=True
        return Response(serialized_users.data, status=status.HTTP_200_OK)

class SignUpView(APIView):
    serializer_class = SignUpSerializer

    def post(self, request: Request):
        serializer = SignUpSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = LogoutSerializer

    def post(self, request: Request):
        try:
            refresh_token = request.data["refresh"]
            refresh_token = RefreshToken(refresh_token)
            refresh_token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)

        except Exception as e:
            error_message = {'error': str(e)}
            return Response(error_message, status=status.HTTP_400_BAD_REQUEST)
