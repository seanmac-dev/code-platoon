from rest_framework.views import APIView
from .serializers import User, UserSerializer
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.status import (
    HTTP_201_CREATED,
    HTTP_204_NO_CONTENT,
    HTTP_400_BAD_REQUEST,
)
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import authenticate

# Create your views here.


class Sign_up(APIView):
    def post(self, request):
        try:
            data = request.data.copy()
            data["username"] = request.data["email"]
            new_user = User.objects.create_user(**data)
            new_token = Token.objects.create(user=new_user)
            return Response(
                {"email": new_user.email, "token": new_token.key},
                status=HTTP_201_CREATED,
            )
        except Exception as e:
            print(e)
            return Response(
                "Hmm, something went wrong with signup", status=HTTP_400_BAD_REQUEST
            )


class Log_in(APIView):
    def post(self, request):
        try:
            email = request.data["email"]
            password = request.data["password"]
            user = authenticate(username=email, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({"client": user.email, "token": token.key})
            return Response(
                "Something went wrong creating a token", status=HTTP_400_BAD_REQUEST
            )
        except Exception as e:
            print(e)
            return Response("Something went wrong", status=HTTP_400_BAD_REQUEST)


class UserPermissions(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]


class Log_out(UserPermissions):
    def post(self, request):
        request.user.auth_token.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class Info(UserPermissions):
    def get(self, request):
        user = UserSerializer(request.user)

        return Response(user.data)

    def put(self, request):
        user = UserSerializer(request.user, data=request.data, partial=True)
        if user.is_valid():
            user.save()
            return Response(user.data)
        return Response(user.errors, status=HTTP_400_BAD_REQUEST)
