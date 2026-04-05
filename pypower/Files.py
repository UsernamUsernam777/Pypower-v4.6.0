import os as _os
def read_write_txt_file(file_txt, do='read', text=None, create_if_no=False):
    if create_if_no:
        make_if_not_exists(file_txt, 'txt')
    if do == 'read':
        with open(file_txt, 'r', encoding='utf-8') as f:
            return f.read().strip()
    else:
        if _os.path.exists(file_txt):
            with open(file_txt, 'w', encoding='utf-8') as f:
                f.write(text or '')
def make_if_not_exists(path, type=''):
    """Create a folder (type='') or empty file at path if it doesn't exist."""
    if not _os.path.exists(path):
        if type == '':
            _os.mkdir(path)
        else:
            with open(path, 'w', encoding='utf-8') as f:
                pass
def append_to_file(path, text, side='bottom'):
    """Append text to a file removing double blank lines."""
    old_text = read_write_txt_file(path)
    with open(path, 'w', encoding='utf-8') as b:
        if side == 'top':
            new_text = text + '\n' + old_text
        else:
            new_text = old_text + '\n' + text
        b.write(new_text.replace('\n\n', '\n'))
