# -----------------------------------------------------------
# flask microblog example application
#o
# (C) 2015 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# import required modules
import os
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort,
render_template, flash
