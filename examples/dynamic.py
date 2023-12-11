from typing import Union

from markpy.component import Component


class Column(Component[Union['Row', str]]):
    pass


class Row(Component[Union['Column', str]]):
    pass


class Table(Component[Column | Row]):
    pass


data = [
    ['Company', 'Contact', 'Country'],
    ['Alfreds Futterkiste', 'Maria Anders', 'Germany'],
    ['Centro comercial Moctezuma', 'Francisco Chang', 'Mexico'],
]

tree = Table()[*(
    Row()[*(
        Column()[cell] for cell in row
    )]
    for row in data
)]


print(tree)
