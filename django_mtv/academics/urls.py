from django_mtv.academics.views import (
    CourseListView,
    CourseCreateView,
    CourseDetailView,
    CourseUpdateView,
    CourseDeleteView,
    ClazzListView,
    ClazzCreateView,
)
from django.urls import path

urlpatterns = [
    path("course-list/", CourseListView.as_view(), name="course-list"),
    path("course-create/", CourseCreateView.as_view(), name="course-create"),
    path("course-detail/<int:pk>", CourseDetailView.as_view(), name="course-detail"),
    path("course-update/<int:pk>", CourseUpdateView.as_view(), name="course-update"),
    path("course-delete/<int:pk>", CourseDeleteView.as_view(), name="course-delete"),
    path("clazz-list/", ClazzListView.as_view(), name="clazz-list"),
    path("clazz-create/", ClazzCreateView.as_view(), name="clazz-create"),
]
