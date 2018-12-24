import pandas as pd
from src.utils import get_adj_matrix


def main(args):
    with open(args.input, 'r') as input:
        links = input.readlines()
        adj_matrix = get_adj_matrix(links)

        outlinks_group = []
        inlinks_group = []
        for outlinks in adj_matrix:
            outlinks_group.append(sum(outlinks))
        for inlinks in adj_matrix.T:
            inlinks_group.append(sum(inlinks))

        results = pd.DataFrame({'outlinks': outlinks_group, 'inlinks': inlinks_group})
        results.to_csv(args.output, index=False)

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--input',
                        default='./data/graph_4.txt',
                        help='input graph data file name')
    parser.add_argument('--output',
                        default='exp/link_counts.csv',
                        help='output file name')
    args = parser.parse_args()

    main(args)
