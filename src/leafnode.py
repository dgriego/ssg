from htmlnode import HTMLNode
from validators import validate_value


class LeafNode(HTMLNode):
    def __init__(self, tag, value):
        validate_value(value)

        super().__init__(tag, value)

    def to_html(self):
        if not self.tag:
            return self.value

        return f"<{self.tag}>{self.value}</{self.tag}>"
