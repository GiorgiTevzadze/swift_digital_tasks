from django.contrib.auth import authenticate, login
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken

from .serializers import AccountSerializer
from .models import MyAccount as Account


class RegisterView(APIView):

    def post(self, request):
        print(request.data)
        serializer = AccountSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            print('valid')
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    @staticmethod
    def get_tokens_for_user(user):
        refresh = RefreshToken.for_user(user)
        return refresh

    def post(self, request):
        email = request.data.get['email']
        password = request.data.get['password']
        if not email or not password:
            return Response({'error': 'Please fill all fields'}, status=status.HTTP_400_BAD_REQUEST)

        check_user = Account.objects.get(email=email).exists()
        if not check_user:
            return Response({'error': 'email does not exists'}, status=status.HTTP_400_BAD_REQUEST)

        user = authenticate(email=email, password=password)

        if user is not None:
            login(request, user)

            refresh_token = self.get_tokens_for_user(request.user)

            data = {
                'refresh_token': str(refresh_token),
                'access_token': str(refresh_token.access_token),
                'user_email': request.user.email,
                'id': request.user.pk
            }
            return Response({'success': 'Successfully logged in', 'data': data}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid login details'}, status=status.HTTP_400_BAD_REQUEST)