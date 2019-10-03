from django.db import models
from users.models import User

payroll_settings_labels = [
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


def user_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.user.username, filename)


class UploadReports(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    xls = models.FileField(upload_to=user_directory_path)


class PayrollSettings(models.Model):
    pass


for label in payroll_settings_labels:
    PayrollSettings.add_to_class(label, models.CharField(max_length=16))