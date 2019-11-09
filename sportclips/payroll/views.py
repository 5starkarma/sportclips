from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View

from .forms import UploadForm, ManagerForm, SettingsForm
from .models import PayrollSettings, Reports
from users.models import User
from .payroll import run_payroll

import pandas as pd
import os

pd.options.mode.chained_assignment = None  # default='warn'

filenames = ['/Stylist_Analysis.xls', '/Tips_By_Employee_Report.xls',
             '/Employee_Hours1.xls', '/Employee_Hours2.xls',
             '/SC_Client_Retention_Report.xls',
             '/Employee_Service_Efficiency_SC.xls', '/payroll.xlsx']


def filename_error(request):
    return render(request, 'payroll/filename-error.html')


@login_required
def process_payroll(request):
    current_user = request.user._wrapped if hasattr(
        request.user, '_wrapped') else request.user
    m_form = ManagerForm(
        request.POST, current_user_username=str(current_user))
    if request.method == 'POST':
        m_form = ManagerForm(
            request.POST, current_user_username=str(current_user))
        if m_form.is_valid():
            # store_owner = User.objects.filter(groups__name='owner').last()
            # owner_email = store_owner.email
            # send_mail(
            #     f'{current_user}: Payroll complete!',
            #     f'{current_user} has completed payroll for your Sportclips store.',
            #     'davidalford678@gmail.com',
            #     [owner_email],
            #     fail_silently=False,
            # )
            manager_name = m_form.cleaned_data['manager']
            run_payroll(str(current_user), manager_name)
            file_path = (
                    settings.MEDIA_ROOT + str(current_user) + '/payroll.xlsx')
            if not os.path.isfile(file_path):
                return redirect('filename-error')
            response = HttpResponse(
                open(file_path, 'rb').read())
            response['Content-Type'] = 'mimetype/submimetype'
            response['Content-Disposition'] = 'attachment; filename=payroll.xlsx'
            return response
    return render(
        request, 'payroll/select-manager-run-payroll.html', {'m_form': m_form})

#
@login_required
def delete_old_files(request):
    # Reports.objects.all().delete()
    # current_user = str(request.user)
    # for name in filenames:
    #     name = settings.MEDIA_ROOT + current_user + name
    #     if os.path.isfile(name):
    #         os.remove(name)
    #     else:
    #         pass
    return render(request, 'payroll/payroll.html')


class FileUploadView(View):
    form_class = UploadForm
    success_url = reverse_lazy('home')
    template_name = 'upload.html'

    def get(self, request, *args, **kwargs):
        upload_form = self.form_class()
        return render(
            request, self.template_name, {'upload_form': upload_form})

    def post(self, request, *args, **kwargs):
        upload_form = self.form_class(
            request.POST, request.FILES)
        if upload_form.is_valid():
            form = upload_form.save(commit=False)
            form.user = self.request.user
            form.save()
            return redirect(self.success_url)
        else:
            return render(
                request, self.template_name, {'upload_form': upload_form})


def settings_view(request):
    payrollsettings = PayrollSettings.objects.get(id=1)
    if request.method == 'POST':
        form = SettingsForm(
            request.POST, instance=payrollsettings)
        if form.is_valid():
            form.save()
            messages.success(
                request, f'Your settings have been updated!')
            return redirect('payroll')
    else:
        form = SettingsForm(instance=payrollsettings)
    context = {
        'form': form,
    }
    return render(request, 'payroll/settings.html', context)
