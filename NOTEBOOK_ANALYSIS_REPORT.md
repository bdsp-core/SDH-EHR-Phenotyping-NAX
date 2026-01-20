# Notebook Analysis Report

## Overview

This document provides a comprehensive analysis of all Step notebooks (Step1-Step26) in the SDH-EHR-Phenotyping-NAX repository.

## Executive Summary

- **Total Notebooks**: 26 expected, 25 found (Step24 is missing)
- **Notebooks Using config.py**: 1 (only Step1)
- **Notebooks Needing Updates**: 24 (Step2-Step26, excluding missing Step24)
- **Documentation Quality**: Generally good, with clear purpose statements

## Critical Findings

### 1. Missing Notebook
- **Step24** (CPT Logistic Regression) does not exist despite being referenced in README.md
- Was likely the duplicate file "Step24_CPT_logistic_regression_Draft_15 copy.ipynb" that was deleted

### 2. File Extension Issue
- **Step2_ICD_and_Feature_Matrix.IPYNB** had uppercase extension
- **Fixed**: Renamed to lowercase .ipynb for consistency

### 3. Hardcoded Paths
- All notebooks except Step1 use hardcoded absolute paths
- Common pattern: `/home/gregory178/Desktop/NAX project/NAX_SDH/`
- **Impact**: Not portable, won't work on other systems

### 4. Results Location
- All notebooks write output files to root directory or hardcoded paths
- **Should write to**: `results/` subdirectory using `config.get_results_path()`

## Workflow Organization

### Data Preparation (Steps 1-2)
- **Step1**: Feature matrix creation with CPT codes and keywords
  - ✅ Uses config.py
  - Outputs: Feature matrices for MGB and BIDMC

- **Step2**: Add ICD codes and manual annotations
  - ❌ Uses hardcoded paths
  - Outputs: Complete feature matrix with ICD codes

### Training Phase (Steps 3-9)
Logistic Regression (LR):
- **Step3**: Train BIDMC, test MGB (training data)
- **Step4**: Train MGB, test BIDMC (training data)
- **Step5**: Train/test both hospitals with 10-fold CV

Random Forest (RF):
- **Step6**: Error analysis on training data
- **Step7/7b**: RF model implementation
- **Step8**: RF train BIDMC, test MGB
- **Step9**: RF train MGB, test BIDMC

### Testing Phase (Steps 10-12)
- **Step10/10b**: RF test on combined hospitals
- **Step11**: RF testing - train BIDMC, test MGB
- **Step12**: RF testing - train MGB, test BIDMC

### Analysis & Reporting (Steps 13-21)
- **Step13**: Demographics analysis
- **Step14**: False positive/negative analysis for annotation
- **Step15-17**: Feature-specific RF models (ICD, CPT, keywords)
- **Step18**: Generate comparison bar graphs
- **Step19-21**: Cohort reconstruction and error rate estimation

### Final Testing & Analysis (Steps 22-26)
- **Step22**: LR test on both hospitals (10-fold CV)
- **Step23**: ICD-only LR
- **Step24**: **MISSING** (CPT-only LR)
- **Step25**: Keywords-only LR
- **Step26**: Relabel feature importances for presentation

## Detailed Notebook Analysis

