# Data Directory

This directory contains all data files (CSV, pickle models, etc.) used by the SDH-EHR-Phenotyping-NAX project.

## Directory Purpose

All input data files, intermediate results, and trained models are stored here to keep the project root clean and organized.

## Required Data Files

### Input Data Files

The following files are required to run the analysis notebooks:

**Sampling Cohort Files:**
- `BI_sampling_cohort_ICD+_initial_notes.csv` - BIDMC ICD+ initial notes
- `BI_sampling_cohort_ICD_minus_initial_notes.csv` - BIDMC ICD- initial notes
- `MGB_sampling_cohort_ICD+_discharge_notes.csv` - MGB ICD+ discharge notes
- `MGB_sampling_cohort_ICD_minus_discharge_notes.csv` - MGB ICD- discharge notes

**Patient ID Files:**
- `patientIDs_CPT_HeadMRICT_MGB.csv` - MGB patients with CPT codes for head MRI/CT
- `patientIDs_ICD_plus_SDH_BI.csv` - BIDMC patients with ICD+ codes
- `patientIDs_ICD_plus_SDH_MGB.csv` - MGB patients with ICD+ codes
- `patientIDs_ICD_minus2_SDH_BI.csv` - BIDMC patients with ICD- codes
- `patientIDs_ICD_minus2_SDH_MGB.csv` - MGB patients with ICD- codes

**Note:** These data files are NOT included in the repository due to privacy considerations. You must provide your own data files following the expected format.

## Generated Files

The notebooks will generate various intermediate and output files in this directory:

**Feature Matrices:**
- `MGB_BIDMC_CPT_Feature_Matrix_.csv` - Combined feature matrix
- `feature_matrix_MGB_.csv` - MGB feature matrix
- `feature_matrix_BIDMC_.csv` - BIDMC feature matrix
- And various other feature-specific matrices

**Model Files:**
- `RF_model_train_*.pickle` - Random Forest models
- `LR_model_train_*.pickle` - Logistic Regression models
- `*_only_RF_model_*.pickle` - Feature-specific models (ICD, CPT, keywords)

**Results:**
- Various CSV files with predictions, feature importances, and analysis results
- PNG files with visualizations (stored in project root)

## File Organization

Files are automatically read from and written to this directory via the `config.py` module:

```python
import config
df = pd.read_csv(config.get_data_path('filename.csv'))
```

## Data Privacy

**IMPORTANT:** This directory may contain sensitive patient data. Before publishing or sharing:

1. Review all CSV files for Protected Health Information (PHI)
2. Ensure proper de-identification protocols were followed
3. Verify IRB approval for data sharing
4. Consider using synthetic or example data for public repositories

## Git Tracking

By default, data files are excluded from git tracking (see `.gitignore`). This prevents:
- Accidentally committing large files
- Accidentally sharing sensitive patient data
- Repository bloat

If you need to track specific data files, you can:
1. Use Git LFS for large files
2. Modify `.gitignore` to allow specific files
3. Use a separate data repository

## Custom Data Location

If you prefer to store data elsewhere, set the `DATA_DIR` environment variable:

```bash
export DATA_DIR=/path/to/your/data
```

Or create a `.env` file in the project root:
```
DATA_DIR=/path/to/your/data
```

## Questions?

See the main [INSTALLATION.md](../INSTALLATION.md) for setup instructions and troubleshooting.
