from django.db import models
from users.models import User


def user_directory_path(instance, filename):
    return '{0}/{1}'.format(instance.user.username, filename)


class UploadReports(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    xls = models.FileField(upload_to=user_directory_path)


class PayrollSettings(models.Model):
    manager_service_breakpoint = models.CharField(max_length=16)
    manager_service_bonus_cap = models.CharField(max_length=16)
    manager_service_bonus_paid_bb_min = models.CharField(max_length=16)
    manager_service_bonus_thpc_min = models.CharField(max_length=16)
    service_bonus_sales_min = models.CharField(max_length=16)
    service_bonus_cap = models.CharField(max_length=16)
    service_bonus_take_home_sales_min = models.CharField(max_length=16)
    service_bonus_paid_bb_min = models.CharField(max_length=16)
    star_lvl_1_multiplier = models.CharField(max_length=16)
    star_lvl_1_thpc_min = models.CharField(max_length=16)
    star_lvl_1_paid_bb_min = models.CharField(max_length=16)
    star_lvl_1_clients_per_hour_min = models.CharField(max_length=16)
    star_lvl_2_multiplier = models.CharField(max_length=16)
    star_lvl_2_thpc_min = models.CharField(max_length=16)
    star_lvl_2_paid_bb_min = models.CharField(max_length=16)
    star_lvl_2_clients_per_hour_min = models.CharField(max_length=16)
    star_lvl_3_multiplier = models.CharField(max_length=16)
    star_lvl_3_thpc_min = models.CharField(max_length=16)
    star_lvl_3_paid_bb_min = models.CharField(max_length=16)
    star_lvl_3_clients_per_hour_min = models.CharField(max_length=16)
    star_lvl_4_multiplier = models.CharField(max_length=16)
    star_lvl_4_thpc_min = models.CharField(max_length=16)
    star_lvl_4_paid_bb_min = models.CharField(max_length=16)
    star_lvl_4_clients_per_hour_min = models.CharField(max_length=16)
    take_hm_bonus_lvl_1_sales_min = models.CharField(max_length=16)
    take_hm_bonus_lvl_1_multiplier = models.CharField(max_length=16)
    take_hm_bonus_lvl_2_sales_min = models.CharField(max_length=16)
    take_hm_bonus_lvl_2_multiplier = models.CharField(max_length=16)
