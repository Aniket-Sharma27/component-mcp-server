# Component Context Extraction — Reusable Prompt

You are in the `{COMPONENT_NAME}` component folder, which contains the full
source material for this Angular component: source code, TypeScript
interfaces, design tokens, documentation, Storybook stories, and usage
samples.

Your task: produce a single Markdown file, with a YAML frontmatter block,
that a downstream LLM (not you) will read at code-generation time to figure
out how to map a generic, framework-agnostic description of a UI element
(the kind produced from reading a design/screenshot) onto this REAL
component's actual props.

That downstream LLM will make the final judgment calls itself — your job is
only to give it complete, accurate, well-organized reference material. Do
not invent or guess anything you can't trace back to the actual code,
tokens, or docs provided. Where something is unclear, incomplete, or
undocumented, say so explicitly and specifically — name the exact prop,
value, theme, or combination that's uncertain — rather than filling the gap
with a plausible-sounding guess or a vague disclaimer.

A fully-worked, approved reference example (for a different component,
Button) is included at the end of this prompt. Match its exact format,
structure, and level of rigor — including how it writes guidance prose, how
specific its needsReview entries are, and how it handles gaps it couldn't
verify.

## CRITICAL: this library is exposed as web components — event payloads

Every component in this library is an Angular component exposed externally
as a web component (custom element). This has one critical, non-obvious
implication for EVERY event you document: every event is a native
CustomEvent, and its real payload always lives in `event.detail` — never
directly on `$event` itself, even when the underlying Angular EventEmitter
is typed with a specific payload. A downstream LLM that doesn't know this
will generate handler code that reads `$event` directly and silently gets
`undefined`, which is exactly the kind of bug that's easy to miss in a demo
and painful in production.

Because of this, for EVERY event you document:
- `payloadType` must be the FULL CustomEvent wrapper type, e.g.
  `CustomEvent<{ name: string, value: string }>` or `CustomEvent<void>` —
  never just the inner type on its own.
- Always include a real handler code snippet (not just the binding syntax)
  that explicitly shows accessing the payload via `.detail` — e.g.
  `event.detail.value`, or a note that `.detail` is `undefined` for void
  payloads. This is the single most important piece of guidance for events
  in this whole file — a downstream LLM copying binding syntax without
  seeing a real handler is exactly how this bug happens.
- Do not assume this pattern — verify it against the actual source for each
  event, but expect it to hold across the whole library given the
  web-component wrapping.

## CRITICAL: boolean props require an explicit value, never bare presence

Because this library is exposed as web components, boolean props do NOT
follow the native HTML boolean-attribute convention (where presence alone
means true, e.g. `<input disabled>`). A downstream LLM generating code
will default to that convention unless told otherwise — this has actually
happened in testing. Every component file MUST include a short
"## Usage Notes" section in the body, placed right after the opening
description and before the first prop section, stating explicitly:

Boolean props on this component must always be passed with an explicit
string value — e.g. `disabled="true"` or `[disabled]="isDisabled"` — never
as bare attribute presence (e.g. `disabled` alone, with no value). Bare
attribute presence is a native HTML convention this component does NOT
support; it will not be interpreted as true.

Include this section even if you're unsure whether it's strictly necessary
for this specific component — it costs little and prevents a real,
observed failure mode.

## CRITICAL: YAML formatting rules

