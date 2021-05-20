import pandas as pd
import helper

echo = pd.read_csv('echo_dictionaries/Ess_HHx_MH_BF_2020_0521_110531.csv')
V0 = pd.read_csv(
    'split_csv/echo_mama/rawexport/ExportV0ECHO mama_DATA_2021-01-21_IAO.csv')
Pro = pd.read_csv(
    'split_csv/echo_mama/rawexport/ExportPROECHO mama_DATA_2021-01-21_IAO.csv')

addition = ['mh_bf_2s', 'mh_bf_2s_fam___1',
            'mh_bf_2s_fam___2', 'mh_bf_2s_fam___3']
for index, row in V0.iterrows():
    if V0.at[index, 'hypothyroidism'] == 1 or V0.at[index, 'hyperthyroidism'] == 1:
        V0.at[index, 'mh_bf_2s'] = str(1)
    elif V0.at[index, 'hypothyroidism'] == 2 and V0.at[index, 'hyperthyroidism'] == 2:
        V0.at[index, 'mh_bf_2s'] = str(2)
for index, row in V0.iterrows():
    if V0.at[index, 'hypothyroidism2___1'] == 1 or V0.at[index, 'hyperthyroidism2___1'] == 1:
        V0.at[index, 'mh_bf_2s_fam___1'] = str(1)
    elif V0.at[index, 'hypothyroidism2___1'] == 0 and V0.at[index, 'hyperthyroidism2___1'] == 0:
        V0.at[index, 'mh_bf_2s_fam___1'] = str(0)
for index, row in V0.iterrows():
    if V0.at[index, 'hypothyroidism2___2'] == 1 or V0.at[index, 'hyperthyroidism2___2'] == 1:
        V0.at[index, 'mh_bf_2s_fam___2'] = str(1)
    elif V0.at[index, 'hypothyroidism2___2'] == 0 and V0.at[index, 'hyperthyroidism2___2'] == 0:
        V0.at[index, 'mh_bf_2s_fam___2'] = str(0)
for index, row in V0.iterrows():
    if V0.at[index, 'hypothyroidism2___3'] == 1 or V0.at[index, 'hyperthyroidism2___3'] == 1:
        V0.at[index, 'mh_bf_2s_fam___3'] = str(1)
    elif V0.at[index, 'hypothyroidism2___3'] == 0 and V0.at[index, 'hyperthyroidism2___3'] == 0:
        V0.at[index, 'mh_bf_2s_fam___3'] = str(0)
V0 = V0[['protect_id']+addition]

for index, row in Pro.iterrows():
    if Pro.at[index, 'hypothyroidism'] == 1 or Pro.at[index, 'hyperthyroidism'] == 1:
        Pro.at[index, 'mh_bf_2s'] = str(1)
    elif Pro.at[index, 'hypothyroidism'] == 2 and Pro.at[index, 'hyperthyroidism'] == 2:
        Pro.at[index, 'mh_bf_2s'] = str(2)
for index, row in Pro.iterrows():
    if Pro.at[index, 'hypothyroidism2___1'] == 1 or Pro.at[index, 'hyperthyroidism2___1'] == 1:
        Pro.at[index, 'mh_bf_2s_fam___1'] = str(1)
    elif Pro.at[index, 'hypothyroidism2___1'] == 0 and Pro.at[index, 'hyperthyroidism2___1'] == 0:
        Pro.at[index, 'mh_bf_2s_fam___1'] = str(0)
for index, row in Pro.iterrows():
    if Pro.at[index, 'hypothyroidism2___2'] == 1 or Pro.at[index, 'hyperthyroidism2___2'] == 1:
        Pro.at[index, 'mh_bf_2s_fam___2'] = str(1)
    elif Pro.at[index, 'hypothyroidism2___2'] == 0 and Pro.at[index, 'hyperthyroidism2___2'] == 0:
        Pro.at[index, 'mh_bf_2s_fam___2'] = str(0)
for index, row in Pro.iterrows():
    if Pro.at[index, 'hypothyroidism2___3'] == 1 or Pro.at[index, 'hyperthyroidism2___3'] == 1:
        Pro.at[index, 'mh_bf_2s_fam___3'] = str(1)
    elif Pro.at[index, 'hypothyroidism2___3'] == 0 and Pro.at[index, 'hyperthyroidism2___3'] == 0:
        Pro.at[index, 'mh_bf_2s_fam___3'] = str(0)

Pro = Pro[['protect_id']+addition]
#Pro['protect_id'] = Pro['protect_id'].astype(object)


def mh_bf_process():
    visits = ['V0/', 'PRO/']
    df = [V0, Pro]
    for i, visit in enumerate(visits):
        data = pd.read_csv('split_csv/echo_mama/'+str(visit) +
                           'medical_history_biological_family_hhx_mh_bf_pro.csv', dtype=object, encoding='utf-8-sig')
        # print(visit)
        data['protect_id'] = data['protect_id'].astype(int)
        data['medical_history_biological_family_hhx_mh_bf_pro_complete'] = data[
            'medical_history_biological_family_hhx_mh_bf_pro_complete'].astype(int)
        data['medical_history_biological_family_hhx_mh_bf_pro_2_complete'] = data[
            'medical_history_biological_family_hhx_mh_bf_pro_2_complete'].astype(int)
        # print(df[i])
        data = data.merge(df[i], on='protect_id')
        # print(data)
        head = helper.process_head('P')
        head['COHORTPARTICIPANTID'] = head['COHORTPARTICIPANTID'].astype(int)
        final = head.merge(
            data, left_on='COHORTPARTICIPANTID', right_on='protect_id')
        final.loc[:, 'visitname'] = final.loc[:, 'redcap_event_name'].apply(
            lambda x: helper.redcap_event_to_visitname(x))
        final.loc[:, 'formdt'] = pd.to_datetime(
            final.loc[:, 'mh_bf_formdt']).dt.strftime('%m/%d/%Y')
        final = final.rename(columns={'mh_bf_respondent': 'respondent'})
        final = final.rename(columns={'EWCP_PARTICIPANTID': 'participantid'})
        final = final.rename(columns={'mh_bf_otherresp': 'otherresp'})

        for index, row in final.iterrows():
            if final.at[index, 'medical_history_biological_family_hhx_mh_bf_pro_complete'] == 0 or final.at[index, 'medical_history_biological_family_hhx_mh_bf_pro_2_complete'] == 0:
                final.at[index, 'ess_hhx_mh_bf_complete'] = str(0)
            elif final.at[index, 'medical_history_biological_family_hhx_mh_bf_pro_complete'] == 1 or final.at[index, 'medical_history_biological_family_hhx_mh_bf_pro_2_complete'] == 1:
                final.at[index, 'ess_hhx_mh_bf_complete'] = str(1)
            elif final.at[index, 'medical_history_biological_family_hhx_mh_bf_pro_complete'] == 2 and final.at[index, 'medical_history_biological_family_hhx_mh_bf_pro_2_complete'] == 2:
                final.at[index, 'ess_hhx_mh_bf_complete'] = str(2)
        final.columns = [x.lower() for x in final.columns]
        print(final.dtypes)
        final = helper.clean_data(final,0)
        helper.export('Ess_HHx_MH_BF_2020_0521_110531.csv', final, visit)


def main():
    mh_bf_process()


if __name__ == "__main__":
    main()
