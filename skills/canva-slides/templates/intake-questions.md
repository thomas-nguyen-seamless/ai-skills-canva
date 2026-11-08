# Intake questions - ask BEFORE building (never guess the look)

Ask **4-6 at a time**, each with a default, so the user can answer "mặc định" / "default". Derive the
question from the content the user already gave (a law needs a cycle/chain/spiral decision; history needs
a timeline; a data claim needs the real numbers). Never re-ask what the source, the brief or the existing
deck already answers. Write the answers into `plan.json` under `design` **before** any build step.

Generate a tailored set:

```sh
python3 scripts/intake_prompt.py --topic "quy luật phủ định của phủ định" --source textbook --minutes 15 --slides 20
python3 scripts/intake_prompt.py --topic "microservices architecture" --lang en
```

## A. Must know (cannot build without)

1. Purpose: class talk, defence, internal report, or self-reading document?
2. Audience: which year, who grades, what do they already know?
3. Speaking time in minutes and the target slide count?
4. Required source (textbook/PDF): must the wording be verbatim?
5. Deliverable: slides only, or notes + Q&A + print version?
6. Language and register: academic, presentation, casual?

## B. Format and look (ask explicitly, offer the default)

| Dimension | Question | Default |
|---|---|---|
| Ground and colour | Light `#F7F8FA` or dark navy? Brand colours/logo from the school or faculty? | light + one blue accent |
| Density | Sparse (presenter, <=25 words/slide), medium (talk, <=40), detailed (document, <=75)? | talk |
| Visual language | Engraving/illustration, flat vector, photography, diagrams only, minimal? | native diagrams + one engraving |
| Type | Modern sans (Arial/Inter) or academic serif? Lecture-hall size or screen reading? | sans, body 34-38 px on 1920x1080 |
| Layout | Equal card grid, two columns, horizontal timeline, full-bleed image? Agenda slide? | card grid + agenda |
| Imagery | Your own photos, AI art, public domain, or none? Any image that must appear? | user/AI art for cover + illustration, no stock |
| Examples | How many, from which domains (nature, society, thought, computing)? Any mandatory case? | 3-4 across domains |
| Citations | Verbatim source wording or paraphrase? Page numbers required? | verbatim + page numbers |
| Special slides | Agenda, review questions, thanks, presenter name and date? | agenda + summary + thanks |
| Constraints | Min/max slides, 16:9, printable A4, PDF sent ahead? | 16:9, PDF alongside |
| Hard bans | What must never be wrong (terms, numbers, order of reasoning)? | course terminology |

Non-negotiables that are **not** questions (state them, do not ask): no emoji anywhere, no accent rule under
titles, no stock clichés, no text baked into images, large type for a classroom.

## C. Questions derived from the topic

| If the topic is about | Ask |
|---|---|
| a law, principle, mechanism | straight chain, closed cycle, or spiral for the mechanism? one diagram per step or one overview? compare with the other laws in the chapter? |
| philosophy, a concept, a category | verbatim textbook wording or paraphrase? keep exactly the listed features or add from other sources (and label them)? examples inside the textbook, outside, or both? |
| history, periods | year timeline or grouped periods? which dates must never be wrong? map or geographic context? |
| a comparison | how many columns and which criteria? conclusion as the last table row or its own slide? |
| a process, steps, pipeline | number the steps or unnumbered arrows? any branch/condition to draw? |
| numbers, metrics, money | source of the numbers, rounding allowed? table, bars, or one big number per slide? which are real vs illustrative? |
| biology, a life cycle | closed loop or open chain? real photos per stage or diagrams only? |
| architecture, systems, network | layered blocks or data flow? annotate specific technologies/versions? |

## D. After the answers

Record them in `plan.json`:

```json
"design": {
  "theme": "light #F7F8FA, one accent #1F5FA8, ink #0F2A43",
  "density": "talk",
  "visual_language": "native diagrams + one engraving band",
  "imagery": "user/AI engravings only, no stock",
  "typography": "Arial, body 34-38 px, titles 52-60 px",
  "examples": "3-4 across nature/society/thought",
  "citations": "verbatim + page numbers",
  "special_slides": "agenda, summary, review questions, thanks",
  "constraints": "20 slides, 16:9, PDF alongside"
}
```

`plan_check.py` warns while this block is missing, and the first build waits for it.
