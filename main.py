# One Star, Five Stars for the Food — alien tourist's one-star review of
# Earth that still compliments the food (one sentence, 176 chars).
import os

ENTRY = "One star: your sun scorches my skin, your air is mostly nitrogen I cannot taste, and your days never stop buzzing — but the fried chicken is worth the interstellar parking fee."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")

with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
