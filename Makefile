# Pre-release check
pre:
	flake8 collective/pece/*.py
	flake8 collective/pece/content/*.py
	bin/test -t collective.pece
	pyroma .
	check-manifest .
	viewdoc
