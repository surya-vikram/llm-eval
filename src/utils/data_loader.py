import json
import os
from typing import Dict, Any

def load_evaluation_data(file_path: str) -> Dict[str, Any]:
    """
    Load and validate evaluation data from a JSON file.
    
    Args:
        file_path (str): Path to the JSON file containing evaluation data
    
    Returns:
        Dict[str, Any]: Processed evaluation data
    
    Raises:
        FileNotFoundError: If the JSON file does not exist
        ValueError: If the JSON file is improperly formatted
    """
    # Ensure the file exists
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"Evaluation data file not found: {file_path}")
    
    # Read the JSON file
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
    except json.JSONDecodeError:
        raise ValueError(f"Invalid JSON format in file: {file_path}")
    
    # Validate basic structure
    required_keys = ['paragraphs', 'metadata']
    for key in required_keys:
        if key not in data:
            raise ValueError(f"Missing required key: {key}")
    
    return data

def extract_model_predictions(data: Dict[str, Any]) -> Dict[str, list]:
    """
    Extract model predictions from the evaluation data.
    
    Args:
        data (Dict[str, Any]): Loaded evaluation data
    
    Returns:
        Dict[str, list]: Extracted model predictions
    """
    questions = []
    ground_truth = []
    model_a_responses = []
    model_b_responses = []
    
    for paragraph in data['paragraphs']:
        for question in paragraph['questions']:
            questions.append(question['question'])
            ground_truth.append(question['ground_truth'])
            model_a_responses.append(question['model_a_response'])
            model_b_responses.append(question['model_b_response'])
    
    return {
        'questions': questions,
        'ground_truth': ground_truth,
        'model_a_responses': model_a_responses,
        'model_b_responses': model_b_responses
    }