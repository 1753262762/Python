#!"d:\program files (x86)\microsoft visual studio\shared\python37_64\python.exe"
# EASY-INSTALL-ENTRY-SCRIPT: 'Twisted==19.2.1','console_scripts','mailmail'
__requires__ = 'Twisted==19.2.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('Twisted==19.2.1', 'console_scripts', 'mailmail')()
    )
