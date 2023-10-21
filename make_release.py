#
# make_release.py
#
#  This script is used to create a new github release (well, to prep for it --
#   some manual action is needed ...)
#
#  Update and checkin files as usual.
#
#  Decide on the new version (see 'version' in system.json, roll up as appropriate)
#  Invoke this file as:
#    python make_release.py <new version>
#
#  This will update system.json (including path to downloads and manifest),
#   delete the old zip file, and create the new zip file (with updated manifest)
#
#  It also adds, commits, and tags with the new version.
#
#  MANUAL ACTIONS REQUIRED:
#    1) using the command line printed out (git push -u origin <version name>) to push WITH TAG to github
#    2) On github (https://github.com/paulbennett3/fvtt-beyond-the-wall/releases), "Draft a new release"
#         - make sure to pick the correct tag (the new version)
#         - pick the correct branch (currently "ga")
#         - drag and drop the new beyond-the-wall.zip and system.json to the "binaries" area
#         - publish the release
#    3) On the release page (you can navigate their via the "latest" link), copy the link address
#        of the system.json file
#    4) In foundry setup, install the new system, pasting the link to system.json you copied above
#    5) Viola! Profit!
#
#


import json
import os
import sys



def main(new_version):
    manifest = 'system.json'
    zipfile = 'beyond-the-wall.zip'

    # update system.json
    with open(manifest) as infile:
        sj = json.load(infile)

    old_version = sj["version"]
    sj["version"] = new_version
    sj["manifest"] = sj["manifest"].replace(old_version, new_version)
    sj["download"] = sj["download"].replace(old_version, new_version)

    with open(manifest, 'wt') as out:
        json.dump(sj, out, indent=4)

    os.unlink(zipfile)
    os.system('zip -r %s *' % zipfile)
    os.system('git add %s' % manifest)
    os.system('git commit -m "making release %s"' % new_version)
    os.system('git tag -a %s -m "release version %s"' % (new_version, new_version))
    print('MANUALLY PUSH TO github using:\n')
    print('  git push -u origin %s' % new_version)
    print('')
    print('Then on github, draft a new release, pick the correct branch ("ga"), tag: %s, drag and drop %s and %s' % (new_version, manifest, zipfile))
    print('Then once released, cut and paste address of system.json from the release into the install path in foundry system install')


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print("ERROR! specify new version on command line")
