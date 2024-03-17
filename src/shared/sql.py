sql_select = "SELECT {columns} FROM {table}"
sql_where = "where {filter}"
sql_join = """
    select {columns}
    from {table_1}
    inner join {table_2} on {join_filter}
"""
