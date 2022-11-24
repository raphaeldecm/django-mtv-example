from django.forms import CheckboxSelectMultiple, TextInput


class GovbrTextInput(TextInput):
    template_name = "widgets/text.html"


class GovbrCheckboxSelectMultiple(CheckboxSelectMultiple):
    option_template_name = "widgets/checkbox_option.html"
