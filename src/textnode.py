from enum import Enum


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self, text, text_type, url=None):
        if not isinstance(text_type, TextType):
            raise Exception("Must be an instance of TextType")
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, textNode):
        if not isinstance(textNode, TextNode):
            raise Exception("Argument must be TextNode")

        for key, val in vars(self).items():
            textNodeVal = textNode.__dict__[key]
            if (
                isinstance(val, TextType) and val.value != textNodeVal.value
            ) or val != textNodeVal:
                return False

        return True

    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"
