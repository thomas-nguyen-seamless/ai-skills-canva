# 08 - Brand kits, brand templates, bulk runs, and the written token block

Sources merged: official `branded-presentation`, `generate-deck`, `brand-check`, `bulk-create` (canva-sdks, Apache-2.0); social `design-and-templates` / `canva` SCALE; TerminalSkills
(dataset-first, silent unknown fields); design-director pre-flight; live tests (zero kits, zero templates, `autofill-design` not mounted).

## 1. Decide the path

```
brand kit exists AND user wants on-brand? -> 2 (legacy generate-design)
brand TEMPLATE exists AND rows of data? -> 3 (template run) [needs autofill-design]
neither (this account) -> 4 (token block + create-design) <- default here
```

Never auto-select a brand kit, even if exactly one exists: ask once ("dùng brand kit X chứ?"). If none exist say so in one line and continue (resolves the official branded-presentation vs generate-deck contradiction).

## 2. On-brand generation (only legacy `generate-design`)

`create-design` **cannot** apply a brand kit or template. Only `generate-design` takes `brand_kit_id`. Facts from its contract:

- `design_type:"presentation"`, optional `asset_ids` (order = slide order), `brand_kit_id`, `length`: `short` (1-5 slides, **default**), `balanced` (5-15), `comprehensive` (15+). Each extra slide adds significant latency. Set `length` explicitly or you get 1-5 slides.
- It returns **candidates**, not a design: the user picks one, then `create-design-from-candidate { job_id, candidate_id }`, and only then can you edit/export/resize.
- Query format (official): three sections in order. **Presentation Brief** (Title, Topic/Scope 1-2 lines, Key Messages 3-5, Constraints, Style Guide) -> **Narrative Arc** (one paragraph) -> **Slide Plan** (per slide: `Slide N - "Exact Title"`, Goal, Bullets 3-6, Visuals, Data/Inputs, Speaker Notes 2-4 sentences, Asset Hint, Transition). Titles unique and <= 65 chars; no `[TBD]`; label invented numbers "example values".
- Open the query with one line stating total slide count and "standard multi-slide deck, never a poster or single page" (official `classroom-helper`; the generator's failure mode is becoming a document).
- `list-brand-kits` scope error: `Missing scopes: [brandkit:read]` -> reconnect the connector.

## 3. Brand-template runs (rows of data -> many designs)

Blocked here (no templates, `autofill-design` unmounted, autofill may need a paid plan; plan gates vary, treat an empty list as normal). If ever available, keep the loop discipline from official `bulk-create`:

1. Show headers, row count and the first rows. 2. `search-brand-templates { dataset:"non_empty" }`. 3. `get-brand-template-dataset { template_id }` - **never guess field names** (an unknown key is silently ignored and yields empty placeholders; names are case-sensitive). 4. Mapping table (template field | type | column | note); confirm. 5. Call the fill tool **sequentially**, one status line per row (`Row 3/50: ok | failed <reason>`), upload images just before the row that needs them, continue past failures, skip empty rows with a warning. 6. For 50+ rows warn and offer a 3-row test; warn there is **no undo**. 7. Results table `row, status, design_url, error`.

`create-design-from-brand-template { brand_template_id, page_numbers? }` makes a plain copy of a template (no data). Tagging a template for autofill: `create-brand-template-draft` -> transaction (`update_autofill_field`) -> commit -> `publish-brand-template`.

## 4. No kit: write the token block, then hold it constant

Because nothing in Canva stores the user's system, **write it in the plan and enforce it in review** (social `design-and-templates` token spec + design-director gates). Fill this block before generating and paste it into the brief:

```
DECK SYSTEM (Vietnamese coursework, 1920x1080)
Format: 16:9
Typefaces: <= 2 families, set by the generator theme (cannot be changed later); check the first render
Hierarchy: slide title 52 | section/card title 40-44 | body 34-38 | support/caption 30-34 | tag 28 (min)
Colour: ink <hex> on paper <hex>; ONE accent <hex>; one muted grey for support text; contrast >= 4.5:1 (target 7:1)
Grid: margins 130 L/R, title top 76, accent rule top 176 (w 90), content from 290, 8-px spacing step
Focal point: one per slide; Visual path: title -> visual -> caption
Tone/terminology: <approved terms, banned mistranslations>
Archetypes: cover, agenda, definition, three-up, comparison, chain, diagram, quote, summary, sources
```

Influence the generator through the brief, not later edits: say "nền sáng, một màu nhấn xanh navy, sơ đồ phẳng, không ảnh stock, không 3D, không gradient" and name the visual per slide. Verify the first render matches; a mismatch is cheaper to regenerate than to repair.

## 5. Brand check (when a reference exists)

Even without a kit, check a deck against the token block with the official verdicts **On brand / Off brand / Can't verify**: colour, typography, logo (use of the user's art), tone/terminology, consistency. Colour and fonts are **not** in the payload: judge from thumbnails, mark "can't verify" when only a thumbnail is available, and ask the user for hex codes and font names instead of guessing. Hard violations (wrong logo, off-palette accent, a 3rd family) vs soft (spacing drift) are reported separately.

## 6. Brand voice / terminology guard (anti-drift)

From social `brand-profile`: keep a `We say ___, never ___` list. For a doctrinal subject (e.g. Marxist-Leninist philosophy) the list is the **approved terms and exact formulations** from the source (e.g. the three properties: khách quan, kế thừa, phổ biến). The generator paraphrases and has silently swapped terms; `scripts/text_diff.py` is the control, and the list is its input.
