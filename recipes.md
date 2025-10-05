# Food Pack - Complete Guide

## Basic Items

- **2 bamboo** → **bamboo sticks**

## Drinks

> Recipe: bamboo sticks + water bucket (in brewing stand) → bamboo water_bottle
> Then: bamboo water_bottle + dye → colored drink

### Texture Generation Commands

```bash
# Example: Generate hot coffee texture
magick drink_hot.png -fuzz 20% -fill "#9D9D97" -opaque "#ff0000" -fuzz 20% -fill "#6B6B6B" -opaque "#0000ff" drink_hot_coffee.png

# Pattern: magick [template] -fuzz 20% -fill "[drink_color]" -opaque "#ff0000" -fuzz 20% -fill "[straw_color]" -opaque "#0000ff" [output_name]
```

### Hot cups

| Color | Hex | Item | Polish | Recipe | Nutrition |
|-------|-----|------|--------|--------|-----------|
| Light gray | #9D9D97 | coffee | kawa | bamboo water_bottle + light gray dye | 2 |
| Gray | #474F52 | tea | herbata | bamboo water_bottle + gray dye | 1 |
| Brown | #835432 | chocolate | czekolada | bamboo water_bottle + brown dye | 4 |

### Cold

| Color | Hex | Item | Polish | Recipe | Nutrition |
|-------|-----|------|--------|--------|-----------|
| Yellow | #FED83D | smoothie | smoothie | bamboo water_bottle + yellow dye | 6 |
| White | #F9FFFE | shake | shake | bamboo water_bottle + white dye | 5 |

### Sparkling

| Color | Hex | Item | Polish | Recipe | Nutrition |
|-------|-----|------|--------|--------|-----------|
| Black | #1D1D21 | cola_zero | cola zero | bamboo water_bottle + black dye | 1 |
| Red | #B02E26 | cola | cola | bamboo water_bottle + red dye + sugar | 3 |
| Cyan | #169C9C | sprite | sprite | bamboo water_bottle + cyan dye + sugar | 2 |
| Light blue | #3AB3DA | soda | soda | bamboo water_bottle + light blue dye | 2 |

### Juice

| Color | Hex | Item | Polish | Recipe | Nutrition |
|-------|-----|------|--------|--------|-----------|
| Orange | #F9801D | orange_juce | pomarańcza | bamboo water_bottle + orange dye | 4 |
| Lime | #80C71F | lemon_juce | cytryna | bamboo water_bottle + lime dye | 3 |
| Green | #5E7C16 | apple_juce | jabłko | bamboo water_bottle + green dye | 4 |
| Blue | #3C44AA | blueberry_juce | borówka | bamboo water_bottle + blue dye | 5 |
| Purple | #8932B8 | grape_juce | winogrono | bamboo water_bottle + purple dye | 4 |
| Magenta | #C74EBD | berry_juce | jagoda | bamboo water_bottle + magenta dye | 4 |
| Pink | #F38BAA | strawberry_juce | truskawka | bamboo water_bottle + pink dye | 4 |

## Food Items

### Meals

| Item | Polish | Recipe | Nutrition |
|------|--------|--------|-----------|
| bamboo_burger | BamBurger | 4 bamboo sticks + bread | 8 |
| bamboo_fries | BamFryty | bamboo sticks (in furnace/smoker/campfire) | 4 |
| bamboo_soup | Bambupa (zupa) | bowl + bamboo stick | 10 |

### Desserts

| Item | Polish | Recipe | Nutrition |
|------|--------|--------|-----------|
| muffin | BamMuffin | wheat + sugar + bamboo stick | 8 |
| ice cream | Bambody (lody) | bamboo stick + ice + stick | 6 |

## Crafting Flow Diagram

```
2x Bamboo
    ↓
Bamboo Sticks
    ↓
┌─────────────────┬─────────────────┬─────────────────┐
│   Water Branch  │   Food Branch   │ Dessert Branch  │
│                 │                 │                 │
│ Water Bucket    │ BamBurger       │ BamMuffin       │
│ + Brewing Stand │ (+ Bread)       │ (+ Wheat+Sugar) │
│        ↓        │                 │                 │
│ Bamboo Water    │ BamFryty        │ Bambody (lody)          │
│ Bottle          │ (Smelting)      │ (+ Ice+Stick)   │
│        ↓        │                 │                 │
│ ┌─────┬─────┬───┼─────┬───────────┼─────────────────┘
│ │Hot  │Cold │Spr│Juce │           │
│ │Drinks│Drinks│kl│     │           │
│ │     │     │   │     │           │
│ │Coffee│Smoothie│Cola│Orange│     │
│ │Tea  │Shake │Sprite│Lemon │     │
│ │Choco│     │Soda │Apple │     │
│ │late │     │     │Blueb.│     │
│ │     │     │     │Grape │     │
│ │     │     │     │Berry │     │
│ │     │     │     │Straw.│     │
└─────┴─────┴───┴─────┴───────────┴─────────────────┘
```

## State Transition Summary

### Phase 1: Material Preparation
- **2x Bamboo** → **Bamboo Sticks**

### Phase 2: Branching
1. **Water Branch**: Bamboo Sticks + Water Bucket (Brewing Stand) → Bamboo Water Bottle
   - **Hot Drinks**: Coffee, Tea, Chocolate
   - **Cold Drinks**: Smoothie, Shake
   - **Sparkling Drinks**: Cola Zero, Cola, Sprite, Soda
   - **Juices**: Orange, Lemon, Apple, Blueberry, Grape, Berry, Strawberry

2. **Food Branch**: Direct crafting from Bamboo Sticks
   - **BamBurger**: + Bread
   - **BamFryty**: Smelting process
   - **Bambupa (zupa)**: + Bowl

3. **Dessert Branch**: Direct crafting from Bamboo Sticks
   - **BamMuffin**: + Wheat + Sugar
   - **Bambody (lody)**: + Ice + Stick

### Phase 3: Consumption
All final products are consumed by the player.

> Ikonki: https://www.svgrepo.com/collection/pixeled-food/
