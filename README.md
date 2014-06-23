# Trac Hamster Plugin 

This trac plugin allows time entries, created in [Project Hamster](http://projecthamster.wordpress.com/), to be sync'd with [Trac](http://trac.edgewall.org/) using [hamster-trac-syncr](https://github.com/alexhayes/hamster-trac-syncr).

# Installation

Firstly you must create the python egg:

	git clone git@github.com:alexhayes/trac-hamster-plugin.git
	sudo python setup.py bdist_egg
	
Then upload the created egg file in the ''dist'' folder using the admin interface
in trac.

# Author

Alex Hayes <alex@alution.com> - special thanks to roi.com.au for sponsoring this development