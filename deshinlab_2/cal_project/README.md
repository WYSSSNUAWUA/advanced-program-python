
Usage
-----

This package provides a small command-line calculator.

Recommended ways to run:

- From the parent directory of `calc_tool` (recommended):

	python -m calc_tool add 10 5

- If you run the script directly from inside the `calc_tool` directory, it will also work, but
	running as a package is the more portable approach:

	cd calc_tool
	python __main__.py add 10 5

If you plan to use the tool often during development, consider installing the package in
editable mode from the project root:

	pip install -e .

