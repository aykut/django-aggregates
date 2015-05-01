django-aggregates
=================
Aggregate, String and Conditional SQL functions to use into Annotate and Aggregate methods. Any kind of contribitions and ideas are welcome.

Installation
=================
    pip install django-aggregates

Usage
=================
    >> from aggregates import StringAgg
    >> People.objects.aggregate(names=StringAgg('name', delimiter(', ')))
    >> {'names': 'Walter, The Dude, Donny, Jesus'}

    >> from aggregates import As
    >> People.objects.values('address__title').annotate(prettyname=As('address__title')).values('prettyname')
    >> [{'prettyname': 'someadress1'}, {'prettyname': 'someaddress2'}]

    >> from aggregates.strings import CharLength
    >> People.objects.annotate(char_len=CharLength('name')).filter(char_len__gt=6)
    >> [<People: Walter>, <People: The Dude>]

    >> from aggregates.conditionals import Coalesce, NullIf
    >> person=People.objects.annotate(null_if=NullIf('name', othercol='surname'))[0]
    >> person.null_if
    >> 'Walter'
    >> person=People.objects.annotate(coalesce=Coalesce('age', default=18))[0]
    >> person.coalesce
    >> 18
    >> person.age
    >>

Available Functions
=================
Aggregates:

    from aggregates import ...
- As
- BitAnd
- BitOr
- BoolAnd  **# Only PostgreSQL**
- BoolOr  **# Only PostgreSQL**
- Every  **# Only PostgreSQL**
- StringAgg  **# Only PostgreSQL**
- XMLAgg  **# Only PostgreSQL**
- Corr  **# Only PostgreSQL**
- CovarPop  **# Only PostgreSQL**
- CovarSamp  **# Only PostgreSQL**
- RegrAvgX  **# Only PostgreSQL**
- RegrAvgY  **# Only PostgreSQL**
- RegrCount  **# Only PostgreSQL**
- RegrIntercept  **# Only PostgreSQL**
- RegrR2  **# Only PostgreSQL**
- RegrSlope  **# Only PostgreSQL**
- RegrSXX  **# Only PostgreSQL**
- RegrSXY  **# Only PostgreSQL**
- RegrSYY  **# Only PostgreSQL**
- Mode  **# Only PostgreSQL 9.4+**
- PercentileCont  **# Only PostgreSQL 9.4+**
- PercentileDisc  **# Only PostgreSQL 9.4+**

Strings:

    from aggregates.string import ...
- BitLength
- CharLength
- CharacterLength
- OctetLength
- Lower
- Upper
- Ascii
- Length
- MD5  **# Only PostgreSQL**

Conditionals:

    from aggregates.conditionals import ...
- NullIf
- Coalesce  **# Only PostgreSQL**

Requirements
==================================
- Django 1.2+

TODO
=================
- UnitTests.
- More detailed informations about functions.
- JSON functions and operations
