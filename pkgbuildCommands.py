# ST2Commands: makepkg, makepkg_src, makepkg_gen, namcap_check
# Main menu entry:
# {
# "caption": "PKGBUILD Tools",
# "mnemonic": "P",
# "children":
#     [
#         { "caption": "Build Package", "mnemonic": "B", "command": "makepkg" },
#         { "caption": "Generate MD5", "mnemonic": "D", "command": "makepkg_gen" },
#         { "caption": "Generate Source", "mnemonic": "S", "command": "makepkg_src" },
#         { "caption": "Validate", "mnemonic": "V", "command": "namcap_check"}
#     ]
# }

import os
import sublime
import sublime_plugin

class MakepkgCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if self.view.file_name():
            folder_name, file_name = os.path.split(self.view.file_name())

        print folder_name, file_name
        self.view.window().run_command('exec', {'cmd': ['makepkg', '-c', '-p', file_name], 'working_dir': folder_name, 'quiet': False})

class MakepkgSrcCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if self.view.file_name():
            folder_name, file_name = os.path.split(self.view.file_name())

        print folder_name, file_name
        self.view.window().run_command('exec', {'cmd': ['makepkg', '-c', '--source', '-p', file_name], 'working_dir': folder_name, 'quiet': False})

class MakepkgGenCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if self.view.file_name():
            folder_name, file_name = os.path.split(self.view.file_name())

        print folder_name, file_name
        self.view.window().run_command('exec', {'cmd': ['makepkg', '-c', '-g', '-p', file_name], 'working_dir': folder_name, 'quiet': False})        

class NamcapCheckCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        if self.view.file_name():
            folder_name, file_name = os.path.split(self.view.file_name())

        print folder_name, file_name
        self.view.window().run_command('exec', {'cmd': ['namcap', file_name], 'working_dir': folder_name, 'quiet': False})        

