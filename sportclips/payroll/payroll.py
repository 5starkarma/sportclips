import os
import numpy as np
import pandas as pd
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect


def get_employee_names(test):
    tips_file = 'media/' + test + '/Tips_By_Employee_Report.xls'
    df_employee_names = pd.read_excel(
        tips_file, sheet_name=0, header=None, skiprows=7)
    df_employee_names.rename(
        columns={0: 'Employee'}, inplace=True)
    df_employee_names['Employee'] = \
        df_employee_names['Employee'].str.lower()
    employee_names = df_employee_names.loc[:, 'Employee'].tolist()
    return [(name, name) for name in employee_names]


@login_required
def run_payroll(request, man_name):
    # get current logged in user
    current_user = str(request.user)
    print(current_user)
    # check if file names of uploaded files are correct
    names = ['media/'+current_user+'/Stylist_Analysis.xls',
             'media/'+current_user+'/Tips_By_Employee_Report.xls',
             'media/'+current_user+'/Employee_Hours1.xls',
             'media/'+current_user+'/Employee_Hours2.xls',
             'media/'+current_user+'/SC_Client_Retention_Report.xls',
             'media/'+current_user+'/Employee_Service_Efficiency_SC.xls']
    for name in names:
        if not os.path.isfile(name):
            return redirect('filename-error')

    # place uploaded files into variables
    sar = 'media/'+current_user+'/Stylist_Analysis.xls'
    sar2 = 'media/'+current_user+'/Stylist_Analysis.xls'
    tips = 'media/'+current_user+'/Tips_By_Employee_Report.xls'
    hours_wk1 = 'media/'+current_user+'/Employee_Hours1.xls'
    hours_wk2 = 'media/'+current_user+'/Employee_Hours2.xls'
    retention = 'media/'+current_user+'/SC_Client_Retention_Report.xls'
    efficiency = 'media/'+current_user+'/Employee_Service_Efficiency_SC.xls'
    print('begin payroll now')

    # begin processing payroll
    df_sar = pd.read_excel(
        sar, sheet_name=0, header=None, skiprows=4)
    df_sar2 = pd.read_excel(
        sar2, sheet_name=0, header=None, skiprows=4)
    df_tips = pd.read_excel(
        tips, sheet_name=0, header=None, skiprows=0)
    df_hours1 = pd.read_excel(
        hours_wk1, header=None, skiprows=5)
    df_hours2 = pd.read_excel(
        hours_wk2, header=None, skiprows=5)
    df_retention = pd.read_excel(
        retention, sheet_name=0, header=None, skiprows=8)
    df_efficiency = pd.read_excel(
        efficiency, sheet_name=0, header=None, skiprows=5)

    df_sar.rename(
        columns={0: 'Store', 1: 'First', 2: 'Last', 3: 'Service Clients',
                 4: 'Percent Request', 5: 'Neck Trims',
                 6: 'Take Home Only Clients', 7: 'Total Clients',
                 8: 'Service Sales', 9: 'Take Home Sales', 10: 'Net Sales',
                 11: 'Total Hours', 12: 'Store Hours', 13: 'Non-Store Hours',
                 14: 'Take Home Per Client', 15: 'Total Avg Ticket',
                 16: 'Service Sales Per Hour', 17: 'Clients Per Hour',
                 18: 'Number of MVPs', 19: 'Paid MVP Percent',
                 20: 'Number of Paid Triple Plays',
                 21: 'Paid Triple Play Percent',
                 22: 'Paid BB Percent', 23: '1New Client BB',
                 24: 'New Client BB', 25: 'Number of New Clients',
                 26: 'Percent New Clients', 27: 'Number of Kids',
                 28: 'Percent Kids'}, inplace=True)
    df_sar['Employee'] = df_sar['First'].astype(str) + ' ' + df_sar['Last']
    df_sar['Employee'] = df_sar['Employee'].str.lower()
    df_sar['Paid BB Percent'] = df_sar['Paid BB Percent'].astype('float')

    df_sar.rename(
        columns={0: 'Store', 1: 'First', 2: 'Last', 3: 'Service Clients',
                 4: 'Percent Request', 5: 'Neck Trims',
                 6: 'Take Home Only Clients', 7: 'Total Clients',
                 8: 'Service Sales', 9: 'Take Home Sales',
                 10: 'Net Sales', 11: 'Total Hours', 12: 'Store Hours',
                 13: 'Non-Store Hours', 14: 'Take Home Per Client',
                 15: 'Total Avg Ticket', 16: 'Service Sales Per Hour',
                 17: 'Clients Per Hour', 18: 'Number of MVPs',
                 19: 'Paid MVP Percent', 20: 'Number of Paid Triple Plays',
                 21: 'Paid Triple Play Percent', 22: 'Paid BB Percent',
                 23: '1New Client BB', 24: 'New Client BB',
                 25: 'Number of New Clients', 26: 'Percent New Clients',
                 27: 'Number of Kids', 28: 'Percent Kids'}, inplace=True)

    df_sar['Employee'] = df_sar['First'].astype(str) + ' ' + df_sar['Last']
    df_sar['Employee'] = df_sar['Employee'].str.lower()
    df_sar['Paid BB Percent'] = df_sar['Paid BB Percent'].astype('float') / 100

    df_sar1 = df_sar.loc[:, ['Store', 'Employee',
                             'Total Clients', 'Clients Per Hour',
                             'Service Sales', 'Take Home Sales',
                             'Take Home Per Client', 'Service Sales Per Hour',
                             'Paid BB Percent', 'New Client BB']]

    df_sar.rename(
        columns={0: 'Store', 1: 'First', 2: 'Last', 3: 'Service Clients',
                 4: 'Percent Request', 5: 'Neck Trims',
                 6: 'Take Home Only Clients', 7: 'Total Clients',
                 8: 'Service Sales', 9: 'Take Home Sales', 10: 'Net Sales',
                 11: 'Total Hours', 12: 'Store Hours', 13: 'Non-Store Hours',
                 14: 'Take Home Per Client', 15: 'Total Avg Ticket',
                 16: 'Service Sales Per Hour', 17: 'Clients Per Hour',
                 18: 'Number of MVPs', 19: 'Paid MVP Percent',
                 20: 'Number of Paid Triple Plays',
                 21: 'Paid Triple Play Percent',
                 22: 'Paid BB Percent', 23: '1New Client BB',
                 24: 'New Client BB', 25: 'Number of New Clients',
                 26: 'Percent New Clients', 27: 'Number of Kids',
                 28: 'Percent Kids'}, inplace=True)
    df_sar['Employee'] = df_sar['First'].astype(str) + ' ' + df_sar['Last']
    df_sar['Employee'] = df_sar['Employee'].str.lower()
    df_sar['Paid BB Percent'] = df_sar['Paid BB Percent'].astype('float')

    df_tips['Pay Period'] = df_tips.loc[1, 1]
    df_tips.rename(columns={0: 'Employee', 3: 'Credit Tips'}, inplace=True)
    df_tips = df_tips.drop(df_tips.index[:6])
    df_tips = df_tips.loc[:, ['Employee', 'Credit Tips', 'Pay Period']]
    df_tips['Employee'] = df_tips['Employee'].str.lower()

    df_pp = df_tips.iloc[0, 2]

    df_all_employees = pd.merge(df_sar1, df_tips, how='left', on='Employee').fillna(0)
    df_all_employees['Pay Period'] = df_pp

    df_hours1[0] = df_hours1[0].str.lower()
    df_hours1.rename(columns={0: 'Employee', 1: 'Date', 5: 'Hours1'}, inplace=True)
    df_hours1 = df_hours1.loc[:, ['Employee', 'Date', 'Hours1']]
    df_hours1['Hours1'] = df_hours1[
        'Hours1'].str.replace(r"[a-zA-Z]", '').astype('float')
    df_hours1_002 = df_hours1.dropna(subset=['Employee', 'Date', 'Hours1'])
    df_hours1_003 = df_hours1_002.groupby(['Employee', 'Date']).sum().reset_index()
    df_hours1_003['Regular Hours'] = 0
    df_hours1_003['Regular Hours'] = np.where(
        (df_hours1_003['Hours1']) < 8,
        (df_hours1_003['Hours1']), 8)
    df_hours1_003['OT1'] = 0
    df_hours1_003['OT1'] = np.where(
        (df_hours1_003['Hours1']) > 8,
        (df_hours1_003['Hours1']) - 8,
        (df_hours1_003['OT1']))
    df_hours1_003['Cum hours'] = df_hours1_003.groupby('Employee')['Hours1'].transform('cumsum')
    df_hours1_003['Week OT1'] = np.where(df_hours1_003['Cum hours'] -
                                         df_hours1_003['Hours1'] > 40,
                                         df_hours1_003['Hours1'],
                                         df_hours1_003['Cum hours'] - 40)

    df_hours1_003['OT1'] = np.where(df_hours1_003['Cum hours'] > 40,
                                    df_hours1_003['Week OT1'],
                                    df_hours1_003['OT1'])
    df_hours1_003 = df_hours1_003.loc[:, ['Employee', 'Date', 'Hours1', 'OT1']]
    df_hours1_003 = df_hours1_003.groupby(['Employee']).sum().reset_index()
    resolution = 0.25
    df_hours1_003['Hours1'] = (
        (df_hours1_003[['Hours1']].div(resolution)).round().mul(resolution))
    df_hours1_003['OT1'] = (
        (df_hours1_003[['OT1']].div(resolution)).round().mul(resolution))

    df_hours2[0] = df_hours2[0].str.lower()
    df_hours2.rename(columns={0: 'Employee', 1: 'Date', 5: 'Hours2'}, inplace=True)
    df_hours2 = df_hours2.loc[:, ['Employee', 'Date', 'Hours2']]
    df_hours2['Hours2'] = df_hours2[
        'Hours2'].str.replace(r"[a-zA-Z]", '').astype('float')
    df_hours2_002 = df_hours2.dropna(subset=['Employee', 'Date', 'Hours2'])

    df_hours2_003 = df_hours2_002.groupby(['Employee', 'Date']).sum().reset_index()
    df_hours2_003['Regular Hours'] = 0
    df_hours2_003['Regular Hours'] = np.where(
        (df_hours2_003['Hours2']) < 8,
        (df_hours2_003['Hours2']), 8)
    df_hours2_003['OT2'] = 0
    df_hours2_003['OT2'] = np.where(
        (df_hours2_003['Hours2']) > 8,
        (df_hours2_003['Hours2']) - 8,
        (df_hours2_003['OT2']))

    df_hours2_003['Cum hours'] = df_hours2_003.groupby('Employee')['Hours2'].transform('cumsum')

    df_hours2_003['Week OT2'] = np.where(df_hours2_003['Cum hours'] - df_hours2_003['Hours2'] > 40,
                                         df_hours2_003['Hours2'],
                                         df_hours2_003['Cum hours'] - 40)

    df_hours2_003['OT2'] = np.where(df_hours2_003['Cum hours'] > 40,
                                    df_hours2_003['Week OT2'],
                                    df_hours2_003['OT2'])

    df_hours2_003 = df_hours2_003.loc[:, ['Employee', 'Date', 'Hours2', 'OT2']]

    df_hours2_003 = df_hours2_003.groupby(['Employee']).sum().reset_index()
    resolution = 0.25
    df_hours2_003['Hours2'] = (
        (df_hours2_003[['Hours2']].div(resolution)).round().mul(resolution))
    df_hours2_003['OT2'] = (
        (df_hours2_003[['OT2']].div(resolution)).round().mul(resolution))

    df_all_employees = pd.merge(
        df_all_employees,
        df_hours1_003,
        how='left',
        on='Employee').fillna(0)

    df_all_employees = pd.merge(
        df_all_employees,
        df_hours2_003,
        how='left',
        on='Employee').fillna(0)

    df_all_employees['Total Hours'] = (
            df_all_employees['Hours1'] +
            df_all_employees['Hours2'])

    df_all_employees['Service Sales Min Qualifier'] = 40.0

    df_all_employees['Service Bonus'] = (
            (df_all_employees['Service Sales Per Hour'] -
             df_all_employees['Service Sales Min Qualifier']) *
            (df_all_employees['Paid BB Percent'] *
             df_sar['Store Hours']))

    df_all_employees['Service Bonus'] = np.where(
        (df_all_employees['Service Bonus']) > 150, 150,
        (df_all_employees['Service Bonus'])).round(2)

    df_all_employees['Service Bonus'] = np.where(
        (df_all_employees['Service Bonus']) < 0.01, 0,
        (df_all_employees['Service Bonus'])).round(2)

    df_all_employees['Service Bonus'] = np.where(
        (df_all_employees['Take Home Sales']) < 100, 0,
        (df_all_employees['Service Bonus'])).round(2)

    df_all_employees['Service Bonus'] = np.where(
        (df_all_employees['Paid BB Percent']) < 0.3, 0,
        (df_all_employees['Service Bonus'])).round(2)

    df_all_employees['Take Home Tier'] = np.where(
        df_all_employees['Take Home Sales'] < 99, 0, np.where(
            df_all_employees['Take Home Sales'] > 200, 0.2, 0.1))

    df_all_employees['Take Home Bonus'] = (
            df_all_employees['Take Home Tier'] * df_all_employees['Take Home Sales']).round(2)

    df_all_employees['Star Bonus Increase'] = 0.00

    df_all_employees['Star Bonus Increase'][
        (df_all_employees['Take Home Per Client'] > 1.49) &
        (df_all_employees['Paid BB Percent'] > 0.34) &
        (df_all_employees['Clients Per Hour'] > 1.79)] = 0.25

    df_all_employees['Star Bonus Increase'][
        (df_all_employees['Take Home Per Client'] > 1.74) &
        (df_all_employees['Paid BB Percent'] > 0.39) &
        (df_all_employees['Clients Per Hour'] > 1.99)] = 0.50

    df_all_employees['Star Bonus Increase'][
        (df_all_employees['Take Home Per Client'] > 1.99) &
        (df_all_employees['Paid BB Percent'] > 0.44) &
        (df_all_employees['Clients Per Hour'] > 2.19)] = 1.00

    df_all_employees['Star Bonus Increase'][
        (df_all_employees['Take Home Per Client'] > 2.99) &
        (df_all_employees['Paid BB Percent'] > 0.64) &
        (df_all_employees['Clients Per Hour'] > 2.19)] = 2.00

    df_all_employees['Star Bonus'] = (
            df_all_employees['Star Bonus Increase'] *
            df_all_employees['Total Hours']).round(2)
    df_all_employees = df_all_employees[
        ['Store', 'Employee', 'Pay Period', 'Hours1', 'Hours2',
         'OT1', 'OT2', 'Total Hours', 'Credit Tips', 'Total Clients',
         'Clients Per Hour', 'New Client BB', 'Take Home Sales',
         'Take Home Tier', 'Take Home Per Client', 'Service Sales',
         'Service Sales Per Hour', 'Paid BB Percent',
         'Service Sales Min Qualifier', 'Star Bonus Increase', 'Star Bonus',
         'Service Bonus', 'Take Home Bonus']].fillna(0)

    df_all_employees['OT'] = df_all_employees['OT1'] + df_all_employees['OT2']
    df_all_employees['Holiday'] = ''
    df_all_employees['PTO Hours'] = ''
    df_all_employees['Other Hours/Training'] = ''
    df_all_employees['Other Pay'] = ''
    df_all_employees['Season Ticket Bonus'] = ''
    df_all_employees['Star Level'] = 'N/A'

    df_all_employees['Star Level'][
        (df_all_employees['Take Home Per Client'] > 0.99) &
        (df_all_employees['Paid BB Percent'] > 0.29)] = 'Rising Star!'
    df_all_employees['Star Level'][
        (df_all_employees['Take Home Per Client'] > 1.49) &
        (df_all_employees['Paid BB Percent'] > 0.34) &
        (df_all_employees['Clients Per Hour'] > 1.79)] = 'Star!'
    df_all_employees['Star Level'][
        (df_all_employees['Take Home Per Client'] > 1.74) &
        (df_all_employees['Paid BB Percent'] > 0.39) &
        (df_all_employees['Clients Per Hour'] > 1.99)] = 'All-Star!'
    df_all_employees['Star Level'][
        (df_all_employees['Take Home Per Client'] > 1.99) &
        (df_all_employees['Paid BB Percent'] > 0.44) &
        (df_all_employees['Clients Per Hour'] > 2.19)] = 'MVP!'
    df_all_employees['Star Level'][
        (df_all_employees['Take Home Per Client'] > 2.99) &
        (df_all_employees['Paid BB Percent'] > 0.64) &
        (df_all_employees['Clients Per Hour'] > 2.19)] = 'Platinum!'

    df_all_employees = df_all_employees[[
        'Store', 'Employee', 'Pay Period', 'Hours1', 'Hours2',
        'OT', 'Holiday', 'PTO Hours', 'Other Hours/Training',
        'Other Pay', 'Total Hours', 'Credit Tips',
        'Total Clients', 'Clients Per Hour', 'Take Home Sales',
        'Take Home Tier', 'Take Home Per Client', 'Service Sales',
        'Service Sales Per Hour', 'Paid BB Percent', 'Service Sales Min Qualifier',
        'Star Bonus Increase', 'Star Bonus', 'Service Bonus',
        'Take Home Bonus', 'Season Ticket Bonus', 'Star Level',
        'New Client BB']].fillna(0)

    df_store = df_all_employees[['Store', 'Employee', 'Pay Period', 'Hours1',
                                 'Hours2', 'Total Hours', 'OT', 'Holiday',
                                 'PTO Hours', 'Other Hours/Training',
                                 'Credit Tips', 'Other Pay', 'Service Bonus',
                                 'Take Home Bonus', 'Star Bonus',
                                 'Season Ticket Bonus', 'Star Level']]

    df_all_employees['Client Excitement'] = ''
    df_all_employees['Client Retention'] = ''
    df_all_employees['Return Retention'] = ''
    df_all_employees['Varsity Times'] = ''
    df_all_employees['MVP Times'] = ''

    df_manager = df_all_employees[df_all_employees['Employee'].str.contains(man_name)]
    df_manager['Service Breakpoint'] = 1870
    df_manager['Manager Service Diff'] = (
            df_manager['Service Sales'] -
            df_manager['Service Breakpoint'])
    df_manager['Store BB Percent'] = df_all_employees.iloc[-1, 19]
    df_manager['Service Bonus'] = (
            df_manager['Store BB Percent'] *
            df_manager['Manager Service Diff']).round(2)
    df_manager['Star Bonus'] = 0
    df_manager = df_manager[[
        'Store', 'Pay Period', 'Employee', 'Hours1', 'Hours2',
        'Total Hours', 'OT', 'Holiday', 'PTO Hours',
        'Other Hours/Training', 'Credit Tips', 'Other Pay',
        'Service Bonus', 'Take Home Bonus', 'Star Bonus',
        'Season Ticket Bonus', 'Star Level']]
    df_manager['Service Bonus'] = np.where(
        df_manager['Service Bonus'] > 300, 300,
        df_manager['Service Bonus'])
    df_manager['Service Bonus'] = np.where(
        df_manager['Service Bonus'] < 0, 0,
        df_manager['Service Bonus'])

    df_store.loc[df_store['Employee'] == man_name] = df_manager
    df_store = df_store[:-1]

    df_store.loc[-1] = [
        df_store.loc[1, 'Store'], 'total salon',
        df_store.loc[1, 'Pay Period'],
        df_store['Hours1'].sum(), df_store['Hours2'].sum(),
        df_store['Total Hours'].sum(), df_store['OT'].sum(), '', '', '',
        df_store['Credit Tips'].sum(), '',
        df_store['Service Bonus'].sum(), df_store['Take Home Bonus'].sum(),
        df_store['Star Bonus'].sum(), '', '']

    df_1on1 = df_all_employees[[
        'Store', 'Employee', 'Pay Period', 'Service Sales Per Hour',
        'Paid BB Percent', 'New Client BB', 'Clients Per Hour',
        'Take Home Per Client', 'Client Excitement',
        'Varsity Times', 'MVP Times']].fillna(0)

    df_1on1_2 = df_1on1[:-1]
    df_retention1 = df_retention[[0, 7, 9]]
    df_retention2 = df_retention1[:-1]

    df_retention2.rename(columns={
        0: 'Employee', 7: 'Client Retention',
        9: 'Return Retention'}, inplace=True)

    df_retention2['Employee'] = df_retention2['Employee'].str.lower()

    df_1on1_3 = df_1on1_2.merge(
        df_retention2, how='left', left_on='Employee',
        right_on='Employee').fillna(0)

    df_1on1_4 = df_1on1_3[[
        'Store', 'Employee', 'Pay Period', 'Service Sales Per Hour',
        'Paid BB Percent', 'New Client BB', 'Clients Per Hour',
        'Take Home Per Client', 'Client Retention',
        'Return Retention', 'Client Excitement']]

    df_efficiency = df_efficiency[:-1]
    df_efficiency = df_efficiency[[0, 1, 4]]

    df_efficiency.rename(columns={
        0: 'Employee', 1: 'MVP Times', 4: 'Varsity Times'}, inplace=True)

    df_efficiency['Employee'] = df_efficiency['Employee'].str.lower()

    df_1on1_5 = df_1on1_4.merge(
        df_efficiency, how='left', left_on='Employee',
        right_on='Employee').fillna(0)

    df_1on1_5['New Client BB'] = (df_1on1_5['New Client BB'] / 100)
    df_1on1_5['Client Retention'] = (df_1on1_5['Client Retention'] / 100)
    df_1on1_5['Return Retention'] = (df_1on1_5['Return Retention'] / 100)

    df_1on1_5['Paid BB Percent'] = df_1on1_5['Paid BB Percent'].round(2)
    df_1on1_5['Clients Per Hour'] = df_1on1_5['Clients Per Hour'].round(2)
    df_1on1_5['Take Home Per Client'] = df_1on1_5[
        'Take Home Per Client'].round(2)
    df_1on1_5['Client Retention'] = df_1on1_5['Client Retention'].round(2)
    df_1on1_5['Return Retention'] = df_1on1_5['Return Retention'].round(2)
    df_1on1_5['MVP Times'] = df_1on1_5['MVP Times'].astype('int')
    df_1on1_5['Varsity Times'] = df_1on1_5['Varsity Times'].astype('int')

    df_1on1_5 = df_1on1_5[['Store', 'Employee', 'Pay Period',
                           'Service Sales Per Hour', 'Paid BB Percent',
                           'New Client BB', 'Take Home Per Client',
                           'Clients Per Hour', 'Client Excitement',
                           'Client Retention', 'Return Retention',
                           'Varsity Times', 'MVP Times'
                           ]]

    li = len(df_1on1_5.index)

    # Create variables for dynamic sheet names
    number_rows = len(df_store.index) + 1
    sheet1 = df_1on1.loc[0, 'Store']
    sheet2 = df_1on1_5.loc[0, 'Store'] + ' One-on-One'

    # Create a Pandas Excel writer using XlsxWriter as the engine.
    writer = pd.ExcelWriter(
        'media/'+current_user+'/payroll.xlsx', engine='xlsxwriter')

    # Convert the data-frame to an XlsxWriter Excel object.
    df_store.to_excel(writer, index=False, sheet_name=sheet1)
    df_1on1_5.to_excel(writer, index=False, sheet_name=sheet2)

    # Get the xlsxwriter objects from the data-frame writer object.
    workbook = writer.book
    worksheet1 = writer.sheets[sheet1]
    worksheet2 = writer.sheets[sheet2]

    worksheet2.merge_range('A35:C36', 'Stylist Signature')
    worksheet2.merge_range('D35:E36', 'Date')
    worksheet2.merge_range('F35:I36', 'Managers Note')
    worksheet2.merge_range('A37:C38', 'Stylist Signature')
    worksheet2.merge_range('D37:E38', 'Date')
    worksheet2.merge_range('F37:I38', 'Managers Note')
    worksheet2.merge_range('A39:C40', 'Stylist Signature')
    worksheet2.merge_range('D39:E40', 'Date')
    worksheet2.merge_range('F39:I40', 'Managers Note')
    worksheet2.merge_range('A41:C42', 'Stylist Signature')
    worksheet2.merge_range('D41:E42', 'Date')
    worksheet2.merge_range('F41:I42', 'Managers Note')
    worksheet2.merge_range('A43:C44', 'Stylist Signature')
    worksheet2.merge_range('D43:E44', 'Date')
    worksheet2.merge_range('F43:I44', 'Managers Note')
    worksheet2.merge_range('A45:C46', 'Stylist Signature')
    worksheet2.merge_range('D45:E46', 'Date')
    worksheet2.merge_range('F45:I46', 'Managers Note')
    worksheet2.merge_range('A47:C48', 'Stylist Signature')
    worksheet2.merge_range('D47:E48', 'Date')
    worksheet2.merge_range('F47:I48', 'Managers Note')
    worksheet2.merge_range('A49:C50', 'Stylist Signature')
    worksheet2.merge_range('D49:E50', 'Date')
    worksheet2.merge_range('F49:I50', 'Managers Note')
    worksheet2.merge_range('A51:C52', 'Stylist Signature')
    worksheet2.merge_range('D51:E52', 'Date')
    worksheet2.merge_range('F51:I52', 'Managers Note')
    worksheet2.merge_range('A53:C54', 'Stylist Signature')
    worksheet2.merge_range('D53:E54', 'Date')
    worksheet2.merge_range('F53:I54', 'Managers Note')
    worksheet2.merge_range('A55:C56', 'Stylist Signature')
    worksheet2.merge_range('D55:E56', 'Date')
    worksheet2.merge_range('F55:I56', 'Managers Note')
    worksheet2.merge_range('A57:C58', 'Stylist Signature')
    worksheet2.merge_range('D57:E58', 'Date')
    worksheet2.merge_range('F57:I58', 'Managers Note')

    data_format1 = workbook.add_format(
        {'bg_color': '#ffffff'})
    data_format2 = workbook.add_format(
        {'bg_color': '#e5e5e5'})
    dollar_format = workbook.add_format(
        {'num_format': '$#,##0.00'})
    per_format = workbook.add_format(
        {'num_format': '0%'})
    store_total_format = workbook.add_format(
        {'font_size': 40, 'bold': True})

    worksheet1.conditional_format("$A$1:$Q$%d" % number_rows,
                                   {"type": "formula",
                                    "criteria": '=INDIRECT("B"&ROW())="total salon"',
                                    "format": store_total_format})

    worksheet2.conditional_format(1, 3, li, 3, {
        'type': 'cell', 'criteria': 'less than',
        'value': 3400, 'format': dollar_format})

    worksheet2.conditional_format(1, 4, li, 4, {
        'type': 'cell', 'criteria': 'less than',
        'value': 5, 'format': per_format})

    worksheet2.conditional_format(1, 5, li, 5, {
        'type': 'cell', 'criteria': 'less than',
        'value': 80, 'format': per_format})

    worksheet2.conditional_format(1, 6, li, 6, {
        'type': 'cell', 'criteria': 'less than',
        'value': 100, 'format': dollar_format})

    worksheet2.conditional_format(1, 7, li, 7, {
        'type': 'cell', 'criteria': 'less than',
        'value': 100, 'format': dollar_format})

    worksheet2.conditional_format(1, 8, li, 8, {
        'type': 'cell', 'criteria': 'less than',
        'value': 20, 'format': per_format})

    worksheet2.conditional_format(1, 9, li, 9, {
        'type': 'cell', 'criteria': 'less than',
        'value': 100, 'format': per_format})

    worksheet2.conditional_format(1, 10, li, 10, {
        'type': 'cell', 'criteria': 'less than',
        'value': 100, 'format': per_format})

    for row in range(0, li + 1, 2):
        worksheet1.set_row(row, cell_format=data_format1)
        worksheet1.set_row(row + 1, cell_format=data_format2)
        worksheet1.write(row, 0, None)
        worksheet1.write(row + 1, 0, None)

    for row in range(0, li + 1, 2):
        worksheet2.set_row(row, cell_format=data_format1)
        worksheet2.set_row(row + 1, cell_format=data_format2)
        worksheet2.write(row, 0, None)
        worksheet2.write(row + 1, 0, None)

    chart = workbook.add_chart({'type': 'column'})
    chart1 = workbook.add_chart({'type': 'column', 'num_format': '0%'})
    chart2 = workbook.add_chart({'type': 'column'})

    # [sheet name, first_row, first_col, last_row, last_col]
    chart.add_series({'name': 'Clients Per Hour',
                      'categories': [sheet2, 1, 1, li, 1],
                      'values': [sheet2, 1, 6, li, 6],
                      'gradient': {'colors': ['red', 'black'], }})
    chart1.add_series({'name': 'Paid Back Bar %',
                       'categories': [sheet2, 1, 1, li, 1],
                       'values': [sheet2, 1, 4, li, 4],
                       'gradient': {'colors': ['red', 'black']},
                       'type': 'percentage'})
    chart2.add_series({'name': 'Take Home Per Client',
                       'categories': [sheet2, 1, 1, li, 1],
                       'values': [sheet2, 1, 7, li, 7],
                       'gradient': {'colors': ['red', 'black']}})

    chart.set_x_axis({'num_font': {'rotation': 45}})
    chart1.set_x_axis({'num_font': {'rotation': 45}})
    chart2.set_x_axis({'num_font': {'rotation': 45}})

    chart.set_style(12)
    chart1.set_style(12)
    chart2.set_style(12)

    worksheet2.insert_chart((li + 1), 0, chart, {'x_scale': .65, 'y_scale': 1.5})
    worksheet2.insert_chart((li + 1), 4, chart1, {'x_scale': .65, 'y_scale': 1.5})
    worksheet2.insert_chart((li + 1), 8, chart2, {'x_scale': .7, 'y_scale': 1.5})
    worksheet1.insert_image('O22', 'media/1.png')
    worksheet2.insert_image('J44', 'media/1.png')
    print('save next')

    writer.save()
    workbook.close()
