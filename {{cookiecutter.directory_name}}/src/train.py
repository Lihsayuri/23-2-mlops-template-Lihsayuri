import pandas as pd
import pickle
from lightgbm import LGBMClassifier
from sklearn.metrics import classification_report, confusion_matrix
from sklearn.model_selection import train_test_split
from sklearn.compose import make_column_transformer
from sklearn.preprocessing import OneHotEncoder

df = pd.read_csv("data/[your processed data file].csv")

X = df.drop("[target column]", axis=1)
y = df["[target column]"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1912)

# In case you want to use OneHotEncoder
one_hot_enc = make_column_transformer(
    (OneHotEncoder(handle_unknown="ignore", drop="first"), "[categorical column]"),
    remainder="passthrough")

X_train = one_hot_enc.fit_transform(X_train)
X_train = pd.DataFrame(X_train, columns=one_hot_enc.get_feature_names_out())

X_test = pd.DataFrame(one_hot_enc.transform(X_test), columns=one_hot_enc.get_feature_names_out())

model = "The model you want to use"
model.fit(X_train, y_train)

# Specify the file path where you want to save the pickle file
file_path = "models/model.pkl"

# Save the model as a pickle file
with open(file_path, "wb") as f:
    pickle.dump(model, f)

file_path = "models/ohe.pkl"

# Save the OneHotEncoder as a pickle file
with open(file_path, "wb") as f:
    pickle.dump(one_hot_enc, f)

