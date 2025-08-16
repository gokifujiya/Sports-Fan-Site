from django.urls import path
from . import views

app_name = "core"

urlpatterns = [
    path('', views.index, name='index'),
    path('rules/', views.rules, name='rules'),
    path('notables/', views.notablesList, name='notables_list'),
    path('notables/<int:notablesIndex>/', views.notablesDetail, name='notables_detail'),
    path('externalLinks/', views.externalLinks, name='external_links'),
]
