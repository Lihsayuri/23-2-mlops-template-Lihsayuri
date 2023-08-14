import pickle
import pandas as pd

model = pickle.load(open("models/model.pkl", "rb"))

# Carrega o arquivo do bank_predict.csv 
df = pd.read_csv("data/[the file you want to predict].csv")
X_test = "df transformed"

y_pred = model.predict(X_test)

# Adiciona uma nova coluna 'y_pred' com as predições 
df['y_pred'] = y_pred

# Salva o DataFrame atualizado de novo no CSV file
df.to_csv("data/bank_predict.csv", index=False)



