import statsmodels.api as sm
import numpy as np

def forward_selection(X, y):
    remaining = list(range(X.shape[1]))
    selected = []
    current_score = float('inf')

    while remaining:
        scores = []
        
        for candidate in remaining:
            variables = selected + [candidate]
            X_model = sm.add_constant(X[:, variables])
            model = sm.OLS(y, X_model).fit()
            score = model.aic  # pode usar AIC, BIC ou p-value
            scores.append((score, candidate))
        
        scores.sort()
        best_score, best_candidate = scores[0]

        if best_score < current_score:
            remaining.remove(best_candidate)
            selected.append(best_candidate)
            current_score = best_score
        else:
            break

    return selected

selected_vars = forward_selection(X, y)
print("Variáveis selecionadas:", selected_vars)