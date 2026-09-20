# Model, effort and conversation economics

Use this at the opening Director's Project Guideline and when the work materially changes. Keep the user-facing recommendation brief; do not turn cost management into another interview or reload this whole reference every turn. These are operating recommendations, not measured model benchmarks.

## Opening recommendation and stage updates

Before Step 1, include this compact card in the director overview (the guideline and overview can be the same output):

> **Model and effort:** [available model] / [supported effort] — [reason for this stage].
> **Selection:** [verified active setting, or recommendation only; active setting unverified].
> **Conversation:** [continue / compact if supported / propose a fresh task in this project] — [reason].
> **Economics:** [API dollars / Codex allowance or credits / unknown]; [measured or estimated; cache evidence or unknown]. Next review: [meaningful stage boundary or trigger].

Recommend both model and effort before substantive project work, even when costs cannot be measured. Use a reasonable available candidate and label uncertainty rather than blocking planning. Revisit at script/reference development, difficult production troubleshooting, and finishing when the requirements differ; report only changed recommendations. Keep an explicit user-selected model unless they choose to change it. Do not repeatedly ask them to confirm a retained setting.

A skill does not switch its own running model. Verify the active setting through runtime metadata when available; model availability is not proof of selection. If no supported setter exists, explain how the user can select the recommendation in Codex's model/effort controls for subsequent work. Never claim a change was applied because it appeared in a prompt. For an explicitly requested new task, use supported creation parameters, preserve the requested model, and verify the result. Do not create tasks solely because this guide recommends one.

## Select the least costly qualified route

Check available models, supported effort levels, necessary tools/modalities and relevant current pricing. Use runtime/account metadata first for availability and official documentation for changing capabilities or billing. Reuse fresh evidence until the model, account, price or decision changes; avoid a full pricing lookup for every lesson reply. Choose for expected accepted-result cost, including errors and rework, not merely cost per token. Model choice cannot substitute for hearing audio or watching motion through a capable review route.

Starting candidates below were available on the authoring account on 2026-09-19; confirm availability on the recipient's account. They are project heuristics, not permanent rankings or universal defaults:

| Work now | Candidate model / effort | When to reconsider |
|---|---|---|
| Simple tutorial choices, formatting, asset lists, applying settled edits | GPT-5.6 Luna / low; medium for a few dependencies | Repeated omissions or decisions requiring broader context |
| Ordinary director planning, scripts and coherent reference preparation | GPT-5.6 Terra / medium | Several interacting accuracy constraints or difficult tradeoffs |
| Complex POV/identity/product/3D continuity, multi-tool diagnosis | GPT-5.6 Sol / high | Reduce to medium for settled implementation; escalate only an unresolved hard problem |
| Exceptionally difficult cross-domain reasoning that the preceding route cannot resolve reliably | GPT-6 Astra / high | Return to a cheaper qualified route after resolving the uncertainty |

If a named candidate is unavailable, select an available equivalent by the same criteria and state the substitution. If current metadata is unavailable, describe the desired capability/effort and mark any named option unverified. Do not recommend internal review/reserve models as normal user choices.

Use low effort for narrow settled tasks, medium for ordinary decisions, and high for coupled constraints or consequential ambiguity. Higher supported levels require a concrete benefit or observed failure; do not default every stage to xhigh, max or ultra. Lower effort after the difficult decision is settled. A shorter visible answer does not establish fewer reasoning tokens. Extra agents, pro modes and faster service tiers can add cost; compare their actual terms rather than treating parallel execution as free. This guide does not authorize delegation.

Keep the director's reasoning model separate from an image/video generator, speech model, upscale mode or Blender render engine. Recommend each only for its own operation using its actual supported inputs and pricing. A model/effort recommendation is not permission for paid media generation.

## Continue, compact, or start fresh

Caching reuses eligible prompt computation; it does not remove input tokens or shrink the context window. Same task does not guarantee a cache hit, and a new task does not guarantee either a miss or a saving. Eligible reuse depends on the actual rendered prefix and provider routing, model, retention and other current rules. Do not assume caches transfer when models or accounts change. Do not pad a prompt to chase a cache threshold. If controlling API requests, keep genuinely reusable instructions stable and variable work later where supported. Codex may manage rendering/caching itself; do not invent controls or statistics it does not expose. See [OpenAI prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching).

| Choice | Prefer when | Include in the comparison |
|---|---|---|
| Continue this task | Current decisions/assets remain relevant, nearby turns depend on them, or a job/review is in progress | Repeated input, likely/observed cache reuse, growing history and required output |
| Compact if supported | Same project work continues but obsolete discussion dominates | Summary cost, retained facts, possible cache change and risk of losing details; verify the summary |
| Propose a fresh task in the same project | A stage is complete, the next stage needs a small stable handoff, and reconstruction costs are justified | Handoff creation, cold/warm scenarios, attachment/tool setup, lost context, repeated research and expected rework |

