from validators import validate_children_list


class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        validate_children_list(children)
        self.tag = tag.lower() if tag else tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError()

    def props_to_html(self):
        props = " "
        for key, value in self.props.items():
            props += f'{key}="{value}" '
        return props

    def __repr__(self):
        return f"{self.__class__.__name__}({self.tag}, {self.value}, {self.children}, {self.props})"
