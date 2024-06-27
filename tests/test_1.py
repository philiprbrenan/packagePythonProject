import sys
sys.path.insert(1, "../src/")
for p in sys.path:
  print(p)
import hello as h

def test_aaa():
  assert h.hello() == 42
