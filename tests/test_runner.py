try:
    from unittest.mock import patch
except ImportError:
    from mock import patch

from proofreader.runner import run, _run_command


def test_it_will_return_1_exit_code_on_failure(bad_py_file):
    try:
        run(targets=[bad_py_file.strpath])
    except SystemExit as exception:
        assert exception.code == 1


def test_it_will_return_zero_exit_code_on_success(good_py_file):
    try:
        run(targets=[good_py_file.strpath])
    except SystemExit as exception:
        assert exception.code == 0


def test_run_command_will_return_a_bool():
    with patch('proofreader.runner.Popen') as mock_popen:
        mock_popen.returncode = 0
        result = _run_command('dummy_cmd', [''], [''])
        assert isinstance(result, bool)
