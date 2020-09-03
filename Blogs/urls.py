from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, SportView,SportDetailsView, AddSportArticles
#from . import views

urlpatterns=[
    #path('',views.home, name="home")
    path('',HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-details"),
    path('post_blog/', AddPostView.as_view(), name='add_post'),
    path('sport/', SportView.as_view(), name="sport"),
    path('sportarticle/<int:pk>',SportDetailsView.as_view(), name="sport-articles" ),
    path('post_sport/', AddSportArticles.as_view(), name='add_sport'),

]