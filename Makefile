docs:
	rst2html.py --stylesheet=docutils_basic.css --link-stylesheet README.rst index.html

version:
	aws_feed --csv_file=data/regions.csv --basedir=${PWD}/api
