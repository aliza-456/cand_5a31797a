import math

def kmeans_assign(points, centroids):
    assignments = []

    for p in points:
        best_idx = 0
        best_dist = float("inf")

        for i, c in enumerate(centroids):
            dist = math.sqrt(sum((pi - ci) ** 2 for pi, ci in zip(p, c)))
            if dist < best_dist or (dist == best_dist and i < best_idx):
                best_dist = dist
                best_idx = i

        assignments.append(best_idx)

    return assignments
