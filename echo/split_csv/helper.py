import pandas as pd
from os import listdir,mkdir 
abrv = {'household_composition_dem_hhc_p': 'hhc_p',
 'income_assistance_financial_strain_dem_iafs_p': 'iafs_p',
 'language_and_acculturation_dem_la_p': 'la_p',
 'lifestyle_prg_life_pp': 'life_pp',
 'maternal_food_source_and_preparation_prg_mfsp': 'mfsp',
 'caregiver_occupation_and_employment_dem_occ_cg': 'occ_cg',
 'promis_global_health_scale_cnp_pgh': 'pgh',
 'promis_sleep_disturbance_4a_prg_psd4a': 'psd4a',
 'promis_sleeprelated_impairment_4a_prg_psri4a': 'psri4a',
 'perceived_stress_scale_cnp_pss10': 'pss10',
 'the_everyday_discrimination_scale_cnp_weds': 'weds',
 'health_insurance_coverage_ess_hhx_hic': 'hic'}
echo = {'household_composition_dem_hhc_p': 'Ess_Dem_HHC_P_2020_0521_104635.csv',
 'income_assistance_financial_strain_dem_iafs_p': 'Ess_Dem_IAFS_P_2020_0521_104952.csv',
 'language_and_acculturation_dem_la_p': 'Ess_Dem_LA_P_2020_0521_105232.csv',
 'lifestyle_prg_life_pp': 'Ess_Prg_Life_PP_2020_0521_110120.csv',
 'maternal_food_source_and_preparation_prg_mfsp': 'Ess_Prg_MFSP_2020_0521_110321.csv',
 'caregiver_occupation_and_employment_dem_occ_cg': 'Ess_Dem_Occ_CG_2020_0521_114108.csv',
 'promis_global_health_scale_cnp_pgh': 'Ess_CNP_PGH_2020_0521_114843.csv',
 'promis_sleep_disturbance_4a_prg_psd4a': 'Ess_Prg_PSD4a_2020_0521_120207.csv',
 'promis_sleeprelated_impairment_4a_prg_psri4a': 'Ess_Prg_PSRI4a_2020_0521_120500.csv',
 'perceived_stress_scale_cnp_pss10': 'Ess_CNP_PSS10_2020_0521_120657.csv',
 'the_everyday_discrimination_scale_cnp_weds': 'Ess_CNP_WEDS_2020_0521_120844.csv',
 'health_insurance_coverage_ess_hhx_hic': 'Ess_HHx_HIC_2020_0603_173916.csv'}
def redcap_event_to_visitname(x):

    if x =='v0_pre01_arm_1':
        return 'Pre01'
    if x == 'v1_pre02_arm_1':
        return 'Pre02'
    if x == 'v2_pre03_arm_1':
        return 'Pre03'
    if x == 'v3_pre04_arm_1':
        return 'Pre04'
    if x == 'echopro_pre05_arm_1':
        return 'Pre05'
def formdt_respondent_complete(abrv,echo,form,i):
    abrv = abrv[form]
    echo = echo[form]
    if i == 1:
        return abrv+'_formdt'
    if i == 2:
        return abrv+'_respondent'
    if i == 3:
        return abrv+'_otherresp'
    else:
        return echo.rsplit('_',3)[0]+'_complete'
def export(export_form,final,visit):
    #print(final.head())
    ed = pd.read_csv('echo_dictionaries/' + export_form)
    need_cols = ed.loc[~ed['Uploaded Variable Name'].isna(),'Uploaded Variable Name'].unique().tolist()
    #print(need_cols)
    formname = ed['Uploaded Form ID'].unique()[0]
    print(formname)

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
        mkdir('dataexport/'+formname + '/pervisit')
    except:
        pass

    final[need_cols].fillna('').to_csv('dataexport/' + formname + '/' + \
                                    'pervisit/' + \
                                    str(protocolid) + '_' + \
                                    str(cohortid) + '_' + \
                                    siteid + '_' + \
                                    formname + '_' \
                                    + str(year) + '_' \
                                    + str(month) \
                                    + str(day) +  \
                                    '~' + str(visit[:-1]) +'.csv', index = False, encoding='utf-8-sig')
def clean_data(final):
    final = final.loc[final['formdt'] != 'NaT',:]
    #final = final.loc[~final[pin].isna(),:]
    final.replace('_6','-6',inplace=True)
    final.replace('_7','-7',inplace=True)
    final.replace('_8','-8',inplace=True)
    print(final.shape)
    return final
consent_echoALL = pd.read_excel('ParticipantRegistration_Export.xlsx')

consent_echoALL.columns = [x.upper() for x in consent_echoALL.columns]
cool = ['protocolid', 'cohortid', 'pin','siteid', 'EWCP_participantid','COHORTPARTICIPANTID','PARTICIPANTTYPE']
head = consent_echoALL[[x.upper() for x in cool]]

head_P = head[head['PARTICIPANTTYPE'] == 'P']
