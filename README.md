# Welcome to the NAX Acute Subdural Hematoma (aSDH) detection repo.

The purpose of this program is to search through clinical records and identify based on clinician notes which patients have aSDH.  
Steps 1-26 can be used to replicate the data featured in the paper.  
Click "Run All" on each step and run them in order. This folder should have all the files needed to replicate this data.  
Steps 1 and 2 create the feature matrix to identify which patients have aSDH.  
Steps 3-9 utilize training data only.  
Steps 10-12, 15-17, and 22-25 use testing data only.  
Below you can find detailed overviews of each of the steps in the project and optional instructions for making a new sampling cohort.  

## Detailed Overview of Each of the Steps
Step 1 creates a feature matrix utilizing Current Procedural Terminology (CPT) codes and keywords that will be used to predict which patients have SDH.  
Step 2 adds ICD code features to the feature matrix and the manual annotations assigned to each patient (positive or negative).  
Step 3 trains on the data from the hospital BIDMC and tests on the patients in MGB using logistic regression for training data only.  
Step 4 trains on the data from the hospital MGB and tests on the patients in BIDMC using logistic regression for training data only.  
Step 5 trains and tests on both hospitals using the training data.  
Step 6 can be used with the training data only to understand the importances of features in the training data and conduct error analysis.  
Step 7 trains and tests both hospitals on the training data using random forest and 10 fold nested cross validation.  
Step 8 trains on the data from the hospital BIDMC and tests on the patients in MGB using random forest.  
Step 9 trains on the data from the hospital MGB and tests on the patients in BIDMC using random forest.  
Step 10 trains and tests both hospitals on the testing data using random forest and 10 fold nested cross validation.  
Step 11 trains on the data from the hospital BIDMC and tests on the patients in MGB using random forest.  
Step 12 trains on the data from the hospital MGB and tests on the patients in BIDMC using random forest.  
Step 13 calculates the demographic information of patients in the MGB and BIDMC sampling cohorts.  
Step 14 allows for the annotator to review the csvs for false\_positive and false\_negative cases from Random Forest testing on both hospitals.  
Step 15 trains and tests on both hospitals with ICD as the only feature using random forest.  
Step 16 trains and tests on both hospitals with CPT as the only feature using random forest.  
Step 17 trains and tests on both hospitals with keywords as the only feature using random forest.  
Step 18 generates bar figures of the testing feature results for comparing them.  
Step 19 reconstructs a cohort for BIDMC to estimate the error rate of the program.  
Step 20 reconstructs a cohort for MGB to estimate the error rate of the program.  
Step 21 calculates the error rate for both hospitals.  
Step 22 trains and tests both hospitals on the testing data using logistic regression and 10 fold nested cross validation.  
Step 23 trains and tests on both hospitals with ICD as the only feature using logistic regression.  
Step 24 trains and tests on both hospitals with CPT as the only feature using logistic regression.  
Step 25 trains and tests on both hospitals with keywords as the only feature using logistic regression.  
Step 26 relabels the feature importances from step 10 to make them more presentable and clear.  

## Optional Instructions for Making a New Sampling Cohort. These steps are not necessary to reproduce the data in this paper.
If you want to make a new sampling cohort please read the following:  
Optional steps 1-5 can be used to make new sampling cohorts using data from Mass General Hospital (MGB) and Beth Israel Hospital (BIDMC) featured in the paper content.  
After optional steps 1-5 are run, please run steps 1-25. Once you finish steps 3 and 4, you must manually annotate the notes.  
You can manually annotate by reading the ICD +/- groups from each hospital into the Annotation\_tool folder.  
Please see the annotation folder for more instructions on how to proceed.  

