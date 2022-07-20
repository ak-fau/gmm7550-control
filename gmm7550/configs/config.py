import sys
import string
import importlib

class Config:

    def __init__(self, cfg_name):
        self.name = cfg_name.lower()
        try:
            self.cfg = importlib.import_module('.%s' % self.name, package='gmm7550.configs')
        except ImportError as e:
            print('Cannot load configuration: "%s"' % self.name, file=sys.stderr)
            print(e, file=sys.stderr)
            exit(1)

    def __getattr__(self, key):
        if hasattr(self.cfg, key):
            return getattr(self.cfg, key)
        else:
            return None

    def name_or_value(self, d, k):
        if d:
            return d[k]
        else:
            return k
