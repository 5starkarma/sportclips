from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.base import View
from .forms import UploadForm, ManagerForm
from .payroll import run_payroll
import pandas as pd
import os.path

pd.options.mode.chained_assignment = None  # default='warn'


def filename_error(request):
    return render(request, 'payroll/filename-error.html')


@login_required
def get_employee_names(request):
    tips_file = 'media/' + str(request.user) + '/Tips_By_Employee_Report.xls'
    df_employee_names = pd.read_excel(
        tips_file, sheet_name=0, header=None, skiprows=7)
    df_employee_names.rename(
        columns={0: 'Employee'}, inplace=True)
    df_employee_names['Employee'] = \
        df_employee_names['Employee'].str.lower()
    employee_names = df_employee_names.loc[:, 'Employee'].tolist()
    return [(name, name) for name in employee_names]


@login_required
def process_payroll(request):
    user = request.user._wrapped if hasattr(
        request.user, '_wrapped') else request.user
    m_form = ManagerForm(request.POST,
                         current_user_username=request.user.username)
    if request.method == 'POST':
        m_form = ManagerForm(request.POST,
                             current_user_username=request.user.username)
        if m_form.is_valid():
            man_name = m_form.cleaned_data['manager']
            run_payroll(request, man_name)
            file_path = 'media/' + str(user) + '/payroll.xlsx'
            if not os.path.isfile(file_path):
                return redirect('filename-error')
            response = HttpResponse(
                open(file_path, 'rb').read())  # Send HttpResponse for download
            response['Content-Type'] = 'mimetype/submimetype'
            response['Content-Disposition'] = \
                'attachment; filename=payroll.xlsx'
            return response
    return render(request, 'payroll/select-manager-run-payroll.html', {'m_form': m_form})


@login_required
def delete_old_files(request):
    current_user = str(request.user)
    filenames = ['/Stylist_Analysis.xls', '/Tips_By_Employee_Report.xls',
                 '/Employee_Hours1.xls', '/Employee_Hours2.xls',
                 '/SC_Client_Retention_Report.xls',
                 '/Employee_Service_Efficiency_SC.xls', '/payroll.xlsx']
    for name in filenames:
        name = 'media/' + current_user + name
        if os.path.isfile(name):
            os.remove(name)
        else:
            pass
    return render(request, 'payroll/payroll.html')


class FileUploadView(View):
    form_class = UploadForm
    success_url = reverse_lazy('home')
    template_name = 'file_upload.html'

    def get(self, request, *args, **kwargs):
        upload_form = self.form_class()
        return render(request, self.template_name, {'upload_form': upload_form})

    def post(self, request, *args, **kwargs):
        upload_form = self.form_class(
            request.POST, request.FILES)
        if upload_form.is_valid():
            # save the form without commit
            form = upload_form.save(commit=False)
            # request the user
            form.user = self.request.user
            # finish saving the form
            form.save()
            return redirect(self.success_url)
        else:
            return render(
                request, self.template_name,
                {'upload_form': upload_form})
