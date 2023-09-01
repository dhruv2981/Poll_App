from django.urls import path
from . import views

app_name="polls"
urlpatterns = [
    path("",views.IndexView.as_view(),name='index'),
    path("results/<int:pk>/",views.ResultsView.as_view(),name='results'),
    path("<int:pk>/",views.DetailView.as_view(),name='detail'),
    path("vote/<int:question_id>/",views.vote,name='vote')
]

