import csv
import sys
import pandas as pd
def check_with_dicts():
    forms_dict = get_forms_in_dict()
    with open('Export_ECHOMamaECHOPRO_2020-06-17_ZRP.csv','r') as data:
        csv_reader = csv.DictReader(data)
        headers = next(csv_reader,None)
        completes = [x for x in headers if 'complete' in x]
        forms = [x.rsplit('_',1)[0] for x in completes]
        result = {'not in dictionary':[f for f in forms if f not in forms_dict]}
        print(result)

def get_headers():
    with open('Export_ECHOMamaECHOPRO_2020-06-17_ZRP.csv','r') as data:
        csv_reader = csv.DictReader(data)
        headers = next(csv_reader,None)
        completes = [x for x in headers if 'complete' in x]
        forms = [x.rsplit('_',1)[0] for x in completes]
        print(forms,len(forms))
        return headers
def get_forms_in_dict():
    dicts = pd.read_csv('ECHOMama_DataDictionary_2020-06-17_ZRP.csv')
    forms = dicts['Form Name'].unique().tolist()
    return forms[1:]
def generate_csvs(li):
    for form_name in li:
        with open('Export_ECHOMamaECHOPRO_2020-06-17_ZRP.csv','r') as data:
            csv_reader = csv.DictReader(data)
            headers = get_headers()
            with open('PRO/'+recover_fname(form_name).rsplit('_',1)[0] + '.csv','w') as new_file:
                fieldnames = ['\ufeffprotect_id','redcap_event_name'] + [header for header in headers if form_name in header]
                csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames)
                csv_writer.writeheader()
                for line in csv_reader:
                    mypart = {key:value for (key,value) in line.items() if key in fieldnames}
                    csv_writer.writerow(mypart)
        print(form_name,len(fieldnames))
def recover_fname(x):
    forms = get_forms_in_dict()
    fname = [fname for fname in forms if x in fname]
    return fname[0]

def main():
    check_with_dicts()
    form_name = sys.argv[1]
    if form_name == 'all':
        names = ['mh_bf']
    else:
        names = [form_name]
    generate_csvs(names)

if __name__=="__main__":
    main()
