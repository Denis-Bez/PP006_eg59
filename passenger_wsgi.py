import sys

import os

INTERP = os.path.expanduser("/var/www/u1640679/data/venv_eg59/bin/python")
if sys.executable != INTERP:
   os.execl(INTERP, INTERP, *sys.argv)

sys.path.append(os.getcwd())

from app import application