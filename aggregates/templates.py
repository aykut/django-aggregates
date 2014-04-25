from django.db.models.sql.aggregates import Aggregate


class CharLength(Aggregate):
    is_ordinal = True
    sql_function = 'CHAR_LENGTH'


class ArrayAgg(Aggregate):
    sql_function = 'ARRAY_AGG'


class BitAnd(Aggregate):
    sql_function = 'BIT_AND'


class BitOr(Aggregate):
    sql_function = 'BIT_OR'


class BoolAnd(Aggregate):
    sql_function = 'BOOL_AND'


class BoolOr(Aggregate):
    sql_function = 'BOOL_OR'


class Every(Aggregate):
    sql_function = 'EVERY'


class StringAgg(Aggregate):
    sql_function = 'STRING_AGG'
    sql_template = "%(function)s(%(field)s, '%(delimiter)s')"

    def __init__(self, col, delimiter=None, **extra):
        super(StringAgg, self).__init__(
            col, delimiter=delimiter if delimiter else '', **extra)


class XmlAgg(Aggregate):
    sql_function = 'XMLAGG'


class Corr(Aggregate):
    sql_function = 'CORR'
    sql_template = '%(function)s(%(field)s, %(y)s)'

    def __init__(self, col, y=None, **extra):
        assert y is not None
        super(Corr, self).__init__(col, y=y, **extra)


class RegrAvgX(Aggregate):
    sql_function = 'REGR_AVGX'
    sql_template = '%(function)s(%(field)s, %(y)s)'

    def __init__(self, col, y=None, **extra):
        assert y is not None
        super(RegrAvgX, self).__init__(col, y=y, **extra)


class RegrAvgY(Aggregate):
    sql_function = 'REGR_AVGY'
    sql_template = '%(function)s(%(field)s, %(y)s)'

    def __init__(self, col, y=None, **extra):
        assert y is not None
        super(RegrAvgY, self).__init__(col, y=y, **extra)


class RegrCount(Aggregate):
    is_ordinal = True
    sql_function = 'REGR_COUNT'
    sql_template = '%(function)s(%(field)s, %(y)s)'

    def __init__(self, col, y=None, **extra):
        assert y is not None
        super(RegrCount, self).__init__(col, y=y, **extra)


class RegrIntercept(Aggregate):
    sql_function = 'REGR_INTERCEPT'
    sql_template = '%(function)s(%(field)s, %(y)s)'

    def __init__(self, col, y=None, **extra):
        assert y is not None
        super(RegrIntercept, self).__init__(col, y=y, **extra)


class RegrR2(Aggregate):
    sql_function = 'REGR_R2'
    sql_template = '%(function)s(%(field)s, %(y)s)'

    def __init__(self, col, y=None, **extra):
        assert y is not None
        super(RegrR2, self).__init__(col, y=y, **extra)


class RegrSlope(Aggregate):
    sql_function = 'REGR_SLOPE'
    sql_template = '%(function)s(%(field)s, %(y)s)'

    def __init__(self, col, y=None, **extra):
        assert y is not None
        super(RegrSlope, self).__init__(col, y=y, **extra)


class RegrSXX(Aggregate):
    sql_function = 'REGR_SXX'
    sql_template = '%(function)s(%(field)s, %(y)s)'

    def __init__(self, col, y=None, **extra):
        assert y is not None
        super(RegrSXX, self).__init__(col, y=y, **extra)


class RegrSXY(Aggregate):
    sql_function = 'REGR_SXY'
    sql_template = '%(function)s(%(field)s, %(y)s)'

    def __init__(self, col, y=None, **extra):
        assert y is not None
        super(RegrSXY, self).__init__(col, y=y, **extra)


class RegrSYY(Aggregate):
    sql_function = 'REGR_SYY'
    sql_template = '%(function)s(%(field)s, %(y)s)'

    def __init__(self, col, y=None, **extra):
        assert y is not None
        super(RegrSYY, self).__init__(col, y=y, **extra)
