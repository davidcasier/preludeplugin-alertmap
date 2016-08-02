

plugin_installed : ipmap/templates/ipmap.py
		python setup.py install
		rm -f ipmap/templates/ipmap.py
		rm -f ipmap/templates/ipmap.pyc
		rm -f ipmap/templates/ipmap.py.bak
		rm -f ipmap/templates/__init__.pyc

ipmap/templates/ipmap.py : ipmap/templates/ipmap.tmpl
			cheetah-compile ipmap/templates/ipmap.tmpl