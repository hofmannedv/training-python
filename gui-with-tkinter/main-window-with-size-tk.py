# -----------------------------------------------------------
# demonstrates how to generate a main window using Tkinter
# that as a window size of 640 x 400 px
#o
# (C) 2026 Frank Hofmann, Freiburg, Germany
# email frank.hofmann@efho.de
# 
# License: GNU Public License (GPL) v.3.0 or later
# SPDX-License-Identifier: GNU General Public License v3.0 or later
# -----------------------------------------------------------

import tkinter as tk

# define root window
root = tk.Tk()

# set the window title
root.title("Cool Application")

# define the window size: 640 x 400
root.geometry('600x400')

# keep the window displaying
root.mainloop()