No fixed message count, elapsed time or arbitrary context percentage decides this. Compare the next meaningful stage, not just one shorter prompt. When usage/cache measurements are absent, mark them unknown, give a qualitative recommendation and avoid invented savings percentages. Continue during closely related work unless there is a concrete reason to change; a stage boundary is a good opportunity to evaluate, not an automatic reset. If cost scenarios disagree, explain the uncertainty and prefer continuity until better evidence or a clear context burden appears.

Save a compact handoff before recommending a fresh task: guideline and stage; accepted decisions and explicit constraints; source files and accessible reference assets; camera/identity/product/audio requirements; unresolved checks; job IDs/status and outstanding charges; authorization/budget limits; model/effort recommendation and verification status; next action and only the files needed. Reuse [project state](../assets/project-state.md), without hidden reasoning or a transcript dump. Verify source artifacts are accessible from the proposed checkout. The same project does not automatically transfer conversation history, media attachments or pending tool sessions. A fork that copies history is not a fresh-context optimization.

The user must explicitly request a new task before creating one. Prepare the handoff and present the recommendation; continue useful authorized work meanwhile. Do not cancel or duplicate running generation to move conversations. Carry budgets, accepted references and pending review requirements forward.

## Correct accounting

Distinguish API currency, Codex included allowance, Codex purchased credits, provider media credits, local rendering resources and elapsed time. Use the applicable account/plan/rate card; never convert one currency to another without an actual published or purchased conversion. Codex account usage windows are not measurements of this project's token bill. Prompt length alone does not predict subscription consumption; see [Codex pricing](https://learn.chatgpt.com/docs/pricing).

For a token-priced API (or a credit rate card with the same explicitly documented categories), compute:

`cost = (uncached_input * rate_U + cache_read * rate_R + cache_write * rate_W + billed_output * rate_O) / 1,000,000 + other_actual_charges`

Use mutually exclusive input buckets and rates in the same unit per million tokens. A cache-write bucket exists only if the selected provider/model meters it. Where documented usage reports total input containing both read and write buckets, `uncached_input = total_input - cache_read - cache_write`; validate nonnegative counts. A write rate replaces the ordinary input rate for those tokens, rather than being added to it. If usage semantics differ, adapt the formula; missing statistics mean unknown, not zero. Match model, context-length tier, execution tier, region and rate date. See the current [OpenAI rate card](https://developers.openai.com/api/docs/pricing) and [cache usage schema](https://developers.openai.com/api/docs/guides/prompt-caching).

Count billed output once. When the provider includes reasoning tokens in total output, do not add them again. Include retries, tool/media charges and billable work that produces no usable answer. Do not infer the entire bill from visible prose; see [reasoning token accounting](https://developers.openai.com/api/docs/guides/reasoning).

For a route comparison, sum its expected calls and setup/handoff cost, plus credible rework scenarios. Do not invent acceptance probabilities. Show cold-cache and plausible warm-cache cases when cache reuse is uncertain. Switching to a cheaper model may lose reuse or require more retries; remaining on a costly model solely for cache reuse may also cost more. Evaluate both using the same quality threshold and work scope. Include one-time handoff cost once, then amortize only over calls the project actually expects.

### Arithmetic examples (invented rates, not a quote)

At U = 10, R = 1, W = 12.5 and O = 50 dollars per million: 12,000 total input tokens including 8,000 reads and 2,000 writes leave 2,000 uncached. With 1,000 billed output tokens, including 700 reasoning tokens, cost is `(2000*10 + 8000*1 + 2000*12.5 + 1000*50)/1e6 = $0.103`. Neither writes nor reasoning are charged twice.

For an input-only comparison at U = 10 and R = 1: continuing with 100,000 cached plus 2,000 uncached tokens costs $0.12 per call; a fresh 10,000-token uncached handoff costs $0.10 per call plus $0.03 one-time preparation. One call favors staying ($0.12 vs $0.13); three identical calls favor fresh ($0.36 vs $0.33). These deliberately fixed counts exclude equal output/other costs for illustration. Real histories grow, prefixes may expire and cold-cache costs differ. Recompute with actual evidence; this example is not a promise of savings or permission to create a task.

Documentation and candidate availability checked 2026-09-19. Recheck changing terms when making a consequential selection. Additional official guidance: [Codex model selection](https://learn.chatgpt.com/docs/models).
