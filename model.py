import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

data = {
    'hour': [6, 9, 12, 15, 18, 21],
    'vehicles': [100, 300, 200, 400, 600, 150],
    'traffic': ['Low', 'High', 'Medium', 'High', 'High', 'Low']
}

df = pd.DataFrame(data)

X = df[['hour', 'vehicles']]
y = df['traffic']

model = RandomForestClassifier()
model.fit(X, y)

pickle.dump(model, open('traffic_model.pkl', 'wb'))

print("Model created successfully")