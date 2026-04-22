import itertools
import statsmodels.api as sm

def best_subset(X, y):
    n_features = X.shape[1]
    best_score = float('inf')
    best_model = None
    best_combination = None

    for k in range(1, n_features + 1):
        for combo in itertools.combinations(range(n_features), k):
            X_model = sm.add_constant(X[:, combo])
            model = sm.OLS(y, X_model).fit()
            score = model.aic

            if score < best_score:
                best_score = score
                best_model = model
                best_combination = combo

    return best_combination, best_model

combo, model = best_subset(X, y)
print("Melhor combinação:", combo)
print(model.summary())