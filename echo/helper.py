import pandas as pd
from os import listdir,mkdir 
import numpy as np

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
'dietary_screener_chb_dsq_pr': 'dsq_pr',
'early_academic_competencies_srp_eac_pr': 'eac_pr',
'language_and_acculturation_dem_la_c': 'la_c',
'medical_hisoty_early_childhood_hhx_mh_ec': 'mh_ec',
'promis_physical_activity_8a_chb_ppa8a_pp': 'ppa8a_pp',
'promis_sleep_disturbance_4a_csh_psd4a_pp': 'psd4a_pp',
'promis_sleeprelated_impairment_4a_csh_psri4a_pp': 'psri4a_pp',
'modified_checklist_for_autism_rmchatr': 'mchatr',
'rothbar_early_childhood_recbqvsf': 'recbqvsf',
'residential_address_history_dem_addr_c':'addr_c',
'airways_questionnaire_early_childhood_air_ec':  'air_ec',
'sleep_health_mshprg': 'mshprg',
'demographics_of_biological_family_dem_b':'dem_b',
'health_insurance_coverage_hic': 'hic',
'health_inssurance_hic': 'hic',
'child_behavior_checklist_cnh_cbcl_pre':'cbcl_pre',
'sleep_health_of_infants_shinf': 'shinf',
'demographics_of_child_dem_c': 'dem_c',
'household_chemical_exposures_bpe_hcexp_pp':'hcexp_pp',
'nih_toolbox_srp_ntppi_pr':'ntppi_pr',
'social_responsive_scale_srs2_pre': 'srs2_pre',
'medical_history_biological_family_hhx_mh_bf':'mh_bf',
'demographics_of_primary_caregiver_dem_cg':'dem_cg',
'occupation_exposure_bpe_oexp_pp':'oexp_pp',
'health_insurance_coverage_ess_hhx_hic':'hic',
'household_chemical_exposure_bpe_hcexp_c':'hcexp_c' ,
'sleep_health_of_children_and_adolescents_shca_pr':'shca_pr',

'ess_dem_ck12e':'ck12e',
'dietary_screener_prg_dsq_sr':'dsq_sr',
'residential_address_history_dem_addr_p':'addr_p',
'covid19_child_parent_report':'c19_cpr',
'covid19_adult_primary':'c19_apv',
'early_care_and_education_dem_ece':'ece',


'asq_cuestionario_de_48_meses':'asq48',
'asq_cuestionario_de_24_meses':'asq24',
'asq_cuestionario_de_36_meses':'asq36',
'asq_cuestionario_de_8_meses': 'asq8',
'asq_cuestionario_de_18_meses': 'asq18',
'asq_cuestionario_de_6_meses': 'asq6',
'asq_cuestionario_de_12_meses':'asq12',
'asq_cuestionario_de_2_meses': 'asq2',
'asq_cuestionario_de_60_meses':'asq60',



}


