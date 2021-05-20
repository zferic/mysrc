import csv
import sys
import pandas as pd
import os
# def check_with_dicts():
#     forms_dict = get_forms_in_dict()
#     with open('Export_ECHOMamaECHOPRO_2020-06-17_ZRP.csv','r') as data:
#         csv_reader = csv.DictReader(data)
#         headers = next(csv_reader,None)
#         completes = [x for x in headers if 'complete' in x]
#         forms = [x.rsplit('_',1)[0] for x in completes]
#         result = {'not in dictionary':[f for f in forms if f not in forms_dict]}
#         print(result)

# def get_headers():
#     with open('Export_ECHOMamaECHOPRO_2020-06-17_ZRP.csv','r') as data:
#         csv_reader = csv.DictReader(data)
#         headers = next(csv_reader,None)
#         completes = [x for x in headers if 'complete' in x]
#         forms = [x.rsplit('_',1)[0] for x in completes]
#         print(forms,len(forms))
#         return headers
def create_visit_dirs():
    visits = ['V0','V1','V2','V3','PRO']
    for v in visits:
        if not os.path.exists(v):
            os.mkdir(v)
def get_forms_in_dict():
    dicts = pd.read_csv('dictionary/ECHOMama_DataDictionary_2021-01-19_IAO.csv')
    forms = dicts['Form Name'].unique().tolist()
    print(forms)
    return forms[1:]
def generate_csvs_V1V2():
    visits = ['V1','V2']
    #visits = ['V0','V1','V2','V3','PRO']
    df = pd.DataFrame(columns = ['form_name','visit'])
    for visit in visits:
        print(visit)
        with open('rawexport/Export'+visit+'ECHO mama_DATA_2021-01-21_IAO.csv','r') as data:
            csv_reader = csv.DictReader(data)
            headers = next(csv_reader,None)
            completes = [x for x in headers if 'complete' in x]
            formdts =[x for x in headers if 'formdt' in x]
            abrv = [x.rsplit('_',1)[0] for x in formdts]
            forms = [x.rsplit('_',1)[0] for x in completes]

            
            print(abrv,forms,len(abrv),len(forms))
            for i,form_name in enumerate(abrv):
                with open('rawexport/Export'+visit+'ECHO mama_DATA_2021-01-21_IAO.csv','r') as data:
                    csv_reader = csv.DictReader(data)
                    if form_name == 'mh_bf' or form_name == 'mh_bf_formdt':
                        continue
                    with open(visit + '/' + forms[i] + '.csv','w') as new_file:

                        if form_name == 'c19_apv':
                            print('here*********************')
                            fieldnames = ['protect_id','redcap_event_name'] + [header for header in headers if form_name in header \
                                                                                                or header == 'covid19_adult_primary_complete' ]
                            print([header for header in headers if form_name in header \
                                                                                                or header == 'covid19_adult_primary_complete' ])                                                              
                        else:
                            fieldnames = ['protect_id','redcap_event_name'] + [header for header in headers if form_name in header]
                        
                        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames)
                        csv_writer.writeheader()
                        for line in csv_reader:
                            mypart = {key:value for (key,value) in line.items() if key in fieldnames}
                            csv_writer.writerow(mypart)
                #df = df.append({'form_name':recover_fname(form_name),'visit':visit},ignore_index=True)
    #df.to_csv("form_list.csv")

def generate_csvs_V0V3PRO():
    visits = ['V0','V3','PRO']
    #visits = ['V0','V1','V2','V3','PRO']
    df = pd.DataFrame(columns = ['form_name','visit'])
    for visit in visits:
        print(visit)
        with open('rawexport/Export'+visit+'ECHO mama_DATA_2021-01-21_IAO.csv','r') as data:
            csv_reader = csv.DictReader(data)
            headers = next(csv_reader,None)
            completes = [x for x in headers if 'complete' in x]
            formdts =[x for x in headers if 'formdt' in x]
            abrv = [x.rsplit('_',1)[0] for x in formdts]
            forms = [x.rsplit('_',1)[0] for x in completes]
            print(abrv,forms,len(abrv),len(forms))
            for i,form_name in enumerate(abrv):
                with open('rawexport/Export'+visit+'ECHO mama_DATA_2021-01-21_IAO.csv','r') as data:
                    csv_reader = csv.DictReader(data)
                    if form_name == 'mh_bf' or form_name == 'mh_bf_formdt':
                        continue

                    print(form_name)
                    with open(visit + '/' + forms[i] + '.csv','w') as new_file:
                        if form_name == 'c19_apv':
                            print('here')
                            fieldnames = ['\ufeffprotect_id','redcap_event_name'] + [header for header in headers if form_name in header \
                                                                                                or 'covid19_adult_primary_complete' in header]
                        else:
                            fieldnames = ['\ufeffprotect_id','redcap_event_name'] + [header for header in headers if form_name in header]
                        
                        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames)
                        csv_writer.writeheader()
                        for line in csv_reader:
                            mypart = {key:value for (key,value) in line.items() if key in fieldnames}
                            csv_writer.writerow(mypart)
                #df = df.append({'form_name':recover_fname(form_name),'visit':visit},ignore_index=True)

def recover_fname(x):
    print(x)
    forms = get_forms_in_dict()
    fname = [fname for fname in forms if x in fname]
    print(fname)
    return fname[0]

def main():
    #check_with_dicts()
    create_visit_dirs()
    generate_csvs_V1V2()
    generate_csvs_V0V3PRO()

if __name__=="__main__":
    main()
