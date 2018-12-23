import numpy as np


def get_pagerank(adj_matrix, DAMPING_FACTOR=0.15, EPSILON=0.01):
    """[summary]
        pagerank values calculation

    Arguments:
        adj_matrix {[float[][]]} -- [[input Adjacent matrix lists like [[1, 0], [0, 1]]]

    Keyword Arguments:
        DAMPING_FACTOR {float} -- [factor of residual probability] (default: {0.15})
        EPSILON {float} -- [factor of change comparision] (default: {0.01})

    Returns:
        [float[]] -- [pagerank values]
    """

    # initialize
    page_length = adj_matrix.shape[0]
    pagerank = np.ones(page_length)
    escape = np.ones(page_length) * (DAMPING_FACTOR / page_length)

    # normalize
    normalize_adj_matrix = adj_matrix / np.linalg.norm(adj_matrix, ord=1, axis=1, keepdims=True)
    normalize_adj_matrix = np.nan_to_num(normalize_adj_matrix)

    is_coverage = False
    while not is_coverage:
        new_pagerank = escape + (1-DAMPING_FACTOR) * np.dot(normalize_adj_matrix.T, pagerank)

        # normalize pagerank
        normalize_pagerank = lambda x: x / sum(new_pagerank)
        new_pagerank = normalize_pagerank(new_pagerank)

        # check is coverage
        diff = abs(sum(new_pagerank - pagerank))
        if diff < EPSILON:
            is_coverage = True
        else:
            pagerank = new_pagerank

    return pagerank