import unittest

from leafnode import LeafNode
from parentnode import ParentNode


class TestParentNode(unittest.TestCase):
    def test_children_and_tag_required(self):
        self.assertRaises(ValueError, ParentNode, None, None)

    def test_to_html_parent_nodes_missing_children(self):
        with self.assertRaises(ValueError) as context:
            ParentNode(
                "p",
                [
                    ParentNode("p", None),
                ],
            )
        self.assertEqual(str(context.exception), "Children are required")

    def test_to_html_parent_nodes_missing_tag(self):
        with self.assertRaises(ValueError) as context:
            ParentNode(
                "p",
                [
                    ParentNode(None, [LeafNode("p", "hello there")]),
                ],
            )
        self.assertEqual(str(context.exception), "Tag is required")

    def test_to_html_leaf_node_has_missing_value(self):
        with self.assertRaises(ValueError) as context:
            ParentNode(
                "p",
                [
                    LeafNode("b", None),
                ],
            )
        self.assertEqual(str(context.exception), "Value is required")

    def test_to_html_only_leaf_nodes(self):
        result = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(node.to_html(), result)

    def test_to_html_leaf_and_parent_nodes(self):
        result = "<p><b>Bold text</b><div>Normal text<i>italic text</i></div></p>"
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                ParentNode(
                    "div",
                    [
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                    ],
                ),
            ],
        )
        self.assertEqual(node.to_html(), result)

    def test_to_html_only_parent_nodes(self):
        result = "<p><div>Normal text<i>italic text</i></div>"
        result += "<div>Normal text<i>italic text</i></div></p>"

        node = ParentNode(
            "p",
            [
                ParentNode(
                    "div",
                    [
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                    ],
                ),
                ParentNode(
                    "div",
                    [
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                    ],
                ),
            ],
        )
        self.assertEqual(node.to_html(), result)


if __name__ == "__main__":
    unittest.main()
