from django.urls import path
from ..views import *
from .views import *
from . import views


from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    # path('', include(router.urls)),
    path('register' , RegisterView.as_view()),
    path('post' , PostView.as_view()),
    path('post/<int:pk>' , PostView.as_view()),
    path('profile' , ProfileView.as_view()),
    path('profile/<int:pk>' , ProfileView.as_view()),
    path('like',LikeView.as_view()),
    path('comment',CommentView.as_view()),
    path('send_friendrequest',Send_FriendRequest.as_view()),
    # path('accept_friendrequest/<int:requestID>',Accept_FriendRequest.as_view()),

    
    path('demotoken' , TokenView.as_view()),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

]
