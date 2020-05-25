from django.shortcuts import render

# Create your views here.
from testapp.models import Student
from django.http import HttpResponse
from django.db.models import Avg, Max, Min, Sum,Q
from datetime import date

def home(request):
    # to get all fields of all record
    qs = Student.objects.all()

    # to get only first followed by getting  last record
    qs = Student.objects.first()
    qs = Student.objects.last()


    # to get only first 3 records
    qs = Student.objects.all()[:3]

    # to get last 3 records
    qs = Student.objects.all()[::-1][:3]

    # to get records between 2nd to 4 th record
    qs = Student.objects.all()[1:4]

    # to get specific field from database
    qs = Student.objects.values_list('name')
    qs = Student.objects.values_list('name', 'marks')

    # to get average of marks of student
    qs = Student.objects.all().aggregate(Avg('marks'))
    #Sum
    qs = Student.objects.all().aggregate(Sum('marks'))
    #Max
    qs = Student.objects.all().aggregate(Max('marks'))
    #Min
    qs = Student.objects.all().aggregate(Min('marks'))
    # Avg of first 5 students
    qs = Student.objects.all()[:5].aggregate(Avg('marks'))



    # gte lte exact
    qs = Student.objects.filter(marks__gte=50)
    qs = Student.objects.filter(marks__lte=50)
    qs = Student.objects.filter(marks__exact=99)

    #  startswith endswith  istartswith contains
    qs = Student.objects.filter(name__startswith='p')
    qs = Student.objects.filter(name__endswith='l')
    qs = Student.objects.filter(name__contains='a')



    # date orm
    specific_date= date(2020,4,15)
    qs = Student.objects.filter(dob__exact=specific_date)



    #  using Q for complex queries
    qs = Student.objects.filter(Q(marks__gte=50)& Q(name__startswith='p'))

    # using negetive Q for not conditions
    qs = Student.objects.filter(Q(marks__gte=50) & ~Q(name__startswith='p'))

     # using more 2 queries
    qs = Student.objects.filter(Q(name__startswith='p')&(Q(marks__gt=50)|~Q(name__startswith ='p')))




    print(qs)
    print(type(qs))

    return HttpResponse(qs)
