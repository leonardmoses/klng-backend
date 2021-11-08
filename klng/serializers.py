from rest_framework import serializers
from .models import User, Portfolio, Project
# from django.contrib.auth.hashers import make_password

#users serializer
class UserSerializer(serializers.HyperlinkedModelSerializer):
    portfolio = serializers.HyperlinkedRelatedField(
        view_name='portfolio_detail',
        read_only=True
    )

    project_url = serializers.ModelSerializer.serializer_url_field(
        view_name='portfolio_detail')

    class Meta:
        model = User
        fields = (
            'id','project_url','portfolio' ,'user_name', 'email', 'password')

# portfolio serializer
class PortfolioSerializer(serializers.HyperlinkedModelSerializer):
    project = serializers.HyperlinkedRelatedField(
        view_name='project_detail',
        many = True,
        read_only=True
    )

    project_url = serializers.ModelSerializer.serializer_url_field(
        view_name='project_detail')

    class Meta:
        model = Portfolio
        fields = ('id','name', 'about', 'github_link','linkedin_link','image_url','project_url','project') 

#Project serializer
class ProjectSerializer(serializers.HyperlinkedModelSerializer):
    portfolio = serializers.HyperlinkedRelatedField(
        view_name='portfolio_detail',
        read_only=True
    )

    portfolio_id = serializers.PrimaryKeyRelatedField(
        queryset=Portfolio.objects.all(),
        source='portfolio'    
        )

    class Meta:
        model = Project
        fields = ('id','portfolio_id', 'project_name', 'desc', 'project_link','image_url','portfolio') 