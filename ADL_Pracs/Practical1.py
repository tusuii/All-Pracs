import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD, Adam, RMSprop
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# Generate synthetic dataset
X, y = make_classification(n_samples=1000, n_features=20, n_classes=2, random_state=42)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Define the feed-forward neural network model
def create_model():
    model = Sequential([
        Dense(64, input_shape=(X_train.shape[1],), activation='relu'),
        Dense(32, activation='relu'),
        Dense(1, activation='sigmoid')
    ])
    return model

# Function to train and evaluate the model
def train_and_evaluate(optimizer):
    model = create_model()
    model.compile(optimizer=optimizer, loss='binary_crossentropy', metrics=['accuracy'])
    model.fit(X_train, y_train, epochs=20, batch_size=32, verbose=0)
    y_pred = (model.predict(X_test) > 0.5).astype("int32")
    accuracy = accuracy_score(y_test, y_pred)
    return accuracy

# Train and evaluate models with different optimizers
optimizers = ['SGD', 'Adam', 'RMSprop']
results = {}
for optimizer in optimizers:
    accuracy = train_and_evaluate(optimizer)
    results[optimizer] = accuracy

# Print the results
for optimizer, accuracy in results.items():
    print(f'Accuracy with {optimizer} optimizer: {accuracy:.4f}')