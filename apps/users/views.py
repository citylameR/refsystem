from django.contrib.auth import get_user_model
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.throttling import UserRateThrottle
import random
import time

from apps.users.models import VerificationCode
from apps.users.serializers import AuthSerializer, UserSerializer


class AuthViewSet(viewsets.ViewSet):
    serializer_class = AuthSerializer
    throttle_classes = [UserRateThrottle]

    def request_code(self, request):
        phone = request.data['phone']
        code = random.randint(1000, 9999)

        VerificationCode.objects.create(phone=phone, code=code)

        time.sleep(2)

        return Response({'message': 'Code sent'})

    def check_code(self, request):
        phone = request.data['phone']
        code = request.data['code']

        if VerificationCode.objects.filter(phone=phone, code=code).exists():
            return Response({'message': 'Code verified'})
        else:
            return Response({'message': 'Wrong code'}, status=400)


class UserProfileViewSet(viewsets.ViewSet):
    serializer_class = UserSerializer

    def retrieve(self, request, pk=None):
        User = get_user_model()
        user = User.objects.get(pk=pk)
        serializer = UserSerializer(user)

        return Response(serializer.data)