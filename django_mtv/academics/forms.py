from django_mtv.academics.models import Course, Subject, Clazz
from django_mtv.students.models import Student
from django.forms import (
    ModelForm,
    ModelMultipleChoiceField,
    CheckboxSelectMultiple,
    CharField,
)
from django_mtv.core.widgets import GovbrCheckboxSelectMultiple, GovbrTextInput


class CreateCourseForm(ModelForm):
    class Meta:
        model = Course
        fields = (
            "name",
            "subjects",
        )

    subjects = ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=GovbrCheckboxSelectMultiple,
    )


class CreateClazzForm(ModelForm):
    class Meta:
        model = Clazz
        fields = (
            "name",
            "subject",
            "students",
        )

    name = CharField(widget=GovbrTextInput)
    students = ModelMultipleChoiceField(
        queryset=Student.objects.all(),
        widget=GovbrCheckboxSelectMultiple,
    )
