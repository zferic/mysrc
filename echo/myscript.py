import pandas as pd
import helper
from helper import abrv,echo

def process_each_form(list_forms):
    visits=['V0/','V1/','V2/','V3/','PRO/','C1/','C2/','C3/','C4/','C5/','C6/','C7/','C8/','C9/','C10/','C11/','C12/','C13/']

    noform = []
    hasform = []
    for form in list_forms:
        print("processing form name:"+form)
        try:
            export_form = echo[form]
            print("corresponding echo form:"+export_form)
            hasform.append(form)
        except:
            print("does't have abbrv -- " + form)
            noform.append(form)
            continue

        for i, visit in enumerate(visits):
            try:
                data = pd.read_csv('outputexports/' + str(visit)+form+'.csv',dtype=object,encoding='utf-8-sig')
                print(data.shape)
                print(visit)

                if form == 'the_everyday_discrimination_scale_cnp_weds' and visit == 'V0/':
                    print('Raw Data Shape')
                    print(data.shape)
            except:
                print(form + '-failed at visit :' + visit)
            
                continue

            
            if i > 4:
                head = helper.process_head('C')
                final = head.merge(data, left_on = 'COHORTPARTICIPANTID', right_on = 'crece_id')
            else:
                head = helper.process_head('P')

                final = head.merge(data, left_on = 'COHORTPARTICIPANTID', right_on = 'protect_id')

            if form == 'essi2' or form == 'maternal_depression_cesd2' or 'asq' in form:
                col1=helper.formdt_respondent_complete2(abrv,echo,form,1)
                col2=helper.formdt_respondent_complete2(abrv,echo,form,2)

                if 'asq' not in form:
                    col4=helper.formdt_respondent_complete2(abrv,echo,form,4)
                if 'asq' in form:
                    col4=helper.formdt_respondent_complete2(abrv,echo,form,44)

                if 'hhc_p' not in form and 'iafs_p' not in form and 'addr_p' not in form \
                and 'hcexp_pp' not in form and 'oexp_pp' not in form and 'life_pp' not in form:
                    col3=helper.formdt_respondent_complete2(abrv,echo,form,3)
                    final = final.rename(columns = {col3:'otherresp'})
            else:
                col1=helper.formdt_respondent_complete(abrv,echo,form,1)
                col2=helper.formdt_respondent_complete(abrv,echo,form,2)
                col4=helper.formdt_respondent_complete(abrv,echo,form,4)
                if 'hhc_p' not in form and 'iafs_p' not in form and 'addr_p' not in form \
                and 'hcexp_pp' not in form and 'oexp_pp' not in form and 'life_pp' not in form:
                    col3=helper.formdt_respondent_complete(abrv,echo,form,3)
                    final = final.rename(columns = {col3:'otherresp'})

            print(col1,col2,col4)
            final.loc[:,'visitname'] = final.loc[:,'redcap_event_name'].apply(lambda x: helper.redcap_event_to_visitname(x))
            print(final.columns)
            final.loc[:,'formdt'] = pd.to_datetime(final.loc[:,col1]).dt.strftime('%m/%d/%Y')
            final = final.rename(columns = {col2:'respondent'})
            final = final.rename(columns = {'EWCP_PARTICIPANTID':'participantid'})
            if 'asq' in form:
                print(final.columns)
            print(final.columns)
            final.loc[:,col4] = final.loc[:,[col for col in final.columns if 'complete' in col][0]]
            final.loc[:,abrv[form]+'_deidentified'] = 0
            print('here------------------------>>>'+form)
            if abrv[form] == 'c19_cpr' or abrv[form] == 'c19_apv':
                print('here------------------------>>>')
                final['sequencenum'] = ''
                final[abrv[form]+ '_language'] = ''

            final.columns=[x.lower() for x in final.columns]
            final = helper.clean_data(final,col4)

            if form == 'the_everyday_discrimination_scale_cnp_weds' and visit == 'V0/':
                print(final.shape)

                #assert 1 == 2
            #print(final.dtypes)
            if len(final.index) !=0:
                print('in final.....')
                final.loc[:,'ftr_mode'] = str(2)
                final.loc[:,'ftr_setting'] = str(1)
                final.loc[:,'ftr_deidentified'] =str(0)
                helper.export(export_form,final,visit)

    return noform, hasform 
