from django import forms
from .models import UploadReports
from .payroll import get_employee_names


class UploadForm(forms.ModelForm):
    class Meta:
        model = UploadReports
        fields = ('xls', 'user', 'path', )
        exclude = ('user', 'path', )


class ManagerForm(forms.Form):
    manager = forms.ChoiceField(choices=[], widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        username = kwargs.pop('current_user_username')
        super().__init__(*args, **kwargs)
        self.fields['manager'].choices = get_employee_names(username)