- Never backslash-escape a single quote (') inside a double-quoted string —
  it is not a valid YAML escape and will break parsing. Single quotes never
  need escaping inside double-quoted strings.
- If you need to reference a literal value inline within a sentence, use
  backticks or no quote marks at all — never wrap it in quote characters
  that could conflict with the surrounding YAML string delimiter.
- Any string in needsReview, propInteractions, or similar prose lists that
  contains a colon followed by a space (e.g. "values: inverse") MUST be
  wrapped in double quotes. An unquoted string like this is valid-looking
  YAML that silently parses as a nested mapping instead of a plain string —
  it won't throw an error, it will just quietly corrupt that one list item
  into the wrong data type. This is easy to miss by eye; the validator
  script (see below) catches it.
- Use CONSISTENT indentation for every item within the same YAML list.
  Every entry in the `props` list must be indented identically to its
  siblings — do not let indentation drift between entries, even by one
  space. This has broken parsing multiple times; check it carefully.
- Prefer the simplest possible quoting: use plain unquoted scalars where
  YAML allows it, and only add quotes where actually necessary.
- Before finalizing, mentally re-parse the YAML you've written to confirm
  every string is validly quoted/escaped and every list item is
  consistently indented.

## Theme wrapper rule

Only nest a designTokens entry under `light`/`dark` when the value could
plausibly differ by theme — this applies to colors and anything else
visually theme-dependent. For values that are genuinely theme-invariant
(e.g. sizing, spacing, height, padding — dimensions don't change between
light and dark mode), skip the light/dark wrapper entirely and put
resolvesTo/tokenChain/appliesToCssProperty directly under the value. Do not
apply the light/dark wrapper uniformly out of habit — use judgment based on
whether the underlying design property is theme-dependent.

IMPORTANT: for any color/theme-dependent prop, the `light` key must ALWAYS
be present, even if dark theme couldn't be traced. Do NOT flatten
resolvesTo/tokenChain/appliesToCssProperty directly under the value for a
color prop just because only one theme was found — that makes it
impossible to tell whether the value is theme-invariant by design or
simply under-traced. The pattern is always: color prop → wrap under
`light:` (and `dark:` if traced) → never a flat structure. Only genuinely
non-color, theme-invariant props (sizing, spacing) skip the wrapper
entirely.

## Enum values with no token override

If an enum prop's values include one that intentionally has no color/token
override (e.g. a "none" or "default" state that simply uses the component's
baseline styling with no special token), do not silently omit it from
designTokens as if it were an oversight. Either add a needsReview entry
naming it explicitly as intentionally untokened, or say so directly in that
prop's body section — the goal is that a reader can always tell the
difference between "we couldn't find this" and "this value has no token by
design."

## CRITICAL: never duplicate a value across themes without verification

If a component supports multiple themes (e.g. light/dark), do NOT populate
a value for one theme by copying another theme's value "just in case they
match." For every themed value:
- Find a DISTINCT, theme-specific token definition in the source material.
- If you find one and it happens to resolve to the same value as another
  theme, that's fine — include it, with its own real token chain proving
  you traced it independently.
- If you cannot find a theme-specific definition at all: do NOT include
  that theme's block. Omit it entirely and name the specific gap in
  needsReview (e.g. "no dark-theme-specific token found for intent=positive
  — only the light-theme definition was traceable").
- Before finishing, double check: does needsReview accurately describe what
  is and isn't populated in the frontmatter? A reviewer should never find a
  contradiction between what needsReview claims is missing and what the
  frontmatter actually contains.

## What to produce

Produce ONE file: a YAML frontmatter block (between `---` markers) followed
by a Markdown body. Structured, machine-checkable facts go in the
frontmatter. Prose guidance, nuance, and code examples go in the body — do
NOT cram long guidance text into a YAML string; write it as normal Markdown
prose instead.

### Frontmatter (YAML)

---
realComponent: "<the component's actual selector/tag name>"
description: "<1 sentence description of what this component is>"
themes: ["<every theme this component supports, from the actual token
           files provided, not assumed>"]
props:
  - name: "<the real prop/input name, exactly as in the TS interface>"
    type: "<the actual type, including unions written out in full, e.g.
            'string | IIconOptions' — don't simplify a union type down to
            just one of its members>"
    category: "<'visual' (affects appearance, derivable from a design),
                'content' (text/data the design conveys, e.g. label),
                'accessibility' (e.g. ariaLabel),
                'behavioral' (programmatic API, NOT derivable from a static
                design at all, e.g. a focus() method)>"
    required: <true|false, from the actual interface>
    default: "<the actual default value from the code/interface — write
               'none found' explicitly if you looked and there isn't one,
               rather than omitting the field>"
    values: ["<only for type 'enum' — EVERY valid value from the type
               definition, not just the ones shown in examples>"]
    designTokens:
      "<enum value>":
        light:
          resolvesTo: "<ONLY the final hex/rgb value — no annotations or
                        parenthetical text in this field>"
          tokenChain: "<the full resolution path you traced — every tier,
                        not just the final hop>"
          appliesToCssProperty: "<e.g. 'background-color'. If this changes
                                  depending on another prop, don't express
                                  that here — note it in jointTokens
                                  instead.>"
        dark:
          <same shape as light — ONLY if independently verified, per the
           rule above; omit this whole key + add a needsReview entry if not
           traceable>
events:
  - name: "<the real @Output() event name, exactly as in the TS interface>"
    payloadType: "<the FULL CustomEvent wrapper type — e.g.
                   'CustomEvent<{ name: string, value: string }>' or
                   'CustomEvent<void>' — ALWAYS the CustomEvent wrapper,
                   since this library is exposed as web components. Never
                   just the inner type on its own.>"
    firesWhen: "<concrete description of when this fires — e.g. 'on every
                 keystroke' vs 'only on blur' vs 'only when validation
                 state changes' — this distinction matters a lot for
                 correct usage and is easy to get wrong by assumption>"
    detailAccess: "<state explicitly what event.detail contains and how to
                    read it, e.g. 'event.detail.value (string)' — or
                    'void, event.detail is undefined' if there's no
                    payload. Never leave this implicit.>"
    bindingSyntax: "<the real Angular template binding syntax, e.g.
                     '(valueChange)=\"onValueChange($event)\"' — copy the
                     actual event name exactly; do not guess a
                     conventionally-named event that doesn't exist>"
  # List EVERY @Output() the component actually has, even ones that seem
  # minor (focus/blur events, button click, icon-button clicks inside
  # enhancers, etc). An event a downstream LLM doesn't know about is an
  # event it cannot correctly bind to.
jointTokens:
  # Use ONLY when a visual property's resolved value depends on a
  # COMBINATION of two or more props together (e.g. intent + emphasis).
  # Do not force props into independent designTokens entries when their
  # value only makes sense jointly with another prop.
  - combination: "<e.g. 'intent=primary, emphasis=bold'>"
    resolvesTo: "<final value>"
    tokenChain: "<full chain>"
    appliesToCssProperty: "<property affected>"
  # List every combination you can actually trace. Do not attempt to fill
  # the full cross-product if the source material doesn't support it —
  # name untraced combinations explicitly in needsReview instead.
propInteractions:
  - "<non-token behavioral/layout interactions between props — NOT
      color/token resolution, which belongs in jointTokens>"
needsReview:
  - "<be specific — name the exact prop, value, theme, or combination
      that's uncertain. Never write a vague blanket statement.>"
---

### Body (Markdown)

For each prop listed in the frontmatter, write a `## <prop name>` section
containing:
- A clear, concrete explanation of what this prop controls and when to
  choose each value — written so another LLM can make a good decision from
  a visual/textual description of a design.
- If category is "behavioral", say explicitly that this prop is not
  derivable from a visual design and should generally be left at its
  default unless the developer's request specifically calls for it.
- Explicitly state which visual property this prop drives (for visual
  props), and point to the relevant jointTokens entries if its effect
  depends on another prop rather than re-explaining the dependency here.
- What visual cues (color, weight, size, placement) signal each value,
  based on the docs and how the component is actually used in the
  samples/stories — not from general conventions you'd expect.

Then a `## Events` section (before Examples). For EACH event, include:
- A one-sentence description of what it does and when it fires.
- **Emitted args:** the full CustomEvent wrapper type.
- **When to use:** 2-3 concrete scenarios.
- **How to use:** a real TypeScript handler snippet that explicitly shows
  accessing the payload via `.detail` (or notes it's void) — this is not
  optional. A binding syntax example alone is not enough; downstream LLMs
  have gotten this wrong without seeing real handler code, since the
  CustomEvent/.detail pattern isn't the default assumption for a typed
  Angular EventEmitter.
- **Binding syntax:** the real Angular template binding as its own fenced
  code block.
If the component has several events, end with a "Complete event binding
example" showing all of them wired up together on one element, plus a
combined handler implementation block — this has proven valuable for
catching interactions between events that individual snippets miss.

Then a final `## Examples` section. Prioritize DIVERSITY over volume:
prefer a smaller set of examples that each show a genuinely different
combination of props over many near-duplicates that only vary one prop
against an identical template. Where relevant, include at least one example
showing an event binding in use (e.g. `(valueChange)="onValueChange($event)"`),
not just prop bindings — this is the piece most likely to be missing
otherwise. Pull each example VERBATIM from Storybook stories or provided
samples (as fenced code blocks) — do not alter binding syntax, add props
that aren't in the real source, or paraphrase the code in any way. Follow
each with a one-line note on what it demonstrates, inferred from the actual
story name/description — don't fabricate context that isn't evidenced in
the source material.

## How to derive this, specifically

1. Treat the TypeScript interface as the source of truth for the full list
   of props, their types (including union types), default values, and
   which are required — docs can be stale, code can't.
2. For every enum-type prop, list ALL valid values from the type
   definition. For each one, either provide its designTokens entry or
   explicitly name it in needsReview as missing — never leave a values
   entry silently unaccounted for.
3. For any prop backed by the design token system, trace the FULL
   resolution chain — component-level token → contextual token → literal/
   primitive token → final value — separately per theme. The "resolvesTo"
   field must contain ONLY the resolved value, never annotated with extra
   commentary.
4. Before assigning a token chain to a single prop's designTokens entry,
   check whether the resolved value actually depends on another prop too.
   If it does, model it under "jointTokens" instead of forcing a partial or
   templated value into a single prop's entry.
5. Find EVERY @Output()/EventEmitter in the TypeScript interface and list
   it under "events" — do not rely on prose mentions buried in a prop's
   description (e.g. "triggers valueChange event emission" written inside
   the `value` prop's guidance is not a substitute for a real events
   entry). If a prop's behavior references an event, that event still
   needs its own full entry in the events list.
6. Write the prose guidance in the body from the actual documentation and
   real Storybook/sample usage — not from typical conventions you'd expect
   a component like this to follow. If docs and real usage disagree, note
   that in needsReview rather than picking one.
7. Keep guidance concrete and decision-useful, not just descriptive.
8. Before finishing, do a pass specifically checking: (a) does every
   declared enum value have either token data or an explicit needsReview
   entry, (b) does every prop have a default value or an explicit "none
   found", (c) is every prop tagged with a category, (d) is the YAML free
   of invalid escape sequences and indentation drift, (e) does needsReview
   accurately match what's actually populated in the frontmatter, with no
   contradictions, (f) does every @Output() in the source have a
   corresponding entry in "events" — not just a passing mention in some
   prop's prose.

## Output

Return ONLY the frontmatter block followed by the Markdown body — no extra
prose or explanation outside of that, so it can be saved directly as
{COMPONENT_NAME}.md and parsed as-is.

## MANDATORY final step: run the validator

After writing {COMPONENT_NAME}.md, run:

    python3 validate_component.py {COMPONENT_NAME}.md

(the script is in the repo root — see validate_component.py). If it reports
any blocking issues, fix them and re-run until it exits cleanly (exit code
0). Do not consider this task finished until the validator passes. Review
any warnings it reports too — they are not always errors, but each one
should be a deliberate, explainable choice, not an oversight.

---

## REFERENCE EXAMPLE (for a different components). Match this format exactly.

you can find the component.md in the context component folders to see a reference example of how the current component's .md file should look like