echo = {'household_composition_dem_hhc_p': 'Ess_Dem_HHC_P_2021_0126_130304.csv',
'income_assistance_financial_strain_dem_iafs_p': 'Ess_Dem_IAFS_P_2021_0126_130337.csv',
'language_and_acculturation_dem_la_p': 'Ess_Dem_LA_P_2021_0126_130407.csv',
'lifestyle_prg_life_pp': 'Ess_Prg_Life_PP_2021_0126_130746.csv',
'maternal_food_source_and_preparation_prg_mfsp': 'Ess_Prg_MFSP_2021_0126_130813.csv',

'caregiver_occupation_and_employment_dem_occ_cg': 'Ess_Dem_Occ_CG_2021_0126_130420.csv',
'promis_global_health_scale_cnp_pgh': 'Ess_CNP_PGH_2021_0126_125757.csv',

'promis_sleep_disturbance_4a_prg_psd4a': 'Ess_Prg_PSD4a_2021_0128_104200.csv',
'promis_sleeprelated_impairment_4a_prg_psri4a':'Ess_Prg_PSRI4a_2021_0128_104150.csv',

'perceived_stress_scale_cnp_pss10': 'Ess_CNP_PSS10_2021_0126_125817.csv',
'the_everyday_discrimination_scale_cnp_weds': 'Ess_CNP_WEDS_2021_0126_125831.csv',

'health_insurance_hic': 'Ess_HHx_HIC_2021_0126_130533.csv',
'child_birth_information_hhx_cbi': 'Ess_HHx_CBI_2021_0126_130515.csv',
'airways_questionnaire_cph_air_inf': 'Ess_CPH_Air_Inf_2021_0126_125858.csv',
'child_physical_examination_cph_cape_i': 'Ess_CPH_CAPE_I_2021_0126_125921.csv',
'child_global_health_cwb_cgb': 'Ess_CWB_CGB_2021_0126_130043.csv',

########################
'escala_de_clima_social_familiar_hse_fes_coh': 'Ess_HSE_FES_Coh_2021_0126_130654.csv',
'household_exposure_to_secondhand_smoke_bpe_heshs_c': 'Ess_BPE_HESHS_C_2021_0126_124744.csv',
'household_composition_dem_hhc_c': 'Ess_Dem_HHC_C_2021_0126_130248.csv',
'income_assistance_financial_strain_dem_iafs_c': 'Ess_Dem_IAFS_C_2021_0126_130319.csv',
'infant_feeding_practices_chb_ifp': 'Ess_CHB_IFP_2021_0126_125007.csv',
'medical_histoy_biological_family_hhx_mh_bf': 'Ess_HHx_MH_BF_2021_0126_130548.csv',


'medical_history_infancy_hhx_mh_i': 'Ess_HHx_MH_I_2021_0126_130623.csv',
'parenting_scale_hse_pars': 'Ess_HSE_PARS_2021_0126_130707.csv',
'rothbart_very_short_form_ribqrvsf': 'Ess_CNH_RIBQRvSF_2021_0126_125503.csv',
'maternal_depression_cesd2': 'Ess_CNP_CESD_2021_0124_014704.csv',
'essi2': 'Ess_CNP_ESSI_2020_0626_183620.csv',
'adverse_childhood_experience_hse_ace_pr': 'Ess_HSE_ACE_PR_2021_0126_130642.csv',

'child_physical_examination_cph_cape_c': 'Ess_CPH_CAPE_C_2021_0126_125909.csv',
'complementary_feeding_history_chb_cfh': 'Ess_CHB_CFH_2021_0126_124922.csv',
'child_food_source_and_preparation_chb_cfsp': 'Ess_CHB_CFSP_2021_0126_124937.csv',
'child_global_health_cwb_cgb': 'Ess_CWB_CGB_2021_0126_130043.csv',
'dietary_screener_chb_dsq_pr': 'Ess_CHB_DSQ_PR_2021_0126_124950.csv',
'early_academic_competencies_srp_eac_pr': 'Ess_SRP_EAC_PR_2021_0126_130942.csv',


'language_and_acculturation_dem_la_c': 'Ess_Dem_LA_C_2021_0126_130357.csv',
'medical_hisoty_early_childhood_hhx_mh_ec': 'Ess_HHx_MH_EC_2021_0124_015250.csv',
'promis_physical_activity_8a_chb_ppa8a_pp': 'Ess_CHB_PPA8a_PP_2021_0126_032449.csv',
'promis_sleep_disturbance_4a_csh_psd4a_pp': 'Ess_CSH_PSD4a_PP_2021_0126_025844.csv',
'promis_sleeprelated_impairment_4a_csh_psri4a_pp': 'Ess_CSH_PSRI4a_PP_2021_0126_130002.csv',




'modified_checklist_for_autism_rmchatr': 'Rec_RCh_MCHATR_2021_0126_131020.csv',
'rothbar_early_childhood_recbqvsf': 'Ess_CNH_RECBQvSF_2021_0126_125424.csv',
'health_insurance_coverage_hic': 'Ess_HHx_HIC_2021_0124_030519.csv',
'health_inssurance_hic':'Ess_HHx_HIC_2021_0124_030519.csv',
'health_insurance_coverage_ess_hhx_hic':'Ess_HHx_HIC_2021_0124_030519.csv',
'nih_toolbox_srp_ntppi_pr':'Ess_SRP_NTPPI_PR_2021_0124_030721.csv',
'occupation_exposure_bpe_oexp_pp':'Ess_BPE_OExp_PP_2021_0124_030846.csv',
'dietary_screener_prg_dsq_sr':'Ess_Prg_DSQ_SR_2021_0124_031018.csv',
'household_chemical_exposures_bpe_hcexp_pp':'Ess_BPE_HCExp_PP_2021_0124_030705.csv',
'residential_address_history_dem_addr_p':'Ess_Dem_Addr_P_2021_0124_031041.csv',
'residential_address_history_dem_addr_c':'Ess_Dem_Addr_C_2021_0126_025950.csv',
'household_chemical_exposure_bpe_hcexp_c':'Ess_BPE_HCExp_C_2021_0124_030931.csv',
'household_chemical_exposures_bpe_hcexp_pp':'Ess_BPE_HCExp_C_2021_0124_030931.csv',
'health_insurance_coverage_ess_hhx_hic':'Ess_HHx_HIC_2021_0124_030519.csv',
'airways_questionnaire_early_childhood_air_ec':'Ess_CPH_Air_EC_2021_0124_025152.csv',
'demographics_of_child_dem_c':'Ess_Dem_Dem_C_2021_0126_225048.csv',
'demographics_of_primary_caregiver_dem_cg':'Ess_Dem_Dem_CG_2021_0126_230246.csv',
'sleep_health_of_children_and_adolescents_shca_pr':'Ess_CSH_SHCA_PR_2021_0128_134901.csv',
'ess_dem_ck12e':'Ess_Dem_CK12E_2021_0125_005510.csv',
'covid19_child_parent_report':'Ess_HHx_C19_cPR_2021_0126_130504.csv',  #missing complete variable
'covid19_adult_primary':'Ess_HHx_C19_aPV_2021_0126_130443.csv', #missing complete variable
'early_care_and_education_dem_ece':'Ess_Dem_ECE_2021_0124_030537.csv',
'sleep_health_mshprg':'Ess_Prg_MSHPrg_2021_0124_213608.csv',
'demographics_of_biological_family_dem_b':'Ess_Dem_Dem_B_2021_0124_030414.csv',
'sleep_health_of_infants_shinf':'Ess_CSH_SHInf_2021_0124_213518.csv',
'social_responsive_scale_srs2_pre':'Ess_CNH_SRS2_Pre_2021_0124_214437.csv',
'child_behavior_checklist_cnh_cbcl_pre':'Ess_CNH_CBCL_Pre_2021_0126_125342.csv',
'asq_cuestionario_de_24_meses':'Ess_CNH_ASQ_24_2021_0126_001726.csv',
'asq_cuestionario_de_36_meses':'Ess_CNH_ASQ_36_2021_0126_001752.csv',
'asq_cuestionario_de_8_meses': 'Ess_CNH_ASQ_8_2021_0126_001610.csv',
'asq_cuestionario_de_18_meses': 'Ess_CNH_ASQ_18_2021_0126_001659.csv',
'asq_cuestionario_de_6_meses': 'Ess_CNH_ASQ_6_2021_0126_001501.csv',
'asq_cuestionario_de_12_meses':'Ess_CNH_ASQ_12_2021_0126_001633.csv',
'asq_cuestionario_de_2_meses': 'Ess_CNH_ASQ_2_2021_0126_001427.csv',
'asq_cuestionario_de_60_meses':'Ess_CNH_ASQ_60_2021_0126_001902.csv',
'asq_cuestionario_de_48_meses':'Ess_CNH_ASQ_48_2021_0126_001821.csv'
}


 
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
    if i == 44:
        return 'asq_cuestionario_de_' + abrv.replace('asq','') +'_meses_complete'
    else:
        return 'ftr_complete'

