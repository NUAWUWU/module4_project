from django.urls import path
from .views import index, top_sellers, advert_post, register, login, profile, advertisement

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', advert_post, name='advertisement-post'),
    path('register/', register, name='register'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),
    path('advertisement/', advertisement, name='advertisement'),
]
