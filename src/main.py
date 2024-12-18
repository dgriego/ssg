from htmlnode import HTMLNode
from textnode import TextNode, TextType


def main():
    t = TextNode("This is a text Node", TextType.NORMAL, "https://www.danielgriego.com")
    h = HTMLNode("p", "hello world", None, {"class": "p-whatever"})

    print(t)
    print(h)


main()
