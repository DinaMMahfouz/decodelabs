import pandas as pd
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Create a dataset
X, y = make_classification(n_samples=1000, n_features=20, n_informative=10, n_redundant=2, n_classes=2, random_state=1)

features = pd.DataFrame(X, columns=['feature_' + str(i) for i in range(X.shape[1])])
features.head()

labels = pd.DataFrame(y, columns=['label'])
labels.head()

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=1)

# Create a logistic regression model
model = LogisticRegression()

# Train the model on the training data
model.fit(X_train, y_train)

# Make predictions on the testing data
y_pred = model.predict(X_test)

# Calculate the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)
print('Accuracy:', accuracy)

# Calculate the confusion matrix
confusion = confusion_matrix(y_test, y_pred)
print('Confusion matrix:')
print(confusion)

# Print the classification report
print('Classification report:')
print(classification_report(y_test, y_pred))