# bamboo-food

Bedrock add-on: food and drinks based on bamboo. 2× bamboo → bamboo sticks, then
three branches — drinks (bamboo water bottle + water + dye → 17 drinks), meals
(`bamboo:burger`, `bamboo:fries`, `bamboo:soup`), desserts (`muffin`, `ice_cream`).
Namespace `bamboo:`. targetVersion 1.21.110.

## Conventions

- All 44 identifiers in `BP/` are `bamboo:*`. `bridge:` does not appear.
- Item and recipe filenames are consistent `snake_case`. Note the `juice`
  typo is preserved in the code as `orange_juice` — leave it, renaming means
  touching recipes, textures and translations.
- `recipes.md` tables list MC colour order with hex values.
- Textures are recoloured from a template with ImageMagick: `#ff0000` is the
  drink colour, `#0000ff` the straw. See `recipes.md` for the command.
- Translations `["en_US", "pl_PL"]`, `languages.json` present in both BP and RP.

## Structure

- `BP/recipes/` — sticks, brewing, juice, food.
- `BP/items/` — `cold/`, `hot/`, `juice/`, `food/`.
- `recipes.md` / `recipes.mc` — crafting tree and 3-phase strategy.
- `docs/` — a single inventory screenshot, no documentation.
- `verify_all.py`, `minecraft_check.py`, `console_utils.py` — validation.

## Known issues

- **`recipes.md` and the code disagree on meal names.** The doc writes
  `bamboo_burger`, the actual identifiers are `bamboo:burger`, `bamboo:fries`,
  `bamboo:soup`. The doc is the one that's wrong.
- The drink count is 17, not 16 (7 cold + 3 hot + 7 juice).
- BP and RP UUIDs are **different and correctly paired** — BP `dependencies[0]`
  points at the RP header. This is the healthy pattern; don't "fix" it into a
  shared UUID.
- `verify_all.py` differs from `books`/`just-clock` only in its docstring — the
  function list is identical.
- `BP/manifest.json` header version `[1,0,209]` vs module `[1,0,201]` — normal,
  the builder only bumps the header.