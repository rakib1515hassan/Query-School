from django.urls import path
from Query_Time import views

urlpatterns = [

    path('query-time/', views.Query_Time, name='Query_Time'),


    path('query-20/', views.Query_201, name='Query_201'),
    path('query-202/', views.Query_202, name='Query_202'),
    path('query-203/', views.Query_203, name='Query_203'),
    path('query-204/', views.Query_204, name='Query_204'),
    path('query-205/', views.Query_205, name='Query_205'),
    path('query-206/', views.Query_206, name='Query_206'),
    path('query-207/', views.Query_207, name='Query_207'),
    path('query-208/', views.Query_208, name='Query_208'),
    path('query-209/', views.Query_209, name='Query_209'),
    path('query-210/', views.Query_210, name='Query_210'),
    path('query-211/', views.Query_211, name='Query_211'),

]