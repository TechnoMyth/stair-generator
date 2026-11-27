"""Copies each engine's user guide from its product repository into this site, so the site and the shipped guides match.

  python sync_docs.py [--unreal PATH] [--unity PATH]

PATH is the guide's folder. The defaults expect the product repositories beside this clone. An engine whose guide isn't
found is skipped, leaving its pages as they are.
"""

import argparse
import os
import shutil

here = os.path.dirname(os.path.abspath(__file__))
parser = argparse.ArgumentParser()
parser.add_argument("--unreal", default=os.path.join(here, "..", "PluginDev", "Plugins", "StairGenerator", "Docs"))
parser.add_argument("--unity", default=os.path.join(here, "..", "..", "Unity", "StairGenerator", "Packages", "com.technomyth.stairgenerator", "Documentation~"))
args = parser.parse_args()

for engine, source in (("unreal", args.unreal), ("unity", args.unity)):
    target = os.path.join(here, "docs", engine)
    if not os.path.isfile(os.path.join(source, "index.md")):
        print(f"{engine}: no guide at {source}, skipped")
        continue
    if os.path.isdir(target):
        shutil.rmtree(target)
    shutil.copytree(source, target)
    # The changelog beside the guide becomes its changelog page, which the Unity package links to
    changelog = os.path.join(source, "..", "CHANGELOG.md")
    if os.path.isfile(changelog):
        shutil.copyfile(changelog, os.path.join(target, "changelog.md"))
    print(f"{engine}: copied {source} to {target}")
