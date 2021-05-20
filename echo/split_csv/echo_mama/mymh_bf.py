import csv
import sys
import pandas as pd
def generate_csvs():
    visits = ['V0','PRO']
    for visit in visits:
        print(visit)
        with open('rawexport/Export'+visit+'ECHO mama_DATA_2021-01-21_IAO.csv','r') as data:
            csv_reader = csv.DictReader(data)
            headers = next(csv_reader,None)
            with open(visit + '/medical_history_biological_family_hhx_mh_bf_pro.csv','w') as new_file:
                fieldnames = ['\ufeffprotect_id','redcap_event_name'] + [header for header in headers if 'mh_bf' in header]
                csv_writer = csv.DictWriter(new_file,fieldnames=fieldnames)
                csv_writer.writeheader()
                for line in csv_reader:
                    mypart = {key:value for (key,value) in line.items() if key in fieldnames}
                    csv_writer.writerow(mypart)
        print(len(fieldnames)) 
def main():
    #check_with_dicts()
    generate_csvs()

if __name__=="__main__":
    main()
