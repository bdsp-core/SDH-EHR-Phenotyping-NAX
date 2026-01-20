# Pre-Publication Cleanup Checklist

## Priority 1: CRITICAL (Block Publication)

- [ ] **Hardcoded Paths**: Replace all `/home/gregory178/Desktop/NAX project/NAX_SDH/` paths
  - Notebooks affected: Step1, Optional_Step3-5
  - Solution: Create `config.py` with `DATA_DIR` variable
  - Files to modify:
    - Step1_Feature_Matrix.ipynb
    - Optional_Step3_generateSamplingCohort_BI.ipynb
    - Optional_Step4_generateSamplingCohort_MGB.ipynb
    - Optional_Step5_pos_icd_to_csv.ipynb
    - Annotation_tool/READ_ME.py

- [ ] **Data Privacy Review**: Audit what should/shouldn't be in public repo
  - Patient notes CSVs: 11-37MB
  - Patient ID files with condition data
  - Decision: Remove data or create synthetic examples
  
- [ ] **Create requirements.txt**
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

- [ ] **Create .gitignore**
  ```
  # Data files
  *.pickle
  *.pkl
  data/
  models/
  
  # Large CSVs
  *sampling_cohort*.csv
  *Complete_Notes.csv
  patientIDs_*.csv
  
  # OS artifacts
  .DS_Store
  *.swp
  *~
  
  # Python
  __pycache__/
  *.pyc
  .pytest_cache/
  
  # Jupyter
  .ipynb_checkpoints/
  
  # IDE
  .vscode/
  .idea/
  ```

## Priority 2: HIGH (Strongly Recommended)

- [ ] **Create config.yaml or config.py**
  ```python
  # config.py
  import os
  
  # Data directories
  DATA_DIR = os.getenv('DATA_DIR', './data')
  MODELS_DIR = os.path.join(DATA_DIR, 'models')
  RESULTS_DIR = os.path.join(DATA_DIR, 'results')
  ```

- [ ] **Remove .DS_Store**: `git rm --cached .DS_Store`

- [ ] **Remove duplicate notebooks**: `Step24_CPT_logistic_regression_Draft_15 copy.ipynb`

- [ ] **Remove test/placeholder file**: `hey.txt`

- [ ] **Create INSTALLATION.md with setup instructions**

- [ ] **Add data schema documentation**: Document expected CSV format

## Priority 3: MEDIUM (Recommended)

- [ ] **Create .github/workflows/ for CI/CD**
  - Notebook execution tests
  - Reproducibility checks

- [ ] **Add CONTRIBUTING.md** for development guidelines

- [ ] **Add CITATION.cff** for academic citation

- [ ] **Consolidate common code patterns**
  - Cross-validation setup is repeated
  - Model evaluation metrics repeated
  - Consider creating `src/utils.py`

- [ ] **Add docstrings to notebooks**
  - Each notebook should have cell 1: description
  - Function documentation for complex operations

- [ ] **Create docs/ folder with:**
  - methodology.md
  - data_schema.md
  - workflow_diagram.md

## Priority 4: OPTIONAL (Nice to Have)

- [ ] **Dockerfile** for reproducible environment

- [ ] **Docker-compose** for annotation tool

- [ ] **Unit tests** for data processing steps

- [ ] **Pre-commit hooks** for code quality

- [ ] **Package as Python module** (setup.py)

- [ ] **GitHub Actions**: Automated notebook execution

---

## Quick Implementation Guide

### Step 1: Config Management (30 min)
```python
# config.py
import os
from pathlib import Path

PROJECT_DIR = Path(__file__).parent
DATA_DIR = os.getenv('DATA_DIR', str(PROJECT_DIR / 'data'))
MODELS_DIR = os.path.join(DATA_DIR, 'models')
RESULTS_DIR = os.path.join(DATA_DIR, 'results')

# In notebooks: replace hardcoded paths with:
import config
df = pd.read_csv(os.path.join(config.DATA_DIR, 'file.csv'))
```

### Step 2: .gitignore Setup (5 min)
```bash
# Add to .gitignore
echo "*.pickle" >> .gitignore
echo "data/" >> .gitignore
echo ".DS_Store" >> .gitignore
git rm --cached .DS_Store
git add .gitignore
git commit -m "Add proper .gitignore and remove OS artifacts"
```

### Step 3: requirements.txt (5 min)
```bash
pip freeze | grep -E "pandas|numpy|scikit|matplotlib|tqdm|seaborn|scipy|nltk" > requirements.txt
```

### Step 4: Data Privacy Decision (2-4 hours)
- [ ] Review current patient data files
- [ ] Consult with IRB/compliance team
- [ ] Decide: Include in repo, GitHub LFS, or separate download
- [ ] Document in README

### Step 5: Path Replacement (2-3 hours)
- [ ] Create config.py
- [ ] Update all notebooks to use config
- [ ] Test locally with relative paths

---

## Testing After Cleanup

1. **Fresh clone test**: Clone repo, verify all notebooks run
2. **Path test**: Verify no absolute paths remain
3. **Import test**: Verify all packages in requirements.txt
4. **Data test**: Verify data loading works with new paths
5. **Execution test**: Run through Step 1-5 sequentially

---

## Files Status

| File | Status | Action |
|------|--------|--------|
| config.py | Missing | CREATE |
| requirements.txt | Missing | CREATE |
| .gitignore | Missing | CREATE |
| INSTALLATION.md | Missing | CREATE |
| hey.txt | Present | DELETE |
| .DS_Store | Present | REMOVE |
| Step24_CPT...copy.ipynb | Present | DELETE |
| Step1_Feature_Matrix.ipynb | Hardcoded paths | EDIT |
| Optional_Step3-5.ipynb | Hardcoded paths | EDIT |
| Annotation_tool/READ_ME.py | Hardcoded path | EDIT |

