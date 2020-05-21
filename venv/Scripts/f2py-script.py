#!"F:\2020研一下学期hufuping\论文\食品微生物数据挖掘\Inferring Disease-Associated MicroRNAs Using Semi-supervised Multi-Label Graph Convolutional Networks\代码\DimiG_Python3\venv\Scripts\python.exe" -x
# EASY-INSTALL-ENTRY-SCRIPT: 'numpy==1.18.4','console_scripts','f2py'
__requires__ = 'numpy==1.18.4'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('numpy==1.18.4', 'console_scripts', 'f2py')()
    )
