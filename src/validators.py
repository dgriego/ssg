def validate_tag(tag):
    if not tag:
        raise ValueError("Tag is required")


def validate_children(children):
    if not children:
        raise ValueError("Children are required")


def validate_value(value):
    if not value:
        raise ValueError("Value is required")


def validate_children_list(children):
    from htmlnode import HTMLNode

    if (
        children
        and len(list(filter(lambda x: not isinstance(x, HTMLNode), children))) > 0
    ):
        raise ValueError("children must be HTMLNode")


def check_exists(prop):
    def check(fn):
        def wrapper(*args):
            obj = args[0]
            match prop:
                case "children":
                    validate_children(obj.children)
                case "tag":
                    validate_tag(obj.tag)

            return fn(obj)

        return wrapper

    return check
