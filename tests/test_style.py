import compileall
import os

# External modules.
import pep8

FLINTROCK_ROOT_DIR = (
    os.path.dirname(
        os.path.dirname(
            os.path.realpath(__file__))))

TEST_TARGETS = [
    'setup.py',
    'flintrock/',
    'tests/']

TEST_PATHS = [
    os.path.join(FLINTROCK_ROOT_DIR, path) for path in TEST_TARGETS]


def test_code_compiles():
    for path in TEST_PATHS:
        if os.path.isdir(path):
            result = compileall.compile_dir(path)
        else:
            result = compileall.compile_file(path)
        # NOTE: This is not publicly documented, but a return of 1 means
        #       the compilation succeeded.
        #       See: http://bugs.python.org/issue25768
        assert result == 1


def test_pep8_compliance():
    style = pep8.StyleGuide(
        config_file=os.path.join(FLINTROCK_ROOT_DIR, 'tox.ini'))
    result = style.check_files(TEST_PATHS)
    assert result.total_errors == 0
