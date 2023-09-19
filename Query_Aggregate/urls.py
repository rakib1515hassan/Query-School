from django.urls import path
from Query_Aggregate import views

urlpatterns = [

    path('query-aggregate/', views.Query_Aggregate, name='Query_Aggregate'),


    path('query-301/', views.Query_301, name='Query_301'),
    path('query-302/', views.Query_302, name='Query_302'),
    path('query-303/', views.Query_303, name='Query_303'),


]