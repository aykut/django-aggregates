from django.db.models.sql.aggregates import Aggregate


class Coalesce(Aggregate):
    sql_function = 'COALESCE'
    sql_template = '%(function)s(%(field)s %(othercols)s, %(default)s)'

    def __init__(self, col, othercols=None, default=0, **extra):
        othercols = othercols or []
        assert isinstance(othercols, (list, tuple))
        super(Coalesce, self).__init__(
            col, othercols=othercols, default=default, **extra)

    def as_sql(self, qn, connection):
        "Return the aggregate, rendered as SQL with parameters."
        params = []

        if hasattr(self.col, 'as_sql'):
            field_name, params = self.col.as_sql(qn, connection)
        elif isinstance(self.col, (list, tuple)):
            field_name = '.'.join([qn(c) for c in self.col])
        else:
            field_name = self.col

        dbtable = field_name.split('.')[0]
        othercols = self.extra.pop('othercols', [])
        othercols = ', '.join(['.'.join(
            [dbtable, qn(ocol)]) for ocol in othercols])

        substitutions = {
            'function': self.sql_function,
            'field': field_name,
        }
        substitutions.update(self.extra)
        substitutions.update(
            {'othercols': ', ' + othercols if othercols else othercols})

        return self.sql_template % substitutions, params


class NullIf(Aggregate):
    sql_function = 'NULLIF'
    sql_template = '%(function)s(%(field)s, %(othercol)s)'

    def __init__(self, col, othercol=None, **extra):
        assert othercol is not None
        super(NullIf, self).__init__(col, othercol=othercol, **extra)
