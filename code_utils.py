import ast
import shutil
from io import StringIO
from contextlib import contextmanager


@contextmanager
def optional_file_open(optional_path, *args, **kwargs):
    """Open a fileobj pointing to a file or a StringIO obj if None.
    Argument:
        :optional_path: A path to open. If None, a StringIO obj is used.

    Optional Arguments:
        :close: (default True) If the object is a fileobj, indicates if should
                               be closed at the end.
    """
    close = kwargs.pop('close', False)
    if optional_path:
        fp = open(optional_path, *args, **kwargs)
    else:
        fp = StringIO()
    try:
        yield fp
    finally:
        if optional_path and close:
            fp.close()


def is_valid_python_code(code):
    try:
        ast.parse(code)
    except SyntaxError:
        return False
    return True


def _email_txt_file_to_python_set(txt_path, result_path=None, validate=True,
                                  set_variable_name='INVALID_DOMAIN_SETS'):
    """Turns a multiline text file into a valid Python set.
    """
    sio = StringIO()
    with open(txt_path, 'r') as origin:
        sio.write('%s = {' % set_variable_name)

        for line in origin:
            sio.write("'{}', ".format(line.strip()))

    sio.write('}')
    sio.seek(0)
    if validate and not is_valid_python_code(sio.read()):
        raise ValueError('Python Code Invalid. Check original file')

    sio.seek(0)
    if result_path:
        with open(result_path, 'w') as fp:
            shutil.copyfileobj(sio, fp)
            sio.close()
    return sio


if __name__ == '__main__':
    _email_txt_file_to_python_set(
        'throwaway_domains.txt', 'invalid_domains.py')
