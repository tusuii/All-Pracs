from sklearn.ensemble import RandomForestRegressor

X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = [10, 20, 30]

model = RandomForestRegressor(n_estimators=100, random_state=42)

model.fit(X, y)
new_input = [[2, 3, 4]]
prediction = model.predict(new_input)

print(prediction)
