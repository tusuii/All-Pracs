# Import necessary libraries
using ScikitLearn: @sk_import
@sk_import ensemble: RandomForestRegressor
using Random: seed!

X = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
y = [10, 20, 30]
seed!(42)

model = RandomForestRegressor(n_estimators=100)

fit!(model, X, y)
new_input = [[2, 3, 4]]
prediction = predict(model, new_input)

println(prediction)
