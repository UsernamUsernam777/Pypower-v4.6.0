import customtkinter as _ctk
import os as _os
import subprocess as _subprocess
def in_bg(duration, action=None):
    """Run action in a background thread after duration seconds."""
    t = _ctk.CTk()
    t.after(duration*1000, action)
    t.destroy()
def create_app(path, icon=None, move_to_folder=None, name=None):
    """Build a standalone .exe from a .py file using PyInstaller, then clean up build files."""
    def mainloop():
        from shutil import rmtree
        if not _os.path.exists(path):
            print('Error!')
        else:
            pj = _os.path.dirname(path)
            n_py = _os.path.basename(path)
            n_exe = _os.path.basename(path).replace('.py', '.exe')
            n_spec = _os.path.basename(path).replace('.py', '.spec')
            pro = ['pyinstaller', '--onefile', '--windowed', n_py]
            _os.chdir(pj)
            if icon:
                pro.append(f'--icon={icon}')
            if name:
                pro.append(f'--name={name}')
            p = _subprocess.Popen(pro, creationflags=_subprocess.CREATE_NO_WINDOW)
            p.wait()
            if _os.path.exists(_os.path.join('dist', n_exe)):
                _os.replace(_os.path.join('dist', n_exe), _os.path.join(pj, n_exe))
            if _os.path.exists(_os.path.join(pj, n_exe)):
                rmtree('dist', ignore_errors=True)
                rmtree('build', ignore_errors=True)
                _os.remove(n_spec)
            if _os.path.exists(path.replace('.py', '.exe')):
                if move_to_folder:
                    new = _os.path.join(move_to_folder, n_exe)
                    _os.replace(path.replace('.py', '.exe'), new)
                else:
                    new = path.replace('.py', '.exe')
                print(f"App Created Successed in {new}")
    in_bg(1, mainloop)
