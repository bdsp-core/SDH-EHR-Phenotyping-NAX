# SDH-EHR-Phenotyping-NAX: Comprehensive Codebase Analysis

## Executive Summary

This is a machine learning research project for detecting **Acute Subdural Hematoma (aSDH)** in clinical EHR records using predictive phenotyping. The codebase consists of 26+ sequential Jupyter notebooks written in Python, processing clinical data from two hospitals (BIDMC and Mass General/MGB) to train and validate classification models.

**Key Finding**: This is a data-intensive research project that **requires significant cleanup before publication** on GitHub due to hardcoded paths, large data files, and embedded credentials.

---

## 1. DIRECTORY STRUCTURE & FILE ORGANIZATION

### Root Directory Layout
```
SDH-EHR-Phenotyping-NAX/
├── README.md                          # Project documentation
├── LICENSE                            # MIT License (2024, BDSP)
├── Annotation_tool/                   # Sub-folder: manual annotation interface
├── Step1_Feature_Matrix.ipynb         # Workflow steps 1-26+ (main analysis)
├── Step2_ICD_and_Feature_Matrix.ipynb
├── ... (26 total step notebooks)
├── Optional_Step1-5.ipynb             # Optional cohort generation steps
├── Data files                         # 242 CSV/pickle/PNG artifacts
├── Models                             # Trained sklearn models (pickle files)
└── .git/                              # Git repository
```

### Data Organization
- **CSV Data Files**: ~240+ CSV files containing clinical notes, ICD codes, CPT codes
- **Model Artifacts**: 20+ Random Forest & Logistic Regression pickle files (1-13MB each)
- **Feature Matrices**: Pre-computed feature matrices from notes, ICD, CPT codes
- **Results**: PNG visualizations, prediction CSVs, feature importance rankings
- **Annotation Tool**: HTML-based interface with supporting CSS/JS/Python files

### File Inventory
```
Total files in root: 284 items
- Jupyter Notebooks: 31 (.ipynb files)
- Python Scripts: 2 (Annotation_tool/)
- CSV Data/Results: ~200+ files (largest: 44MB patientIDs_CPT_HeadMRICT_MGB.csv)
- Pickle Models: 30+ trained models
- Images: 60+ PNG visualizations
- Config/Other: HTML annotation tool, JS/CSS files
```

---

## 2. PROGRAMMING LANGUAGES & TECHNOLOGIES

### Primary Language
- **Python 3.x** exclusively used for all analysis
- **Jupyter Notebooks** as development/execution environment

### Key Dependencies (by usage frequency)

| Library | Frequency | Purpose |
|---------|-----------|---------|
| scikit-learn | 73 | ML models (RandomForest, LogisticRegression, cross-validation) |
| pandas | 36 | Data manipulation and CSV I/O |
| numpy | 28 | Numerical operations |
| matplotlib | 23 | Data visualization (plots, graphs) |
| scikit-optimize | 18 | Hyperparameter tuning |
| pickle | 16 | Model serialization |
| tqdm | 13 | Progress bars |
| seaborn | 9 | Advanced statistical visualization |
| scipy | 9 | Statistical tests (e.g., DeLong test for AUC comparison) |
| thunderpack | 7 | Data compression/loading (non-standard) |
| nltk | 2 | Natural Language Toolkit for text processing |
| csv, re, gc, random, zipfile, tempfile, io | Various | Utilities |

### External Requirements
- **Non-standard package**: `thunderpack` - used for data compression (requires investigation)
- **Optional**: MLstatkit - appears in one notebook

---

## 3. HARDCODED PATHS - CRITICAL ISSUES

### PRIMARY ISSUE: Absolute Filesystem Paths
All notebooks contain hardcoded paths specific to developer's machine. This is the **most critical cleanup item**.