| Step | Purpose | Input Files | Output Files | config.py | Priority |
|------|---------|-------------|--------------|-----------|----------|
| 1 | Feature matrix with CPT/keywords | `data/`BI_sampling*, MGB_sampling* | Root: feature_matrix*.csv | ✅ | ✅ Done |
| 2 | Add ICD codes & annotations | Hardcoded paths | feature_matrix_notes_CPT_and_ICD_.csv | ❌ | 🔴 High |
| 3 | LR: Train BI, Test MGB | train_data_.csv | PNG plots, CSV metrics | ❌ | 🔴 High |
| 4 | LR: Train MGB, Test BI | train_data_.csv | PNG plots, CSV metrics | ❌ | 🔴 High |
| 5 | LR: Both hospitals 10-fold CV | train_data_.csv | 10 pickle models, PNG, CSV | ❌ | 🔴 High |
| 6 | Error analysis (training) | Hardcoded paths | Analysis outputs | ❌ | 🟡 Med |
| 7/7b | RF model variants | Hardcoded paths | Pickle models, metrics | ❌ | 🟡 Med |
| 8 | RF: Train BI, Test MGB | Hardcoded paths | Pickle, PNG, CSV | ❌ | 🟡 Med |
| 9 | RF: Train MGB, Test BI | Complete_merged_feature_matrix* | Pickle, PNG, CSV | ❌ | 🔴 High |
| 10/10b | RF: Test combined hospitals | Hardcoded paths | Pickle, PNG, CSV | ❌ | 🟡 Med |
| 11 | RF test: Train BI, Test MGB | Complete_merged_feature_matrix* | Pickle, PNG, CSV | ❌ | 🔴 High |
| 12 | RF test: Train MGB, Test BI | Complete_merged_feature_matrix* | Pickle, PNG, CSV | ❌ | 🔴 High |
| 13 | Demographics | Hardcoded paths | Demographics outputs | ❌ | 🟡 Med |
| 14 | FP/FN analysis | false_*_ids.csv, Complete_Notes | false_*_with_notes.csv | ❌ | 🟡 Med |
| 15 | RF ICD-only | Complete_merged_feature_matrix* | PNG, CSV, pickle | ❌ | 🔴 High |
| 16 | RF CPT-only | Complete_merged_feature_matrix* | PNG, CSV, pickle | ❌ | 🔴 High |
| 17 | RF keywords-only | Complete_merged_feature_matrix* | PNG, CSV | ❌ | 🔴 High |
| 18 | Generate comparison graphs | Hardcoded data arrays | Display only | ❌ | 🟢 Low |
| 19 | Cohort reconstruction (BI) | complete_df_initial.csv, Thunderpack | BI_random_unique.csv, BI_df_pred.csv | ❌ | 🔴 High |
| 20 | Cohort reconstruction (MGB) | complete_df_discharge.csv, Thunderpack | MGB_random_unique.csv, MGB_df_pred.csv | ❌ | 🔴 High |
| 21 | Combined error rate | *_random_unique.csv, *_df_pred.csv | Print results only | ❌ | 🟢 Low |
| 22 | LR: Test both hospitals | test_data_.csv | 10 pickles, PNG, CSV | ❌ | 🔴 High |
| 23 | LR ICD-only | train_data_.csv, test_data_.csv | 10 pickles, PNG, CSV | ❌ | 🔴 High |
| 24 | **MISSING** | N/A | N/A | ❌ | 🔴 Critical |
| 25 | LR keywords-only | test_data_.csv | 10 pickles, PNG, CSV | ❌ | 🔴 High |
| 26 | Relabel feature importances | feature_importances_test.csv | Display figure | ❌ | 🟢 Low |

## Recommendations

### Immediate Actions Required

1. **Recover or Recreate Step24**
   - Check git history for deleted "Step24_CPT_logistic_regression_Draft_15 copy.ipynb"
   - Or create new Step24 following pattern of Step23/Step25

2. **Update All Notebooks to Use config.py**
   - Add `import config` to each notebook
   - Replace hardcoded `/home/gregory178/Desktop/NAX project/NAX_SDH/` with `config.get_data_path()`
   - Use `config.get_results_path()` for all output files

3. **Relocate Output Files**
   - PNG plots → `results/figures/`
   - Pickle models → `data/models/`
   - CSV metrics → `results/metrics/`

### Path Update Pattern

**Current (hardcoded):**
```python
df = pd.read_csv("/home/gregory178/Desktop/NAX project/NAX_SDH/train_data_.csv")
plt.savefig('my_plot.png')
```

**Updated (portable):**
```python
import config
df = pd.read_csv(config.get_data_path('train_data_.csv'))
plt.savefig(config.get_results_path('my_plot.png'))
```

## Testing Status

- ✅ **Step1**: Fully updated and tested with config.py
- ⏸️ **Steps 2-26**: Analysis complete, updates pending
- ❌ **Step24**: Missing, needs recovery/recreation

## Next Steps

1. Update README.md with complete step documentation (see next section)
2. Systematically update notebooks (prioritize High priority ones first)
3. Test each updated notebook in sequence
4. Document any dependencies or issues discovered during testing

## Documentation Quality

**Excellent** (clear purpose, methodology, comments):
- Steps 1, 3, 4, 5, 12, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 25

**Good** (basic documentation):
- Steps 2, 6, 7, 7b, 8, 9, 10, 10b, 11, 26

**Needs Improvement**:
- Step 13 (file too large, limited visible documentation)

## Common Dependencies

All notebooks require:
- pandas, numpy, matplotlib
- scikit-learn (LogisticRegression, RandomForestClassifier, metrics, cross_val_score)
- pickle (for model serialization)

Specialized:
- **Step1**: nltk, config.py
- **Steps with Bayes optimization**: skopt.BayesSearchCV
- **Steps 19-20**: ThunderReader
- **Visualization steps**: seaborn, scipy.interpolate

## File Size Summary

- Largest notebooks: Step25 (448KB), Step23 (347KB), Step22 (253KB)
- Smallest notebooks: Step21 (15KB), Step19 (15KB), Step20 (16KB)
- Average size: ~100KB

This indicates heavy computation in LR testing notebooks and lighter analysis in cohort reconstruction.

---

**Report Generated**: 2026-01-20
**Repository**: SDH-EHR-Phenotyping-NAX
**Analysis**: Comprehensive review of 25 Step notebooks
