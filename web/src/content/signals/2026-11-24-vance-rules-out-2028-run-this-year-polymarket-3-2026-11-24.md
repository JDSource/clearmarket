---
signal_id: "CMSIG2026112408"
signal_slug: "vance-rules-out-2028-run-this-year-polymarket-3-2026-11-24"
headline: "Vance rules out 2028 run this year: Polymarket 3%"
semantic_title: "Vance declining 2028 presidential run this year stays near zero"
telemetry: "Polymarket 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-24T14:53:18.000Z"
event_id: "CM-EVT-Q16SDF41Z3"
event_slug: "vance-announces-he-wont-run-for-president-in-2028-this-year"
event_question: "Will Vance announce he won't run for President in 2028 this year?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x82141371409da1f4b21c5da853ee821c1acbb5c542a52ababc920df9546ec932"
  question_raw: "Vance announces he won't run for President in 2028 this year?"
  current_price: 0.029
  volume_24h_usd: 115.0
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a 3% chance Vance announces he will not run for president in 2028 before year-end 2026, via UMA oracle."
  - "Democrats' midterm sweep elevates the 2028 Republican succession question, but the market sees near-zero chance Vance exits the race this calendar year."
  - "Event CM-EVT-5H09B63413 on who runs for the 2028 Democratic nomination saw trading volume surge 7,229 times day-over-day, the midterm result is drawing intense prediction-market attention to 2028."
  - "Resolution requires a public statement from Vance explicitly declining a 2028 presidential run before December 31, 2026, per UMA oracle."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Post-midterm analysis flags Vice President JD Vance and Secretary of State Marco Rubio as the leading 2028 Republican contenders following Democrats' historic House sweep."
    publisher: "The Hill Staff"
    published_at: "2026-11-24T14:53:18.000Z"
    source_url: "https://thehill.com/homenews/campaign/fight-for-2028/6239407-vance-rubio-newsom-trump-2028-stakes-post-midterms-discussion/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "The Hill Staff"
        source_url: "https://thehill.com/homenews/campaign/fight-for-2028/6239407-vance-rubio-newsom-trump-2028-stakes-post-midterms-discussion/"
        retrieved_at: "2026-11-27T07:47:43+00:00"
  - type: "pm_response"
    notes: "Polymarket holds the Vance-exits-2028 contract at 3%, while Democratic nomination interest is surging in volume terms on the companion event."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "The Hill Staff: Who will the GOP back in 2028? Marco Rubio, JD Vance or someone else?"
    url: "https://thehill.com/homenews/campaign/fight-for-2028/6239407-vance-rubio-newsom-trump-2028-stakes-post-midterms-discussion/"
    published_at: "2026-11-24T14:53:18.000Z"
    retrieved_at: "2026-11-27T07:47:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
