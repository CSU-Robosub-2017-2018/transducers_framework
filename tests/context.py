# context.py - Allows tests to run from the tests directory more easily
import os
import sys
sys.path.insert(0, os.path.abspath('..'))

from transducers_framework.transducers_framework.transducers.pressure_model_86 import pressure_model_86