import math

def knn_predict(train_X, train_y, test_X, k):
    predictions = []

    for test_point in test_X:
        distances = []
        for x, y in zip(train_X, train_y):
            dist = math.sqrt(sum((a - b) ** 2 for a, b in zip(x, test_point)))
            distances.append((dist, y))

        distances.sort(key=lambda x: (x[0], x[1]))
        k_neighbors = distances[:k]

        vote_count = {}
        for _, label in k_neighbors:
            vote_count[label] = vote_count.get(label, 0) + 1

        max_votes = max(vote_count.values())
        candidates = [label for label, cnt in vote_count.items() if cnt == max_votes]

        predictions.append(min(candidates))

    return predictions
