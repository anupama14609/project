from django.urls import path
from .views import home, about, postComment,contact, posts,search, handelSignUp,handelLogin,handelLogout

urlpatterns = [
    path('', home, name='home' ),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('search', search, name="search"),
    path('signup', handelSignUp, name="handleSignUp"),
    path('login', handelLogin, name="handleLogin"),
    path('logout', handelLogout, name="handleLogout"),
    path('blog/<str:slug>', posts, name='posts'),
    path('postComment', postComment, name="postComment"),
]
