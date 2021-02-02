# Some dependent packages
import os.path
import os
import toolchain
from os import path

# Application some variables
src = []
path = []
subsrc = []
subsrctype = type(subsrc)
srctype = type(src)

curDir = os.getcwd()
# PROJECT = path.join(curDir, 'discovery')
PROJECT = 'discovery'
TARGET = PROJECT + '.elf'
HEX_TARGET = PROJECT + '.hex'
BIN_TARGET = PROJECT + '.bin'

# Set the runtime environment
env = Environment(
    tools=['mingw'],
    PLATFORM = toolchain.PLATFORM,
    AS=toolchain.AS, ASFLAGS=toolchain.AFLAGS,
    CC=toolchain.CC, CCFLAGS=toolchain.CFLAGS,
    AR=toolchain.AR, ARFLAGS='-rc',
    CXX=toolchain.CXX, CXXFLAGS=toolchain.CXXFLAGS,
    LINK=toolchain.LINK, LINKFLAGS=toolchain.LFLAGS,
    CCCOMSTR="Compiling $TARGET", LINKCOMSTR="Linking $TARGET",
)

build_dir = 'build/' + str(env['PLATFORM']) + '/'

# Search all SConscript file
for root, dirs, files in os.walk(str(Dir('#'))):
    for item in files:
        if item == 'SConscript':
            temp = SConscript(os.path.join(root, item), variant_dir = build_dir + root, duplicate=0)
            
            if isinstance(temp, subsrctype):
                subsrc += temp

# Add all h files to CPPPATH and add all c files to src
for item in subsrc:
    if isinstance(item, str):
        path.append(item)
    elif isinstance(item, srctype):
        src += item

# Building
out = env.Program(TARGET, src, CPPPATH=path)

# Post Action
a1 = env.AddPostAction(TARGET, toolchain.OBJCPY + ' -Oihex ' + '$TARGET ' + HEX_TARGET)
a2 = env.AddPostAction(TARGET, toolchain.OBJCPY + ' -Obinary -S ' + '$TARGET ' + BIN_TARGET)
env.SideEffect(HEX_TARGET, a1)
env.SideEffect(BIN_TARGET, a2)
