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

    def __init__(self, col, delimiter=False, **extra):
        super(StringAgg, self).__init__(
            col, delimiter=str(delimiter) if delimiter else '', **extra)


class XmlAgg(Aggregate):
    sql_function = 'XMLAGG'
