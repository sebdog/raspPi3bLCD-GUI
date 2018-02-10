import sys
from cx_Freeze import setup, Executable

setup(
	name="Chair",
	version = "0.1",
	description = "prototype",
	executables = [Executables("Chair.py",base=None)])