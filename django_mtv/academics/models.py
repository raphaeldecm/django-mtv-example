from django.db import models
from django.utils.translation import gettext_lazy as _
from django_mtv.core.models import BaseModel
from django_mtv.core.constants import MAX_CHAR_FIELD_NAME_LENGTH
from django_mtv.students.models import Student
from django.urls import reverse


class Subject(BaseModel):
    name = models.CharField(
        verbose_name=_("Name"), max_length=MAX_CHAR_FIELD_NAME_LENGTH, unique=True
    )

    class Meta:
        verbose_name = _("Subject")
        verbose_name_plural = _("Subjects")

    def __str__(self):
        return self.name


class Course(BaseModel):
    name = models.CharField(
        verbose_name=_("Name"), max_length=MAX_CHAR_FIELD_NAME_LENGTH, unique=True
    )

    subjects = models.ManyToManyField(
        Subject,
        verbose_name=_("Subjects"),
        related_name="courses",
    )

    class Meta:
        verbose_name = _("Course")
        verbose_name_plural = _("Courses")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("course-detail", kwargs={"pk": self.pk})


class Clazz(BaseModel):
    name = models.CharField(
        verbose_name=_("Name"), max_length=MAX_CHAR_FIELD_NAME_LENGTH, unique=True
    )

    subject = models.ForeignKey(
        Subject,
        verbose_name=_("Subject"),
        on_delete=models.PROTECT,
        related_name="classes",
    )

    students = models.ManyToManyField(
        Student,
        verbose_name=_("Students"),
        related_name="courses",
    )

    class Meta:
        verbose_name = _("Class")
        verbose_name_plural = _("Classes")

    def __str__(self):
        return self.name
