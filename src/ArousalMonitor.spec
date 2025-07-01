# -*- mode: python ; coding: utf-8 -*-


a = Analysis(
    ['main.py'],
    pathex=[],
    binaries=[],
    datas=[('../resources', 'resources')],
    hiddenimports=[],
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
    name='ArousalMonitor',
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
)
app = BUNDLE(
    exe,
    name='ArousalMonitor.app',
    icon=None,
    bundle_identifier='com.skulltech.arousalmonitor',
    info_plist={
        'NSBluetoothAlwaysUsageDescription':
            'L’app utilizza il Bluetooth per connettersi alla fascia Coospo HW9 e leggere HR e RR.',
        'CFBundleName': 'ArousalMonitor',
        'CFBundleDisplayName': 'Arousal Monitor',
        'CFBundleShortVersionString': '3.0',
        'CFBundleVersion': '3.0.0',
    }
)
