from .base import BaseAggregate


class CharLength(BaseAggregate):
    name = 'CharLength'


class ArrayAgg(BaseAggregate):
    name = 'ArrayAgg'