#### Examples Found:
```python
# From Step1_Feature_Matrix.ipynb and others:
BI_minus = pd.read_csv("/home/gregory178/Desktop/NAX project/NAX_SDH/BI_sampling_cohort_ICD_minus_initial_notes.csv")
BI_plus = pd.read_csv("/home/gregory178/Desktop/NAX project/NAX_SDH/BI_sampling_cohort_ICD+_initial_notes.csv")
MGB_minus = pd.read_csv("/home/gregory178/Desktop/NAX project/NAX_SDH/MGB_sampling_cohort_ICD_minus_discharge_notes.csv")
MGB_plus = pd.read_csv("/home/gregory178/Desktop/NAX project/NAX_SDH/MGB_sampling_cohort_ICD+_discharge_notes.csv")
CPTs = pd.read_csv('/home/gregory178/Desktop/NAX project/NAX_SDH/patientIDs_CPT_HeadMRICT_MGB.csv')

# From Annotation_tool/READ_ME.py:
path = "/home/gregory178/Desktop/NAX project/NAX_SDH/Annotation_tool_training_error/"
```

#### Notebooks Affected:
- Step1_Feature_Matrix.ipynb - 6+ hardcoded paths
- Optional_Step3_generateSamplingCohort_BI.ipynb - 4 paths
- Optional_Step4_generateSamplingCohort_MGB.ipynb - 4 paths  
- Optional_Step5_pos_icd_to_csv.ipynb - 4 paths
- Annotation_tool/READ_ME.py - 1 path (but with user instruction)

#### Paths to Replace:
- `/home/gregory178/Desktop/NAX project/NAX_SDH/` - All instances
- Replace with relative paths or `os.path.dirname(__file__)` pattern

---

## 4. DEPENDENCIES & CONFIGURATION FILES

### Currently Missing
```
MISSING:
- requirements.txt or requirements-dev.txt
- setup.py or pyproject.toml
- environment.yml (Conda)
- Dockerfile
- .gitignore (proper one)
- .github/workflows/ (CI/CD)
- documentation/dependencies.md
```

### Current State
- No centralized dependency tracking
- Versions of packages not specified anywhere
- Users must manually install: `pip install pandas numpy scikit-learn matplotlib scikit-optimize tqdm seaborn scipy nltk thunderpack`
- NLTK data may need downloading separately: `nltk.download('punkt')` etc.

### Recommendation
Create `requirements.txt`:
```
pandas>=1.3.0
numpy>=1.20.0
scikit-learn>=1.0.0
matplotlib>=3.3.0
scikit-optimize>=0.9.0
tqdm>=4.60.0
seaborn>=0.11.0
scipy>=1.7.0
nltk>=3.6.0
```

Note: `thunderpack` may need to be removed or replaced with standard libraries

---

## 5. CONFIGURATION & METADATA FILES

### Existing Files
- `.git/` - Version control initialized
- `.claude/settings.local.json` - Claude IDE settings (local only)
- `LICENSE` - MIT License present (good!)
- `README.md` - Documentation exists (26 steps documented)
- `hey.txt` - Artifact file (should be deleted)

### Annotation Tool Config
- `Annotation_tool/regexes.js` - Keywords for highlighting clinical notes
- `Annotation_tool/css.css` - UI styling
- `Annotation_tool/data.js` - Auto-generated data file (reproducible)
- `Annotation_tool/20240429_annotation tool_open source (1).html` - Main UI

### Missing Recommended Files
```
Missing:
- .gitignore (should exclude: *.pickle, large CSVs, .DS_Store, data/, models/)
- CONTRIBUTING.md
- CITATION.cff or citation format
- .github/workflows/ (testing, documentation builds)
- docs/ folder with detailed methodology
- config/ folder for configurable parameters
```

---

## 6. MAIN ENTRY POINTS & SCRIPTS

### Execution Model: Sequential Notebooks
The project is **not** designed as a Python package but as a sequence of notebooks:

