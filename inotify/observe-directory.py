# -----------------------------------------------------------
# demonstrates how to react on changes in a directory
# using the inotify interface
#o
# (C) 2025 Frank Hofmann, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
#
# inspired by this post on Lowendbox:
# https://lowendbox.com/blog/instant-reactions-to-filesystem-events-with-inotify/
# -----------------------------------------------------------

# import required Python modules
import sys
import inotify.adapters
import os

# read the directory to be observed as first parameter
if len(sys.argv) > 1:
    directory = sys.argv[1]

    # start with observation in case the given directory actually exists
    if os.path.exists(directory):
        # initialize inotify loop
        marker = inotify.adapters.Inotify()

        # add directory to be observed
        marker.add_watch(directory)

        # go through every generated event
        for event in marker.event_gen(yield_nones=False):
            (_, eventType, path, filename) = event

            # output changes in the observed directory
            print("PATH=[{}] FILENAME=[{}] EVENT_TYPES={}".format( 
                path, filename, eventType)
            )
    else:
        # given directory does not exist, return with exit code 2
        print ("Error: given directory {} does not exist".format(directory))
        sys.exit(2)
else:
    # script called without parameters, return with exit code 1
    print ("Error: script called without directory as parameter")
    sys.exit(1)