def export(export_form,final,visit):
    #print(final.head())
    ed = pd.read_csv('echo_dictionaries/' + export_form)
    need_cols = ed.loc[~ed['Uploaded Variable Name'].isna(),'Uploaded Variable Name'].unique().tolist()
    print(ed.columns)
    formname = ed['Uploaded Form ID'].unique()[0]
    print(ed.head())
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
        print('made dir')
    except:
        print('error')
        pass

    if 'ASQ' in formname:
        print(final.head())

        
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
                                    + str(day) +  \
                                    '~' + str(visit[:-1])
                                    )
    print(final.columns)

    ##add otherrsp

    if 'otherresp' in need_cols and 'otherresp' not in final.columns:
        final['otherresp'] = ''

    if 'ace_pr_otherrespon' in need_cols and 'ace_pr_otherrespon' not in final.colums:
        final['ace_pr_otherrespon'] = ''

    for x in final.columns:
        if 'sequencenum' in x:
            origs = [x for x in final.columns if 'sequencenum' in x][0]
            
            new = origs.split('_')

            new2 = new[len(new)-1]

            print(new2)
            
            final.rename(columns = {origs:new2}, inplace = True)
   


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

        
    

def clean_data(final,complete):
    print(final.shape)
    #final = final.loc[final[complete.lower()] != str(0),:]
    #print(final.shape)
    final = final.loc[final['formdt'] != 'NaT',:]
    final = final.loc[final['formdt'] != '',:]
   
    #final['formdt'] = final['formdt'].astype(str)

    final = final.loc[~final['formdt'].isnull(),:]
    #one more check
    final['formdt'] = final['formdt'].astype(str)

    final = final[final['formdt'].str.len() >2]
    
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
    
