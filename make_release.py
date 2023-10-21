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
