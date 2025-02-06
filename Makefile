install:
	pip install -r requirements.txt
	python setup.py install

uninstall:
	pip uninstall hash_crack
	rm -rf build dist hash_crack.egg-info
