# -----------------------------------------------------------
# display a progress bar using the tqdm module
#
# (C) 2023 Frank Hofmann, Germany
# email frank.hofmann@efho.de
# License: BSD 2-Clause License
# SPDX-License-Identifier: BSD 2-Clause License
# -----------------------------------------------------------

import time
from tqdm import tqdm

for i in tqdm(range(10)):
    time.sleep(1)
