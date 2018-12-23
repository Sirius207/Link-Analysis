import pandas as pd

from src.utils import get_adj_matrix
from src.hits import get_hits

exp_links = ['','1,3','1,4','1,5','1,6']

base_path = './exp/graph_1'

def run(input_path):
    with open(input_path, 'r') as input:
        links = input.readlines()

        total_hubs = []
        total_authority = []
        for exp_link in exp_links:
            if exp_link != '':
                links.append(exp_link)

            adj_matrix = get_adj_matrix(links)
            hubs, authorities = get_hits(adj_matrix)

            # Output values to files
            total_hubs.append(hubs)
            total_authority.append(authorities)

        hub_results = pd.DataFrame(total_hubs)
        hub_results.to_csv(base_path + '/hubs.csv')
        authorities_results = pd.DataFrame(total_authority)
        authorities_results.to_csv(base_path + '/authority.csv')



run(base_path + '/new.txt')