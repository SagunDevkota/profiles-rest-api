from django.urls import path,include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset',views.HelloViewSet,base_name='hello-viewset')
router.register('profile',views.UserProfileViewset,base_name='profile')
router.register('feed',views.UserProfileFeedViewSet,base_name='feed')
urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()),
    path('',include(router.urls)),
    path("login/", views.UserLoginAPIView.as_view()),
]