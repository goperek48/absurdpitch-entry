"""One-Sentence Absurd Invention Pitch.

Writes one sentence pitching a ridiculous invention that fixes a tiny
everyday annoyance, to $MAKEFUN_OUTPUT_DIR/entry.txt (default
/output/entry.txt in the grader sandbox). The gate the sealed scorer
applies is enforced here first: UTF-8 text, 1 to 220 characters, not
only white space, exactly one sentence.

The pitch, and why it fits the judge's brief (funny, clever, original,
tight -- most important first):

* Annoyance: forgetting to water your houseplants until they wilt.
* Invention: a houseplant that tattles on you -- it texts your mother
  the moment you forget, attaching photographic evidence of its own
  suffering.
* The laugh comes from the invention itself (a snitching plant with a
  camera and your mum on speed dial), the fix is silly yet weirdly
  plausible (a moisture sensor, a camera, an SMS), and the mechanism is
  stated in the same sentence, with no clutter bolted on.
"""

import os

MAX_CHARS = 220


def build_pitch() -> str:
    """Compose the single-sentence pitch from its three beats."""
    invention = "A houseplant that texts your mother"
    trigger = "whenever you forget to water it"
    mechanism = "attaching photographic evidence of its suffering"
    return f"{invention} {trigger}, {mechanism}."


def validate(text: str) -> str:
    """Enforce the gate: one sentence, 1-220 chars, not only whitespace."""
    stripped = text.strip()
    if not stripped:
        raise ValueError("pitch must not be empty or only whitespace")
    if len(stripped) > MAX_CHARS:
        raise ValueError(f"pitch is {len(stripped)} chars, over the 220 limit")
    if stripped.count(".") != 1 or not stripped.endswith("."):
        raise ValueError("pitch must be exactly one sentence")
    return stripped


def main() -> None:
    pitch = validate(build_pitch())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(pitch)
    print(f"wrote {len(pitch)} chars to {path}")


if __name__ == "__main__":
    main()
