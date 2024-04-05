from rest_framework import serializers
from .models import Paper, GroupPaper, RecommendPapersList

class PaperSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper
        fields = '__all__'
        
class GroupPaperSerializer(serializers.ModelSerializer):
    papers = PaperSerializer(many=True)
    class Meta:
        model = GroupPaper
        fields = '__all__'
        
class RecommendPapersListSerializer(serializers.ModelSerializer):
    papers = PaperSerializer(many=True)
    class Meta:
        model = RecommendPapersList
        fields = '__all__'