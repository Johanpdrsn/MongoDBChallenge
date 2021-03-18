#!/usr/bin/env python
import argparse
import json
import sys

# we expect arguments to be passed via stdin
parser = argparse.ArgumentParser("Flattens the content of a JSON object")
parser.add_argument('stdin', nargs='?',
                    type=argparse.FileType('r'), default=sys.stdin)

args = parser.parse_args()

# if stdin is empty we exit
if not sys.stdin.isatty():
    input = args.stdin.read()
else:
    print("The program requires input via stdin")
    exit()


# assert the input is a valid JSON object
try:
    json_object = json.loads(input)
except Exception:
    print("Input not a valid JSON object")
    exit()


def flatten(obj):
    # the object to return
    flattened_obj = {}

    def recursive_flat(inner_obj, name=""):
        # recursive call when object is a dict
        if type(inner_obj) is dict:
            for key in inner_obj:
                recursive_flat(inner_obj[key], name + key + '.')

        # list are not needed, but why not
        elif type(inner_obj) is list:
            list_index = 0

            for key in inner_obj:
                recursive_flat(key, name + str(list_index) + '.')
                list_index += 1

        # the value is a simple value and we can just add it
        else:
            # we don't want the extra period, thus "-1"
            flattened_obj[name[:-1]] = inner_obj

    recursive_flat(obj)

    return flattened_obj


flat_json = flatten(json_object)
print(json.dumps(flat_json, indent=4))
