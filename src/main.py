from htmlnode import HTMLNode
from leafnode import LeafNode
from parentnode import ParentNode
from text_node_utilities import (
    extract_markdown_images,
    extract_markdown_link,
    split_nodes_delimiter,
)
from textnode import TextNode
from enums import TextType, TextTypeDelimiter


def main():
    t = TextNode("This is a text Node", TextType.BOLD, "https://www.danielgriego.com")
    t2 = TextNode("This is a **text Node** with bold", TextType.NORMAL)
    t3 = TextNode("This is a text Node with **bold**", TextType.NORMAL)
    h = HTMLNode("p", "hello world", None, {"class": "p-whatever"})
    leaf = LeafNode("p", "text", {"class": "div-wrapper", "id": "con"})
    leaf2 = LeafNode("p", "wword")
    leaf3 = LeafNode("div", "stop")
    parent2 = ParentNode("div", [leaf2, leaf3], {"class": "div-wrapper", "id": "con"})
    parent = ParentNode("div", children=[leaf, parent2])

    # print(split_nodes_delimiter([t2], TextTypeDelimiter.*ITALIC, TextType.ITALIC))
    # print(split_nodes_delimiter([t, t3], TextTypeDelimiter.BOLD, TextType.BOLD))
    # print(text_node_to_html_node(t))
    # print(h)
    # print(leaf.to_html())
    # print(parent.to_html())
    text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
    # text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
    print(extract_markdown_link(text))


main()
