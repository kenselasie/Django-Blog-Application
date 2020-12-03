from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from .models import Users

class UserSerializer(serializers.ModelSerializer):
    # username = serializers.CharField(
    #         required=True,
    #         validators=[UniqueValidator(queryset=Users.objects.all())],
    #         min_length=5,
    #         max_length=20
    #         ),
    # password = serializers.CharField(
    #         required=True,
    #         max_length=256
    #         )

    class Meta:
        model = Users
        fields = '__all__'

    # def create(self, validated_data):
    #     user = Users.objects.create_user(validated_data['username'], validated_data['password'])
    #     return user



# class GetMethodUserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Users
#         fields = '__all__'