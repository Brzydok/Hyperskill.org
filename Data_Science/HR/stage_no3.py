import pandas as pd
import requests
import os


if __name__ == '__main__':

    if not os.path.exists('../Data'):
        os.mkdir('../Data')

    # Download data if it is unavailable.
    if ('A_office_data.xml' not in os.listdir('../Data') and
        'B_office_data.xml' not in os.listdir('../Data') and
        'hr_data.xml' not in os.listdir('../Data')):
        print('A_office_data loading.')
        url = "https://www.dropbox.com/s/jpeknyzx57c4jb2/A_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/A_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('B_office_data loading.')
        url = "https://www.dropbox.com/s/hea0tbhir64u9t5/B_office_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/B_office_data.xml', 'wb').write(r.content)
        print('Loaded.')

        print('hr_data loading.')
        url = "https://www.dropbox.com/s/u6jzqqg1byajy0s/hr_data.xml?dl=1"
        r = requests.get(url, allow_redirects=True)
        open('../Data/hr_data.xml', 'wb').write(r.content)
        print('Loaded.')

        # All data in now loaded to the Data folder.

    #  read files
    df_office_A = pd.read_xml("../Data/A_office_data.xml")
    df_office_B = pd.read_xml("../Data/B_office_data.xml")
    df_hr = pd.read_xml("../Data/hr_data.xml")

    #  change indexes
    df_office_A.index = 'A' + df_office_A['employee_office_id'].astype(str)
    df_office_B.index = 'B' + df_office_B['employee_office_id'].astype(str)
    df_hr.index = df_hr['employee_id'].astype(str)

    #  merging after index
    df_offices = pd.concat([df_office_A, df_office_B], ignore_index=False)
    df_total = pd.merge(left=df_offices, right=df_hr, how="inner", left_index=True, right_index=True, indicator=True)
    df_total.drop(columns=["employee_office_id", "employee_id", "_merge"], inplace=True)
    df_total.sort_index(inplace=True)

    #  What are the departments of the top ten employees in terms of working hours?
    df_new = df_total.sort_values(by="average_monthly_hours", ascending=False)
    print(df_new["Department"].head(10).tolist())

    #  What is the total number of projects on which IT department employees with low salaries have worked?
    df_it_low = df_total[(df_total["Department"] == "IT") & (df_total["salary"] == "low")]
    print(df_it_low.number_project.sum())

    #  What are the last evaluation scores and the satisfaction levels of the employees A4, B7064, and A3033?
    employees = df_total.loc[["A4", "B7064", "A3033"]]
    columns = employees[["last_evaluation", "satisfaction_level"]]
    print(columns.values.tolist())

