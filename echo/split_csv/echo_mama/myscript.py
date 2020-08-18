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
def generate_csvs():
    visits = ['V0','V1','V2','V3','PRO']
    for visit in visits:
        print(visit)
        with open('Export'+visit+'ECHO mama_DATA_2020-08-12_ZRP.csv','r') as data:
            csv_reader = csv.DictReader(data)
            headers = next(csv_reader,None)
            completes = [x for x in headers if 'complete' in x]
            formdts =[x for x in headers if 'formdt' in x]
            abrv = [x.rsplit('_',1)[0] for x in formdts]
            forms = [x.rsplit('_',1)[0] for x in completes]
            print(abrv,forms,len(abrv),len(forms))
            for i,form_name in enumerate(abrv):
                with open('Export'+visit+'ECHO mama_DATA_2020-08-12_ZRP.csv','r') as data:
                    csv_reader = csv.DictReader(data)
                    if form_name == 'mh_bf' or form_name == 'mh_bf_formdt':
                        continue
                    with open(visit + '/' + forms[i+1] + '.csv','w') as new_file:
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
    #check_with_dicts()
    generate_csvs()

if __name__=="__main__":
    main()
