import numpy as np

EPSILON = 0.001

def links_to_nodes(link):
    link = link.replace('\n', '')
    nodes = link.split(',')
    return nodes

def generate_adj_matrix(node_lists):
    node_dict = dict()
    for nodes in node_lists:
        for node in nodes:
            if node not in node_dict:
                node_dict[node] = 1

    node_counts = len(node_dict)
    adj_matrix = np.zeros((node_counts, node_counts))

    for nodes in node_lists:
        source = int(nodes[0])
        sink = int(nodes[1])
        adj_matrix[source - 1][sink -1] = 1

    return adj_matrix


def get_hits(links):
    node_lists = list(map(links_to_nodes, links))

    adj_matrix = generate_adj_matrix(node_lists)

    is_coverage = False
    hubs = np.ones(adj_matrix.shape[0])
    authorities = np.dot(adj_matrix.T, hubs)
    while not is_coverage:
        new_authorities = np.dot(adj_matrix.T, hubs)
        new_hubs = np.dot(adj_matrix, authorities)

        # normalization
        normalize_auth = lambda x: x / sum(new_authorities)
        normalize_hubs = lambda x: x / sum(new_hubs)
        new_authorities = normalize_auth(new_authorities)
        new_hubs = normalize_hubs(new_hubs)

        diff = abs(sum(new_hubs - hubs) + sum(new_authorities - authorities))
        if diff < EPSILON:
            is_coverage = True
        else:
            authorities = new_authorities
            hubs = new_hubs

    return (new_hubs, new_authorities)

