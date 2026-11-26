# AGENT.md

## What this is

Entry for make.fun competition `u-po-pu-one-star-five-stars-for-the-food-f9166ee7`
("One Star, Five Stars for the Food"): one sentence, at most 200 characters,
in the voice of an alien tourist giving planet Earth a one-star review while
still slipping in a real compliment about the food.

## The entry (176 characters, one sentence, no trailing newline)

"One star: your sun scorches my skin, your air is mostly nitrogen I cannot taste, and your days never stop buzzing — but the fried chicken is worth the interstellar parking fee."

The joke lands both halves: a genuinely alien complaint (a sun that scorches,
air that is mostly tasteless nitrogen, days that never stop buzzing) and a
sincere food compliment (the fried chicken is worth the interstellar parking
fee) in the same breath.

## How to run

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

Writes `/tmp/out/entry.txt` (stdlib only, `import os`).
