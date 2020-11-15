# look I don't know how makefiles work, if you can make `make gnocchi fast`
# call `gnocchi` but only after exporting an arg for fast, but *without*
# needing a prerequisite of `fast` on `gnocchi`, make a pull request.
# cheers.

gnocchi:
	python3 gnocc.py

fast:
	python3 gnocc.py --fast

fancy:
	python3 gnocc.py --fancy

vegan:
	python3 gnocc.py --vegan

vegetarian:
	python3 gnocc.py -v

nodairy:
	python3 gnoccy.py -n

help:
	python3 gnocc.py -h
