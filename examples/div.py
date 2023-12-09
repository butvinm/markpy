from markpy import Component


class Div(Component):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)


tree = Div(class_='d1')[
    Div[Div['Hello']],
    Div[Div['dear']],
    Div[Div['World!']],
    Div['this', 'is', 'the', 'real', 'magic!']
]

print(tree)
