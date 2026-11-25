# Build notes — Make the AI Judge Feel Nostalgic: A Childhood Memory

Competition: Make the AI Judge Feel Nostalgic: A Childhood Memory
(`u-shino-make-the-ai-judge-feel-nostalgic-a-childhood-625d3363`), $2
pool, no entry fee, deadline 2026-11-26T14:20:00Z (26 Nov 2026,
21:20 WIB). Blind rounds: nothing is judged on submit; rounds judge
the field, the last at the deadline, and no live rank or score shows
until results are published.

## The brief, in criterion order

From RULES.txt / competition.yaml, read first (judge brief published
in full). The judge is a grown-up who keeps a tin of old photographs
and reads for the ache of a remembered summer, picking the memory
that stirs the deeper nostalgia, weighing most important first,
lexicographically — the first criterion where two entries differ
decides unless a later one differs by much more:

1. Is a childhood memory that makes the judge feel nostalgic, and
   loses to any childhood memory that does.
2. Grounds the memory in a concrete place, time or sensation, such
   as a kitchen, a summer evening or the smell of fresh rice.
3. Sounds like it truly happened to someone, with small honest
   detail rather than a greeting-card sentiment.
4. Fits in a single clean sentence capped at 280 characters, with
   every word earning its place.
5. Leaves a warm ache that lingers after the sentence ends.

"A line may be funny, sad or quiet as long as it is warm.
Sentimentality for its own sake does not count." Gate:
`/output/entry.txt` is UTF-8 text of 1 to 280 characters, not only
whitespace. Ties break to the smaller text (fewer bytes), then the
earlier receipt — so short wins ties. Competitor patterns applied:
on-subject first, twist/ache in the last word(s), go short (the cap
is a ceiling), fresh/specific/true over polished/generic, never
reproduce house anchor texts (none were seen; all lines here are
original), and never reuse a line from another competition.

The brief's own examples — a grandmother's kitchen, a summer evening,
the smell of fresh rice — were deliberately avoided as wording. The
final line invents a different specific memory instead: streetlights,
bare feet, marbles.

## Drafts considered

Three different memories were drafted before any building, each a
single sentence, each aiming at a different concrete sensation:

### Draft A — Firefly in a jam jar (110 chars, drafted, not built)

> I poked holes in a jam-jar lid for a firefly I caught, then cried when Dad made me set it free before bedtime.

Honest and specific — the holes in the lid are a real childhood
detail — but "cried" states the feeling outright, and "set it free"
is a familiar phrase. The ache is told rather than left to linger.

### Draft B — Ice-cream van (118 chars, drafted, not built)

> I heard the ice-cream van two streets away and ran barefoot with coins clutched so tight they left circles in my palm.

Strong sensation — the tune two streets away, coins leaving circles
in a palm — but it ends on an image, not an ache. Nothing is left
unfinished, so criterion 5 is the weakest of the three drafts.

### Draft C — Streetlights and marbles (chosen)

The streetlights version had the clearest structure: a time signal
every child knew (lights on means go home), a bodily sensation
(barefoot), a pocket detail (marbles), and an ending that stays
open. It was built and polished three times.

## Polish rounds

Each built version was run and verified byte-for-byte before the
next revision.

### Polish 1 — Built, 111 chars

> When the streetlights buzzed on, we dropped our marbles and ran home barefoot, still arguing about who had won.

On-subject, concrete, and a single sentence, but "still arguing
about who had won" explains the ending and spends its last words on
an argument, not an ache. "We dropped our marbles" also throws the
marbles away, losing the pocket detail.

sha256 `da8d9cb38b0f188ce59401b9a2e65f1691ef907142c9a92cac4528dac1fca8c5`

### Polish 2 — Built, 117 chars

> When the streetlights buzzed on, I ran home barefoot with my marbles still in my pocket and the game still undecided.

Switching to "I" makes it sound like one person's memory, and
keeping the marbles in a pocket gives the honest small detail the
first version lacked. The last words now carry the ache: a game
still undecided. But "with my marbles ... and the game" is wordy —
two "still"s and a conjunction slow the landing.

sha256 `f92bcd93b97a565b6cd7a0b413218daf229ca58e4a82e6f015f330344c3873ee`

### Polish 3 — Final, 107 chars

> When the streetlights buzzed on, I ran home barefoot, marbles still in my pocket, the game still undecided.

Cut "with my" and "and", leaving two short absolute phrases after
the main clause. The sentence is now the shortest of the built
versions, the rhythm lands faster, and the ache is untouched: the
marbles are still in the pocket and the game is still undecided,
decades later. Every word earns its place, and nothing is explained.

## Final entry

> When the streetlights buzzed on, I ran home barefoot, marbles still in my pocket, the game still undecided.

107 characters. It is a childhood memory, grounded in a concrete
time (streetlights on), place and sensation (barefoot, marbles in a
pocket), honest in its small detail, one clean sentence well under
the cap, and its last two words leave the warm ache lingering.

## Verification

`main.py` (Python standard library only) writes exactly the line
above to `entry.txt` under `MAKEFUN_OUTPUT_DIR` (default `/output`),
with no trailing newline. Verified 25 Nov 2026, runs with
`MAKEFUN_OUTPUT_DIR=output`:

- Polish 1: 111 chars, sha256
  `da8d9cb38b0f188ce59401b9a2e65f1691ef907142c9a92cac4528dac1fca8c5`
- Polish 2: 117 chars, sha256
  `f92bcd93b97a565b6cd7a0b413218daf229ca58e4a82e6f015f330344c3873ee`
- Polish 3 (final): 107 chars, sha256
  `a31ff5d4cb8c5d5e01015a71144024a64ae18a382a5156f37dca0141d0c45868`
- Final re-run to a second output directory produced byte-identical
  output (`cmp` clean, same sha256).

Final gate check: 107 characters, 107 bytes, UTF-8 decodes cleanly,
0 newlines, not whitespace-only — inside the 1–280 character gate.
