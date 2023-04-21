from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin, \
    DestroyModelMixin
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny
from .models import CustomUser, Verification
from .serializers import UserMiniSerializer, VerificationSerializer

# Create your views here.

'''
    This class retrieve users information,

'''
class UserListViewset(GenericAPIView, ListModelMixin):
    serializer_class = UserMiniSerializer
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.none()
    ordering = "-date_joined"
    filter_fields = ("id", "email", "phone_number", "nationality", "marital_status", "gender", "verification_status")
    search_fields = ("id", "email", "phone_number", "nationality", "marital_status", "gender", "verification_status")
    ordering_fields = ("date_joined", "first_name", "last_name", "birthdate", "nationality", "gender", "verification_status")

    def get_queryset(self):
        if self.request.user.is_staff:
            return CustomUser.objects.all()
        return CustomUser.objects.filter(id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


'''
    This class accept the user id and retrieve, update, and delete his/her information,

'''
class UserDetailViewset(GenericAPIView, RetrieveModelMixin, UpdateModelMixin):
    serializer_class = UserMiniSerializer
    permission_classes = [IsAuthenticated]
    queryset = CustomUser.objects.none()

    def get_queryset(self):
        if self.request.user.is_staff:
            return CustomUser.objects.all()
        return CustomUser.objects.filter(id=self.request.user.id)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
        