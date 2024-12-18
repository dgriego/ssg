import unittest

from leafnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_with_no_value(self):
        self.assertRaises(ValueError, LeafNode, "p", None)

    def test_to_html_with_tag(self):
        leaf = LeafNode("p", "text")
        self.assertTrue(leaf.to_html(), "<p>text</p>")

    def test_to_html_without_tag(self):
        leaf = LeafNode("p", "text")
        self.assertTrue(leaf.to_html(), "text")


if __name__ == "__main__":
    unittest.main()
