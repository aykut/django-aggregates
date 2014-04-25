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


class Corr(BaseAggregate):
    name = 'Corr'


class RegrAvgX(BaseAggregate):
    name = 'RegrAvgX'


class RegrAvgY(BaseAggregate):
    name = 'RegrAvgY'


class RegrCount(BaseAggregate):
    name = 'RegrCount'


class RegrIntercept(BaseAggregate):
    name = 'RegrIntercept'


class RegrR2(BaseAggregate):
    name = 'RegrR2'


class RegrSlope(BaseAggregate):
    name = 'RegrSlope'


class RegrSXX(BaseAggregate):
    name = 'REGR_SXX'


class RegrSXY(BaseAggregate):
    name = 'REGR_SXY'


class RegrSYY(BaseAggregate):
    name = 'REGR_SYY'