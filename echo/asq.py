import pandas as pd
import helper

import os

asq_files = os.listdir('asqraw')


mapping = {'ECHOBebe_ASQ12_DATA_2021-01-27.csv':'Ess_CNH_ASQ_12_2021_0129_161854.csv',            
        'ECHOEarlyChildhood_ASQ18DATA_2021-01-27.csv' : 'Ess_CNH_ASQ_18_2021_0129_161901.csv',   
        'ECHOEarlyChildhood_ASQ48DATA_2021-01-27.csv' : 'Ess_CNH_ASQ_48_2021_0129_170509.csv',
        'ECHOBebe_ASQ2_DATA_2021-01-27.csv' : 'Ess_CNH_ASQ_2_2021_0129_161828.csv',       
        'ECHOEarlyChildhood_ASQ24DATA_2021-01-27.csv' : 'Ess_CNH_ASQ_24_2021_0129_161907.csv',
        'ECHOEarlyChildhood_ASQ60DATA_2021-01-27.csv' : '',
        'ECHOBebe_ASQ6_DATA_2021-01-27.csv' : 'Ess_CNH_ASQ_6_2021_0129_161841.csv',        
        'ECHOEarlyChildhood_ASQ36DATA_2021-01-27.csv': 'Ess_CNH_ASQ_36_2021_0129_161913.csv',
        'ECHOEarlyChildhood_ASQ60DATA_2021-01-27.csv':'Ess_CNH_ASQ_60_2021_0129_164115.csv'}


def runasq():

    for file in asq_files:

        print(file)
        dict_name = mapping[file]
        print('here')

        print(dict_name)
        ed= pd.read_csv('echo_dictionaries/' + dict_name, encoding='utf-8-sig')
        formname = ed['Uploaded Form ID'].unique()[0]


        need_cols = ed.loc[~ed['Uploaded Variable Name'].isna(),'Uploaded Variable Name'].unique().tolist()

        data = pd.read_csv('asqraw/' + file, dtype=object, encoding='latin-1')
        # print(visit)
        data['crece_id'] = data['crece_id']

        #data = data.merge(df[i], on='protect_id')
        # print(data)
        head = helper.process_head('C')
        head['COHORTPARTICIPANTID'] = head['COHORTPARTICIPANTID']

        final = head.merge(
            data, left_on='COHORTPARTICIPANTID', right_on='crece_id')

        final.loc[:, 'visitname'] = final.loc[:, 'redcap_event_name'].apply(
            lambda x: helper.redcap_event_to_visitname(x))
        
        formdt = [x for x in final.columns if 'formdt' in x][0]

        complete = [x for x in final.columns if 'complete' in x][0]
        respondent = [x for x in final.columns if 'respondent' in x][0]
        otherresp = [x for x in final.columns if 'otherresp' in x][0]
        sequencenum = [x for x in final.columns if 'sequencenum' in x][0]

        final['sequencenum'] = final[sequencenum]

        final.loc[:, 'formdt'] = pd.to_datetime(
            final.loc[:, formdt]).dt.strftime('%m/%d/%Y')
        
        final = final.rename(columns={respondent: 'respondent'})
        final = final.rename(columns={'EWCP_PARTICIPANTID': 'participantid'})
        final = final.rename(columns={otherresp: 'otherresp'})


        final.columns = [x.lower() for x in final.columns]

        if '48' in formname:
            print(final.columns)

        final[need_cols]
        
        final = helper.clean_data(final,0)
        
        
        from datetime import datetime
        datetime.now().date()

        protocolid = final['protocolid'].unique()[0]
        cohortid   = final['cohortid'].unique()[0]
        siteid     = final['siteid'].unique()[0]
        year       = datetime.now().date().year
        day        = datetime.now().date().day

        if len(str(day)) == 1:
            day = '0' + str(day)
        month      = datetime.now().date().month
        if len(str(month)) == 1:
            month = '0' + str(month)
        try:
            mkdir('dataexport/'+formname)
        except:
            pass
        try:
            mkdir('dataexport/'+formname + '/export')
            print('made dir')
        except:
            print('error')
            pass


            
        print('WRITING********************************')
        print(final.shape)
        print('dataexport/' + formname + '/' + \
                                        'pervisit/' + \
                                        str(protocolid) + '_' + \
                                        str(cohortid) + '_' + \
                                        siteid + '_' + \
                                        formname + '_' \
                                        + str(year) + '_' \
                                        + str(month) \
                                        + str(day)
                                        )
        


        final[need_cols].fillna('').to_csv('asqsubmission/' + \
                                        str(protocolid) + '_' + \
                                        str(cohortid) + '_' + \
                                        siteid + '_' + \
                                        formname + '_' \
                                        + str(year) + '_' \
                                        + str(month) \
                                        + str(day) +'.csv', index = False, encoding='utf-8-sig')

def main():
    
    runasq()

    
if __name__ == "__main__":
    main()