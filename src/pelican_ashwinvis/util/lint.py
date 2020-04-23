#!/usr/bin/env python
import sys

from restructuredtext_lint import cli
from pelican import Pelican, settings

# By doing the following all the custom rst directives in the plugins would be
# registered
pelican_settings = settings.read_settings("pelicanconf.py")
pelican = Pelican(pelican_settings)

min_error_level = 3  # log, info, warning, error, critical
errors_found = False

cli._main(sys.argv[1:])
