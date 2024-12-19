from htmlnode import HTMLNode
from validators import validate_value


class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        validate_value(value)

        super().__init__(tag, value, None, props)

    def to_html(self):
        if not self.tag:
            return self.value

        props = self.props_to_html() if self.props else ""

        return f"<{self.tag}{props}>{self.value}</{self.tag}>"
