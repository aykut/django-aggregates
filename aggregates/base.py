from django.db.models.aggregates import Aggregate

from . import templates


class BaseAggregate(Aggregate):
    def add_to_query(self, query, alias, col, source, is_summary):
        klass = getattr(templates, self.name)
        aggregate = klass(col, source=source,
                          is_summary=is_summary, **self.extra)
        query.aggregates[alias] = aggregate
