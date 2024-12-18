from htmlnode import HTMLNode
from validators import check_exists, validate_tag, validate_children


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        validate_tag(tag)
        validate_children(children)
        super().__init__(tag, None, children, props)

    @check_exists("tag")
    @check_exists("children")
    def to_html(self):
        str = f"<{self.tag}>"

        for child in self.children:
            str += child.to_html()

        return str + f"</{self.tag}>"
