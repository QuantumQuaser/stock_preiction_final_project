# Model Development Journey: Stock Prediction Challenge


# Stock Prediction Model Development Summary

## Objective Definition
- **Goal**: Predict the best performing stock out of a given set for the next week.
- **Factors Considered**: 
  - Risk-to-reward ratio
  - Expected weekly profits
  - Technical indicators such as RSI, MACD, Bollinger Bands, and Fibonacci Retracements.

## Data Collection
- **Source**: Historical stock data from Yahoo Finance for selected stocks.
- **Features**: Daily prices, volumes, and technical indicators.

## Data Preprocessing
- **Cleaning**: 
  - Handling missing values
  - Removing duplicates
  - Ensuring data consistency
- **Feature Engineering**: 
  - Calculating technical indicators
  - Integrating sentiment analysis and Nifty trend data

## Model Selection and Initial Training
- **Models Used**: 
  - Gradient Boosting
  - Random Forest
  - LSTM
- **Initial Training**: Models were trained using the processed features.

## Addressing Class Imbalance
- **Problem Identified**: Poor performance on the minority class due to class imbalance.
- **Solutions Implemented**:
  - SMOTE for oversampling
  - Adjusted class weights
  - Explored different metrics for evaluation

## Model Refinement
- **Enhanced LSTM**: 
  - Improved architecture with more layers and neurons
- **Hyperparameter Tuning**: 
  - Adjusted model parameters for better performance
- **Threshold Tuning**: 
  - Experimented with different decision thresholds for classification

## Model Evaluation and Iteration
- **Ongoing Evaluation**: 
  - Focused on precision, recall, and F1-score, especially for the minority class
- **Iteration**: 
  - Models were iteratively refined based on evaluation results for a better balance between precision and recall

## Final Results and Analysis
- **Observations**:
  - Improved recall for the minority class
  - Ongoing challenges with precision
- **Trade-Offs**: 
  - A consistent theme was balancing precision and recall, highlighting the complexity in predicting stock performance in imbalanced datasets

## Key Decisions and Logic
- **Class Imbalance Strategy**: 
  - Focused on techniques like resampling and class weight adjustments
- **LSTM Enhancement**: 
  - Chosen due to the sequential nature of stock data, enhanced to capture complex patterns
- **Threshold Tuning**: 
  - Crucial for managing the precision-recall trade-off

---




## Initial Model Evaluation Results

The initial evaluation of the models showed challenges in predicting the minority class. Below are the precision, recall, and F1-scores for each model:

### Gradient Boosting Classifier

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 1.00      | 1.00   | 1.00     | 2229    |
| 1     | 0.00      | 0.00   | 0.00     | 10      |
|       |           |        |          |         |
| **Accuracy** | | | **0.99** | **2239** |
| **Macro Avg** | 0.50 | 0.50 | 0.50 | 2239 |
| **Weighted Avg** | 0.99 | 0.99 | 0.99 | 2239 |

### Random Forest Classifier

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 1.00      | 1.00   | 1.00     | 2229    |
| 1     | 0.00      | 0.00   | 0.00     | 10      |
|       |           |        |          |         |
| **Accuracy** | | | **1.00** | **2239** |
| **Macro Avg** | 0.50 | 0.50 | 0.50 | 2239 |
| **Weighted Avg** | 0.99 | 1.00 | 0.99 | 2239 |

### XGBoost Classifier

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 1.00      | 1.00   | 1.00     | 2229    |
| 1     | 0.00      | 0.00   | 0.00     | 10      |
|       |           |        |          |         |
| **Accuracy** | | | **0.99** | **2239** |
| **Macro Avg** | 0.50 | 0.50 | 0.50 | 2239 |
| **Weighted Avg** | 0.99 | 0.99 | 0.99 | 2239 |


## Phase 1: Identifying the Challenge of Class Imbalance

In the first phase, I recognized a common hurdle in machine learning: class imbalance. Our dataset exhibited a significant disproportion, with an overwhelming majority of instances in one class. This led to our models excelling at predicting the majority class while struggling with the minority class, as evidenced by the low precision and recall for the latter.

### Addressing Imbalance
To counteract this imbalance, i explored several strategies:
- **Resampling Techniques**: Balancing the dataset by either oversampling the minority class or undersampling the majority class.
- **Weighted Classes**: Adjusting the models to give higher importance to the minority class.
- **Synthetic Data Generation**: Utilizing SMOTE for generating synthetic samples of the minority class.

## Phase 2: Refining the Gradient Boosting Classifier

## GBoost Classifier Evaluation

The results after tuning the GBoost Classifier:

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 1.00      | 0.91   | 0.95     | 2229    |
| 1     | 0.03      | 0.70   | 0.07     | 10      |
|       |           |        |          |         |
| **Accuracy**      |         |        | **0.91** | **2239** |
| **Macro Avg**     | 0.52    | 0.81   | 0.51    | 2239    |
| **Weighted Avg**  | 0.99    | 0.91   | 0.95    | 2239    |


Upon refining the Gradient Boosting Classifier, I observed a substantial improvement in recall for the minority class. However, this gain in recall came with a reduction in precision for the same class and a slight drop in overall accuracy.

### Insights
- **Trade-off Between Precision and Recall**: An increased ability to identify the best-performing stocks was offset by a higher rate of false positives.
- **Macro Average F1-Score**: Despite these adjustments, the overall balance between precision and recall, as measured by the macro average F1-score, showed little improvement.

