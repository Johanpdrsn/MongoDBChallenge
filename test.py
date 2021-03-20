#!/usr/bin/env python

import unittest
import json
from app import Flatten


class TestFlatten(unittest.TestCase):

    def test_example(self):
        with open("test/cases/example.json", 'r') as inp, open("test/results/flat_example.json") as out:
            json_inp = json.loads(inp.read())
            flat_result = Flatten(json_inp).flat_json
            result = json.dumps(flat_result, indent=4)
            self.assertEqual(result, out.read())

    def test_glossary(self):
        with open("test/cases/glossary.json", 'r') as inp, open("test/results/flat_glossary.json") as out:
            json_inp = json.loads(inp.read())
            flat_result = Flatten(json_inp).flat_json
            result = json.dumps(flat_result, indent=4)
            self.assertEqual(result, out.read())

    def test_nested(self):
        with open("test/cases/nested.json", 'r') as inp, open("test/results/flat_nested.json") as out:
            json_inp = json.loads(inp.read())
            flat_result = Flatten(json_inp).flat_json
            result = json.dumps(flat_result, indent=4)
            self.assertEqual(result, out.read())

    def test_symbols(self):
        with open("test/cases/symbols.json", 'r') as inp, open("test/results/flat_symbols.json") as out:
            json_inp = json.loads(inp.read())
            flat_result = Flatten(json_inp).flat_json
            result = json.dumps(flat_result, indent=4)
            self.assertEqual(result, out.read())

    def test_numbers(self):
        with open("test/cases/numbers.json", 'r') as inp, open("test/results/flat_numbers.json") as out:
            json_inp = json.loads(inp.read())
            flat_result = Flatten(json_inp).flat_json
            result = json.dumps(flat_result, indent=4)
            self.assertEqual(result, out.read())


if __name__ == '__main__':
    unittest.main()
