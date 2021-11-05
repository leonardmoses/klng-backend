from rest_framework import serializers
from .models import User, Portfolio, Project
from django.contrib.auth.hashers import make_password

#users serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    
    def create(self, validated_data):
        users = User.objects.create_user(
            password=make_password(
                validated_data['user_name'].pop('password')
            ),
            **validated_data.pop('user_name')
        )

    def update(self, instance, validated_data):
        if 'user_name' in validated_data:
            instance.users.password = make_password(
                validated_data.get('user_name').get('password', instance.user.password)
            )
            instance.users.save()

    class Meta:
        model = User
        fields = (
            'id', 'user_name', 'email', 'password')

# portfolio serializer
class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
    projects = serializers.HyperlinkedRelatedField(
        view_name='project_show',
        many = True,
        read_only=True
    )

    portfolio_url = serializers.ModelSerializer.serializer_url_field(
        view_name='portfolio_show')

    class Meta:
        model = Portfolio
        fields = ('id','name', 'about', 'github_link','linkdin_link','image_url','portfolio_url') 

#Project serializer
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    portfolio = serializers.HyperlinkedRelatedField(
        view_name='portfolio_show',
        read_only=True
    )

    portfolio_id = serializers.PrimaryKeyRelatedField(
        queryset=Portfolio.objects.all(),
        source='name'    
        )

    class Meta:
        model = Project
        fields = ('id','name','portfolio_id', 'project_name', 'desc', 'project_link','image_url') 