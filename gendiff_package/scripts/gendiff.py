import argparse


def main():
    parser = argparse.ArgumentParser(description='Generate diff')
    parser.add_argument('first_file', type=str)
    parser.add_argument('second_file', type=str)
    parser.add_argument('-f', '--format', default='stylish',
                        help='output format (default: "stylish")')
    args = parser.parse_args()
    return args.first_file, args.second_file, args.format


if __name__ == '__main__':
    main()