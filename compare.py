import sys
import os
from src.utils.data_loader import load_evaluation_data, extract_model_predictions
from src.evaluation.main import ModelComparator

# Add the project root to the Python path
project_root = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, project_root)

def main():
    # Load data from JSON file
    data_path = os.path.join(project_root, 'data', 'sample.json')
    data = load_evaluation_data(data_path)
    
    # Extract model predictions
    predictions = extract_model_predictions(data)
    
    # Initialize comparator
    comparator = ModelComparator(
        questions=predictions['questions'],
        ground_truth=predictions['ground_truth'],
        model_a_responses=predictions['model_a_responses'],
        model_b_responses=predictions['model_b_responses']
    )
    
    # Generate detailed comparison
    comparison_df = comparator.generate_detailed_comparison()
    
    # Visualize performance
    comparator.visualize_performance(comparison_df)
    
    # Generate detailed report
    comparator.generate_detailed_report(comparison_df)
    
    # Print results
    print(comparison_df)

if __name__ == '__main__':
    main()