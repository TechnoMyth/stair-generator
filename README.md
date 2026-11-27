# Stair Generator docs

The public documentation for Stair Generator, to be published at https://docs.technomyth.com/stair-generator/. Bug
reports and questions for every engine go in this repository's
[issues](https://github.com/TechnoMyth/stair-generator/issues), labelled by engine.

The Unity package's `package.json` links here with `documentationUrl` and `changelogUrl`.

The Unreal guide is copied in by `sync_docs.py` but kept out of the site by `.gitignore` until the plugin is
released. Then remove that line and add the guide to the `nav` in `mkdocs.yml`.

The site is organised by engine, under one landing page (`docs/index.md`):

| Engine | Pages | Guide written in |
|---|---|---|
| Unity | `docs/unity/`, at `/stair-generator/unity/` | The package, at `Packages/com.technomyth.stairgenerator/Documentation~` in the Unity StairGenerator repository |
| Unreal Engine | `docs/unreal/`, at `/stair-generator/unreal/` (when the plugin exists) | The plugin, at `Plugins/StairGenerator/Docs` in the PluginDev repository |

Each guide ships with its product; this repository adds the site around copies of them. The shipped products link to
their engine's page (the Unity package's help links and, once published, its `documentationUrl` use `https://docs.technomyth.com/stair-generator/unity/`),
so those paths must not change. Another engine gets its own folder and a line in `sync_docs.py`.

## Updating

1. Edit the guide in its product repository.
2. Run `python sync_docs.py` to copy the guides in. It expects the product repositories beside this clone
   (`../PluginDev` and `../../Unity/StairGenerator`), skips any it can't find, and takes `--unreal` and `--unity`
   paths otherwise. Add the Unreal guide to the `nav` in `mkdocs.yml` when it is first published.
3. Commit and push to `main`. `.github/workflows/publish.yml` builds the site with MkDocs Material and pushes it to
   the `gh-pages` branch, which Pages serves.

To preview locally: `pip install mkdocs-material`, then `mkdocs serve`.

## How it is hosted

The same way as the Gear Generator docs (`gear-generator-docs` beside this clone):

- **This repository:** Settings > Pages deploys from the `gh-pages` branch. As a project site it takes the
  organization site's domain, so it appears under `/stair-generator/`, with each engine below that.
- **Organization site:** `TechnoMyth/technomyth.github.io` holds the index page listing the plugins and has the custom
  domain `docs.technomyth.com`. Add Stair Generator to its index page when this site is first published.
- **DNS and HTTPS:** handled for the whole domain by Cloudflare (see the Gear Generator docs README); nothing to do
  per product.
