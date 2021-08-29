"""
Account Api Views
"""

# Django RestFramework
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework.authtoken.models import Token

# Serializers
from .serializers import UserSerializer, UserCustomSerializer

# Forms
from accounts.forms import SignupForm

#Models
from accounts.models import User


class SignupAPIView(APIView):
    """
    Create a new user and return the access tokens
    """
    permission_classes = (permissions.AllowAny,)

    def post(self, request, version):
        """
        register a new user
        :param request:
        :param version:
        :return: success or serialized errors
        """
        try:
            if not User.objects.filter(username=request.data["email"]).exists():
                user_created = User.objects.create_user(
                    username=request.data["email"],
                    password=request.data["password"],
                    first_name=request.data["first_name"],
                    last_name=request.data["last_name"],
                    email=request.data["email"]
                )

                token = Token.objects.get_or_create(user=user_created)

                data = {
                    'user': UserCustomSerializer(user_created).data,
                    'access_token': token[0].key
                }

                return Response(
                    data,
                    status=status.HTTP_201_CREATED
                )

            return Response([{
                'status': 'error',
                'msg': 'user already exists',
            }], status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response([{
                'status': 'error',
                'msg': 'email invalid.',
            }], status=status.HTTP_400_BAD_REQUEST)


class UserRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = UserCustomSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def get_object(self):
        return self.request.user
