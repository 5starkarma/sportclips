from django import forms
from .models import Reports, PayrollSettings
from .payroll import get_employee_names


class UploadForm(forms.ModelForm):
    class Meta:
        model = Reports
        fields = (
            'user',
            'stylist_analysis',
            'tips_by_employee',
            'hours_week_1',
            'hours_week_2',
            'client_retention',
            'employee_service_efficiency',
        )
        exclude = ('user',)


class ManagerForm(forms.Form):
    manager = forms.ChoiceField(choices=[], widget=forms.RadioSelect)

    def __init__(self, *args, **kwargs):
        username = kwargs.pop('current_user_username')
        print(username)
        super().__init__(*args, **kwargs)
        self.fields['manager'].choices = get_employee_names()


class SettingsForm(forms.ModelForm):

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
            'take_hm_bonus_lvl_2_sales_min', 'take_hm_bonus_lvl_2_multiplier',
        ]
