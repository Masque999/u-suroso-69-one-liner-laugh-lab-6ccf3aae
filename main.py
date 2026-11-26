import os

LINE = "I was only trying to clean under the bed, and the sock attacked first \u2014 I have the dust, the witnesses, and the lint to prove it."

# The entry must be exactly one line of 1-200 characters, with no
# leading or trailing whitespace and a proper ending.
assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars"
assert "\n" not in LINE
assert LINE == LINE.strip(), "line has leading or trailing whitespace"
assert LINE[-1] in ".!?", "line must end with terminal punctuation"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8") as f:
    f.write(LINE)
