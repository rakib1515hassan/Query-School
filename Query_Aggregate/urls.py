from django.urls import path
from Query_Aggregate import views

urlpatterns = [

    path('query-aggregate/', views.Query_Aggregate, name='Query_Aggregate'),


    # path('query-301/', views.Query_301, name='Query_301'),


]