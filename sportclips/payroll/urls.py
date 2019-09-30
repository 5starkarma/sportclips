from django.urls import path, reverse_lazy
from . import views as payroll_views

urlpatterns = [
    path('payroll/', payroll_views.delete_old_files,
         name='payroll'),
    path('filename-error/', payroll_views.filename_error,
         name='filename-error'),
    path('stylist/', payroll_views.FileUploadView.as_view(
        success_url=reverse_lazy('tips'),
        template_name='payroll/stylist.html'),
         name='stylist'),
    path('tips/', payroll_views.FileUploadView.as_view(
        success_url=reverse_lazy('hours1'),
        template_name='payroll/tips.html'),
         name='tips'),
    path('hours1/', payroll_views.FileUploadView.as_view(
        success_url=reverse_lazy('hours2'),
        template_name='payroll/hours1.html'),
         name='hours1'),
    path('hours2/', payroll_views.FileUploadView.as_view(
        success_url=reverse_lazy('client-retention'),
        template_name='payroll/hours2.html'),
         name='hours2'),
    path('client-retention/', payroll_views.FileUploadView.as_view(
        success_url=reverse_lazy('service-efficiency'),
        template_name='payroll/client-retention.html'),
         name='client-retention'),
    path('service-efficiency/', payroll_views.FileUploadView.as_view(
        success_url=reverse_lazy('select_manager_run_payroll'),
        template_name='payroll/service-efficiency.html'),
         name='service-efficiency'),
    path('select-manager-run-payroll/', payroll_views.process_payroll,
         name='select_manager_run_payroll'),
]
