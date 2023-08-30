from django.urls import path
from .views import index, top_sellers, advert_post, advertisement

urlpatterns = [
    path('', index, name='main-page'),
    path('top-sellers/', top_sellers, name='top-sellers'),
    path('advertisement-post/', advert_post, name='advertisement-post'),
    path('advertisement/', advertisement, name='advertisement'),
]
