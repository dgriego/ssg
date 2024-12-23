import re
from warnings import warn
from leafnode import LeafNode
from enums import TextType, TextTypeDelimiter
from textnode import TextNode


def text_node_to_html_node(text_node):
    match text_node.text_type:
        case TextType.NORMAL:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode("b", text_node.text)
        case TextType.ITALIC:
            return LeafNode("i", text_node.text)
        case TextType.CODE:
            return LeafNode("code", text_node.text)
        case TextType.LINK:
            return LeafNode("a", text_node.text, {"href": text_node.url})
        case TextType.IMAGE:
            return LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})
        case _:
            raise Exception("invalid text type")


def split_nodes_delimiter(old_nodes, delimiter: TextTypeDelimiter, text_type: TextType):
    if not isinstance(delimiter, TextTypeDelimiter):
        raise ValueError("Delimiter must be TextTypeDelimiter value")

    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.NORMAL:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter.value)
        if len(sections) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.NORMAL))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]+)\]\(([https:\/\/]?.*?[jpeg|gif|jpg|png])\)", text)


def extract_markdown_link(text):
    return re.findall(
        r"\[([^\[\]]+)\]\(([https:\/\/]?[www.]?.+?[.]+\w+?[\/]?.*?)\)", text
    )
