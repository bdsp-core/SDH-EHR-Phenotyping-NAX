#!/usr/bin/env python3
"""
Final cleanup script to fix remaining hardcoded paths
"""

import json
import re
from pathlib import Path

def clean_notebook(notebook_path):
    """Remove remaining hardcoded paths"""

    with open(notebook_path, 'r', encoding='utf-8') as f:
        nb = json.load(f)

    changes = 0

    for cell in nb['cells']:
        if cell['cell_type'] == 'code':
            source = ''.join(cell['source'])
            original = source

            # Fix: '/home/gregory178/Desktop/NAX project/NAX_SDH/' + config.get_data_path(...)
            # Should be just: config.get_data_path(...)
            source = re.sub(
                r"['\"](?:/home/gregory178/Desktop/NAX project/NAX_SDH/)?['\"]\s*\+\s*config\.get_(?:data|results)_path\(([^)]+)\)",
                r"config.get_data_path(\1)",
                source
            )

            # Fix double nesting: config.get_data_path(config.get_data_path(...))
            source = re.sub(
                r"config\.get_(?:data|results)_path\(config\.get_(?:data|results)_path\(([^)]+)\)\)",
                r"config.get_data_path(\1)",
                source
            )

            # Replace any remaining hardcoded paths
            source = re.sub(
                r"['\"](?:/home/gregory178/Desktop/NAX project/NAX_SDH/)([^'\"]+\.(?:csv|png|pickle))['\"]",
                lambda m: f"config.get_data_path('{m.group(1)}')" if any(x in m.group(1) for x in ['train_data', 'test_data', 'feature_matrix', 'Complete_merged']) else f"config.get_results_path('{m.group(1)}')",
                source
            )

            if source != original:
                changes += 1
                cell['source'] = source.splitlines(keepends=True)

    if changes > 0:
        with open(notebook_path, 'w', encoding='utf-8') as f:
            json.dump(nb, f, indent=1, ensure_ascii=False)

    return changes

if __name__ == '__main__':
    notebooks = sorted(Path('.').glob('Step*.ipynb'))
    total = 0

    for nb in notebooks:
        changes = clean_notebook(nb)
        if changes > 0:
            print(f"Cleaned {nb.name}: {changes} cells updated")
            total += changes

    print(f"\nTotal notebooks cleaned: {total}")
