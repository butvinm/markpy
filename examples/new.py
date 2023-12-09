demo_page(title='Components')[
    c.Div[
        c.Heading(level=2)['Text'],
        c.Text['This is a text component.'],
    ],
    c.Div(class_name='border-top mt-3 pt-1')[
        c.Heading(level=2)['Paragraph'],
        c.Paragraph['This is a paragraph component.'],
    ],
    c.Div(class_name='border-top mt-3 pt-1')[
        c.Heading(level=2)['Heading'],
        c.Heading(level=3)['This is an H3'],
        c.Heading(level=4)['This is an H4'],
    ],
    c.Div(class_name='border-top mt-3 pt-1')[
        c.Heading(level=2)['Code'],
        c.Code(language='python')[
            """\
            from pydantic import BaseModel

            class Delivery(BaseModel):
            dimensions: tuple[int, int]

            m = Delivery(dimensions=['10', '20'])
            print(m.dimensions)
            #> (10, 20)
            """
        ],
    ],
    c.Div(class_name='border-top mt-3 pt-1')[
        c.Heading(level=2)['Link List'],
        c.Markdown[
            'This is a simple unstyled list of links, '
            'LinkList is also used in `Navbar` and `Pagination`.'
        ],
        c.LinkList[
            c.Link(on_click=GoToEvent(url='/'))[
                c.Text['Internal Link - the the home page']
            ],
            c.Link(on_click=GoToEvent(url='https://pydantic.dev'))[
                c.Text['Pydantic (External link)']
            ],
        ],
    ],
    c.Div(class_name='border-top mt-3 pt-1')[
        c.Heading(level=2)['Button and Modal'],
        c.Paragraph['The button below will open a modal with static content.'],
        c.Button(on_click=PageEvent(name='static-modal'))['Show Static Modal'],
        c.Modal(
            open_trigger=PageEvent(name='static-modal'),
        )[
            c.Title['Static Modal'],
            c.Body[
                c.Paragraph['This is some static content that was set when the modal was defined.'],
            ],
            c.Footer(on_click=PageEvent(name='static-modal', clear=True))[
                c.Button['Close'],
            ],
        ],
    ],
    c.Div(class_name='border-top mt-3 pt-1')[
        c.Heading(level=2)['Dynamic Modal'],
        c.Markdown[
            'The button below will open a modal with content loaded from the server when '
            "it's opened using `ServerLoad`."
        ],
        c.Button(on_click=PageEvent(name='dynamic-modal')
                 )['Show Dynamic Modal'],
        c.Modal(
            open_trigger=PageEvent(name='dynamic-modal'),
        )[
            c.Title['Dynamic Modal'],
            c.Body[
                c.ServerLoad(path='/components/dynamic-content'),
            ],
            c.Footer(on_click=PageEvent(name='dynamic-modal', clear=True))[
                c.Button['Close'],
            ],
        ],
    ],
    c.Div(class_name='border-top mt-3 pt-1')[
        c.Heading(level=2)['Server Load'],
        c.Paragraph['Even simpler example of server load, replacing existing content.'],
        c.Button(on_click=PageEvent(name='server-load')
                 )['Load Content from Server'],
        c.Div(class_name='py-2')[
            c.ServerLoad(
                path='/components/dynamic-content',
                load_trigger=PageEvent(name='server-load'),
            )[
                c.Text['before']
            ],
        ],
    ],
    c.Div(class_name='border-top mt-3 pt-1')[
        c.Heading(level=2)['Server Load SSE'],
        c.Markdown['`ServerLoad` can also be used to load content from an SSE stream.'],
        c.Button(on_click=PageEvent(name='server-load-sse')
                 )['Load SSE content'],
        c.Div(class_name='my-2 p-2 border rounded')[
            c.ServerLoad(
                path='/components/sse',
                sse=True,
                load_trigger=PageEvent(name='server-load-sse'),
            )[
                c.Text['before']
            ],
        ],
    ],
    c.Div(class_name='border-top mt-3 pt-1',)[
        c.Heading(level=2)['Iframe'],
        c.Markdown['`Iframe` can be used to embed external content.'],
        c.Iframe(src='https://pydantic.dev', width='100%', height=400),
    ],
    c.Div(class_name='border-top mt-3 pt-1')[
        c.Heading(level=2)['Image'],
        c.Paragraph['An image component.'],
        c.Image(
            src='https://avatars.githubusercontent.com/u/110818415',
            alt='Pydantic Logo',
            width=200,
            height=200,
            loading='lazy',
            referrerpolicy='no-referrer',
            class_name='border rounded',
        ),
    ],
]
