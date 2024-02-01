from django.db import models
from django_filters import DateFromToRangeFilter, rest_framework, DateTimeFromToRangeFilter
from django_filters.rest_framework import FilterSet

class Student(models.Model):

    name = models.TextField()

    birth_date = models.DateField(
        null=True,
    )


class Course(models.Model):

    name = models.TextField()

    students = models.ManyToManyField(
        Student,
        blank=True,
    )


class FilterCourse(FilterSet):
    date = DateTimeFromToRangeFilter()

    class Meta:
        model = Course
        fields = ['id']
