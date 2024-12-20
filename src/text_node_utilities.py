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

    # old implementation
    # new_nodes = []
    # size = len(delimiter.value)
    # for node in old_nodes:
    #     if node.text_type is not TextType.NORMAL:
    #         continue
    #
    #     inc = 0
    #
    #     while True:
    #         first_d = node.text.find(delimiter.value, inc)
    #         second_d = node.text.find(delimiter.value, first_d + size)
    #
    #         if first_d == inc and second_d > -1:
    #             text = node.text[first_d + size : second_d]
    #             new_nodes.append(TextNode(text, text_type))
    #             inc = second_d + size
    #             continue
    #
    #         if first_d >= 0 and second_d == -1:
    #             first_d = node.text.find(delimiter.value, first_d + size)
    #
    #         text = node.text[inc:]
    #         if first_d > -1 and second_d > -1:
    #             text = node.text[inc:first_d]
    #             inc = first_d
    #
    #         if text:
    #             new_nodes.append(TextNode(text, TextType.NORMAL))
    #
    #         if inc >= len(node.text) or first_d < 0:
    #             break
