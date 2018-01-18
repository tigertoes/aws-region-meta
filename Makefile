docs:
	rst2html.py README.rst index.html

version:
	aws_feed --csv_file=data/regions.csv --basedir=${PWD}/api
