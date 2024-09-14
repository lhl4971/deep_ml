def euclidean_distance(p1: tuple, p2: tuple) -> float:
    if len(p1) != len(p2):
        return -1
    s = 0
    for i in range(len(p1)):
        s += (p1[i] - p2[i]) ** 2
    return s ** 0.5


def nearest_point(p: tuple, lst: list[tuple]) -> tuple:
    l_distance = [euclidean_distance(p, c) for c in lst]
    arg_max = l_distance.index(min(l_distance))
    return lst[arg_max]


def mean_tuples(lst: list[tuple]) -> tuple:
    result = [0] * len(lst[0])
    for tpl in lst:
        for i in range(len(lst[0])):
            result[i] += tpl[i]
    return tuple(r / len(lst) for r in result)


def k_means_clustering(
        points: list[tuple[float, float]],
        k: int,
        initial_centroids: list[tuple[float, float]],
        max_iterations: int
        ) -> list[tuple[float, float]]:
    deviation = 1e-4
    centroids = initial_centroids
    for _ in range(max_iterations):
        centroids_dict = {key: [] for key in centroids}
        for p in points:
            centroids_dict[nearest_point(p, centroids)].append(p)
        new_centroids = [
            mean_tuples(cl_points) for cl_points in centroids_dict.values()
            ]
        for i in range(k):
            if euclidean_distance(centroids[i], new_centroids[i]) < deviation:
                return [
                    tuple(round(num, 4) for num in t) for t in new_centroids
                    ]
        centroids = new_centroids
    return [tuple(round(num, 4) for num in t) for t in centroids]