```
WORKFLOW EXECUTION ORDER:
├── Data Preparation (All hospitals)
│   ├── Step1_Feature_Matrix.ipynb              → Creates feature matrix from notes
│   └── Step2_ICD_and_Feature_Matrix.ipynb      → Adds ICD codes + manual annotations
│
├── Training Phase (Steps 3-9, 13-17, 23-25)
│   ├── Step3-4: Hospital-specific logistic regression
│   ├── Step5: Combined logistic regression
│   ├── Step6: Error analysis
│   ├── Step7-9: Random Forest training
│   ├── Steps 13-17: Feature-specific models (ICD-only, CPT-only, Keywords-only)
│   ├── Steps 23-25: Logistic regression variants
│   └── Step26: Rename/format feature importances
│
├── Testing Phase (Steps 10-12, 22)
│   ├── Step10: RF on both hospitals (test data)
│   ├── Step11-12: Hospital cross-validation
│   └── Step22: LR on both hospitals (test data)
│
├── Analysis & Reporting
│   ├── Step14: False positive/negative analysis
│   ├── Step18: Generate comparison graphs
│   ├── Step19-21: Cohort reconstruction & error rates
│   └── delong_test_compare_AUC.ipynb: Statistical comparison
│
└── Optional: Generate New Cohorts
    ├── Optional_Step1-2: Extract ICD cohorts
    └── Optional_Step3-5: Generate sampling cohorts
```

### No Standalone Scripts
- **No main.py, run.py, or command-line interface**
- Requires manual "Run All" on each notebook in sequence
- Depends on previous notebook outputs (CSV/pickle files)

### Annotation Tool Entry Points
- `Annotation_tool/READ_ME.py` - Converts CSV to JSON for annotation UI
- `Annotation_tool/20240429_annotation_tool_open source (1).html` - Open in browser
- `Annotation_tool/Instructions.py` - User instructions

---

## 7. CODEBASE PATTERNS & OBSERVATIONS

### Notebook Structure
- **All code cells, no markdown**: Notebooks only have code and brief inline comments
- **No documentation strings**: No docstrings, minimal function documentation
- **Linear execution**: Each notebook depends on outputs of previous ones
- **Average notebook size**: 200KB-800KB (large with many cells)
- **Consistent naming**: Column names standardized (PatientID, BDSPPatientID, etc.)

### Data Flow Patterns
```
Step1 → [notes features] → Step2 → [+ ICD codes + labels] → Steps 3-26
```

### Machine Learning Patterns
- **Models used**: LogisticRegression, RandomForestClassifier
- **Cross-validation**: 10-fold nested cross-validation (Steps 7, 10, 22)
- **Hyperparameter tuning**: scikit-optimize (BayesSearchCV)
- **Metrics computed**: AUC, PR, Sensitivity, Specificity, Confidence Intervals
- **Multiple feature sets**: Notes + ICD + CPT codes + Keywords tested separately

### Code Quality Issues
- Repetitive code across notebooks (copy-paste patterns visible)
- Inconsistent variable naming conventions
- No error handling or validation
- No logging
- No unit tests
- Inline comments not comprehensive

---

## 8. DATA FILES OVERVIEW

### Largest Files (May Need Exclusion from Public Repo)

```
Size    | File Name
--------|-----------------------------------------------------------
44 MB   | patientIDs_CPT_HeadMRICT_MGB.csv
37 MB   | MGB_BIDMC_Complete_Notes.csv
25 MB   | MGB_Complete_Notes.csv (contains patient notes text)
25 MB   | MGB_CPT_.csv
13 MB   | MGB_sampling_cohort_ICD+_discharge_notes.csv (sensitive)
13 MB   | RF_model_train_allhospitals_Notes+ICD+Med_fold10.pickle
12 MB   | BI_sampling_cohort_ICD_minus_initial_notes.csv (sensitive)
11 MB   | MGB_sampling_cohort_ICD_minus_discharge_notes.csv (sensitive)
11 MB   | BIDMC_CPT_.csv
11 MB   | BIDMC_Complete_Notes.csv (contains patient notes)
```

