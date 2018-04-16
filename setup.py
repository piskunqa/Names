from cx_Freeze import setup, Executable

include = ["main_parser.py", "data.txt", "results.txt"]
includes = ['multiprocessing', 'requests', 'os']
excludes = ['Tkinter']
packages = ['idna']
setup(
    name="Names",
    version="0.1",
    description="FawN",
    options={
        'build_exe': {'includes': includes, 'excludes': excludes, 'packages': packages, 'include_files': include}},
    executables=[Executable("__init__.py")]
)
