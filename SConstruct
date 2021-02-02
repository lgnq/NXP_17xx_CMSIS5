import os
from os import path

# toolchains options
ARCH = 'ARM'
CPU  = 'cortex-m3'

PLATFORM  = 'gcc'
EXEC_PATH = r'/usr/bin'
BUILD     = 'debug'

curDir = os.getcwd()
PROJECT = path.join(curDir, 'mbed17xx')
TARGET     = PROJECT + '.elf'
HEX_TARGET = PROJECT + '.hex'
BIN_TARGET = PROJECT + '.bin'

if PLATFORM == 'gcc':
    # toolchains
    PREFIX = 'arm-none-eabi-'

    CC      = PREFIX + 'gcc'
    AS      = PREFIX + 'gcc'
    AR      = PREFIX + 'ar'
    CXX     = PREFIX + 'g++'
    LINK    = PREFIX + 'gcc'
    
    SIZE    = PREFIX + 'size'
    OBJDUMP = PREFIX + 'objdump'
    OBJCPY  = PREFIX + 'objcopy'

    LD_SCRIPT = 'ldscript_rom_gnu.ld'

    DEVICE = ' -mcpu=cortex-m3 -mthumb -ffunction-sections -fdata-sections'
    CFLAGS = DEVICE + ' -Dgcc'
    AFLAGS = ' -c' + DEVICE + ' -x assembler-with-cpp -Wa,-mimplicit-it=thumb '
    LFLAGS = DEVICE + ' -nostartfiles -Wl,--gc-sections,-Map=mbed.map,-cref,-u,Reset_Handler -T ' + LD_SCRIPT

    if BUILD == 'debug':
        CFLAGS += ' -O0 -gdwarf-2 -g'
        AFLAGS += ' -gdwarf-2'
    else:
        CFLAGS += ' -O2'

    CXXFLAGS = CFLAGS


# Application some variables
src = []
path = []
subsrc = []
subsrctype = type(subsrc)
srctype = type(src)

# Set the runtime environment
env = Environment(
    tools=['mingw'],
    AS=AS, ASFLAGS=AFLAGS,
    CC=CC, CCFLAGS=CFLAGS,
    AR=AR, ARFLAGS='-rc',
    CXX=CXX, CXXFLAGS=CXXFLAGS,
    LINK=LINK, LINKFLAGS=LFLAGS,
    CCCOMSTR="Compiling $TARGET", LINKCOMSTR="Linking $TARGET",
)

build_dir = 'build/'

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
env.SideEffect(PROJECT+'.map', out)

# Post Action
a1 = env.AddPostAction(TARGET, OBJCPY + ' -Oihex ' + '$TARGET ' + HEX_TARGET)
a2 = env.AddPostAction(TARGET, OBJCPY + ' -Obinary -S ' + '$TARGET ' + BIN_TARGET)
env.SideEffect(HEX_TARGET, a1)
env.SideEffect(BIN_TARGET, a2)

env.AddPostAction(TARGET, SIZE + ' $TARGET')
