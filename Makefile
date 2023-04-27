.PHONY: test

# Basic commands
venv:
	rm -rf venv
	python3 -m venv venv
	. venv/bin/activate

venv-win:
	python -m venv --clear venv
	.\venv\Scripts\activate

install:
	venv/bin/pip install --upgrade pip setuptools pip
	venv/bin/pip --no-cache-dir install -r requirements.txt

install-win:
	.\venv\Scripts\pip.exe install --upgrade pip setuptools pip
	.\venv\Scripts\pip.exe --no-cache-dir install -r requirements.txt

clean-venv:
	rm -rf venv