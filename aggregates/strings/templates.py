from django.db.models.sql.aggregates import Aggregate


class BitLength(Aggregate):
    is_ordinal = True
    sql_function = 'BIT_LENGTH'


class CharLength(Aggregate):
    is_ordinal = True
    sql_function = 'CHAR_LENGTH'


class CharacterLength(Aggregate):
    is_ordinal = True
    sql_function = 'CHARACTER_LENGTH'


class OctetLength(Aggregate):
    is_ordinal = True
    sql_function = 'OCTET_LENGTH'


class Lower(Aggregate):
    sql_function = 'LOWER'


class Upper(Aggregate):
    sql_function = 'UPPER'


class Ascii(Aggregate):
    is_ordinal = True
    sql_function = 'ASCII'


class Length(Aggregate):
    is_ordinal = True
    sql_function = 'LENGTH'


class MD5(Aggregate):
    sql_function = 'MD5'
