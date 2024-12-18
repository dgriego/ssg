from htmlnode import HTMLNode
from leafnode import LeafNode
from textnode import TextNode, TextType


def main():
    t = TextNode("This is a text Node", TextType.NORMAL, "https://www.danielgriego.com")
    h = HTMLNode("p", "hello world", None, {"class": "p-whatever"})
    leaf = LeafNode("p", "text")

    print(t)
    print(h)
    print(leaf.to_html())


main()
