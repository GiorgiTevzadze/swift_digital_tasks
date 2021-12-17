from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from django.http import Http404
from .serializers import ShortenerSerializer, ShortenerPremiumSerializer
from django.shortcuts import redirect
from django.http import HttpResponseRedirect, HttpResponse
from .models import Shortener

class ShortenerAPIView(APIView):
    @staticmethod
    def post(request):
        # x = request.user
        # if User.objects.get(username=x).is_staff:
        # # if request.user.is_admin:
        #     serializer = ShortenerPremiumSerializer(data=request.data)
        #     if serializer.is_valid():
        #         serializer.save()
        #         return Response(serializer.data, status=status.HTTP_201_CREATED)
        #     return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
        # else:
            serializer = ShortenerSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)


class RedirectShortenerAPIView(APIView):
    @staticmethod
    def get_object(short_code):
        try:
            short = Shortener.objects.get(short_code=short_code)
            short.count += 1
            short.save()
            return HttpResponseRedirect(redirect_to=short.original_url)
        except Shortener.DoesNotExist:
            return Http404('url does not exist')

    def get(self, request, short_code):
        url = self.get_object(short_code=short_code)
        return HttpResponse(url.url, status=status.HTTP_200_OK)

