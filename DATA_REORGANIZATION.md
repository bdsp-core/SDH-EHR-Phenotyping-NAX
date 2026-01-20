# Data Directory Reorganization Summary

## What Changed

All 194 data files (CSV, pickle, and pkl files) have been moved from the project root to a new `data/` subdirectory for better organization.

## Benefits

1. **Cleaner Repository Structure** - Project root is no longer cluttered with data files
2. **Better Separation of Concerns** - Code and data are clearly separated
3. **Easier Git Management** - Data files are now in one location and excluded via .gitignore
4. **Professional Organization** - Follows standard project structure conventions

## File Moves

### From (Root Directory):
```
SDH-EHR-Phenotyping-NAX/
├── BI_sampling_cohort_ICD+_initial_notes.csv
├── patientIDs_CPT_HeadMRICT_MGB.csv
├── RF_model_train_*.pickle
└── ... (191 more data files)
```

### To (Data Subdirectory):
```
SDH-EHR-Phenotyping-NAX/
└── data/
    ├── README.md (documentation)
    ├── .gitkeep (ensures directory is tracked)
    ├── BI_sampling_cohort_ICD+_initial_notes.csv
    ├── patientIDs_CPT_HeadMRICT_MGB.csv
    ├── RF_model_train_*.pickle
    └── ... (191 more data files)
```

## Configuration Updates

**config.py** has been updated to use `data/` as the default directory:

```python
# Before:
DATA_DIR = Path(os.getenv('DATA_DIR', PROJECT_ROOT))

# After:
DATA_DIR = Path(os.getenv('DATA_DIR', PROJECT_ROOT / 'data'))
```

## Notebook Compatibility

**No changes needed!** All notebooks already use `config.get_data_path()` which automatically resolves to the correct location.

Example from Step1_Feature_Matrix.ipynb:
```python
import config
MGB_plus = pd.read_csv(config.get_data_path("MGB_sampling_cohort_ICD+_discharge_notes.csv"))
# This now correctly points to: data/MGB_sampling_cohort_ICD+_discharge_notes.csv
```

## Git Tracking

### What's Tracked:
- `data/` directory structure
- `data/README.md` (documentation)
- `data/.gitkeep` (ensures directory exists)

### What's Ignored:
- `data/*.csv` - All CSV files in data/
- `data/*.pickle` - All pickle files in data/
- `data/*.pkl` - All pkl files in data/

This prevents large data files from being committed while maintaining the directory structure.

## Verification

Test that everything works:

```bash
# Verify config points to data/
python config.py

# Should show:
# Data Directory: /path/to/project/data
# ✓ Found 112 CSV files in data/
# ✓ Found 82 model files in data/
```

## For New Users

When cloning this repository:

1. The `data/` directory will exist (via .gitkeep)
2. `data/README.md` will explain what files are needed
3. Place your data files in `data/` directory
4. Run notebooks as normal - they'll automatically find data in `data/`

## For Existing Users

If you already have the repository:

1. **Data files have been moved** from root to `data/`
2. **No code changes needed** - notebooks use config.get_data_path()
3. **Just pull the latest changes** and everything will work

## Custom Data Location

If you prefer to keep data elsewhere:

```bash
export DATA_DIR=/path/to/your/data
```

Or create `.env` file:
```
DATA_DIR=/path/to/your/data
```

## Summary

✅ All 194 data files moved to `data/` subdirectory
✅ config.py updated to default to `data/`
✅ .gitignore updated to exclude data files
✅ data/README.md documents expected files
✅ Notebooks work without modification
✅ Cleaner, more professional repository structure

No action required - notebooks will automatically find data in the new location!
