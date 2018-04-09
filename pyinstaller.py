#-*- coding:utf-8 -*-
__author__ = 'Administrator'


if __name__ == '__main__':
    from PyInstaller.__main__ import run
    # opts=['main.py','-D','--icon=main.ico','--version-file=version.txt','--upx-dir=upx394w']
    # opts=['main.py','-F']
    opts=['main.spec']
    run(opts)

