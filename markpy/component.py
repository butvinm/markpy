from typing import Any, Generic, Self, Type, TypeVar

ChildT = TypeVar('ChildT')


class Component(Generic[ChildT]):
    INDENT = '    '

    children: tuple[ChildT]

    def __class_getitem__(
        cls: Type[Self],
        key: ChildT | tuple[ChildT],
    ) -> Self:
        if not isinstance(key, tuple):
            key = (key, )

        obj = cls()
        return obj.__getitem__(key)

    def __getitem__(self, key: ChildT | tuple[ChildT]) -> Self:
        if not isinstance(key, tuple):
            key = (key, )

        self.children = key
        return self

    def get_public_attrs(self) -> dict[str, Any]:
        return {
            name: value
            for name, value in self.__dict__.items()
            if not name.startswith('_') and name != 'children'
        }

    def attrs_repr(self) -> str:
        attrs: list[str] = []
        for name, value in self.get_public_attrs().items():
            attrs.append('{name}={value}'.format(
                name=name,
                value=repr(value),
            ))

        return ' '.join(attrs)

    def tree_repr(self, indent: int = 0) -> str:
        tag = self.__class__.__name__
        attrs = self.attrs_repr()

        text = Component.INDENT * indent

        if attrs:
            text += '<{tag} {args}>'.format(
                tag=tag,
                args=self.attrs_repr(),
            )
        else:
            text += '<{tag}>'.format(tag=tag)

        if self.children:
            text += '\n'
            for child in self.children:
                if isinstance(child, Component):
                    text += child.tree_repr(indent + 1)
                else:
                    text += Component.INDENT * (indent + 1)
                    text += str(child)
                    text += '\n'

        text += Component.INDENT * indent
        text += '</{tag}>\n'.format(tag=tag)
        return text

    def __repr__(self) -> str:
        return self.tree_repr()