### Sensitivity Concerns
- **Patient Clinical Notes**: Multiple CSV files contain de-identified patient notes
- **Patient IDs**: Files contain patient identifiers (BDSPPatientID, BDSP_PatientID)
- **ICD/CPT Codes**: Disease/procedure information tied to patients
- **Recommendation**: These should likely be removed from public repository

### Model Files
- 30+ trained Random Forest & Logistic Regression pickle files
- Purpose: For reproducibility and paper results
- Size: 1-13MB each
- **Total model storage**: ~200MB

---

## 9. PUBLICATION READINESS ASSESSMENT

### CRITICAL ISSUES (Must Fix Before Publishing)

| Issue | Severity | Impact | Fix Effort |
|-------|----------|--------|-----------|
| Hardcoded filesystem paths in all notebooks | CRITICAL | Won't run anywhere else | HIGH |
| Patient data/notes in CSV files | CRITICAL | Privacy/ethics concern | HIGH |
| No requirements.txt | HIGH | Can't install dependencies | LOW |
| Large data files in git | HIGH | Repo bloat, slow clones | HIGH |
| No CI/CD, no tests | MEDIUM | No reproducibility guarantee | MEDIUM |
| Copy-paste code duplication | MEDIUM | Maintenance nightmare | MEDIUM |
| No .gitignore | MEDIUM | Will commit artifacts | LOW |
| OS artifacts (.DS_Store) committed | MINOR | Clutter | LOW |

### IMPORTANT NOTES

1. **Data Privacy**: The data files contain actual clinical notes and patient identifiers. This likely requires:
   - IRB review for open-source release
   - De-identification verification
   - Possible exclusion from public repo (GitHub LFS or separate data source)

2. **Reproducibility**: Current state requires:
   - Manual step-by-step notebook execution
   - Having exact same CSV files in exact same locations
   - No automation or scripting

3. **Maintenance**: Would be difficult for others to:
   - Fix bugs in the workflow
   - Adapt to new data
   - Run in CI/CD environment
   - Deploy as a service

---

## 10. RECOMMENDATIONS FOR CLEANUP & PUBLICATION

### Phase 1: Essential Fixes (MUST DO)
1. Create `requirements.txt` with pinned versions
2. Create comprehensive `.gitignore` 
3. Replace all hardcoded paths with relative paths or config file
4. Create `config.yaml` or `config.py` for data directories
5. Add `.DS_Store` cleanup (already in one .gitignore rule suggested)

### Phase 2: Data Management (CRITICAL)
1. Remove patient data CSVs from git (use `.gitignore`)
2. Create `data/` directory structure documented in README
3. Consider GitHub LFS for large model files
4. Document data sources and privacy compliance
5. Create synthetic data example for testing

### Phase 3: Code Improvement (IMPORTANT)
1. Consolidate repetitive code into functions/utilities
2. Create `src/` folder with reusable modules
3. Add docstrings and comments
4. Create unit tests
5. Add input validation and error handling

### Phase 4: Documentation (RECOMMENDED)
1. Create `docs/` folder with:
   - Data schema documentation
   - Methodology explanation
   - Installation guide
   - Usage examples
2. Add CONTRIBUTING.md
3. Add CITATION.cff for academic citation
4. Create workflow diagram

### Phase 5: Infrastructure (OPTIONAL)
1. Add `.github/workflows/` for CI/CD
2. Consider packaging as Python module
3. Add Docker support
4. Add pre-commit hooks

---

## 11. FILE LISTING BY CATEGORY

