from django.db import models
from django.utils.translation import gettext_lazy as _
from django_mtv.core.models import BaseModel
from django_mtv.core.constants import MAX_CHAR_FIELD_NAME_LENGTH


class Student(BaseModel):
    name = models.CharField(
        verbose_name=_("Name"), max_length=MAX_CHAR_FIELD_NAME_LENGTH, unique=True
    )
    code = models.PositiveBigIntegerField(verbose_name=_("Code"), unique=True)
    email = models.EmailField(_("Email"), max_length=MAX_CHAR_FIELD_NAME_LENGTH)
    birth_date = models.DateField(_("Birth date"), auto_now=False, auto_now_add=False)

    class Meta:
        verbose_name = _("Student")
        verbose_name_plural = _("Students")

    def __str__(self):
        return self.name
