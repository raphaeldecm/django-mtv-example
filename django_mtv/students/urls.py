from django_mtv.students.views import (
    StudentListView,
    StudentCreateView,
)
from django.urls import path

urlpatterns = [
    path("student-list/", StudentListView.as_view(), name="student-list"),
    path("student-create/", StudentCreateView.as_view(), name="student-create"),
]
