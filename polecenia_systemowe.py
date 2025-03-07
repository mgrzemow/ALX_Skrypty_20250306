import os
# bez czytania outputu
# os.system('dir')

import subprocess
# dawniej:
# subprocess.popen('dir')
# od wersji
r = subprocess.run('dir',
                   shell=True,
                   capture_output=True,
                   encoding='cp1252')
print(r.stdout)
import re
wr = '\d\d'
t = '2d'
m = re.match(wr, t)
if m:
    print(m)
else:
    print('nie ma dopasowania')