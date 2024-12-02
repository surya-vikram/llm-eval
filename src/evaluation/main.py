import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class ModelComparator:
    def __init__(self, questions, ground_truth, model_a_responses, model_b_responses):
        """
        Initialize the comparator with evaluation data
        
        :param questions: List of questions
        :param ground_truth: Ground truth labels
        :param model_a_responses: Model A predictions
        :param model_b_responses: Model B predictions
        """
        self.questions = questions
        self.ground_truth = ground_truth
        self.model_a_responses = model_a_responses
        self.model_b_responses = model_b_responses
    
    def calculate_performance_metrics(self, predictions):
        """
        Calculate comprehensive performance metrics
        
        :param predictions: Model predictions
        :return: Dictionary of performance metrics
        """
        # True Positives, False Positives, False Negatives
        tp = sum((p == gt) and p for p, gt in zip(predictions, self.ground_truth))
        fp = sum((p != gt) and p for p, gt in zip(predictions, self.ground_truth))
        fn = sum((p != gt) and not p for p, gt in zip(predictions, self.ground_truth))
        
        # Precision, Recall, F1 Score
        precision = tp / (tp + fp) if (tp + fp) > 0 else 0
        recall = tp / (tp + fn) if (tp + fn) > 0 else 0
        f1 = 2 * (precision * recall) / (precision + recall) if (precision + recall) > 0 else 0
        
        # Accuracy
        accuracy = sum(p == gt for p, gt in zip(predictions, self.ground_truth)) / len(self.ground_truth)
        
        return {
            'accuracy': accuracy,
            'precision': precision,
            'recall': recall,
            'f1_score': f1,
            'total_correct': sum(p == gt for p, gt in zip(predictions, self.ground_truth)),
            'total_questions': len(self.ground_truth)
        }
    
    def generate_detailed_comparison(self):
        """
        Generate a comprehensive comparison of model performances
        
        :return: Detailed comparison DataFrame
        """
        # Calculate performance metrics
        model_a_metrics = self.calculate_performance_metrics(self.model_a_responses)
        model_b_metrics = self.calculate_performance_metrics(self.model_b_responses)
        
        # Prepare comparison data
        comparison_data = [
            {'Model': 'Model A', **model_a_metrics},
            {'Model': 'Model B', **model_b_metrics}
        ]
        
        # Create DataFrame
        return pd.DataFrame(comparison_data)
    
    def visualize_performance(self, comparison_df, output_dir='visualizations/graphs'):
        """
        Create multiple visualizations of model performance
        
        :param comparison_df: DataFrame with model performance metrics
        :param output_dir: Directory to save visualization files
        """
        # Ensure output directory exists
        import os
        os.makedirs(output_dir, exist_ok=True)
        
        # 1. Bar Plot of Performance Metrics
        plt.figure(figsize=(12, 6))
        metrics_to_plot = ['accuracy', 'precision', 'recall', 'f1_score']
        
        comparison_df.plot(x='Model', y=metrics_to_plot, kind='bar', rot=0)
        plt.title('Model Performance Comparison', fontsize=16)
        plt.ylabel('Score', fontsize=12)
        plt.legend(title='Metrics', bbox_to_anchor=(1.05, 1), loc='upper left')
        plt.tight_layout()
        plt.savefig(f'{output_dir}/model_performance_comparison.png')
        plt.close()
        
        # 2. Question-Level Detailed Analysis
        plt.figure(figsize=(15, 6))
        
        # Prepare question-level accuracy data
        question_accuracy = {
            'Model A': [p == gt for p, gt in zip(self.model_a_responses, self.ground_truth)],
            'Model B': [p == gt for p, gt in zip(self.model_b_responses, self.ground_truth)]
        }
        
        # Create box plot of question accuracies
        df_accuracy = pd.DataFrame(question_accuracy)
        sns.boxplot(data=df_accuracy)
        plt.title('Distribution of Question-Level Accuracy', fontsize=16)
        plt.ylabel('Accuracy', fontsize=12)
        plt.tight_layout()
        plt.savefig(f'{output_dir}/question_accuracy_distribution.png')
        plt.close()
        
        # 3. Confusion Matrix Heatmap
        plt.figure(figsize=(10, 8))
        
        # Combine data for heatmap
        confusion_data = {
            'Model A Correct': sum(p == gt for p, gt in zip(self.model_a_responses, self.ground_truth)),
            'Model A Incorrect': sum(p != gt for p, gt in zip(self.model_a_responses, self.ground_truth)),
            'Model B Correct': sum(p == gt for p, gt in zip(self.model_b_responses, self.ground_truth)),
            'Model B Incorrect': sum(p != gt for p, gt in zip(self.model_b_responses, self.ground_truth))
        }
        
        confusion_df = pd.DataFrame.from_dict(confusion_data, orient='index', columns=['Count'])
        sns.heatmap(confusion_df, annot=True, cmap='YlGnBu', fmt='g')
        plt.title('Model Prediction Accuracy Heatmap', fontsize=16)
        plt.tight_layout()
        plt.savefig(f'{output_dir}/prediction_accuracy_heatmap.png')
        plt.close()
    
    def generate_detailed_report(self, comparison_df, output_path='visualizations/reports/model_comparison_report.md'):
        """
        Generate a markdown report of the model comparison
        
        :param comparison_df: DataFrame with model performance metrics
        :param output_path: Path to save the markdown report
        """
        # Ensure output directory exists
        import os
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        
        with open(output_path, 'w') as f:
            # Title and Metadata
            f.write("# Model Performance Comparison Report\n\n")
            
            # Performance Summary
            f.write("## Performance Summary\n")
            f.write(comparison_df.to_markdown(index=False))
            
            # Detailed Question Analysis
            f.write("\n\n## Question-Level Breakdown\n")
            for i, (q, gt, a, b) in enumerate(zip(self.questions, self.ground_truth, self.model_a_responses, self.model_b_responses), 1):
                f.write(f"### Question {i}: {q}\n")
                f.write(f"- **Ground Truth:** {gt}\n")
                f.write(f"- **Model A Response:** {a} ({'Correct' if a == gt else 'Incorrect'})\n")
                f.write(f"- **Model B Response:** {b} ({'Correct' if b == gt else 'Incorrect'})\n\n")