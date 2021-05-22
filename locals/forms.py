from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Row, Column, Field

from .models import Local, Executive, Member


class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Field("name")
            )
        )


# MemberForm
class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        exclude = ["local"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field("name"),
            Field("address"),
            Row(
                Column("phone1", css_class="col mt-0"),
                Column("phone2", css_class="col mt-0"),
                css_class="g-4 row mt-1"
            ),
            Field("occupation")
        )

