from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from textnode import TextNode, TextType, text_node_to_html_node


def main():
    t = TextNode("This is a text Node", TextType.LINK, "https://www.danielgriego.com")
    h = HTMLNode("p", "hello world", None, {"class": "p-whatever"})
    leaf = LeafNode("p", "text", {"class": "div-wrapper", "id": "con"})
    leaf2 = LeafNode("p", "wword")
    leaf3 = LeafNode("div", "stop")
    parent2 = ParentNode("div", [leaf2, leaf3], {"class": "div-wrapper", "id": "con"})
    parent = ParentNode("div", children=[leaf, parent2])

    print(text_node_to_html_node(t))
    print(h)
    print(leaf.to_html())
    print(parent.to_html())


main()
