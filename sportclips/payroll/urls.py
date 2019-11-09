from django.urls import path, reverse_lazy
from . import views as payroll_views

urlpatterns = [
    path(
        'payroll/', payroll_views.delete_old_files,
        name='payroll'),
    path(
        'upload/', payroll_views.FileUploadView.as_view(
        success_url=reverse_lazy('select_manager_run_payroll'),
        template_name='payroll/upload.html'),
        name='upload'),
    path(
        'select-manager-run-payroll/', payroll_views.process_payroll,
        name='select_manager_run_payroll'),
    path(
        'settings/', payroll_views.settings_view,
        name='settings'),
]
