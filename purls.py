#!/usr/bin/env python

import re
import sys

blob = sys.stdin.read()
urls = re.findall(r"(https?://[A-Za-z0-9-._~:/?#\[\]@!$&'()*+,;=]+)", blob)
print "\n".join(urls)
