from django.urls import path
from Aarticle import views


app_name = 'Aarticle'
urlpatterns = [
    path('', views.Aarticle, name='Aarticle'),
    path('articleRead/<int:articleId>/', views.articleRead, name='articleRead'),
    path('articleCreate/', views.articleCreate, name='articleCreate'),
    path('articleUpdate/<int:articleId>/', views.articleUpdate, name='articleUpdate'),
    path('articleDelete/<int:articleId>/', views.articleDelete, name='articleDelete'),
    path('articleSearch/', views.articleSearch, name='articleSearch'),
    path('articleLike/<int:articleId>/', views.articleLike, name='articleLike'),
    path('commentCreate/<int:articleId>/', views.commentCreate, name='commentCreate'),
    path('commentUpdate/<int:commentId>/', views.commentUpdate, name='commentUpdate'),
    path('commentDelete/<int:commentId>/', views.commentDelete, name='commentDelete'),
    path('person/', views.person, name='person'),
    path('personarticle/', views.personarticle, name='personarticle'),
]