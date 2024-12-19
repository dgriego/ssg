import unittest

from leafnode import LeafNode
from textnode import TextNode, TextType, text_node_to_html_node


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("this is a text node", TextType.BOLD)
        node2 = TextNode("this is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_text_node_to_html_node_normal(self):
        node = TextNode("normal", TextType.NORMAL)
        leaf = text_node_to_html_node(node)
        self.assertIsInstance(leaf, LeafNode)
        self.assertEqual(leaf.value, node.text)

    def test_text_node_to_html_node_bold(self):
        node = TextNode("normal", TextType.BOLD)
        leaf = text_node_to_html_node(node)
        self.assertIsInstance(leaf, LeafNode)
        self.assertEqual(leaf.tag, "b")

    def test_node_to_html_node_italic(self):
        node = TextNode("normal", TextType.ITALIC)
        leaf = text_node_to_html_node(node)
        self.assertIsInstance(leaf, LeafNode)
        self.assertEqual(leaf.tag, "i")

    def test_node_to_html_node_code(self):
        node = TextNode("normal", TextType.CODE)
        leaf = text_node_to_html_node(node)
        self.assertIsInstance(leaf, LeafNode)
        self.assertEqual(leaf.tag, "code")

    def test_node_to_html_node_link(self):
        url = "https://www.danielgriego.com"
        node = TextNode("normal", TextType.LINK, url)
        leaf = text_node_to_html_node(node)
        self.assertIsInstance(leaf, LeafNode)
        self.assertEqual(leaf.tag, "a")
        self.assertEqual(leaf.props["href"], url)

    def test_node_to_html_node_img(self):
        url = "path/to/img.jpg"
        alt = "image"
        node = TextNode(alt, TextType.IMAGE, url)
        leaf = text_node_to_html_node(node)
        self.assertIsInstance(leaf, LeafNode)
        self.assertEqual(leaf.tag, "img")
        self.assertEqual(leaf.props["src"], url)
        self.assertEqual(leaf.props["alt"], alt)


if __name__ == "__main__":
    unittest.main()
