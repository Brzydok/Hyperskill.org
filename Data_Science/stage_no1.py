

import pandas as pd
import requests
import os

# scroll down to the bottom to implement your solution

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

    # write your code here
a_df = pd.read_xml("../Data/A_office_data.xml")
b_df = pd.read_xml("../Data/B_office_data.xml")
hr_df = pd.read_xml("../Data/hr_data.xml")

a_df['a_index'] = ['A' + str(x) for x in a_df['employee_office_id']]
a_df = a_df.set_index('a_index', drop=True)
b_df['b_index'] = ['B' + str(x) for x in b_df['employee_office_id']]
b_df = b_df.set_index('b_index', drop=True)
hr_df = hr_df.set_index('employee_id')
print(list(a_df.index))
print(list(b_df.index))
print(list(hr_df.index))

