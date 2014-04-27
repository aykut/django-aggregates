django-aggregates
=================
Aggregate, String and Conditional SQL functions to use into Annotate and Aggregate methods.

Any kind of contribtions and ideas are welcome.

Installation
=================
    pip install django-aggregates

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


