from itertools import combinations


# NOTE: To calculate the clustering accuracy, we need to compare the true clusters with the predicted clusters.
# The function get_pairs takes a cluster (a list of lists) and returns a set of pairs of names.
# Each pair is a tuple of two names, and the pairs are sorted to ensure consistency.
# This function was done to avoid the problem of having to find the correct cluster to compare with the predicted clusters.
# However, according to Professor LSL, this is an creative solution, however confusing and its not clear if it is correct.
# Nevertheless, this is a known algorithm called "Pairwise F1-Score" and it is used in many clustering algorithms.
# But for professors to understand it and belive in it, we need to find papers and articles that use it and cite them.
def get_pairs(cluster):
    pairs = set()
    for group in cluster:
        if len(group) == 1:
            a = group[0]
            pairs.add((a, a))
        else:
            for a, b in combinations(sorted(group), 2):
                pairs.add((a, b))
    return pairs


# NOTE: This function calculates the clustering accuracy based on the true clusters and predicted clusters.
# It uses precision, recall, and F1 score as metrics.
# The function also takes an optional parameter training_names to filter the clusters based on the training set.
# For more details on the metrics, search about "precision", "recall", and "F1 score" in the internet, as it is a well documented subject.
def clustering_accuracy(true_clusters, predicted_clusters):  
    true_pairs = get_pairs(true_clusters)
    pred_pairs = get_pairs(predicted_clusters)

    tp = len(true_pairs & pred_pairs)
    fp = len(pred_pairs - true_pairs)
    fn = len(true_pairs - pred_pairs)

    precision = tp / (tp + fp) if (tp + fp) > 0 else 0.0
    recall = tp / (tp + fn) if (tp + fn) > 0 else 0.0
    f1 = 2 * precision * recall / (precision + recall) if (precision + recall) > 0 else 0.0

    return {
        "precision": precision,
        "recall": recall,
        "f1_score": f1
    }


# cluster_A = [["Test", "Test1"], ["Hello"], ["Sun", "Sun1"]]
# print(get_pairs(cluster_A))
# # {('Sun', 'Sun1'), ('Test', 'Test1'), ('Hello', 'Hello')}
# cluster_B = [["Test", "Test1", "Test2"], ["Hello"]]
# print(get_pairs(cluster_B))
# # {('Test', 'Test1'), ('Test', 'Test2'), ('Test1', 'Test2'), ('Hello', 'Hello')}

# metrics = clustering_accuracy(cluster_A, cluster_B)
# print(metrics)
# # {'precision': 0.5, 'recall': 0.6666666666666666, 'f1_score': 0.5714285714285715}
