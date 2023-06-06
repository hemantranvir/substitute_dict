"""substitute function/script to replace values of input json."""

import argparse
import json


def replace_value(input_dict, depth):
    """To replace values of input dict recursively based on depth"""
    for key, value in input_dict.items():
        if isinstance(value, dict):
            if depth - 1 > 0:
                replace_value(value, depth - 1)
        else:
            input_dict[key] = {'_content': value, '_type': str(type(value))}


def substitute(input_path, depth, output_path):
    """To handle input/output files and high level substitution"""
    # Open input file and load the json as dict
    try:
        with open(input_path, 'r') as f:
            input_data = json.load(f)
    except FileNotFoundError as exc:
        print('Input file/path not found, please check the path and try again')
        raise exc
    except Exception as exc:
        raise exc

    # Recursively call replace_value to replace values matching the criteria
    # Since dict is mutable, we will use the same input object to update
    # the values to save on memory
    replace_value(input_data, depth)

    # Serializing json
    output_json = json.dumps(input_data, indent=4)

    # Writing to output file
    try:
        with open(output_path, "w") as o:
            o.write(output_json)
    except FileNotFoundError as exc:
        print(f'Failed to save to output file, exception is {str(exc)}')
        raise exc
    except Exception as exc:
        raise exc


def check_positive(value):
    ivalue = int(value)
    if ivalue <= 0:
        raise argparse.ArgumentTypeError(f'{value} is an invalid positive \
        int value')
    return ivalue


def main(input_path, depth, output_path):
    """The main entry point of the program."""
    substitute(input_path, depth, output_path)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("input_path", type=str,
                        help="Path to input json file")
    parser.add_argument("depth", type=check_positive,
                        help="Depth of substitution to be carried out. \
                        1 --> Only first level substition i.e origianl \
                        dict values will be substituted. \
                        2 --> Subsitition will happen until one \
                        sub dictonary deep and so on")
    parser.add_argument("output_path", type=str,
                        help="Path to output json file")
    args = parser.parse_args()

    main(args.input_path, args.depth, args.output_path)
