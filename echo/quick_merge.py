import pandas as pd
from os import listdir
from os import mkdir
import shutil
import os
def merge_forms_from_visits(forms):
    for form in forms:
        print("handling folder " + form)
        if form == '.DS_Store':
            continue
        filenames = listdir('dataexport/' + form + '/pervisit')
        if filenames:
            print(filenames[0].split('~')[0])

            filescsv = [ filename for filename in filenames if filename.endswith( '.csv' ) ]

            files = []

            for file in filescsv:
                print(file)
                tmp = pd.read_csv('dataexport/' + form + '/pervisit/' +file,dtype=object)
                files.append(tmp)

            try:
                mkdir('./dataexport/' + form + '/' + 'export')
            except:
                pass
            pd.concat(files).fillna('').to_csv('dataexport/' + form + '/' + 'export/' + filenames[0].split('~')[0] +'.csv', index = False)
forms = listdir('./dataexport')
forms = [form for form in forms if form != 'quick_merge.py']
merge_forms_from_visits(forms)
for root, dirs, files in os.walk('.'):  # replace the . with your starting directory
    #print(root.rsplit('/',1)[-1])
    if root.rsplit('/',1)[-1] == 'export':
        #shutil.rmtree(root)
        for file in files:
            path_file = os.path.join(root,file)
            shutil.copy2(path_file,'./upload-08-28') 
