from django import forms
from .models import UploadReports, PayrollSettings, settings_labels
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
        print(username)
        super().__init__(*args, **kwargs)
        self.fields['manager'].choices = get_employee_names(username)


class SettingsForm(forms.ModelForm):

    class Meta:
        model = PayrollSettings
        fields = settings_labels
