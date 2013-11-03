# -*- mode: python -*-
a = Analysis(['meta-spider.py'],
             pathex=['/home/rwilson/projects/http/meta-spider'],
             hiddenimports=[],
             hookspath=None,
             runtime_hooks=None)
pyz = PYZ(a.pure)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='meta-spider',
          debug=False,
          strip=None,
          upx=True,
          console=True )
