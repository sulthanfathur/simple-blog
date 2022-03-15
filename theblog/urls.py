from django.urls import path
# from . import views
from .views import AddCommentView, AddPostView, EditPostView, HomeView, ArticleDetailView, DeletePostView

urlpatterns = [
    # path('', views.home, name="home"),
    path('', HomeView.as_view(), name="home"),
    path('article/<int:pk>', ArticleDetailView.as_view(), name="article-detail"),
    path('create_post/', AddPostView.as_view(), name="add_post"),
    path('article/edit/<int:pk>', EditPostView.as_view(), name="edit_post"),
    path('article/<int:pk>/Remove', DeletePostView.as_view(), name="delete_post"),
    path('article/<int:pk>/Comment', AddCommentView.as_view(), name='add_comment')
]
