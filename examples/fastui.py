from typing import Any, Callable
from markpy.component import Component


class Div(Component[Any]):
    def __init__(self, class_name: str):
        self.class_name = class_name


class Heading(Component[str]):
    def __init__(self, level: int):
        self.level = level


class Markdown(Component[str]):
    pass


class Link(Component[Any]):
    def __init__(self, on_click: Callable[[], Any]):
        self.on_click = on_click


class LinkList(Component[Link]):
    pass


class Text(Component[str]):
    pass


Div(class_name='border-top mt-3 pt-1')[
    Heading(level=2)['Link List'],
    Markdown()[
        'This is a simple unstyled list of links, '
        'LinkList is also used in `Navbar` and `Pagination`.'
    ],
    LinkList()[
        Link(on_click=lambda: print('Hello'))[
            Text()['Internal Link - go to the home page']
        ],
        Link(on_click=lambda: print('Hello'))[
            Text()['Pydantic (External link)']
        ],
    ],
]
