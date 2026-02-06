def minmax_scale(X):
    if not X:
        return []

    rows = len(X)
    cols = len(X[0])
    result = [[0.0] * cols for _ in range(rows)]

    for j in range(cols):
        column = [X[i][j] for i in range(rows)]
        min_j = min(column)
        max_j = max(column)

        if max_j == min_j:
            for i in range(rows):
                result[i][j] = 0.0
        else:
            for i in range(rows):
                value = (X[i][j] - min_j) / (max_j - min_j)
                result[i][j] = round(value, 4)

    return result
