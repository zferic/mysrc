import pandas as pd
import helper
from helper import abrv,echo

def process_each_form(list_forms):
    visits=['V0/','V1/','V2/','V3/','PRO/','C1/','C2/','C3/','C4/','C5/','C6/','C7/','C8/','C9/','C10/','C11/','C12/','C13/']
    for form in list_forms:
        print("processing form name:"+form)
        export_form = echo[form]
        print("corresponding echo form:"+export_form)

        for i, visit in enumerate(visits):
            try:
                data = pd.read_csv(str(visit)+form+'.csv',dtype=object,encoding='utf-8-sig')
                print(visit)
            except:
                continue
            if i > 4:
                head = helper.process_head('C')
                final = head.merge(data, left_on = 'COHORTPARTICIPANTID', right_on = 'crece_id')
            else:
                head = helper.process_head('P')
                final = head.merge(data, left_on = 'COHORTPARTICIPANTID', right_on = 'protect_id')

            if form == 'essi2' or form == 'maternal_depression_cesd2':
                col1=helper.formdt_respondent_complete2(abrv,echo,form,1)
                col2=helper.formdt_respondent_complete2(abrv,echo,form,2)
                col4=helper.formdt_respondent_complete2(abrv,echo,form,4)
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
            final.loc[:,'formdt'] = pd.to_datetime(final.loc[:,col1]).dt.strftime('%m/%d/%Y')
            final = final.rename(columns = {col2:'respondent'})
            final = final.rename(columns = {'EWCP_PARTICIPANTID':'participantid'})
            final.loc[:,col4] = final.loc[:,[col for col in final.columns if 'complete' in col][0]]

            final.columns=[x.lower() for x in final.columns]
            final = helper.clean_data(final)
            #print(final.dtypes)
            if len(final.index) !=0:
                final.loc[:,'ftr_mode'] = str(2)
                final.loc[:,'ftr_setting'] = str(1)
                final.loc[:,'ftr_deidentified'] =str(1)
                helper.export(export_form,final,visit)
def main():
    forms = ['household_composition_dem_hhc_p', 'income_assistance_financial_strain_dem_iafs_p', 'language_and_acculturation_dem_la_p', 'lifestyle_prg_life_pp', 'maternal_food_source_and_preparation_prg_mfsp', 'caregiver_occupation_and_employment_dem_occ_cg', 'promis_global_health_scale_cnp_pgh', 'promis_sleep_disturbance_4a_prg_psd4a', 'promis_sleeprelated_impairment_4a_prg_psri4a', 'perceived_stress_scale_cnp_pss10', 'the_everyday_discrimination_scale_cnp_weds', 'health_insurance_hic','child_birth_information_hhx_cbi','airways_questionnaire_cph_air_inf','child_physical_examination_cph_cape_i','child_global_health_cwb_cgb','escala_de_clima_social_familiar_hse_fes_coh','household_exposure_to_secondhand_smoke_bpe_heshs_c','household_composition_dem_hhc_c','income_assistance_financial_strain_dem_iafs_c','infant_feeding_practices_chb_ifp','medical_histoy_biological_family_hhx_mh_bf','medical_history_infancy_hhx_mh_i','parenting_scale_hse_pars','rothbart_very_short_form_ribqrvsf','maternal_depression_cesd2','essi2','adverse_childhood_experience_hse_ace_pr','child_physical_examination_cph_cape_c','child_food_source_and_preparation_chb_cfsp','dietary_screener_chb_dsq_pr','early_academic_competencies_srp_eac_pr','language_and_acculturation_dem_la_c','medical_hisoty_early_childhood_hhx_mh_ec','promis_physical_activity_8a_chb_ppa8a_pp','promis_sleep_disturbance_4a_csh_psd4a_pp','promis_sleeprelated_impairment_4a_csh_psri4a_pp','modified_checklist_for_autism_rmchatr','rothbar_early_childhood_recbqvsf']
    process_each_form(forms)
    print(str(len(forms))+"forms are processed")
if __name__ == "__main__":
    main()
