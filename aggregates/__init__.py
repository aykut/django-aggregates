from .base import BaseAggregate


class CharLength(BaseAggregate):
    name = 'CharLength'


class ArrayAgg(BaseAggregate):
    name = 'ArrayAgg'


class BitAnd(BaseAggregate):
    name = 'BitAnd'


class BitOr(BaseAggregate):
    name = 'BitOr'


class BoolAnd(BaseAggregate):
    name = 'BoolAnd'


class BoolOr(BaseAggregate):
    name = 'BoolOr'


class Every(BaseAggregate):
    name = 'Every'


class StringAgg(BaseAggregate):
    name = 'StringAgg'


class XmlAgg(BaseAggregate):
    name = 'XmlAgg'
