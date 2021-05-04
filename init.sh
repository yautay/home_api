#!/bin/sh

./usr/local/bin/uwsgi --emperor /var/www/html/mock-rest/uwsgi.ini --enable-threads
