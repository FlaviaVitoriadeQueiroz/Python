from sklearn.linear_model import Lasso

model_lasso = Lasso(alpha=0.1)
model_lasso.fit(X, y)

print("Intercepto:", model_lasso.intercept_)
print("Coeficientes:", model_lasso.coef_)