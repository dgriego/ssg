import unittest

from htmlnode import HTMLNode


class TestHTMLNode(unittest.TestCase):
    def test_children_are_html_nodes(self):
        child_node = HTMLNode("p")
        parent_node = HTMLNode("div", children=[child_node])
        self.assertEqual(parent_node.children[0], child_node)
        self.assertRaises(ValueError, HTMLNode, "p", children=["t"])

    def test_tag_to_lower(self):
        node = HTMLNode("P")
        self.assertEqual(node.tag, node.tag.lower())

    def test_props_to_html(self):
        node = HTMLNode("p", "this is a text node", None, {"class": "test-class"})
        self.assertEqual(node.props_to_html(), ' class="test-class"')

    def test_to_html(self):
        node = HTMLNode("p", "this is a text node", None, {"class": "test-class"})
        self.assertRaises(NotImplementedError, node.to_html)


if __name__ == "__main__":
    unittest.main()
