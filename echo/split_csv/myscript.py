import pandas as pd
import helper
from helper import abrv,echo,head_P

def process_each_form(list_forms):
    visits=['V0/','V1/','V2/','V3/','PRO/']
    for form in list_forms:
        print("processing form name:"+form)
        export_form = echo[form]
        print("corresponding echo form:"+export_form)

        for visit in visits:
            try:
                data = pd.read_csv(str(visit)+form+'.csv',dtype=object,encoding='utf-8-sig')
                print(visit)
            except:
                continue
            final = head_P.merge(data, left_on = 'COHORTPARTICIPANTID', right_on = 'protect_id')


            col1=helper.formdt_respondent_complete(abrv,echo,form,1)
            col2=helper.formdt_respondent_complete(abrv,echo,form,2)
            col4=helper.formdt_respondent_complete(abrv,echo,form,4)
            print(col1,col2,col4)
            final.loc[:,'visitname'] = final.loc[:,'redcap_event_name'].apply(lambda x: helper.redcap_event_to_visitname(x))
            final.loc[:,'formdt'] = pd.to_datetime(final.loc[:,col1]).dt.strftime('%m/%d/%Y')
            final = final.rename(columns = {col2:'respondent'})
            final = final.rename(columns = {'EWCP_PARTICIPANTID':'participantid'})
            final.loc[:,col4] = final.loc[:,[col for col in final.columns if 'complete' in col][0]]


            if 'hhc_p' not in form and 'iafs_p' not in form and 'addr_p' not in form \
                and 'hcexp_pp' not in form and 'oexp_pp' not in form and 'life_pp' not in form:
                col3=helper.formdt_respondent_complete(abrv,echo,form,3)
                print(col3)
                final = final.rename(columns = {col3:'otherresp'})

            final.columns=[x.lower() for x in final.columns]
            final = helper.clean_data(final)
            #print(final.dtypes)
            if len(final.index) !=0:
                final.loc[:,'ftr_mode'] = 2
                final.loc[:,'ftr_setting'] = 1
                final.loc[:,'ftr_deidentified'] =1
                helper.export(export_form,final,visit)
def main():
    forms = ['household_composition_dem_hhc_p', 'income_assistance_financial_strain_dem_iafs_p', 'language_and_acculturation_dem_la_p', 'lifestyle_prg_life_pp', 'maternal_food_source_and_preparation_prg_mfsp', 'caregiver_occupation_and_employment_dem_occ_cg', 'promis_global_health_scale_cnp_pgh', 'promis_sleep_disturbance_4a_prg_psd4a', 'promis_sleeprelated_impairment_4a_prg_psri4a', 'perceived_stress_scale_cnp_pss10', 'the_everyday_discrimination_scale_cnp_weds', 'health_insurance_coverage_ess_hhx_hic']
    process_each_form(forms)
    print(str(len(forms))+"forms are processed")
if __name__ == "__main__":
    main()
