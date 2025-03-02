import os
import shutil

Import("env")

#print(env.Dump())

board = env["BOARD"]
libdeps_dir = env["PROJECT_LIBDEPS_DIR"]

destdir = f'{libdeps_dir}/{board}/no-OS-FatFS-SD-SDIO-SPI-RPi-Pico/src/include'

if os.path.isdir(destdir):
    shutil.copy('patches/ffconf.h', destdir)
