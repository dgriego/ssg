import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
    def test_tag_to_lower(self):
        node = HTMLNode("P")
        self.assertEqual(node.tag, node.tag.lower())

    def test_props_to_html(self):
        node = HTMLNode("p", "this is a text node", None, {"class": "test-class"})
        self.assertEqual(node.props_to_html(), ' class="test-class" ')

    def test_to_html(self):
        node = HTMLNode("p", "this is a text node", None, {"class": "test-class"})
        self.assertRaises(NotImplementedError, node.to_html)


if __name__ == "__main__":
    unittest.main()
