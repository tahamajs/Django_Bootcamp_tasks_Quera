# serializer file

from rest_framework import serializers
from .models import Question, Answer

class QuestionSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=100)
    body = serializers.CharField()
    user = serializers.CharField()
    tags = serializers.CharField()
    created_at = serializers.DateTimeField()
    updated_at = serializers.DateTimeField()
    upvoters = serializers.CharField()
    downvoters = serializers.CharField()
    votes = serializers.CharField()

    def create(self, validated_data):
        return Question.objects.create(**validated_data)

    def validated_body(self, value):
        if len(value) < 10:
            raise serializers.ValidationError("Body must be more than 10 characters")
        return value



    def update(self, instance, validated_data):
        instance.title = validated_data.get('title' , instance.title)
        instance.body = validated_data.get('body' , instance.body)
        instance.user = validated_data.get('user' , instance.user)
        instance.tags = validated_data.get('tags' , instance.tags)
        instance.created_at = validated_data.get('created_at' , instance.created_at)
        instance.updated_at = validated_data.get('updated_at' , instance.updated_at)
        instance.upvoters = validated_data.get('upvoters' , instance.upvoters)
        instance.downvoters = validated_data.get('downvoters' , instance.downvoters)
        instance.votes = validated_data.get('votes' , instance.votes)
        instance.save()
        return instance