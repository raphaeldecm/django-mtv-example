from django_mtv.students.models import Student
from django.forms import ModelForm, CharField, TextInput


class CreateStudentForm(ModelForm):
    birth_date = CharField(
        widget=TextInput(attrs={"class": "data-input", "placeholder": "dd/mm/aaaa"})
    )

    class Meta:
        model = Student
        fields = (
            "name",
            "code",
            "email",
            "birth_date",
        )
