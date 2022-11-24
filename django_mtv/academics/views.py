from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django_mtv.academics.models import Course, Clazz
from django_mtv.academics.forms import CreateCourseForm, CreateClazzForm
from django_mtv.academics.filters import CourseFilter


class CourseListView(LoginRequiredMixin, ListView):
    model = Course
    queryset = Course.objects.all()  # prefetch_related("subjects")
    filterset_class = CourseFilter
    paginate_by = 2

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = CourseFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.filterset.form
        return context


class CourseCreateView(LoginRequiredMixin, CreateView):
    model = Course
    form_class = CreateCourseForm
    success_url = reverse_lazy("course-list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)


class CourseDetailView(DetailView):
    model = Course


class CourseUpdateView(UpdateView):
    model = Course
    form_class = CreateCourseForm
    success_url = reverse_lazy("course-list")


class CourseDeleteView(DeleteView):
    model = Course
    success_url = reverse_lazy("course-list")


class ClazzListView(LoginRequiredMixin, ListView):
    model = Clazz


class ClazzCreateView(LoginRequiredMixin, CreateView):
    model = Clazz
    form_class = CreateClazzForm
    success_url = reverse_lazy("clazz-list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)
