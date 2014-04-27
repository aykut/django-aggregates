from .base import BaseAggregate


class As(BaseAggregate):
    name = 'As'


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


class XMLAgg(BaseAggregate):
    name = 'XMLAgg'


class Corr(BaseAggregate):
    name = 'Corr'


class CovarPop(BaseAggregate):
    name = 'COVAR_POP'


class CovarSamp(BaseAggregate):
    name = 'COVAR_SAMP'


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
