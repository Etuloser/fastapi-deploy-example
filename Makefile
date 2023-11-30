clean:
	rm -rf build dist main.spec
build:
	pyinstaller -D main.py