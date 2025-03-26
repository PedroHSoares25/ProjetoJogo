
from cx_Freeze import setup, Executable

executables = [Executable("main.py")]

setup(
    name="GUNSHOT",
    version="1.0",
    description="GUNSHOT app",
    options={"build_exe": {"packages": ["pygame"]}},
    executables=executables
)