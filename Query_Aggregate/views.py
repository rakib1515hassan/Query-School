from django.shortcuts import render
from Basic_Query.models import Student, Teacher, Query_Code
from django.db import connection
from django.http import HttpResponse

from django.db.models import Q, F, Value, FloatField
from django.db.models.aggregates import Avg, Max, Min, Count, Sum



# Create your views here.
def Query_Aggregate(request):
    return render(request, 'Query\query_aggregate.html')