# Installation Guide

This guide will help you set up the SDH-EHR-Phenotyping-NAX project on your local machine.

## Prerequisites

- Python 3.8 or higher
- pip or conda package manager
- Git (for cloning the repository)
- Jupyter Notebook or JupyterLab

## Installation Steps

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/SDH-EHR-Phenotyping-NAX.git
cd SDH-EHR-Phenotyping-NAX
```

### 2. Set Up Python Environment

You can use either **pip** or **conda** to set up your environment.

#### Option A: Using pip (recommended)

```bash
# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

#### Option B: Using conda

```bash
# Create environment from environment.yml
conda env create -f environment.yml

# Activate the environment
conda activate sdh-ehr-phenotyping
```

### 3. Download NLTK Data

Some notebooks require NLTK data. Download it by running:

```python
import nltk
nltk.download('punkt')
```

Or run this in your terminal:

```bash
python -c "import nltk; nltk.download('punkt')"
```

### 4. Set Up Data Directory

The project stores all data files in the `data/` subdirectory. You have two options:

#### Option A: Use the default data/ directory (recommended)

Simply place all your data files (CSV files, model files, etc.) in the `data/` subdirectory:

```bash
cd SDH-EHR-Phenotyping-NAX
# Place your data files here:
ls data/
# Should show: BI_sampling_cohort_ICD+_initial_notes.csv, patientIDs_CPT_HeadMRICT_MGB.csv, etc.
```

See [data/README.md](data/README.md) for a complete list of required files.

#### Option B: Use a custom data directory

If you want to store data elsewhere, set the `DATA_DIR` environment variable:

```bash
# On macOS/Linux:
export DATA_DIR=/path/to/your/data

# On Windows:
# set DATA_DIR=C:\path\to\your\data
```

Or create a `.env` file in the project root:

```
DATA_DIR=/path/to/your/data
```

### 5. Verify Installation

Test that everything is installed correctly:

```bash
python config.py
```

This should print the configuration paths without errors.

### 6. Launch Jupyter

```bash
jupyter notebook
```

Or if you prefer JupyterLab:

```bash
jupyter lab
```

## Data Requirements

### Required Data Files

The following data files are expected in the `data/` directory:

**Input Data:**
- `MGB_sampling_cohort_ICD+_discharge_notes.csv`
- `MGB_sampling_cohort_ICD_minus_discharge_notes.csv`
- `BI_sampling_cohort_ICD+_initial_notes.csv`
- `BI_sampling_cohort_ICD_minus_initial_notes.csv`
- `patientIDs_CPT_HeadMRICT_MGB.csv`
- `patientIDs_ICD_plus_SDH_BI.csv`
- `patientIDs_ICD_plus_SDH_MGB.csv`
- `patientIDs_ICD_minus2_SDH_BI.csv`
- `patientIDs_ICD_minus2_SDH_MGB.csv`

**Note:** The actual data files are not included in this repository due to privacy considerations. Please ensure you have the appropriate data files before running the notebooks.

## Execution Order

The notebooks should be executed in the following order:

1. **Step1_Feature_Matrix.ipynb** - Creates feature matrix from notes
2. **Step2_ICD_and_Feature_Matrix.ipynb** - Adds ICD codes and annotations
3. **Steps 3-26** - Follow numerical order for model training and analysis

### Optional Steps

- **Optional_Step1-2** - Generate ICD cohorts (only if creating new cohorts)
- **Optional_Step3-5** - Generate sampling cohorts (only if creating new cohorts)

## Troubleshooting

### Import Errors

If you encounter import errors, ensure all dependencies are installed:

```bash
pip install -r requirements.txt --upgrade
```

### Path Errors

If you get "File not found" errors, verify:
1. Your data files are in the correct directory
2. The `DATA_DIR` environment variable is set correctly (if using custom location)
3. Run `python config.py` to check the configured paths

### NLTK Errors

If you get NLTK-related errors, download the required data:

```python
import nltk
nltk.download('punkt')
nltk.download('punkt_tab')
```

### Jupyter Kernel Issues

If Jupyter doesn't recognize your virtual environment:

```bash
# Install ipykernel in your environment
pip install ipykernel

# Add your environment to Jupyter
python -m ipykernel install --user --name=sdh-ehr-phenotyping
```

## Additional Configuration

### For Thunderpack Data (Optional Steps 3-4)

If you're running Optional_Step3 or Optional_Step4 which use Thunderpack:

1. Ensure you have access to the Thunderpack data directories
2. Update the paths in cells 2 and 5 to point to your Thunderpack data location
3. These paths are external to the project and specific to your data storage setup

### For Large Model Files

If you have large pickle model files (>100MB), consider using Git LFS:

```bash
git lfs install
git lfs track "*.pickle"
```

## Getting Help

If you encounter any issues not covered here:

1. Check that all dependencies are correctly installed
2. Verify your Python version is 3.8 or higher
3. Review the error messages carefully for missing files or permissions issues
4. Consult the main README.md for additional project information

## Next Steps

After successful installation:

1. Review the README.md for project overview
2. Start with Step1_Feature_Matrix.ipynb
3. Follow the notebook execution order listed above
