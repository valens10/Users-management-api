from django.utils import timezone
from rest_framework.serializers import ModelSerializer
from .models import CustomUser, Verification
from django.contrib.auth.models import Group


class GroupMiniSerializer(ModelSerializer):
    class Meta:
        model = Group
        fields = ["name"]


class UserMiniSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = "__all__"

    def to_representation(self, instance):
        serialized_data = super(UserMiniSerializer, self).to_representation(instance)
        serialized_data['nationality'] = instance.nationality.name

        if instance.birthdate:
            now = timezone.now().date()
            td = now - instance.birthdate
            years = int(td.days / 365)
            serialized_data['age'] = f"{years} Years"
        else:
            serialized_data['age'] = None
        return serialized_data

    def update(self, instance, validated_data):
        if validated_data.get("email") and instance.email and validated_data.get("email") != instance.email:
            validated_data["is_email_verified"] = False
        return super(UserMiniSerializer, self).update(instance, validated_data)


class VerificationSerializer(ModelSerializer):
    class Meta:
        model = Verification
        fields = "__all__"
