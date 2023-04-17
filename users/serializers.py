from rest_framework import routers, serializers, viewsets
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


from .models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User    
        fields = "__all__"


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email']
        )
        
        user.set_password(validated_data['password'])
        user.save()
        return user

    class Meta:
        model = User    
        fields = ('id', 'username', 'email', 'password')



class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        data = super().validate(attrs)
        data['username'] = self.user.username
        return data