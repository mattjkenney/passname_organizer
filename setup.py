application_title= 'Password Manager'
main_python_file= 'pass_man.py'
icon_file= 'main.ico'
packs = []
mods = []
files_to_include = ['applicationClassv2.py',
                    'menu.py',
                    'show.png',
                    'write.png']
build_exe_options = {'includes': mods, 'packages': packs,
                     'include_files': files_to_include}
your_name= 'Matt Kenney'
program_description= '''

Save and recall your login data for all your accounts
in this app.  For utmost security, save all these files
to a usb drive where it can be locked in a safe space.

'''

#main
import sys

from cx_Freeze import setup, Executable

base=None
##if sys.platform=='win32':
##    base= 'Win32GUI'

setup(
    name= application_title,
    version= '1.0',
    description= program_description,
    author= your_name,
    options= {'build_exe': build_exe_options},
    executables= [Executable(main_python_file, base= base, icon= icon_file)])
