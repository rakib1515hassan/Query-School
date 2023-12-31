from django.urls import path
from Basic_Query.View import create, views

urlpatterns = [
    ## create.py
    path('', create.home, name='home'),
    path('query/', create.Query, name='Query'),
    path('query-code-add/', create.Query_CodeView, name='Query_CodeView'),
    path('Result/', create.Result, name='Result'),

    path('add-student/', create.add_student, name='add_student'),
    path('all-student/', create.all_student, name='all_student'),
    path('add-teacher/', create.add_teacher, name='add_teacher'),
    path('all-teacher/', create.all_teacher, name='all_teacher'),





    ## views.py
    path('query-101/', views.Query_101, name='Query_101'),
    path('query-102/', views.Query_102, name='Query_102'),
    path('query-103/', views.Query_103, name='Query_103'),
    path('query-104/', views.Query_104, name='Query_104'), 
    path('query-105/', views.Query_105, name='Query_105'),
    path('query-106/', views.Query_106, name='Query_106'),
    path('query-107/', views.Query_107, name='Query_107'),
    path('query-108/', views.Query_108, name='Query_108'),
    path('query-109/', views.Query_109, name='Query_109'),
    path('query-110/', views.Query_110, name='Query_110'),
    path('query-111/', views.Query_111, name='Query_111'),
    path('query-112/', views.Query_112, name='Query_112'),
    path('query-113/', views.Query_113, name='Query_113'),
    path('query-114/', views.Query_114, name='Query_114'),
    path('query-115/', views.Query_115, name='Query_115'),

]


