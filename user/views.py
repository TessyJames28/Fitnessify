from django.shortcuts import render
from rest_framework import generics
from .models import UserRegistration
from .serializers import UserRegistrationSerializer, UserLoginSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.contrib.auth.hashers import check_password
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.views import APIView

# Create your views here.
class UserRegistrationView(generics.CreateAPIView):
    queryset = UserRegistration.objects.all()
    serializer_class = UserRegistrationSerializer


# Login view function
# @api_view(['POST'])
# def login(request):
#     username = request.data.get('username')
#     email = request.data.get('email')
#     password = request.data.get('password')

#     print(f"username: {username}, email: {email}, password: {password}")
#     try:
#         user = UserRegistration.objects.filter(username=username).first()
#     except UserRegistration.DoesNotExist:
#         user = None
    
#     print(f"username: {user.username}, email: {user.email}, password: {user.password}")
#     # user_auth = authenticate(username=username, email=email, password=password)
#     # print(f"user: {user}")
#     # if user_auth and check_password(password, user.password):
#     if user is not None and check_password(password, user.password):
#         print(user)
#         token = Token.objects.filter(user=user).first()

#         if token:
#             # If a token already exists, return the existing token
#             return token
#         else:
#             # If no token exists, create a new one
#             token = Token.objects.create(user=user)
#             return token
#         # return Response({"success": "success"}, 200)
#     else:
#         return Response({"error": "Invalid username or password"}, 401)


class UserLoginView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        User = UserRegistration
        try:
            user = User.objects.get(username=serializer.validated_data['username'])
        except User.DoesNotExist:
            return Response({'error': 'Invalid credentials'}, status=401)

        if not check_password(serializer.validated_data['password'], user.password):
            return Response({'error': 'Invalid credentials'}, status=401)

        # Generate the token
        refresh = RefreshToken.for_user(user)
        token = {
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        }

        # response = Response(token, status=200)

        # Add tokens to the response headers
        # response['Authorization'] = f'Bearer {str(refresh.access_token)}'
        # response['Refresh-Token'] = str(refresh)

        return Response(token, status=200)
        