#!/usr/bin/env python3
"""
Script to update hardcoded paths in Jupyter notebooks to use config.py
"""

import json
import re
import sys
from pathlib import Path

def update_notebook_paths(notebook_path):
    """Update paths in a notebook to use config.py"""

    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    changes = {
        'data_reads': 0,
        'data_writes': 0,
        'result_writes': 0,
        'config_added': False
    }

    # Check if config is already imported
    has_config = False
    first_code_cell_idx = None

    for idx, cell in enumerate(nb['cells']):
        if cell['cell_type'] == 'code':
            if first_code_cell_idx is None:
                first_code_cell_idx = idx
            source = ''.join(cell['source'])
            if 'import config' in source:
                has_config = True
                break

    # Add config import to first code cell if not present
    if not has_config and first_code_cell_idx is not None:
        cell = nb['cells'][first_code_cell_idx]
        source = ''.join(cell['source'])

        # Add import config at the beginning
        if source.strip():
            new_source = 'import config\n' + source
            cell['source'] = new_source.splitlines(keepends=True)
            changes['config_added'] = True

    # Process all cells for path replacements
    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            original_source = source

            # Pattern for data file reads (input files)
            # Pattern: /home/gregory178/Desktop/NAX project/NAX_SDH/filename.csv
            pattern1 = r"['\"](?:/home/gregory178/Desktop/NAX project/NAX_SDH/)([^'\"]+)['\"]"

            def replace_data_read(match):
                filename = match.group(1)
                changes['data_reads'] += 1
                return f"config.get_data_path('{filename}')"

            source = re.sub(pattern1, replace_data_read, source)

            # Pattern for data file writes (to data directory)
            # Common data files that should stay in data/
            data_output_files = [
                'feature_matrix_notes_CPT_and_ICD_.csv',
                'Complete_merged_feature_matrix_notes_CPT_and_ICD_.csv',
                'train_data_.csv',
                'test_data_.csv',
                'MGB_BIDMC_CPT_Feature_Matrix_.csv'
            ]

            # Pattern for output files - CSV and image files
            pattern2 = r"['\"](?:/home/gregory178/Desktop/NAX project/NAX_SDH/)?([^'\"]+\.(?:csv|png|pickle|pkl))['\"]"

            def replace_output(match):
                full_match = match.group(0)
                filename = match.group(1)

                # Skip if already using config
                if 'config.get_' in full_match:
                    return full_match

                # Check if it's a data file or result file
                if any(df in filename for df in data_output_files):
                    changes['data_writes'] += 1
                    return f"config.get_data_path('{filename}')"
                else:
                    changes['result_writes'] += 1
                    return f"config.get_results_path('{filename}')"

            source = re.sub(pattern2, replace_output, source)

            # Handle model pickle dumps (should go to data/models but we'll use data for now)
            pattern3 = r"with open\s*\(\s*['\"]([^'\"]+\.pickle)['\"]"

            def replace_model(match):
                filename = match.group(1)
                if 'model_' in filename:
                    changes['data_writes'] += 1
                    return f"with open(config.get_data_path('{filename}')"
                return match.group(0)

            source = re.sub(pattern3, replace_model, source)

            # Update the cell if changes were made
            if source != original_source:
                cell['source'] = source.splitlines(keepends=True)

    # Save the updated notebook
    with open(notebook_path, 'w', encoding='utf-8') as f:
        json.dump(nb, f, indent=1, ensure_ascii=False)

    return changes

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python update_notebook_paths.py <notebook_path>")
        sys.exit(1)

    notebook_path = sys.argv[1]
    changes = update_notebook_paths(notebook_path)

    print(f"Updated {Path(notebook_path).name}:")
    print(f"  - Config added: {changes['config_added']}")
    print(f"  - Data reads updated: {changes['data_reads']}")
    print(f"  - Data writes updated: {changes['data_writes']}")
    print(f"  - Result writes updated: {changes['result_writes']}")
    print(f"  - Total changes: {changes['data_reads'] + changes['data_writes'] + changes['result_writes']}")
