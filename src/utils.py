import numpy as np


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


def get_adj_matrix(links):
    node_lists = list(map(links_to_nodes, links))
    adj_matrix = generate_adj_matrix(node_lists)
    return adj_matrix