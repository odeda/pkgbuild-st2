# PKGBUILD tools for Sublime Text 2
A bunch of random stuff (seriously)hacked together to make PKGBUILDing more  pleasant.

## Included:

 - tmLanguage (Basically ripped and modified Generic Shell)
 - Build system (clean *forced* makepkg build)
 - Plugin to provide in-app command interface:
    - Namcap PKGBUILD validation - `namcap_check`
    - MD5 generation - `makepkg_gen`
    - Source packaging - `makepkg_src`
    - Package source extraction - `makepkg_ext`
 - Snippets

## Install:
Place PKGBUILD folder in Packages/ dir

## Menu entry sample:
`{caption": "PKGBUILD Tools",
 "mnemonic": "P",
 "children":
     [
         { "caption": "Build Package", "mnemonic": "B", "command": "makepkg" },
         ...
         ...
     ]}`

## Licence
GPL
