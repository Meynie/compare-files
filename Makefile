install:
	poetry install
	
build:
	poetry build
	
publish:
	poetry publish --dry-run
	
package-install:
	py -3 -m pip install --user dist/hexlet_code-0.1.0-py3-none-any.whl
	
package-reinstall:
	py -3 -m pip install --user dist/*.whl --force-reinstall
	
lint:
	poetry run flake8 gendiff_package
	