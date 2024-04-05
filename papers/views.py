from django.shortcuts import render
from .models import Paper, GroupPaper, RecommendPapersList
from .serializers import PaperSerializer, GroupPaperSerializer, RecommendPapersListSerializer
from rest_framework import generics

# Create your views here.

class PaperListCreate(generics.ListCreateAPIView):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer
    
class PaperRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Paper.objects.all()
    serializer_class = PaperSerializer
    
class GroupPaperListCreate(generics.ListCreateAPIView):
    queryset = GroupPaper.objects.all()
    serializer_class = GroupPaperSerializer
    
class GroupPaperRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = GroupPaper.objects.all()
    serializer_class = GroupPaperSerializer
    
# view to add a Paper to a GroupPaper
class GroupPaperAddPaper(generics.UpdateAPIView):
    queryset = GroupPaper.objects.all()
    serializer_class = GroupPaperSerializer
    
    def perform_update(self, serializer):
        paper_id = self.request.data['paper']
        paper = Paper.objects.get(id=paper_id)
        group = GroupPaper.objects.get(id=self.kwargs['pk'])
        group.papers.add(paper)
        serializer.save()
        group.rec_list_updated = False
        group.save()
    
# view to create a RecommendPapersList for a GroupPaper
class RecommendPapersListCreate(generics.ListCreateAPIView):
    queryset = RecommendPapersList.objects.all()
    serializer_class = RecommendPapersListSerializer
    
    def perform_create(self, serializer):
        group_id = self.request.data['group']
        group = GroupPaper.objects.get(id=group_id)
        papers = group.papers.all()
        serializer.save(group=group, papers=papers)
        group.rec_list_updated = False
        group.save()