# MarkPy

Embedding tree markup syntax (similar to HTML, XML) into Python.

## Example

Define your custom component class, e.g., a simple HTML `div`, by inheriting from `Component`:

```python
class Div(Component):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
```

Now you can create an elements tree with a quite expressive syntax:

```python
tree = Div(class_='d1')[
    Div[Div['Hello']],
    Div[Div['dear']],
    Div[Div['World!']],
    Div['this', 'is', 'the', 'real', 'magic!']
]
```

...and even print it as XML:

```python
print(tree)
```

```xml
<Div class_='d1'>
    <Div>
        <Div>
            Hello
        </Div>
    </Div>
    <Div>
        <Div>
            dear
        </Div>
    </Div>
    <Div>
        <Div>
            World!
        </Div>
    </Div>
    <Div>
        this
        is
        the
        real
        magic!
    </Div>
</Div>
```

## Use Cases and Motivation

The inspiration for creating this library comes from component-based libraries such as `Kyvi`, `FastUI`, `PyWebIO`, `PyWebView`, `Flexx`, etc.

Here's an example of how `MarkPy` can make `FastUI` components less redundant:

Current component declaration:

```python
c.Div(
    components=[
        c.Heading(text='Link List', level=2),
        c.Markdown(
            text=(
                'This is a simple unstyled list of links, '
                'LinkList is also used in `Navbar` and `Pagination`.'
            )
        ),
        c.LinkList(
            links=[
                c.Link(
                    components=[c.Text(text='Internal Link - go to the home page')],
                    on_click=GoToEvent(url='/'),
                ),
                c.Link(
                    components=[c.Text(text='Pydantic (External link)')],
                    on_click=GoToEvent(url='https://pydantic.dev'),
                ),
            ],
        ),
    ],
    class_name='border-top mt-3 pt-1',
)
```

...and within `MarkPy`:

```python
c.Div(class_name='border-top mt-3 pt-1')[
    c.Heading(level=2)['Link List'],
    c.Markdown[
        'This is a simple unstyled list of links, '
        'LinkList is also used in `Navbar` and `Pagination`.'
    ],
    c.LinkList[
        c.Link(on_click=GoToEvent(url='/'))[
            c.Text['Internal Link - go to the home page']
        ],
        c.Link(on_click=GoToEvent(url='https://pydantic.dev'))[
            c.Text['Pydantic (External link)']
        ],
    ],
]
```

Is it more readable and has fewer indentations and wrappings, isn't it?
