from django.shortcuts import render
from Basic_Query.models import Student, Teacher, Query_Code
from django.db import connection
from django.http import HttpResponse

from django.db.models import Q, F, Value, FloatField
from django.db.models.aggregates import Avg, Max, Min, Count, Sum



# Create your views here.
def Query_Aggregate(request):
    return render(request, 'Query\query_aggregate.html')




def Query_301(request):

    ## NOTE For ORM
    # average_salary = Teacher.objects.aggregate(Avg('salary'))['salary__avg']

    ## NOTE For SQL If use raw() then, এই ক্ষেত্রে id দেয়া লাগবে 
    sql_query = """
            SELECT id, AVG(salary) AS avg_salary
            FROM basic_query_teacher
        """
    teacher_data = Teacher.objects.raw(sql_query)

    # Extract the average_salary from the result
    average_salary = teacher_data[0].avg_salary if teacher_data else None

    # NOTE For SQL If use connection.cursor() Then, id দেয়া লাগবে না।
    """
        sql_query = ""
            SELECT AVG(salary) AS avg_salary
            FROM basic_query_teacher
        ""
        
        # Execute the SQL query
        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            result = cursor.fetchone()  # Fetch the result

        # Extract the average_salary from the result
        average_salary = result[0] if result else None
    """

    data = {
            'teacher_obj': Teacher.objects.all(),
            'SQL_querry': teacher_data.query,
            'descripetion': f"""
                        <p>সম্পূর্ন Table থেকে সকল Teachers দের Salary Average বের করা হয়েছে ।</p>
                        <h2 style="color: red;">Average Salary = {average_salary} </h2>  
                        এখানে যদি আমরা Query শেষে ['salary__avg'] না লিখতাম তবে, 'salary__avg': {average_salary}
                        এই ভাবে result পেতাম।
                     """,
            'ORM_querry': f"Teacher.objects.aggregate(Avg('salary'))['salary__avg'])",
            'query': Query_Code.objects.get( query_no = 'Query_301' ),
        }    
    return render(request, 'Result/teacher.html', data)





def Query_302(request):

    ## NOTE For ORM
    # teacher_total_salary = Teacher.objects.aggregate(Sum('salary'))['salary__sum']

    ## NOTE For SQL If use raw() then, এই ক্ষেত্রে id দেয়া লাগবে 
    sql_query = """
            SELECT id, SUM(salary) AS total_salary
            FROM basic_query_teacher
        """
    teacher_data = Teacher.objects.raw(sql_query)

    # Extract the average_salary from the result
    teacher_total_salary = teacher_data[0].total_salary if teacher_data else None

    """We can write it,
        if teacher_data:
            teacher_total_salary = teacher_data[0].total_salary
        else:
            teacher_total_salary = None
    """


    # NOTE For SQL If use connection.cursor() Then, id দেয়া লাগবে না।
    
    sql_query = """
            SELECT SUM(salary) AS total_salary
            FROM basic_query_teacher
        """
    
    # Execute the SQL query
    with connection.cursor() as cursor:
        cursor.execute(sql_query)
        result = cursor.fetchone()  # Fetch the result

    # Extract the average_salary from the result
    teacher_total_salary = result[0] if result else None

    """We can write it,
        if result:
            teacher_total_salary = result[0]
        else:
            teacher_total_salary = None
    """
    

    data = {
            'teacher_obj': Teacher.objects.all(),
            'SQL_querry': teacher_data.query,
            'descripetion': f"""
                        <p>সম্পূর্ন Table থেকে সকল Teachers দের Total Salary বের করা হয়েছে ।</p>
                        <h2 style="color: red;">Total Salary = {teacher_total_salary} </h2>  
                        এখানে যদি আমরা ORM Query শেষে ['salary__sum'] না লিখতাম তবে, 'salary__sum': {teacher_total_salary}
                        এই ভাবে result পেতাম।
                     """,
            'ORM_querry': f"Teacher.objects.aggregate(Avg('salary'))['salary__avg'])",
            'query': Query_Code.objects.get( query_no = 'Query_302' ),
        }    
    return render(request, 'Result/teacher.html', data)
    # return HttpResponse()





