import unittest
from main import search_text

class TestAhoCorasick(unittest.TestCase):
    def test_basic_keyword_match(self):
        text = "hello worldhello"
        keywords = ["hello", "world"]
        result = search_text(text, keywords)
        expected = {"hello": [0, 11], "world": [6]}
        self.assertEqual(result, expected)

    def test_no_match(self):
        text = "abcdef"
        keywords = ["xyz", "123"]
        result = search_text(text, keywords)
        expected = {"xyz": [], "123": []}
        self.assertEqual(result, expected)

    def test_overlapping_matches(self):
        text = "abxabcabcaby"
        keywords = ["ab", "abc", "aby"]
        result = search_text(text, keywords)
        expected = {"ab": [0, 3, 6, 9], "abc": [3, 6], "aby": [9]}
        self.assertEqual(result, expected)

    def test_single_character_match(self):
        text = "abcde"
        keywords = ["a", "b", "c", "d", "e"]
        result = search_text(text, keywords)
        expected = {"a": [0], "b": [1], "c": [2], "d": [3], "e": [4]}
        self.assertEqual(result, expected)

    def test_prefix_suffix_matches(self):
        text = "abcabcabc"
        keywords = ["abc", "bc", "c"]
        result = search_text(text, keywords)
        expected = {"abc": [0, 3, 6], "bc": [1, 4, 7], "c": [2, 5, 8]}
        self.assertEqual(result, expected)

    def test_case_sensitivity(self):
        text = "Hello World"
        keywords = ["hello", "world"]
        result = search_text(text, keywords)
        expected = {"hello": [], "world": []}
        self.assertEqual(result, expected)

    def test_failure_link(self):
        text = "ababcab"
        keywords = ["ab", "abc"]
        result = search_text(text, keywords)
        expected = {"ab": [0, 2, 5], "abc": [2]}
        self.assertEqual(result, expected)

    def test_empty_text(self):
        text = ""
        keywords = ["abc", "def"]
        result = search_text(text, keywords)
        expected = {"abc": [], "def": []}
        self.assertEqual(result, expected)

    def test_empty_keywords(self):
        text = "abcde"
        keywords = []
        result = search_text(text, keywords)
        expected = {}
        self.assertEqual(result, expected)

    def test_long_text_short_keywords(self):
        text = "a" * 1000000 + "b"
        keywords = ["a", "b"]
        result = search_text(text, keywords)
        expected = {"a": list(range(1000000)), "b": [1000000]}
        self.assertEqual(result, expected)
