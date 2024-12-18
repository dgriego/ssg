from htmlnode import HTMLNode


class LeafNode(HTMLNode):
    def __init__(self, tag, value):
        if not value:
            raise ValueError("value is required")

        super().__init__(tag, value)

    def to_html(self):
        if not self.tag:
            return self.value

        return f"<{self.tag}>{self.value}</{self.tag}>"
