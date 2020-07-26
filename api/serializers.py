from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token

from .models import (Profile, Poll, Choice, Vote)


class UserSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(
            queryset=User.objects.all())])

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True},
                        'email': {'required': True},
                        'first_name': {'required': True},
                        'last_name': {'required': True},
                        'username': {'required': True}}

    def create(self, validated_data):
        user = User(
            email=validated_data['email'],
            username=validated_data['username'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        Token.objects.create(user=user)
        Profile.objects.create(user=user, username=user.username,
                               firstname=user.first_name,
                               lastname=user.last_name,
                               email=user.email)

        return user


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['firstname', 'lastname', 'username', 'email',
                  'country', 'city', 'bio']


class VoteSerializer(serializers.ModelSerializer):
    voted_by = serializers.SerializerMethodField(read_only=True)
    poll = serializers.SerializerMethodField(read_only=True)

    def get_voted_by(self, obj):
        return obj.voted_by.username

    def get_poll(self, obj):
        return obj.poll.question

    class Meta:
        model = Vote
        fields = '__all__'


class ChoiceSerializer(serializers.ModelSerializer):
    votes = VoteSerializer(many=True, required=False)

    class Meta:
        model = Choice
        fields = '__all__'


class PollSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField(read_only=True)

    def get_created_by(self, obj):
        return obj.created_by.username

    class Meta:
        model = Poll
        fields = '__all__'
