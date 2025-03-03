# from django.urls import path
# from .views import ArticleList, ArticleDetail
# # from .views import article_list, article_details

# urlpatterns = [
#     # path('articles/', article_list, name='article_list'),
#     # path('articles/<slug:slug>/', article_details, name='article_details'),
#     path('articles/', ArticleList.as_view(), name='article_list'),
#     path('articles/<slug:slug>/', ArticleDetail.as_view(), name='article_detail'),
# ]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ArticleViewSet

router = DefaultRouter()
router.register('articles', ArticleViewSet, basename='article')

urlpatterns = [
    path('api/', include(router.urls)),
]