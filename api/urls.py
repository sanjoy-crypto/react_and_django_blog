from django.urls import path
from django.urls.conf import include
from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='articles')
router.register('users',UserViewSet,basename='users')

urlpatterns = [

    path('api/',include(router.urls)),


    # path('article/',ArticleView.as_view(),name="article"),
    # path('create-article/',ArticleCreateView.as_view(),name="create_article"),
    # path('article/<int:pk>/',ArticleDetailView.as_view(),name="article"),
    # path('update-article/<int:pk>/',ArticleUpdateView.as_view(),name="update_article"),
    # path('delete-article/<int:pk>/',ArticleDeleteView.as_view(),name="delete_article"),
]