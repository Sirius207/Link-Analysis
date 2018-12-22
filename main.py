from src.utils import get_adj_matrix
from src.hits import get_hits


def main(args):
    with open(args.input, 'r') as input:
        links = input.readlines()

        adj_matrix = get_adj_matrix(links)
        hubs, authorities =  get_hits(adj_matrix)


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--input',
                        default='./data/graph_1.txt',
                        help='input graph data file name')
    parser.add_argument('--output',
                        default='output.csv',
                        help='output file name')
    args = parser.parse_args()

    main(args)
