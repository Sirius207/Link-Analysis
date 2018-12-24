import pandas as pd

from src.utils import get_adj_matrix
from src.hits import get_hits
from src.pagerank import get_pagerank

exp_links = ['',
            '1,3','1,4','1,5','1,6',
            '3,1','4,1','5,1','6,1',
            ]

add_column = 'add_link'
base_path = './exp/graph_1'

def run(input_path):
    with open(input_path, 'r') as input:
        links = input.readlines()

        total_hubs = []
        total_authority = []
        total_pagerank = []
        for exp_link in exp_links:
            if exp_link != '':
                links.append(exp_link)

            adj_matrix = get_adj_matrix(links)
            hubs, authorities = get_hits(adj_matrix)
            pagerank = get_pagerank(adj_matrix)

            total_hubs.append(hubs)
            total_authority.append(authorities)
            total_pagerank.append(pagerank)

        # write hub results
        hub_results = pd.DataFrame(total_hubs)
        hub_results[add_column] = exp_links
        hub_results.to_csv(base_path + '/hubs.csv')

        # write authority results
        authorities_results = pd.DataFrame(total_authority)
        authorities_results[add_column] = exp_links
        authorities_results.to_csv(base_path + '/authority.csv')

        # write pagerank results
        pagerank_results = pd.DataFrame(total_authority)
        pagerank_results[add_column] = exp_links
        pagerank_results.to_csv(base_path + '/pagerank.csv')


run(base_path + '/new.txt')