# Model Performance Comparison Report

## Performance Summary
| Model   |   accuracy |   precision |   recall |   f1_score |   total_correct |   total_questions |   mcc |   kappa |
|:--------|-----------:|------------:|---------:|-----------:|----------------:|------------------:|------:|--------:|
| Model A |   1        |           1 |      1   |   1        |               3 |                 3 |   1   |     1   |
| Model B |   0.666667 |           1 |      0.5 |   0.666667 |               2 |                 3 |   0.5 |     0.4 |

## Question-Level Breakdown
### Question 1: Does it mention pricing?
- **Ground Truth:** True
- **Model A Response:** True (Correct)
- **Model B Response:** True (Correct)

### Question 2: Is customer support discussed?
- **Ground Truth:** False
- **Model A Response:** False (Correct)
- **Model B Response:** False (Correct)

### Question 3: Does it talk about data encryption?
- **Ground Truth:** True
- **Model A Response:** True (Correct)
- **Model B Response:** False (Incorrect)

