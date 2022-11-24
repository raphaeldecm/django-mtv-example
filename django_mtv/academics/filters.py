from django_filters import FilterSet, CharFilter
from django_mtv.academics.models import Course


class CourseFilter(FilterSet):
    name = CharFilter(lookup_expr="icontains")
    model = Course
