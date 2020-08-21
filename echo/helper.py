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
 'health_insurance_hic': 'hic',
 'child_birth_information_hhx_cbi': 'cbi',
 'airways_questionnaire_cph_air_inf': 'air_inf',
 'child_physical_examination_cph_cape_i': 'cape_i',
    'child_global_health_cwb_cgb': 'cgb',
     'escala_de_clima_social_familiar_hse_fes_coh': 'fes_coh',
      'household_exposure_to_secondhand_smoke_bpe_heshs_c': 'heshs_c',
       'household_composition_dem_hhc_c': 'hhc_c',
        'income_assistance_financial_strain_dem_iafs_c': 'iafs_c',
         'infant_feeding_practices_chb_ifp': 'ifp',
          'medical_histoy_biological_family_hhx_mh_bf': 'mh_bf',
           'medical_history_infancy_hhx_mh_i': 'mh_i',
             'parenting_scale_hse_pars': 'pars',
                 'rothbart_very_short_form_ribqrvsf': 'ribqrvsf',
                  'maternal_depression_cesd2': 'cesd2',
                   'essi2': 'essi2',
 'adverse_childhood_experience_hse_ace_pr': 'ace_pr',
 'child_physical_examination_cph_cape_c': 'cape_c',
 'complementary_feeding_history_chb_cfh': 'cfh',
 'child_food_source_and_preparation_chb_cfsp': 'cfsp',
 'child_global_health_cwb_cgb': 'cgb',
 'dietary_screener_chb_dsq_pr': 'dsq_pr',
 'early_academic_competencies_srp_eac_pr': 'eac_pr',
 'language_and_acculturation_dem_la_c': 'la_c',
 'medical_hisoty_early_childhood_hhx_mh_ec': 'mh_ec',
 'promis_physical_activity_8a_chb_ppa8a_pp': 'ppa8a_pp',
 'promis_sleep_disturbance_4a_csh_psd4a_pp': 'psd4a_pp',
 'promis_sleeprelated_impairment_4a_csh_psri4a_pp': 'psri4a_pp',
 'modified_checklist_for_autism_rmchatr': 'mchatr',
 'rothbar_early_childhood_recbqvsf': 'recbqvsf',
 }
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
 'health_insurance_hic': 'Ess_HHx_HIC_2020_0603_173916.csv','child_birth_information_hhx_cbi': 'Ess_HHx_CBI_2020_0610_114907.csv',
'airways_questionnaire_cph_air_inf': 'Ess_CPH_Air_Inf_2020_0610_115103.csv',
'child_physical_examination_cph_cape_i': 'Ess_CPH_CAPE_I_2020_0610_115159.csv',
    'child_global_health_cwb_cgb': 'Ess_CWB_CGB_2020_0610_115320.csv',
     'escala_de_clima_social_familiar_hse_fes_coh': 'Ess_HSE_FES_Coh_2020_0610_121328.csv',
      'household_exposure_to_secondhand_smoke_bpe_heshs_c': 'Ess_BPE_HESHS_C_2020_0610_121406.csv',
       'household_composition_dem_hhc_c': 'Ess_Dem_HHC_C_2020_0610_121459.csv',
        'income_assistance_financial_strain_dem_iafs_c': 'Ess_Dem_IAFS_C_2020_0610_121202.csv',
         'infant_feeding_practices_chb_ifp': 'Ess_CHB_IFP_2020_0610_122024.csv',
          'medical_histoy_biological_family_hhx_mh_bf': 'Ess_HHx_MH_BF_2020_0610_122134.csv',
           'medical_history_infancy_hhx_mh_i': 'Ess_HHx_MH_I_2020_0610_122201.csv',
             'parenting_scale_hse_pars': 'Ess_HSE_PARS_2020_0610_122305.csv',
                 'rothbart_very_short_form_ribqrvsf': 'Ess_CNH_RIBQRvSF_2020_0610_122657.csv',
                  'maternal_depression_cesd2': 'Ess_CNP_CESD_2020_0626_182900.csv',
                   'essi2': 'Ess_CNP_ESSI_2020_0626_183620.csv',
