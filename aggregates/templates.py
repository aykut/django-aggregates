from django.db.models.sql.aggregates import Aggregate


class CharLength(Aggregate):
    is_ordinal = True
    sql_function = 'CHAR_LENGTH'

    def __init__(self, col, **extra):
        super(CharLength, self).__init__(col, **extra)


class ArrayAgg(Aggregate):
    sql_function = 'ARRAY_AGG'
    sql_template = '%(function)s(%(field)s)'

    def __init__(self, col, **extra):
        super(ArrayAgg, self).__init__(col, **extra)