def Query_303(request):

    ## NOTE For ORM
    # teacher_minimum_salary = Teacher.objects.aggregate(Min('salary'))['salary__min']

    ## NOTE For SQL If use raw() then, এই ক্ষেত্রে id দেয়া লাগবে 
    sql_query = """
            SELECT id, MIN(salary) AS min_salary
            FROM basic_query_teacher
        """
    teacher_data = Teacher.objects.raw(sql_query)

    # Extract the average_salary from the result
    teacher_minimum_salary = teacher_data[0].min_salary if teacher_data else None

    """We can write it,
        if teacher_data:
            teacher_minimum_salary = teacher_data[0].min_salary
        else:
            teacher_minimum_salary = None
    """


    ## NOTE For SQL If use connection.cursor() Then, id দেয়া লাগবে না।
    # sql_query = """
    #         SELECT MIN(salary) AS min_salary
    #         FROM basic_query_teacher
    #     """
    
    # # Execute the SQL query
    # with connection.cursor() as cursor:
    #     cursor.execute(sql_query)
    #     result = cursor.fetchone()  # Fetch the result

    # # Extract the average_salary from the result
    # teacher_minimum_salary = result[0] if result else None

    """We can write it,
        if result:
            teacher_minimum_salary = result[0]
        else:
            teacher_minimum_salary = None
    """
    

    data = {
            'teacher_obj': Teacher.objects.filter(salary = teacher_minimum_salary),
            # 'SQL_querry': teacher_data.query,
            'descripetion': f"""
                        <p>সম্পূর্ন Table থেকে যার Salary সবথেকে কম তার সেই Amount টা দেখানো হয়েছে।</p>
                        <h2 style="color: red;">Minimum Salary = {teacher_minimum_salary} </h2>  
                        এখানে যদি আমরা ORM Query শেষে ['salary__min'] না লিখতাম তবে, 'salary__min': {teacher_minimum_salary}
                        এই ভাবে result পেতাম।
                     """,
            'ORM_querry': f"Teacher.objects.aggregate(Min('salary'))['salary__min'])",
            'query': Query_Code.objects.get( query_no = 'Query_303' ),
        }    
    return render(request, 'Result/teacher.html', data)
    # return HttpResponse()









def Query_333(request):

    ## NOTE For ORM
    teacher_data = Teacher.objects.aggregate(Avg('salary'))['salary__avg']

    ## NOTE For SQL
    # এই query টি MySQL Database এ চলে, SQLite3 তে চলে না।
    # sql_query = f"""
    #         SELECT * 
    #         FROM basic_query_teacher 
    #         WHERE YEAR(joiningDate) = {_year}
    #     """

    # # SQLite3 এর জন্যে,
    # sql_query = f"""
    #         SELECT * 
    #         FROM basic_query_teacher 
    #         WHERE CAST(strftime('%Y', joiningDate) AS INTEGER) = {_year}
    #     """
    
    # teacher_data = Teacher.objects.raw(sql_query)

    print("------------------------")
    # for row in average_salary:
    #     print("Average Salary:", row.avg_salary)
    # print("Avg Salary:", average_salary)
    print("------------------------")

    data = {
            'teacher_obj': Teacher.objects.all(),
            # 'SQL_querry': teacher_data.query,
            'descripetion': f"""
                        <p>সম্পূর্ন Table থেকে সকল Teachers দের Salary Average বের করা হয়েছে ।</p>
                        <h2 style="color: red;">Average = {teacher_data} </h2>  
                        এখানে যদি আমরা Query শেষে ['salary__avg'] না লিখতাম তবে, 'salary__avg': 107121.2727
                        এই ভাবে result পেতাম।
                     """,
            'ORM_querry': f"Teacher.objects.aggregate(Avg('salary'))['salary__avg'])",
            # 'query': Query_Code.objects.get( query_no = 'Query_201' ),
        }    
    return render(request, 'Result/teacher.html', data)
    # return HttpResponse(teacher_data)


