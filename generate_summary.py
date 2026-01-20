#!/usr/bin/env python3
import json
from pathlib import Path
import re

notebooks = [
    "Step2_ICD_and_Feature_Matrix.ipynb",
    "Step3_train_BIDMC_Test_MGB.ipynb",
    "Step4_train_MGB_Test_BIDMC.ipynb",
    "Step5_train_test_both_hospitals.ipynb",
    "Step6_error_analysis_training.ipynb",
    "Step7_random_forest.ipynb",
    "Step7b_random_forest-train_past.ipynb",
    "Step8_RF_train_BIDMC_Test_MGB.ipynb",
    "Step9_RF_train_MGB_Test_BIDMC_Draft_15.ipynb",
    "Step10_RF_test_both_hospitals.ipynb",
    "Step10b_RF_test_both_hospitals-future.ipynb",
    "Step11_test_version_RF_train_BIDMC_Test_MGB_Draft_15.ipynb",
    "Step12_test_version_RF_train_MGB_Test_BIDMC_Draft_15.ipynb",
    "Step13_demographics.ipynb",
    "Step14_FN_FP_analysis.ipynb",
    "Step15_ICD_random_forest_Draft_15.ipynb",
    "Step16_CPT_random_forest_Draft_15.ipynb",
    "Step17_keywords_random_forest_Draft_15.ipynb",
    "Step18_graph_generation.ipynb",
    "Step19_cohort_reconstruction_BI.ipynb",
    "Step20_cohort_reconstruction_MGB.ipynb",
    "Step21_cohort_reconstruction_both.ipynb",
    "Step22_LR_test_both_hospitals.ipynb",
    "Step23_ICD_logistic_regression_Draft_15.ipynb",
    "Step25_kw_logistic_regression_Draft_15.ipynb",
    "Step26_rename_feature_importances.ipynb",
]

results_files = set()
data_files = set()

for nb_name in notebooks:
    if not Path(nb_name).exists():
        continue
    
    with open(nb_name, 'r') as f:
        nb = json.load(f)
    
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            
            # Find config.get_results_path calls
            results = re.findall(r"config\.get_results_path\(['\"]([^'\"]+)['\"]\)", source)
            results_files.update(results)
            
            # Find config.get_data_path calls (outputs only)
            data_outputs = re.findall(r"(?:\.to_csv|\.savefig|pickle\.dump).*?config\.get_data_path\(['\"]([^'\"]+)['\"]\)", source)
            data_files.update(data_outputs)

print("=" * 80)
print("SUMMARY: Files by Directory")
print("=" * 80)
print(f"\nResults Directory (results/): {len(results_files)} files")
for f in sorted(results_files):
    print(f"  - {f}")

print(f"\nData Directory (data/): {len(data_files)} output files")
for f in sorted(data_files):
    print(f"  - {f}")
