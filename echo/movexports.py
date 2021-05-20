import pandas as pd
import os
import shutil

def main():
    'program to move generated exports to outexports for conversion to echo format'

    subdirs = ['echo_bebe', 'echo_child', 'echo_mama']
    bebe_vs = ['C1','C2','C3']
    child_vs = ['C13','C7', 'C9', 'C12', 'C8', 'C6','C4', 'C10', 'C5', 'C11']
    mama_vs = ['V1', 'V0', 'PRO', 'V2', 'V3']

    for dirs in subdirs:

        if dirs == 'echo_bebe':
            
            for x in bebe_vs:
                path = '/users/zlatanferic/Documents/ECHO Prep/mysrc/echo/split_csv/'+ dirs +'/'+x +'/'
                files = os.listdir(path)
                try:
                    os.mkdir('/users/zlatanferic/Documents/ECHO Prep/mysrc/echo/outputexports/' + x)
                except:
                    print('exists')

                for file in files:
                    shutil.copy(path + file, "/users/zlatanferic/Documents/ECHO Prep/mysrc/echo/outputexports/" + x + '/' + file)
                    
        if dirs == 'echo_child':
        
            for x in child_vs:
                path = '/users/zlatanferic/Documents/ECHO Prep/mysrc/echo/split_csv/'+ dirs +'/'+x +'/'
                files = os.listdir(path)

                try:
                    os.mkdir('/users/zlatanferic/Documents/ECHO Prep/mysrc/echo/outputexports/' + x)
                except:
                    print('exists')

                for file in files:
                    shutil.copy(path + file, "/users/zlatanferic/Documents/ECHO Prep/mysrc/echo/outputexports/" + x + '/' + file)
                    
        if dirs == 'echo_mama':
            
            for x in mama_vs:
                path = '/users/zlatanferic/Documents/ECHO Prep/mysrc/echo/split_csv/'+ dirs +'/'+x +'/'
                files = os.listdir(path)

                try:
                    os.mkdir('/users/zlatanferic/Documents/ECHO Prep/mysrc/echo/outputexports/' + x)
                except:
                    print('exists')

                for file in files:
                    shutil.copy(path + file, "/users/zlatanferic/Documents/ECHO Prep/mysrc/echo/outputexports/" + x + '/' + file)

if __name__ == "__main__":
    main()
