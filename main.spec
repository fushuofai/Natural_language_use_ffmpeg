# -*- mode: python ; coding: utf-8 -*-
import os

# 项目根目录
PROJECT_ROOT = os.path.dirname(os.path.abspath(SPECPATH))

# 需要打包的数据文件（相对于项目根目录）
datas = []
for f in [".env", ".env.example"]:
    src = os.path.join(PROJECT_ROOT, f)
    if os.path.exists(src):
        datas.append((src, "."))

a = Analysis(
    ['main.py'],
    pathex=[PROJECT_ROOT],
    binaries=[],
    datas=datas,
    hiddenimports=[
        'PySide6',
        'qt_material',
        'dotenv',
        'openai',
        'core',
        'core.ai_client',
        'core.video_ops',
        'gui',
        'gui.ui_demo',
        'gui.QWidget',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon=['app.ico'],
)
