def softmax_classify(W, b, X):
    predictions = []

    for x in X:
        logits = []
        for i in range(len(W)):
            logit = sum(w * xi for w, xi in zip(W[i], x)) + b[i]
            logits.append(logit)

        max_val = max(logits)
        candidates = [i for i, v in enumerate(logits) if v == max_val]

        predictions.append(min(candidates))

    return predictions
