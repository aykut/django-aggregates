from django.db.models.sql.aggregates import Aggregate


class Coalesce(Aggregate):
    sql_function = 'COALESCE'
    sql_template = '%(function)s(%(field)s, %(default)s)'

    def __init__(self, col, default=0, **extra):
        super(Coalesce, self).__init__(col, default=default, **extra)
