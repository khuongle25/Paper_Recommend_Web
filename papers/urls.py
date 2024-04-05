from django.urls import path
from .views import PaperListCreate, PaperRetrieveUpdateDestroy, GroupPaperListCreate, GroupPaperRetrieveUpdateDestroy, GroupPaperAddPaper, RecommendPapersListCreate

urlpatterns = [
    path('papers/', PaperListCreate.as_view()),
    path('papers/<int:pk>/', PaperRetrieveUpdateDestroy.as_view()),
    path('groups/', GroupPaperListCreate.as_view()),
    path('groups/<int:pk>/', GroupPaperRetrieveUpdateDestroy.as_view()),
    path('groups/<int:pk>/add-paper/', GroupPaperAddPaper.as_view()),
    path('groups/<int:pk>/recommend/', RecommendPapersListCreate.as_view()),
]