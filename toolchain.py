import os
import sys

# toolchains options
ARCH = 'ARM'
CPU  = 'cortex-m3'

PLATFORM  = 'gcc'
EXEC_PATH = sys.executable[0:2] + '/work_tools/arm_gcc/bin'
BUILD     = 'debug'

if PLATFORM == 'gcc':
    # toolchains
    PREFIX = 'arm-none-eabi-'

    CC = PREFIX + 'gcc'
    AS = PREFIX + 'gcc'
    AR = PREFIX + 'ar'
    CXX = PREFIX + 'g++'
    LINK = PREFIX + 'gcc'
    TARGET_EXT = 'elf'
    SIZE = PREFIX + 'size'
    OBJDUMP = PREFIX + 'objdump'
    OBJCPY = PREFIX + 'objcopy'

    DEVICE = ' -mcpu=cortex-m3 -mthumb -ffunction-sections -fdata-sections'
    CFLAGS = DEVICE + ' -Dgcc'
    AFLAGS = ' -c' + DEVICE + ' -x assembler-with-cpp -Wa,-mimplicit-it=thumb '
    LFLAGS = DEVICE + ' -nostartfiles -Wl,--gc-sections,-Map=rt-thread.map,-cref,-u,Reset_Handler -T ldscript_rom_gnu.ld'

    if BUILD == 'debug':
        CFLAGS += ' -O0 -gdwarf-2 -g'
        AFLAGS += ' -gdwarf-2'
    else:
        CFLAGS += ' -O2'

    CXXFLAGS = CFLAGS
    POST_ACTION = OBJCPY + ' -O binary $TARGET rtthread.bin\n' + SIZE + ' $TARGET \n'
