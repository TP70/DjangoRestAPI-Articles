from django.urls import path, include
from .views import ArticleAPIView, GenericAPIView, ArticleViewSet
from rest_framework.routers import DefaultRouter
# from .views import ArticleAPIView

router = DefaultRouter()
router.register('article', ArticleViewSet, basename='article')

urlpatterns = [
    path('viewset/', include(router.urls)),
    path('viewset/<int:pk>/', include(router.urls)),
    # path('article/', article_list),
    path('article/', ArticleAPIView.as_view()),
    # path('detail/<int:id>/', ArticleDetails.as_view()),  # as_view() must be used because it is a class
    path('generic/article/<int:id>/', GenericAPIView.as_view())
    # path('detail/<int:pk>/', article_detail)
]
