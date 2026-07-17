"""
Original file is located at
    https://colab.research.google.com/drive/1ca-jlBvJ4uqpbCHFFgCFp9akIY7FSmGc

"""

import pandas as pd
import numpy as np

patients = pd.read_csv('datasets/patients.csv')
treatments = pd.read_csv('datasets/treatments.csv')
adverse_reactions = pd.read_csv('datasets/adverse_reactions.csv')
treatments_cut = pd.read_csv('datasets/treatments_cut.csv')

# view datasets
print(patients.head())
print(treatments.head())
print(treatments_cut.shape)
print(adverse_reactions)


# export data for manual assessment
with pd.ExcelWriter('created/clinical_trials.xlsx') as writer:
    patients.to_excel(writer,sheet_name='patients')
    treatments.to_excel(writer,sheet_name='treatments')
    treatments_cut.to_excel(writer,sheet_name='treatment_cut')
    adverse_reactions.to_excel(writer,sheet_name='adverse_reactions')

# Automatic Assessment
print(adverse_reactions.info())
print(patients[patients['address'].isnull()])
print(treatments[treatments.duplicated()])
print(treatments[treatments.duplicated(subset=['given_name'	,'surname'])])
print(treatments_cut[treatments_cut.duplicated(subset=['given_name'	,'surname'])])
print(adverse_reactions.duplicated().sum())
print(patients.describe())
print(patients[patients['height'] == 27])
print(treatments_cut.describe())
print(treatments.sort_values('hba1c_change',na_position='first'))


# Always work on the copied data (not on original one)
patients_df = patients.copy()
treatments_df = treatments.copy()
treatments_cut_df = treatments_cut.copy()
adverse_reactions_df = adverse_reactions.copy()

"""
1. Define the problem and the solution
2. Code the solution
3. Test the solution

"""

patients_df['zip_code'] = patients_df['zip_code'].astype('str')
print(patients_df.info())

# code
patients_df[['address','city','state','zip_code','country','contact']].fillna('No data',inplace=True)
# test
print(patients_df.info())


print(treatments.head())
# code
treatments_df['hba1c_change'] = treatments_df['hba1c_start'] - treatments_df['hba1c_end']
treatments_cut_df['hba1c_change'] = treatments_cut_df['hba1c_start'] - treatments_cut_df['hba1c_end']
# test
print(treatments_cut_df.info())



print(patients.head())

### Write the code to get number and email


### 
# 1. concatenating treatment and treatment_cut
# 2. geting property "TYPES" as a column
# 3. creating dosage_start and dosage_end
# 4. drop dosage_range
# 5. remove 'u' from dosage and convert it to int

treatments_df = pd.concat([treatments_df,treatments_cut_df])

treatments_df = treatments_df.melt(id_vars=['given_name', 'surname' ,'hba1c_start', 'hba1c_end','hba1c_change'],var_name='type',value_name='dosage_range')

treatments_df = treatments_df[treatments_df['dosage_range'] != '-']
treatments_df['dosage_start'] = treatments_df['dosage_range'].str.split('-').str.get(0)
treatments_df['dosage_end'] = treatments_df['dosage_range'].str.split('-').str.get(1)

treatments_df.drop(columns='dosage_range',inplace=True)

treatments_df['dosage_start'] = treatments_df['dosage_start'].str.replace('u','')
treatments_df['dosage_end'] = treatments_df['dosage_end'].str.replace('u','')

treatments_df['dosage_start'] = treatments_df['dosage_start'].astype('int')
treatments_df['dosage_end'] = treatments_df['dosage_end'].astype('int')

# removing the reduntant table after merging it's data with treatment_df table
treatments_df = treatments_df.merge(adverse_reactions_df, how ='left', on=['given_name','surname'])

print(treatments_df)