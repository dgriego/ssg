from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode, TextType


def main():
    t = TextNode("This is a text Node", TextType.NORMAL, "https://www.danielgriego.com")
    h = HTMLNode("p", "hello world", None, {"class": "p-whatever"})
    leaf = LeafNode("p", "text")
    leaf2 = LeafNode("p", "wword")
    leaf3 = LeafNode("div", "stop")
    parent2 = ParentNode("div", [leaf2, leaf3])
    parent = ParentNode("div", children=[leaf, parent2])

    print(t)
    print(h)
    print(leaf.to_html())
    print(parent.to_html())


main()