### Jupyter Notebooks (31 total)
```
Main Analysis:
  Step1_Feature_Matrix.ipynb
  Step2_ICD_and_Feature_Matrix.ipynb
  Step3_train_BIDMC_Test_MGB.ipynb
  Step4_train_MGB_Test_BIDMC.ipynb
  Step5_train_test_both_hospitals.ipynb
  Step6_error_analysis_training.ipynb
  Step7_random_forest.ipynb
  Step7b_random_forest-train_past.ipynb
  Step8_RF_train_BIDMC_Test_MGB.ipynb
  Step9_RF_train_MGB_Test_BIDMC_Draft_15.ipynb
  Step10_RF_test_both_hospitals.ipynb
  Step10b_RF_test_both_hospitals-future.ipynb
  Step11_test_version_RF_train_BIDMC_Test_MGB_Draft_15.ipynb
  Step12_test_version_RF_train_MGB_Test_BIDMC_Draft_15.ipynb
  Step13_demographics.ipynb
  Step14_FN_FP_analysis.ipynb
  Step15_ICD_random_forest_Draft_15.ipynb
  Step16_CPT_random_forest_Draft_15.ipynb
  Step17_keywords_random_forest_Draft_15.ipynb
  Step18_graph_generation.ipynb
  Step19_cohort_reconstruction_BI.ipynb
  Step20_cohort_reconstruction_MGB.ipynb
  Step21_cohort_reconstruction_both.ipynb
  Step22_LR_test_both_hospitals.ipynb
  Step23_ICD_logistic_regression_Draft_15.ipynb
  Step24_CPT_logistic_regression_Draft_15 copy.ipynb
  Step25_kw_logistic_regression_Draft_15.ipynb
  Step26_rename_feature_importances.ipynb

Optional/Utility:
  Optional_Step1_BI_ICD_cohort_gen.ipynb
  Optional_Step2_MGB_ICD_cohort_gen.ipynb
  Optional_Step3_generateSamplingCohort_BI.ipynb (1.9MB - large)
  Optional_Step4_generateSamplingCohort_MGB.ipynb (724KB)
  Optional_Step5_pos_icd_to_csv.ipynb
  delong_test_compare_AUC.ipynb
```

### Python Scripts (2)
```
Annotation_tool/READ_ME.py
Annotation_tool/Instructions.py
```

### Annotation Tool Files
```
Annotation_tool/20240429_annotation tool_open source (1).html
Annotation_tool/css.css
Annotation_tool/data.js
Annotation_tool/regexes.js
```

### Important Large Files (should be .gitignore'd)
```
CSV Data (>5MB):
  - All *sampling_cohort*.csv files
  - All *Complete_Notes.csv files
  - patientIDs_CPT_HeadMRICT_MGB.csv (44MB)
  - All merged feature matrix files

Pickle Models:
  - RF_model_train_allhospitals_Notes+ICD+Med_*.pickle (40-13MB)
  - *_only_RF_model_train_*.pickle files
  - model_train_*.pickle files

Images/Outputs:
  - All *.png files (~60 visualizations)
  - Various results CSVs
```

---

## SUMMARY TABLE

| Aspect | Current State | Status |
|--------|---------------|--------|
| **Language** | Python 3 | Good |
| **Framework** | Jupyter Notebooks | Acceptable for research |
| **Dependencies** | Documented via code only | Needs requirements.txt |
| **Hardcoded Paths** | Extensive (/home/gregory178/...) | CRITICAL |
| **Data Privacy** | Contains patient data | CRITICAL |
| **License** | MIT (good!) | Good |
| **Documentation** | README present (good) | Needs improvement |
| **Tests** | None | Missing |
| **CI/CD** | None | Missing |
| **Entry Points** | Sequential notebooks | Not automated |
| **Code Reusability** | Low (repetitive code) | Needs refactoring |
| **Reproducibility** | High (files provided) | Limited by hardcoded paths |
| **Publication Ready** | No | Needs significant cleanup |

---

## CONCLUSION

This is a well-executed research project with good documentation and reproducible results. However, it **requires significant cleanup** before publication on GitHub:

1. **Most Urgent**: Remove/replace hardcoded paths (affects all notebooks)
2. **Very Important**: Address data privacy/sensitivity
3. **Important**: Add requirements.txt, .gitignore, config management
4. **Recommended**: Refactor code for reusability, add tests
5. **Nice to Have**: Docker, CI/CD, comprehensive documentation

**Estimated cleanup effort**: 2-3 weeks of focused work to reach professional publication standard.

