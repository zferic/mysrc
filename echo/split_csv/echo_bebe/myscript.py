import csv
import sys
import os
import pandas as pd
# def check_with_dicts():
#     forms_dict = get_forms_in_dict()
#     with open('ECHOBEBEC3_DATA_2020-06-25_ZRP.csv','r') as data:
#         csv_reader = csv.DictReader(data)
#         headers = next(csv_reader,None)
#         completes = [x for x in headers if 'complete' in x]
#         forms = [x.rsplit('_',1)[0] for x in completes]
#         result = {'not in dictionary':[f for f in forms if f not in forms_dict]}
#         print(result)

# def get_headers():
#     with open('ECHOBEBEC3_DATA_2020-06-25_ZRP.csv','r') as data:
#         csv_reader = csv.DictReader(data)
#         headers = next(csv_reader,None)
#         completes = [x for x in headers if 'complete' in x]
#         forms = [x.rsplit('_',1)[0] for x in completes]
#         #print(forms,len(forms))
#         return headers
def create_visit_dirs():
    visits = ['C1','C2','C3']
    for v in visits:
        if not os.path.exists(v):
            os.mkdir(v)
def get_forms_in_dict():
    dicts = pd.read_csv('ECHOBEBE_DataDictionary_2020-06-25_ZRP.csv')
    forms = dicts['Form Name'].unique().tolist()
    return forms[1:]
def generate_csvs_C1C3():
    visits = ['C1','C3']
    #visits = ['C1','C2','C3']

    df = pd.DataFrame(columns = ['form_name','visit'])
    for visit in visits:
        print(visit)
        with open('Export'+visit+'_DATA_2020-08-27_IAO.csv','r') as data:
            csv_reader = csv.DictReader(data)
            headers = next(csv_reader,None)
            completes = [x for x in headers if 'complete' in x]
            formdts =[x for x in headers if 'formdt' in x]
            abrv = [x.rsplit('_',1)[0] for x in formdts]
            forms = [x.rsplit('_',1)[0] for x in completes]
            print(abrv,forms,len(abrv),len(forms))
            for i,form_name in enumerate(abrv):
                with open('Export'+visit+'_DATA_2020-08-27_IAO.csv','r') as data:
                    csv_reader = csv.DictReader(data)
                    with open(visit + '/' + forms[i] + '.csv','w') as new_file:
                        if form_name == 'essi2_c':
                            fieldnames = ['\ufeffcrece_id','redcap_event_name'] + ['support1', 'support2', 'support3', 'support4', 'support5', 'support6','essi2_pin','essi2_c_formdt','essi2_c_respondent','essi2_c_otherresp','essi2_complete']
                        elif form_name == 'cesd2_c':
                            fieldnames = ['\ufeffcrece_id','redcap_event_name'] + ['depression1', 'depression2', 'depression3', 'depression4', 'depression5', 'depression6', 'depression7', 'depression8', 'depression9', 'depression10', 'depression11', 'depression12', 'depression13', 'depression14', 'depression15', 'depression16', 'depression17', 'depression18', 'depression19', 'depression20', 'maternal_depression_cesd2_complete', 'cesd2_pin', 'cesd2_c_formdt', 'cesd2_c_respondent', 'cesd2_c_otherresp']
                        else:    
                            fieldnames = ['\ufeffcrece_id','redcap_event_name'] + [header for header in headers if form_name in header]
                        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames)
                        csv_writer.writeheader()
                        for line in csv_reader:
                            mypart = {key:value for (key,value) in line.items() if key in fieldnames}
                            csv_writer.writerow(mypart)
                if form_name[:3] != 'asq':
                    df = df.append({'form_name':recover_fname(form_name),'visit':visit},ignore_index=True)
        #df.to_csv("form_list.csv")
def generate_csvs_C2():
    visits = ['C2']
    #visits = ['C1','C2','C3']
    df = pd.DataFrame(columns = ['form_name','visit'])
    for visit in visits:
        print(visit)
        with open('Export'+visit+'_DATA_2020-08-27_IAO.csv','r') as data:
            csv_reader = csv.DictReader(data)
            headers = next(csv_reader,None)
            completes = [x for x in headers if 'complete' in x]
            formdts =[x for x in headers if 'formdt' in x]
            abrv = [x.rsplit('_',1)[0] for x in formdts]
            forms = [x.rsplit('_',1)[0] for x in completes]
            print(abrv,forms,len(abrv),len(forms))
            for i,form_name in enumerate(abrv):
                with open('Export'+visit+'_DATA_2020-08-27_IAO.csv','r') as data:
                    csv_reader = csv.DictReader(data)
                    with open(visit + '/' + forms[i] + '.csv','w') as new_file:
                        if form_name == 'essi2_c':
                            fieldnames = ['crece_id','redcap_event_name'] + ['support1', 'support2', 'support3', 'support4', 'support5', 'support6','essi2_pin','essi2_c_formdt','essi2_c_respondent','essi2_c_otherresp','essi2_complete']
                        elif form_name == 'cesd2_c':
                            fieldnames = ['crece_id','redcap_event_name'] + ['depression1', 'depression2', 'depression3', 'depression4', 'depression5', 'depression6', 'depression7', 'depression8', 'depression9', 'depression10', 'depression11', 'depression12', 'depression13', 'depression14', 'depression15', 'depression16', 'depression17', 'depression18', 'depression19', 'depression20', 'maternal_depression_cesd2_complete', 'cesd2_pin', 'cesd2_c_formdt', 'cesd2_c_respondent', 'cesd2_c_otherresp']
                        else:    
                            fieldnames = ['crece_id','redcap_event_name'] + [header for header in headers if form_name in header]
                        csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames)
                        csv_writer.writeheader()
                        for line in csv_reader:
                            mypart = {key:value for (key,value) in line.items() if key in fieldnames}
                            csv_writer.writerow(mypart)
                if form_name[:3] != 'asq':
                    df = df.append({'form_name':recover_fname(form_name),'visit':visit},ignore_index=True)
    #df.to_csv("form_list.csv")
def recover_fname(x):
    forms = get_forms_in_dict()
    if x == 'cesd2_c':
        x = 'cesd2'
    if x == 'essi2_c':
        x = 'essi2'
    fname = [fname for fname in forms if x in fname]
    #print(fname[0])
    return fname[0]

def main():
    create_visit_dirs()
    generate_csvs_C1C3()
    generate_csvs_C2()

if __name__=="__main__":
    main()