def main():

    # The forms that are going to be processed..

    forms = [#'medical_history_infancy_hhx_mh_i', # check erros relating to columns
            #'residential_address_history_dem_addr_c', # cwe do not process
            'covid19_child_parent_report',
            'infant_feeding_practices_chb_ifp',
            'airways_questionnaire_early_childhood_air_ec',
            #'asq_cuestionario_de_24_meses',  #currently being mapped
            'rothbar_early_childhood_recbqvsf',
            'covid19_adult_primary',
           'lifestyle_prg_life_pp', 
            'medical_history_biological_family_hhx_mh_bf_pro',
            'maternal_food_source_and_preparation_prg_mfsp',
            # 'asq_cuestionario_de_36_meses', #currently being mapped
            'medical_history_biological_family_hhx_mh_bf_pro_2',
            'dietary_screener_chb_dsq_pr',
            'household_composition_dem_hhc_p', 
            'medical_histoy_biological_family_hhx_mh_bf',
           # 'asq_cuestionario_de_8_meses', #currently being mapped
            'promis_sleep_disturbance_4a_csh_psd4a_pp',
            'promis_physical_activity_8a_chb_ppa8a_pp',
            'the_everyday_discrimination_scale_cnp_weds', #not being processed ??
            'modified_checklist_for_autism_rmchatr',
            'escala_de_clima_social_familiar_hse_fes_coh',
            'household_exposure_to_secondhand_smoke_bpe_heshs_c',
            # 'asq_cuestionario_de_18_meses',#currently being mapped
            'rothbart_very_short_form_ribqrvsf',
            #'early_care_and_education_dem_ece', identifier info
            'asq_cuestionario_de_48_meses',
            'promis_sleep_disturbance_4a_prg_psd4a', 
            'promis_global_health_scale_cnp_pgh',
            'sleep_health_mshprg',
            'demographics_of_biological_family_dem_b',
            'health_insurance_coverage_hic',
            'early_academic_competencies_srp_eac_pr',
            'parenting_scale_hse_pars',
            'health_inssurance_hic',
            'child_behavior_checklist_cnh_cbcl_pre',
            #'asq_cuestionario_de_60_meses',#currently being mapped
            'sleep_health_of_infants_shinf',
            'household_composition_dem_hhc_c',
            'income_assistance_financial_strain_dem_iafs_c',
            'child_birth_information_hhx_cbi',
            'income_assistance_financial_strain_dem_iafs_p',
            'demographics_of_child_dem_c',
          #  'household_chemical_exposures_bpe_hcexp_pp', sent by PR
            #'asq_cuestionario_de_6_meses',#currently being mapped
            #'asq_cuestionario_de_12_meses',#currently being mapped
            'language_and_acculturation_dem_la_p',
            'nih_toolbox_srp_ntppi_pr',
            'social_responsive_scale_srs2_pre',
            'promis_sleeprelated_impairment_4a_prg_psri4a', 
            'medical_history_biological_family_hhx_mh_bf',
            #'asq_cuestionario_de_2_meses', #currently being mapped
            'demographics_of_primary_caregiver_dem_cg',
            'maternal_depression_cesd2',
            #'occupation_exposure_bpe_oexp_pp', sent by PR
            'language_and_acculturation_dem_la_c',
            'health_insurance_coverage_ess_hhx_hic',
           # 'household_chemical_exposure_bpe_hcexp_c',             #  identifer - submited by PR
            'sleep_health_of_children_and_adolescents_shca_pr',    # missing some columns -- see errors.txt
            'child_physical_examination_cph_cape_i',
            'adverse_childhood_experience_hse_ace_pr',   
            'medical_hisoty_early_childhood_hhx_mh_ec',
            'child_food_source_and_preparation_chb_cfsp',
           # 'registration',
            'child_global_health_cwb_cgb',
            #'ess_dem_ck12e', #  identifer - submited by PR
            'caregiver_occupation_and_employment_dem_occ_cg',
            'perceived_stress_scale_cnp_pss10',
            'dietary_screener_prg_dsq_sr',
            'airways_questionnaire_cph_air_inf',
            'complementary_feeding_history_chb_cfh',
            #'residential_address_history_dem_addr_p',#  identifer - submited by PR
            'essi2',
            'child_physical_examination_cph_cape_c']


    a,b = process_each_form(forms)
    print('No Form')
    print(a)
    print('Has form')
    print(b)
    print(str(len(forms))+"forms are processed")
if __name__ == "__main__":
    main()
