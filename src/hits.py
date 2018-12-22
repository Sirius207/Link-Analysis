import numpy as np

def get_hits(adj_matrix, EPSILON = 0.001):
    """[summary]
        hubs & authorities calculation
    Arguments:
        adj_matrix {float[][]} -- [input Adjacent matrix lists like [[1, 0], [0, 1]]
        EPSILON {float} -- [factor of change comparision] (default: {0.001})

    Returns:
        [(float[], float[])] -- [return hubs & authorities]
    """
    # initialize to all 1's
    is_coverage = False
    hubs = np.ones(adj_matrix.shape[0])
    authorities = np.ones(adj_matrix.shape[0])

    while not is_coverage:
        # a = A.T h, h = A a,
        new_authorities = np.dot(adj_matrix.T, hubs)
        new_hubs = np.dot(adj_matrix, authorities)

        # normalize
        normalize_auth = lambda x: x / sum(new_authorities)
        normalize_hubs = lambda x: x / sum(new_hubs)
        new_authorities = normalize_auth(new_authorities)
        new_hubs = normalize_hubs(new_hubs)

        # check is coverage
        diff = abs(sum(new_hubs - hubs) + sum(new_authorities - authorities))
        if diff < EPSILON:
            is_coverage = True
        else:
            authorities = new_authorities
            hubs = new_hubs

    return (new_hubs, new_authorities)

