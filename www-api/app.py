#!/usr/bin/env python
import sys
from demo.services.api import app

if __name__ == '__main__':
    port = int(sys.argv[1])
    app.run('0.0.0.0',debug=True,port=port)
