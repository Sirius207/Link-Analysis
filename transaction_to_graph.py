
def main(args):
  with open(args.input, 'r') as input, open(args.output, 'w') as output:
        transactions = input.readlines()

        node_index = []
        for transaction in transactions:
            transaction = transaction.replace(',\n', '')
            nodes = transaction.split(',')
            for id, node in enumerate(nodes):
                if id+1 != len(nodes):
                    if nodes[id] not in node_index:
                        node_index.append(nodes[id])
                    if nodes[id+1] not in node_index:
                        node_index.append(nodes[id+1])

                    source_index = node_index.index(nodes[id])
                    sink_index = node_index.index(nodes[id+1])
                    output.writelines(f'{source_index},{sink_index}\n')


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--input',
                        default='./data/t1_l5_n5.data',
                        help='input graph data file name')
    parser.add_argument('--output',
                        default='./data/t1_l5_n5.txt',
                        help='output file name')
    args = parser.parse_args()

    main(args)