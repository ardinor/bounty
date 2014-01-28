import sys

from bounty import manager

if len(sys.argv) == 1:
    manager.app.run(debug=True, host='0.0.0.0')
else:
    manager.run(host='0.0.0.0')
# from bounty import app
# app.run(debug=True)
