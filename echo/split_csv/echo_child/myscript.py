import csv
import sys
import pandas as pd
def check_with_dicts():
    forms_dict = get_forms_in_dict()
    with open('ECHOEarlyChildhood_DataDictionary_2020-06-26_ZRP.csv','r') as data:
        csv_reader = csv.DictReader(data)
        headers = next(csv_reader,None)
        completes = [x for x in headers if 'complete' in x]
        forms = [x.rsplit('_',1)[0] for x in completes]
        result = {'not in dictionary':[f for f in forms if f not in forms_dict]}
        print(result)

def get_headers():
    pairs = {}
    visits = ['C4','C5','C6','C7','C8','C9','C10','C11','C13']
    for visit in visits:
        with open('Export_ECHOEarlyChildhood-'+visit+'_DATA_2020-06-26_ZRP.csv','r') as data:
            csv_reader = csv.DictReader(data)
            headers = next(csv_reader,None)
            completes = [x for x in headers if 'complete' in x]
            formdts =[x for x in headers if 'formdt' in x]
            abrv = [x.rsplit('_',1)[0] for x in formdts]
            abrv = [x for x in abrv if 'asq' not in x]
            forms = [x.rsplit('_',1)[0] for x in completes]
            forms = [x for x in forms if 'asq' not in x]

            for x in abrv:
                if x == 'cesd2_c' or 'essi2_c':
                    x = x[:4]
                y = [form for form in forms if x in form][0]
                pairs[x]=y
    print(pairs)

        #return headers
def get_forms_in_dict():
    dicts = pd.read_csv('ECHOEarlyChildhood_DataDictionary_2020-06-26_ZRP.csv')
    forms = dicts['Form Name'].unique().tolist()
    #print(forms)
    return forms[1:]
def generate_csvs():
    visits = ['C6','C9','C10','C12','C13']
    #visits = ['C4','C5','C7','C8','C11','C6','C9','C10','C12','C13']
    #visits = ['C4','C5','C7','C8','C11']
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
                    with open(visit+'/'+forms[i+1] + '.csv','w') as new_file:
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
    #check_with_dicts()
    generate_csvs()
    #get_headers()
    #get_forms_in_dict()
if __name__=="__main__":
    main()
