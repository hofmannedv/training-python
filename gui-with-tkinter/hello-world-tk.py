# -----------------------------------------------------------
# demonstrates how to greet you using Tkinter
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

# add a label to the root window
message = tk.Label(root, text="Hello, world!")
message.pack()

# keep the window displaying
root.mainloop()
