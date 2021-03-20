#!/usr/bin/env python
import json
import sys


class Flatten():
    """Object that contains the flattened JSON object"""

    def __init__(self, json_obj) -> None:
        self.flat_json = {}
        self.flatten(json_obj)

    def flatten(self, obj, key_name="") -> None:
        '''Takes a JSON object as argument, and returns a flattened JSON object'''

        # recursive call when object is a dict
        if type(obj) is dict:
            for key in obj:
                self.flatten(obj[key], key_name + key + '.')

        # the input object does not contain arrays
        # so we don't check for them

        # the value is a simple value and we can just add it
        else:
            # we don't want the extra period, thus "-1"
            self.flat_json[key_name[:-1]] = obj


def main() -> None:
    if len(sys.argv) > 1:
        print("We only accept input through stdin, no arguments needed")

    if not sys.stdin.isatty():
        input = sys.stdin.read()
    else:
        input = ""

    # assert the input is a valid JSON object
    try:
        json_object = json.loads(input)
    except Exception:
        print("Input not a valid JSON object")
        exit()

    flattened = Flatten(json_object)

    print(json.dumps(flattened.flat_json, indent=4))


if __name__ == "__main__":
    # stuff only to run when not called via 'import' here
    main()
