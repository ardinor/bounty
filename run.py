import sys

from bounty import manager

if len(sys.argv) == 1:
    manager.app.run(debug=True)
else:
    manager.run()
