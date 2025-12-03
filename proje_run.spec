# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['proje_run.py'],
    pathex=[],
    binaries=[],
    datas=[('logistic_model.pkl', '.'), ('scaler_model.pkl', '.'), ('ornek_video', 'ornek_video'), ('C:\\Users\\HP\\Desktop\\Projeler\\El_Hareketleri\\el_tanima\\Lib\\site-packages\\mediapipe\\modules', 'mediapipe\\modules')],
    hiddenimports=['sklearn', 'sklearn.preprocessing', 'sklearn.linear_model', 'cv2', 'numpy', 'mediapipe'],
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
    name='proje_run',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
