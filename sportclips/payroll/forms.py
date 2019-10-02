from django import forms
from .models import UploadReports, PayrollSettings
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
    manager_service_breakpoint = forms.CharField()
    manager_service_bonus_cap = forms.CharField()
    manager_service_bonus_paid_bb_min = forms.CharField()
    manager_service_bonus_thpc_min = forms.CharField()
    service_bonus_sales_min = forms.CharField()
    service_bonus_cap = forms.CharField()
    service_bonus_take_home_sales_min = forms.CharField()
    service_bonus_paid_bb_min = forms.CharField()
    star_lvl_1_multiplier = forms.CharField()
    star_lvl_1_thpc_min = forms.CharField()
    star_lvl_1_paid_bb_min = forms.CharField()
    star_lvl_1_clients_per_hour_min = forms.CharField()
    star_lvl_2_multiplier = forms.CharField()
    star_lvl_2_thpc_min = forms.CharField()
    star_lvl_2_paid_bb_min = forms.CharField()
    star_lvl_2_clients_per_hour_min = forms.CharField()
    star_lvl_3_multiplier = forms.CharField()
    star_lvl_3_thpc_min = forms.CharField()
    star_lvl_3_paid_bb_min = forms.CharField()
    star_lvl_3_clients_per_hour_min = forms.CharField()
    star_lvl_4_multiplier = forms.CharField()
    star_lvl_4_thpc_min = forms.CharField()
    star_lvl_4_paid_bb_min = forms.CharField()
    star_lvl_4_clients_per_hour_min = forms.CharField()
    take_hm_bonus_lvl_1_sales_min = forms.CharField()
    take_hm_bonus_lvl_1_multiplier = forms.CharField()
    take_hm_bonus_lvl_2_sales_min = forms.CharField()
    take_hm_bonus_lvl_2_multiplier = forms.CharField()

    class Meta:
        model = PayrollSettings
        fields = [
            'manager_service_breakpoint', 'manager_service_bonus_cap',
            'manager_service_bonus_paid_bb_min', 'manager_service_bonus_thpc_min',
            'service_bonus_sales_min', 'service_bonus_cap',
            'service_bonus_take_home_sales_min', 'service_bonus_paid_bb_min',
            'star_lvl_1_multiplier', 'star_lvl_1_thpc_min',
            'star_lvl_1_paid_bb_min', 'star_lvl_1_clients_per_hour_min',
            'star_lvl_2_multiplier', 'star_lvl_2_thpc_min',
            'star_lvl_2_paid_bb_min', 'star_lvl_2_clients_per_hour_min',
            'star_lvl_3_multiplier', 'star_lvl_3_thpc_min',
            'star_lvl_3_paid_bb_min', 'star_lvl_3_clients_per_hour_min',
            'star_lvl_4_multiplier', 'star_lvl_4_thpc_min',
            'star_lvl_4_paid_bb_min', 'star_lvl_4_clients_per_hour_min',
            'take_hm_bonus_lvl_1_sales_min', 'take_hm_bonus_lvl_1_multiplier',
            'take_hm_bonus_lvl_2_sales_min', 'take_hm_bonus_lvl_2_multiplier'
        ]
