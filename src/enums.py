from enum import Enum


class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextTypeDelimiter(Enum):
    ITALIC = "*"
    BOLD = "**"
    CODE = "`"
