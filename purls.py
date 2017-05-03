#!/usr/bin/env python

import re
import sys

pat = re.compile(r"(https?://[A-Za-z0-9-._~:/?#\[\]@!$&'()*+,;=%]+)")
blob = "\n".join([line.strip() for line in sys.stdin.readlines()])

smashed = re.sub(r"\n(\S)", r"\1", blob)
urls = pat.findall(blob)
urls += pat.findall(smashed)

print "\n".join(sorted(list(set(urls))))
