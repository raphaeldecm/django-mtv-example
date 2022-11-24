from django.shortcuts import render
from django.views.generic import (
    ListView,
    CreateView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django_mtv.students.models import Student
from django_mtv.students.forms import CreateStudentForm


class StudentListView(LoginRequiredMixin, ListView):
    model = Student
    queryset = Student.objects.all()


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = Student
    success_url = reverse_lazy("student-list")
    form_class = CreateStudentForm

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
