from proofreader.utils.print_table import PrintTable


def test_can_init_print_table():
    assert PrintTable([])


def test_can_get_column_widths():
    headers = ['one', 'two', 'three']

    table = PrintTable(headers)
    table.add_row(['bigger', 'foo', 'bar'])

    assert table.col_widths == {0: 6, 1: 3, 2: 5}


def test_can_generate_output_string():
    headers = ['one', 'two', 'three']

    table = PrintTable(headers)
    table.add_row(['some', 'foo', 'bar'])

    assert '| some | foo |  bar  |' in str(table)
