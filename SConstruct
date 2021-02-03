import os

ARCH = 'ARM'
CPU  = 'cortex-m3'

PLATFORM  = 'gcc'
EXEC_PATH = r'/usr/bin'
BUILD     = 'debug'

PROJECT    = 'mbed17xx'
TARGET     = PROJECT + '.elf'
HEX_TARGET = PROJECT + '.hex'
BIN_TARGET = PROJECT + '.bin'

if PLATFORM == 'gcc':
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
    LFLAGS = DEVICE + ' -nostartfiles -Wl,--gc-sections,-Map=mbed17xx.map,-cref,-u,Reset_Handler -T ' + LD_SCRIPT

    if BUILD == 'debug':
        CFLAGS += ' -O0 -gdwarf-2 -g'
        AFLAGS += ' -gdwarf-2'
    else:
        CFLAGS += ' -O2'

    CXXFLAGS = CFLAGS

# Set the runtime environment
env = Environment(
    tools     = ['mingw'],

    AS        = AS, 
    CC        = CC, 
    AR        = AR, 
    CXX       = CXX, 
    LINK      = LINK, 

    ASFLAGS   = AFLAGS,
    CCFLAGS   = CFLAGS,
    ARFLAGS   = '-rc',
    CXXFLAGS  = CXXFLAGS,
    LINKFLAGS = LFLAGS,

    ASCOMSTR   = "Compiling $TARGET", 
    CCCOMSTR   = "Compiling $TARGET", 
    LINKCOMSTR = "Linking $TARGET",
)

# Application some variables
src = []
inc = []

# Search all SConscript file and add src/header files
for root, dirs, files in os.walk(str(Dir('#'))):
    for item in files:
        if item == 'SConscript':
            temp = SConscript(os.path.join(root, item), variant_dir = 'build/' + root, duplicate=0)

            src += temp['src']
            inc += temp['inc']          

# Building
out = env.Program(TARGET, src, CPPPATH = inc)
env.SideEffect(PROJECT+'.map', out)

# Post Action
a1 = env.AddPostAction(TARGET, OBJCPY + ' -Oihex ' + '$TARGET ' + HEX_TARGET)
a2 = env.AddPostAction(TARGET, OBJCPY + ' -Obinary -S ' + '$TARGET ' + BIN_TARGET)
env.SideEffect(HEX_TARGET, a1)
env.SideEffect(BIN_TARGET, a2)

env.AddPostAction(TARGET, SIZE + ' $TARGET')
