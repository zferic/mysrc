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
    #visits = ['C5','C6','C7','C9','C10','C11','C13']
    visits = ['C4','C8']
    for visit in visits:
        print(visit)
        with open('Export_ECHOEarlyChildhood-'+visit+'_DATA_2020-06-26_ZRP.csv','r') as data:
            csv_reader = csv.DictReader(data)
            headers = next(csv_reader,None)
            completes = [x for x in headers if 'complete' in x]
            formdts =[x for x in headers if 'formdt' in x]
            abrv = [x.rsplit('_',1)[0] for x in formdts]
            forms = [x.rsplit('_',1)[0] for x in completes]
            print(abrv,forms,len(abrv),len(forms))
            for i,form_name in enumerate(abrv):
                with open('Export_ECHOEarlyChildhood-'+visit+'_DATA_2020-06-26_ZRP.csv','r') as data:
                    csv_reader = csv.DictReader(data)
                    if form_name == 'cesd2_c' or form_name == 'essi2_c':
                        continue
                    with open(visit+'/'+forms[i+1] + '.csv','w') as new_file:
                        fieldnames = ['\ufeffcrece_id','redcap_event_name'] + [header for header in headers if form_name in header]
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
    #get_headers()
    #get_forms_in_dict()
if __name__=="__main__":
    main()
