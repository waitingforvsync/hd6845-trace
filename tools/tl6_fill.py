#!/usr/bin/env python3
"""Replace one bounded section of notes/blocks/tl6.md (from its '## Heading' line to the next
'## ' line) with the text of a file:  tl6_fill.py 'Heading' FILE   (the tracer's own helper:
edits by bounded spans only, never to the end of the file)."""
import sys, os, re
p = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'notes/blocks/tl6.md')
s = open(p).read(); h = sys.argv[1]; body = open(sys.argv[2]).read().strip('\n')
m = re.search(r'^## ' + re.escape(h) + r'[^\n]*\n', s, re.M)
assert m, 'no such heading'
n = re.search(r'^## ', s[m.end():], re.M)
end = m.end() + n.start() if n else len(s)
s = s[:m.end()] + '\n' + body + '\n\n' + s[end:]
open(p, 'w').write(s)
