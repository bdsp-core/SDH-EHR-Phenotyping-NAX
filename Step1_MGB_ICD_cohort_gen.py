#Install all necessary packages to make code run. 
import numpy as np 
import pandas as pd
from tqdm import tqdm
from thunderpack import ThunderReader  # install thunderpack if not yet: pip install thunderpack
import gc


##Run the following code to get the sampling cohorts for MGB

reader = ThunderReader('/media/gregory178/Thunderpacks/Dropbox/zz_EHR_Thunderpacks/MGB/thunderpack_icd_9_10_1m_MGB') # read the thunderpack file

#reminder: ICD+ group is defined as patients who received at least one SDH-related ICD
dfs = []
#Create a loop over all keys to find patients with positive ICD 
for i in tqdm(range(1, 511)):    # create a for loop to loop over all keys: ICD_partition_1, ICD_partition_2, ... You can find all keys by `print(list(reader.keys()))`
    df = reader[f'ICD_partition_{i}']
    df = df[df.ICDCD.astype(str).str.contains('^(?:I62.0|S06.5|432.1|852.2|852.3)')]  # for example, you want to filter and keep only ICDs that starts with G20 or 332.  '^(?:G20|332)' is a regular expression (regex).
    dfs.append(df)
df_icd_plus = pd.concat(dfs, axis=0, ignore_index=True)  # concatenate all filtered dataframes from all partitions into one dataframe
# keep unique patient IDs
df_icd_plus = df_icd_plus[['BDSPPatientID','ShiftedContactDTS','BDSPEncounterID', 'ICDCD']].drop_duplicates()
df_icd_plus.to_csv('patientIDs_ICD_plus_SDH_MGB.csv', index=False)    # save as a CSV file

df_icd_plus = pd.read_csv('patientIDs_ICD_plus_SDH_MGB.csv')


# reminder: ICD- group is defined as patients who never got any SDH-related ICDs
dfs = []
#for i in tqdm(range(1, 511)):  ***Is it the same amount of partitions for this one as well?
for i in tqdm(range(1, 511)):    # create a for loop to loop over all keys: ICD_partition_1, ICD_partition_2, ... You can find all keys by `print(list(reader.keys()))`
    df = reader[f'ICD_partition_{i}']
    df = df[~df.ICDCD.astype(str).str.contains('^(?:I62.0|S06.5|432.1|852.2|852.3)')]  # for example, you want to filter and keep only ICDs that starts with G20 or 332.  '^(?:G20|332)' is a regular expression (regex).
    
    
    df = df[['BDSPPatientID','ShiftedContactDTS','BDSPEncounterID', 'ICDCD']]
    
    dfs.append(df)

    # to further save space, delete df
    del df
    gc.collect()

df_icd_minus = pd.concat(dfs, axis=0, ignore_index=True)  # concatenate all filtered dataframes from all partitions into one dataframe
df_icd_minus = df_icd_minus[['BDSPPatientID','ShiftedContactDTS','BDSPEncounterID','ICDCD']].drop_duplicates()

# because we should make sure these are patients who never got any SDH ICDs
# therefore we should remove patients who are included in the df_icd_plus
# conceptually: df_icd_minus = df_icd_minus - df_icd_plus



df_icd_minus = df_icd_minus[ ~np.in1d(df_icd_minus.BDSPPatientID, df_icd_plus.BDSPPatientID) ]

df_icd_minus.to_csv('patientIDs_ICD_minus2_SDH_MGB.csv', index=False)    # save as a CSV file

#***** Get code for this part. 
# to get the final sampling cohort
# we should do random selection to get 3000 notes in total
# if we have 2 hospitals (MGB, BIDMC)
# and 2 groups (ICD+, ICD-)
# then we need to randomly sample 3000/2/2 = 750/group/hospital
# remember, we should also make sure one note/patient