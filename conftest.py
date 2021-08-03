import os
import sys
from unittest.mock import Mock

# add packages to sys path so they can be imported normally in tests
packages_dir = os.path.join(os.path.dirname(__file__), "packages")
for subdir, _, __ in os.walk(packages_dir):
    sys.path.append(subdir)

# mock modules that are not installed but need to be imported
for module in [
    "pitop.common.ptdm.zmq",
    "zmq",
    "smbus2",
    "smbus",
    "atexit",
]:
    sys.modules[module] = Mock()
