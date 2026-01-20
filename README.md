# NAX Acute Subdural Hematoma (aSDH) Detection

The purpose of this program is to search through clinical records and identify based on clinician notes which patients have aSDH.
Steps 1-26 can be used to replicate the data featured in the paper.
Click "Run All" on each step and run them in order. This folder should have all the files needed to replicate this data.
Steps 1 and 2 create the feature matrix to identify which patients have aSDH.
Steps 3-9 utilize training data only.
Steps 10-12, 15-17, and 22-25 use testing data only.
Below you can find detailed overviews of each of the steps in the project and optional instructions for making a new sampling cohort.

## Installation

Before running the notebooks, please install the required dependencies. See [INSTALLATION.md](INSTALLATION.md) for detailed setup instructions.

### Quick Start

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/SDH-EHR-Phenotyping-NAX.git
cd SDH-EHR-Phenotyping-NAX

# Install dependencies
pip install -r requirements.txt

# Download NLTK data
python -c "import nltk; nltk.download('punkt')"

# Launch Jupyter
jupyter notebook
```

## Dependencies

This project requires Python 3.8+ and the following key packages:
- pandas 2.2.0
- numpy 1.26.4
- scikit-learn 1.4.0
- matplotlib 3.8.2
- seaborn 0.13.2
- nltk 3.8.1
- scipy 1.13.0
- tqdm
- scikit-optimize

For a complete list, see [requirements.txt](requirements.txt). Conda users can use [environment.yml](environment.yml).  

## Workflow Overview

The analysis pipeline consists of 26 steps organized into distinct phases:

### Phase 1: Data Preparation (Steps 1-2)
- **Step 1**: Create feature matrix with CPT codes and keywords
- **Step 2**: Add ICD codes and manual annotations

### Phase 2: Training with Logistic Regression (Steps 3-5)
- **Step 3**: Train on BIDMC, test on MGB (training data)
- **Step 4**: Train on MGB, test on BIDMC (training data)
- **Step 5**: Train/test both hospitals with 10-fold cross-validation

### Phase 3: Training with Random Forest (Steps 6-9)
- **Step 6**: Error analysis on training data
- **Step 7**: Random Forest with 10-fold cross-validation
- **Step 8**: Train on BIDMC, test on MGB
- **Step 9**: Train on MGB, test on BIDMC

### Phase 4: Testing (Steps 10-12)
- **Step 10**: Random Forest on testing data (10-fold CV)
- **Step 11**: RF testing - train BIDMC, test MGB
- **Step 12**: RF testing - train MGB, test BIDMC

### Phase 5: Analysis & Feature Studies (Steps 13-18)
- **Step 13**: Demographics analysis
- **Step 14**: False positive/negative analysis for review
- **Step 15**: RF with ICD-only features
- **Step 16**: RF with CPT-only features
- **Step 17**: RF with keywords-only features
- **Step 18**: Generate comparison graphs

### Phase 6: Validation (Steps 19-21)
- **Step 19**: Cohort reconstruction for BIDMC
- **Step 20**: Cohort reconstruction for MGB
- **Step 21**: Calculate combined error rate

### Phase 7: Final Testing with Logistic Regression (Steps 22-26)
- **Step 22**: LR on testing data (10-fold CV)
- **Step 23**: LR with ICD-only features
- **Step 24**: LR with CPT-only features (**Note**: Missing - needs recovery)
- **Step 25**: LR with keywords-only features
- **Step 26**: Relabel feature importances for presentation

## Detailed Step Descriptions

**Step 1 - Feature Matrix Creation**
Creates a feature matrix using Current Procedural Terminology (CPT) codes and keywords to predict SDH. Processes MGB and BIDMC sampling cohorts. Uses portable paths via config.py.

**Step 2 - ICD Code Integration**
Adds ICD code features to the feature matrix and integrates manual annotations (positive/negative labels) for each patient.

**Step 3 - Logistic Regression Cross-Hospital (BI→MGB)**
Trains logistic regression model on BIDMC data and tests on MGB patients using training data only. Generates feature importance plots and performance metrics.

**Step 4 - Logistic Regression Cross-Hospital (MGB→BI)**
Trains logistic regression model on MGB data and tests on BIDMC patients using training data only.

**Step 5 - Logistic Regression Both Hospitals**
Trains and tests on combined data from both hospitals using 10-fold nested cross-validation. Saves 10 trained models.

**Step 6 - Error Analysis**
Analyzes errors from training data to understand feature importances and model performance characteristics.

**Step 7 - Random Forest Training**
Implements Random Forest classifier with 10-fold nested cross-validation on training data from both hospitals.

**Step 8 - Random Forest Cross-Hospital (BI→MGB)**
Trains Random Forest on BIDMC and tests on MGB data.

**Step 9 - Random Forest Cross-Hospital (MGB→BI)**
Trains Random Forest on MGB and tests on BIDMC data.

**Step 10 - Random Forest Testing**
Applies Random Forest to testing data from both hospitals with 10-fold cross-validation.

**Step 11 - RF Testing Cross-Hospital (BI→MGB)**
Random Forest testing version: train on BIDMC, test on MGB.

**Step 12 - RF Testing Cross-Hospital (MGB→BI)**
Random Forest testing version: train on MGB, test on BIDMC.

**Step 13 - Demographics**
Calculates demographic information for patients in MGB and BIDMC sampling cohorts.

**Step 14 - False Positive/Negative Analysis**
Generates CSVs of false positive and false negative cases for manual annotation review.

**Step 15 - ICD-Only Random Forest**
Trains and tests Random Forest using only ICD code features on both hospitals.

**Step 16 - CPT-Only Random Forest**
Trains and tests Random Forest using only CPT code features on both hospitals.

**Step 17 - Keywords-Only Random Forest**
Trains and tests Random Forest using only keyword features on both hospitals.

**Step 18 - Comparison Graphs**
Generates bar charts comparing Random Forest and Logistic Regression test results across feature sets.

**Step 19 - BIDMC Cohort Reconstruction**
Reconstructs BIDMC cohort to estimate the error rate of the prediction model.

**Step 20 - MGB Cohort Reconstruction**
Reconstructs MGB cohort to estimate the error rate of the prediction model.

**Step 21 - Combined Error Rate**
Calculates and reports the combined error rate across both hospitals.

**Step 22 - Logistic Regression Testing**
Applies logistic regression to testing data from both hospitals with 10-fold nested cross-validation.

**Step 23 - ICD-Only Logistic Regression**
Trains and tests logistic regression using only ICD code features on both hospitals.

**Step 24 - CPT-Only Logistic Regression**
**Missing**: Should train and test logistic regression using only CPT code features. Needs to be recovered or recreated.

**Step 25 - Keywords-Only Logistic Regression**
Trains and tests logistic regression using only keyword features on both hospitals.

**Step 26 - Feature Importance Relabeling**
Relabels feature importances from Step 10 for clearer presentation in figures.  

## Optional Instructions for Making a New Sampling Cohort. These steps are not necessary to reproduce the data in this paper.
If you want to make a new sampling cohort please read the following:  
Optional steps 1-5 can be used to make new sampling cohorts using data from Mass General Hospital (MGB) and Beth Israel Hospital (BIDMC) featured in the paper content.  
After optional steps 1-5 are run, please run steps 1-25. Once you finish steps 3 and 4, you must manually annotate the notes.  
You can manually annotate by reading the ICD +/- groups from each hospital into the Annotation\_tool folder.  
Please see the annotation folder for more instructions on how to proceed.  

