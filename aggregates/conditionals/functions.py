from .base import BaseAggregate


class Coalesce(BaseAggregate):
    name = 'Coalesce'


class NullIf(BaseAggregate):
    name = 'NullIf'
