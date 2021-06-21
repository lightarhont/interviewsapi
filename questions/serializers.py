from rest_framework import serializers
from .models import Interview, Question, Variant


class VariantSerializer(serializers.Serializer):
    
    uid = serializers.CharField()
    text = serializers.CharField()
    
    class Meta:
        model = Variant
    

class QuestionsSerializer(serializers.Serializer):
    
    id = serializers.IntegerField()
    text = serializers.CharField()
    type = serializers.IntegerField()
    variant = VariantSerializer(many=True)
    
    class Meta:
        model = Question


class InterviewsSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    date_start = serializers.DateTimeField()
    date_end = serializers.DateTimeField()
        

class InterviewSerializer(serializers.Serializer):

    id = serializers.IntegerField()
    name = serializers.CharField()
    description = serializers.CharField()
    date_start = serializers.DateTimeField()
    date_end = serializers.DateTimeField()
    question = QuestionsSerializer(many=True)
    
    class Meta:
        model = Interview

    