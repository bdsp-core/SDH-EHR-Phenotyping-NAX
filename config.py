"""
Configuration file for SDH-EHR-Phenotyping-NAX project.

This file centralizes all path configurations to make the codebase portable.
Users can customize paths by setting environment variables or editing this file.

Usage in notebooks:
    import config
    df = pd.read_csv(config.get_data_path('filename.csv'))
"""

import os
from pathlib import Path

# Project root directory (where this config.py file is located)
PROJECT_ROOT = Path(__file__).parent.absolute()

# Data directory - can be overridden with DATA_DIR environment variable
# Default: PROJECT_ROOT/data subdirectory
DATA_DIR = Path(os.getenv('DATA_DIR', PROJECT_ROOT / 'data'))

# Subdirectories
MODELS_DIR = DATA_DIR / 'models'
RESULTS_DIR = PROJECT_ROOT / 'results'  # Results go in project root/results, not in data/
ANNOTATION_TOOL_DIR = PROJECT_ROOT / 'Annotation_tool'


def get_data_path(filename):
    """
    Get the full path to a data file.

    Args:
        filename (str): Name of the data file

    Returns:
        str: Full path to the data file

    Example:
        >>> path = get_data_path('BI_sampling_cohort_ICD_minus_initial_notes.csv')
    """
    return str(DATA_DIR / filename)


def get_model_path(filename):
    """
    Get the full path to a model file.

    Args:
        filename (str): Name of the model file

    Returns:
        str: Full path to the model file
    """
    return str(MODELS_DIR / filename)


def get_results_path(filename):
    """
    Get the full path to a results file.
    Creates the results directory if it doesn't exist.

    Args:
        filename (str): Name of the results file

    Returns:
        str: Full path to the results file

    Example:
        >>> path = get_results_path('output_plot.png')
        >>> plt.savefig(path)
    """
    # Ensure results directory exists
    RESULTS_DIR.mkdir(parents=True, exist_ok=True)
    return str(RESULTS_DIR / filename)


# Print configuration on import (helpful for debugging)
if __name__ == '__main__':
    print("SDH-EHR-Phenotyping-NAX Configuration")
    print("=" * 50)
    print(f"Project Root: {PROJECT_ROOT}")
    print(f"Data Directory: {DATA_DIR}")
    print(f"Models Directory: {MODELS_DIR}")
    print(f"Results Directory: {RESULTS_DIR}")
    print(f"Annotation Tool Directory: {ANNOTATION_TOOL_DIR}")
