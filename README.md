# LLM Model Evaluation Framework

A framework to compare the outputs of multiple LLMs on Boolean question-answering tasks.

## Project Structure
```
├── README.md
├── compare.py         # Main script to run model comparison
├── data               # Directory for input data
│   └── sample.json    # Sample evaluation dataset
├── notebooks          # Jupyter notebooks for experimentation
│   └── experiment.ipynb
├── poetry.lock        # Dependency lock file
├── pyproject.toml     # Project configuration and dependencies
├── src                # Source code
│   ├── evaluation     # Evaluation modules
│   │   ├── __init__.py
│   │   └── main.py    # Main evaluation logic
│   └── utils          # Utility functions
│       ├── __init__.py
│       └── data_loader.py  # Data loading utility
└── visualizations     # Output visualizations and reports
    ├── graphs         # Performance graphs
    └── reports        # Detailed evaluation reports
```

## Setup and Installation

1. Install Poetry:
```bash
pip install poetry
```

2. Install dependencies:
```bash
poetry install
```

3. Run the comparison:
```bash
poetry run python compare.py
```

## Features
- Comprehensive model performance evaluation
- Detailed visualizations
- Markdown report generation
- Modular and extensible design

## Outputs
- Performance metrics
- Visualization graphs in `visualizations/graphs/`
- Detailed markdown report in `visualizations/reports/`