'adverse_childhood_experience_hse_ace_pr': 'Ess_HSE_ACE_PR_2020_0628_155336.csv',
 'child_physical_examination_cph_cape_c': 'Ess_CPH_CAPE_C_2020_0628_155420.csv',
 'complementary_feeding_history_chb_cfh': 'Ess_CHB_CFH_2020_0628_155502.csv',
 'child_food_source_and_preparation_chb_cfsp': 'Ess_CHB_CFSP_2020_0628_155516.csv',
 'child_global_health_cwb_cgb': 'Ess_CWB_CGB_2020_0610_115320.csv',
 'dietary_screener_chb_dsq_pr': 'Ess_CHB_DSQ_PR_2020_0628_155543.csv',
 'early_academic_competencies_srp_eac_pr': 'Ess_SRP_EAC_PR_2020_0628_155613.csv',
 'language_and_acculturation_dem_la_c': 'Ess_Dem_LA_C_2020_0628_155716.csv',
 'medical_hisoty_early_childhood_hhx_mh_ec': 'Ess_HHx_MH_EC_2020_0629_130650.csv',
 'promis_physical_activity_8a_chb_ppa8a_pp': 'Ess_CHB_PPA8a_PP_2020_0628_155907.csv',
 'promis_sleep_disturbance_4a_csh_psd4a_pp': 'Ess_CSH_PSD4a_PP_2020_0628_155934.csv',
 'promis_sleeprelated_impairment_4a_csh_psri4a_pp': 'Ess_CSH_PSRI4a_PP_2020_0628_155947.csv',
 'modified_checklist_for_autism_rmchatr': 'Rec_RCh_MCHATR_2020_0628_160123.csv',
 'rothbar_early_childhood_recbqvsf': 'Ess_CNH_RECBQvSF_2020_0628_160228.csv'}
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
    if x =='c1_inf01_arm_1':
        return 'Inf01'
    if x == 'c2_inf02_arm_1':
        return 'Inf02'
    if x == 'c3_inf03_arm_1':
        return 'Inf03'
    if x =='c4_ec01_arm_1':
        return 'EC01'
    if x == 'c5_ec02_arm_1':
        return 'EC02'
    if x == 'c6_ec03_arm_1':
        return 'EC03'
    if x =='c7_ec04_arm_1':
        return 'EC04'
    if x == 'c8_ec05_arm_1':
        return 'EC05'
    if x == 'c9_ec06_arm_1':
        return 'EC06'
    if x =='c10_ec07_arm_1':
        return 'EC07'
    if x == 'c11_ec08_arm_1':
        return 'EC08'
    if x == 'c12_ec09_arm_1':
        return 'EC09'
    if x == 'c13_ec10_arm_1':
        return 'EC10'
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
def formdt_respondent_complete2(abrv,echo,form,i):
    abrv = abrv[form]
    echo = echo[form]
    if i == 1:
        return abrv+ '_c'+'_formdt'
    if i == 2:
        return abrv+ '_c'+'_respondent'
    if i == 3:
        return abrv+ '_c'+'_otherresp'
    else:
        return 'ftr_complete'
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
    print(final.shape)
    final = final.loc[final['formdt'] != 'NaT',:]
    #final = final.loc[~final[pin].isna(),:]
    final.replace('_6','-6',inplace=True)
    final.replace('_7','-7',inplace=True)
    final.replace('_8','-8',inplace=True)
    print(final.shape)
    return final

def process_head(participant):
    consent_echoALL = pd.read_excel('ParticipantRegistration_Export.xlsx')
    consent_echoALL.columns = [x.upper() for x in consent_echoALL.columns]
    cool = ['protocolid', 'cohortid', 'pin','siteid', 'EWCP_participantid','COHORTPARTICIPANTID','PARTICIPANTTYPE']
    head = consent_echoALL[[x.upper() for x in cool]]
    return head[head['PARTICIPANTTYPE'] == participant]
    
