from typing import Any

from ui.tables.dflt_set import resize_columns_to_contents


def customize_table_row(func: Any):
    def wrapper(*args, **kwargs):
        if "table" in kwargs:
            table = kwargs["table"]

        if table is None:
            return

        table.setSortingEnabled(False)

        func(*args, **kwargs)

        table.setSortingEnabled(True)
        resize_columns_to_contents(table)

    return wrapper
