# -----------------------------------------------------------
# demonstrates how to run an external command using the
# subprocess library
#
# requires Python 3.5
#
# (C) 2017-2025 Frank Hofmann, Germany
# email frank.hofmann@efho.de
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

# include standard modules
import subprocess

subprocess.run(["df", "-h", "/home"])

