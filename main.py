import logging
import pandas as pd

from src.utils import get_adj_matrix
from src.hits import get_hits
from src.pagerank import get_pagerank
from src.simrank import get_simrank

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)
logger.setLevel(level=logging.INFO)

def main(args):
    with open(args.input, 'r') as input:
        links = input.readlines()

        adj_matrix = get_adj_matrix(links)
        hubs, authorities = get_hits(adj_matrix)
        pagerank = get_pagerank(adj_matrix)
        # simRank  calculation
        compare_nodes = (1, 2)
        simrank = get_simrank(compare_nodes, adj_matrix)

        logger.info(f'hubs: {hubs}, authorities: {authorities}')
        logger.info(f'pageRank: {pagerank}')
        logger.info(f'simRank: {simrank}')

        # Output values to files
        results = pd.DataFrame({"hubs": hubs, "authorities": authorities, "pagerank": pagerank})
        results.index.name = 'node'
        results.to_csv(args.output)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--input',
                        default='./data/graph_4.txt',
                        help='input graph data file name')
    parser.add_argument('--output',
                        default='exp/output.csv',
                        help='output file name')
    args = parser.parse_args()

    main(args)
