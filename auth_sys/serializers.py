from rest_framework.serializers import Serializer, ModelSerializer
from rest_framework import serializers

from .models import Users, Profile 


class UsersSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    time_created = serializers.ReadOnlyField()
    

    class Meta:
        model = Users
        fields = ['id', 'email', 'is_superuser', 'is_active', 'is_staff', 'password', 'time_created', 'last_login']


class ProfileSerializer(ModelSerializer):
    # user = serializers.RelatedField(read_only=True)
    user = UsersSerializer(required=True)
    birthday = serializers.ReadOnlyField()

    class Meta:
        model = Profile
        fields = ['user', 'id', 'fullname', 'birthday']

    def create(self, validated_data):
        user_profile = UsersSerializer.create(UsersSerializer(), **validated_data)
        profile = Profile.objects.create(user=user_profile, **validated_data)
        return profile
    
    def update(self, instance, validated_data):
        instance.users = validated_data
        return instance

