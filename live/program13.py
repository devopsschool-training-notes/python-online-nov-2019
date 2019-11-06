# Method 1
# ===============
import subprocess
subprocess.call(['./test.sh']) # Thanks @Jim Dennis for suggesting the []

# Method 2
# ===============
import os
os.system('command')
os.system('ls -l')

# Method 23
# ===============
import subprocess
import shlex
subprocess.call(shlex.split('./test.sh param1 param2'))

# Refer - https://janakiev.com/blog/python-shell-commands/