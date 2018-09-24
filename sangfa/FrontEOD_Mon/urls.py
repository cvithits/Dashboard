from django.urls import path

from . import views

urlpatterns = [

    path('', views.index, name='index'),

    path('hostlist/', views.show_hostlist, name='show_hostlist'),

    path('view/<str:hostname>/', views.show_tools, name='show_tools'),

    path('viewinfo/<str:hostname>/', views.show_toolsinfo, name='show_toolsinfo'),

    #path('<int:question_id>/', views.detail, name='detail'),

    #path('<int:question_id>/results/', views.results, name='results'),

    #path('<int:question_id>/vote/', views.vote, name='vote'),
]