### Moving Forward
I proposed several steps for further enhancement:
- **Threshold Adjustment**: Fine-tuning the model's decision threshold.
- **Feature Engineering and Selection**: Re-evaluating and enhancing the features used for training.
- **Model Complexity**: Experimenting with more complex configurations of the Gradient Boosting model.

## Phase 3: Tweaking Decision Thresholds

## Adjusted Gradient Boosting Classifier Evaluation

After adjusting the Gradient Boosting Classifier, here are the evaluation metrics:

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 1.00      | 0.97   | 0.98     | 2229    |
| 1     | 0.05      | 0.40   | 0.09     | 10      |
|       |           |        |          |         |
| **Accuracy**      |         |        | **0.96** | **2239** |
| **Macro Avg**     | 0.52    | 0.68   | 0.54    | 2239    |
| **Weighted Avg**  | 0.99    | 0.96   | 0.98    | 2239    |


Adjustments to decision thresholds revealed interesting shifts:
- **Increased Precision for Class 1**: A reduction in false positives.
- **Decreased Recall for Class 1**: A lower rate of correctly identifying all true best performers.
- **Improved Precision for Class 0**: Maintaining high precision for the majority class.

### Interpretation
- **Balanced Model**: We achieved a more balanced model in terms of precision and recall for the minority class.
- **Macro Average F1-Score Improvement**: Notable enhancement in the overall balance of the model.

## Enhancing the LSTM Model

I then shifted our focus to the LSTM model, aiming for a more advanced and robust architecture.
## LSTM Model Performance

The performance evaluation of the LSTM model is as follows:

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 1.00      | 1.00   | 1.00     | 2229    |
| 1     | 0.00      | 0.00   | 0.00     | 10      |
|       |           |        |          |         |
| **Accuracy**      |         |        | **1.00** | **2239** |
| **Macro Avg**     | 0.50    | 0.50   | 0.50    | 2239    |
| **Weighted Avg**  | 0.99    | 1.00   | 0.99    | 2239    |


### Key Strategies
1. **Advanced LSTM Architecture**: Introducing more layers, implementing dropout, and utilizing Bidirectional LSTM.
2. **Data Preparation Enhancements**: Incorporating longer time steps and more relevant features.
3. **Hyperparameter Tuning**: Adjusting units in LSTM layers, learning rate, and experimenting with batch sizes and epochs.

Despite these efforts, the LSTM model still faced challenges in accurately predicting the minority class, mirroring issues observed in other classifiers.

## Phase 4: LSTM Model Adjustments with Class Weights

## LSTM Model Performance with Class Weights

After applying class weights to the LSTM model, the performance metrics are as follows:

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 1.00      | 0.85   | 0.92     | 2229    |
| 1     | 0.02      | 0.80   | 0.05     | 10      |
|       |           |        |          |         |
| **Accuracy**      |         |        | **0.85** | **2239** |
| **Macro Avg**     | 0.51    | 0.83   | 0.48    | 2239    |
| **Weighted Avg**  | 0.99    | 0.85   | 0.92    | 2239    |

*Accuracy: 0.8530594015185351*




Adjusting the LSTM model with class weights led to remarkable changes:
- **Significantly Improved Recall for Class 1**: Successfully identifying minority class instances.
- **Low Precision for Class 1**: Continued challenges with a high rate of false positives.
- **Reduced Overall Accuracy**: A decrease in the model's accuracy due to these adjustments.

## Phase 5: Threshold Experimentation with LSTM

## LSTM Model Performance at Various Thresholds

### Performance at Threshold 0.4

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 1.00      | 0.73   | 0.84     | 2229    |
| 1     | 0.01      | 0.90   | 0.03     | 10      |
|       |           |        |          |         |
| **Accuracy**      |         |        | **0.73** | **2239** |
| **Macro Avg**     | 0.51    | 0.82   | 0.44    | 2239    |
| **Weighted Avg**  | 0.99    | 0.73   | 0.84    | 2239    |

*Accuracy: 0.7324698526127735*

### Performance at Threshold 0.5

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 1.00      | 0.76   | 0.87     | 2229    |
| 1     | 0.02      | 0.90   | 0.03     | 10      |
|       |           |        |          |         |
| **Accuracy**      |         |        | **0.76** | **2239** |
| **Macro Avg**     | 0.51    | 0.83   | 0.45    | 2239    |
| **Weighted Avg**  | 1.00    | 0.76   | 0.86    | 2239    |

*Accuracy: 0.7641804376953998*

### Performance at Threshold 0.6

| Class | Precision | Recall | F1-Score | Support |
|-------|-----------|--------|----------|---------|
| 0     | 1.00      | 0.80   | 0.89     | 2229    |
| 1     | 0.02      | 0.90   | 0.04     | 10      |
|       |           |        |          |         |
| **Accuracy**      |         |        | **0.80** | **2239** |
| **Macro Avg**     | 0.51    | 0.85   | 0.46    | 2239    |
| **Weighted Avg**  | 1.00    | 0.80   | 0.88    | 2239    |

*Accuracy: 0.7963376507369362*


In our final phase, we experimented with various thresholds for the LSTM model, seeking an optimal balance:

- **Threshold Variations**: Testing at 0.4, 0.5, and 0.6 showed different impacts on precision and recall.
- **Precision-Recall Trade-Off**: Highlighting the ongoing challenge of balancing these two metrics.
- **Threshold Selection**: Emphasizing the importance of choosing an appropriate threshold based on specific application needs.


