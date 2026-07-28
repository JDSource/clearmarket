---
signal_id: "CMSIG2026072808"
signal_slug: "mcconnell-resigns-before-midterms-kalshi-15-2026-07-28"
headline: "McConnell resigns before midterms: Kalshi 15%"
semantic_title: "McConnell resignation before midterms stays a long shot"
telemetry: "Kalshi 15%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-28T00:00:00.000Z"
event_id: "CM-EVT-DF795XDRC0"
event_slug: "kxretiremm-26"
event_question: "Will Mitch McConnell resign his office before the midterms?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXRETIREMM-26"
  question_raw: "Will Mitch McConnell resign his office early?"
  current_price: 0.15
  volume_24h_usd: 16848.32
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Kalshi prices a 15% chance that Senator Mitch McConnell resigns his Senate office before the midterms."
  - "The health crisis narrative is consistent with a non-trivial but long-shot probability; markets are not pricing resignation as likely."
  - "Companion Kalshi contract CM-EVT-YTTGGKBGT3 prices 65% on the Senate voting on the CLARITY Act before the August recess, a separate legislative deadline at risk."
  - "Resolves via Library of Congress official records; resignation requires a formal filing, distinct from absence due to health."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Senator Mitch McConnell's health crisis was cited as a potential factor threatening a government shutdown as Senate Republicans face pressure to cancel the August recess."
    publisher: "theweek.in"
    published_at: "2026-07-28T00:00:00.000Z"
    source_url: "https://www.theweek.in/news/world/2026/07/28/how-us-senator-mitch-mcconnells-health-crisis-is-threatening-a-government-shutdown.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "theweek.in"
        source_url: "https://www.theweek.in/news/world/2026/07/28/how-us-senator-mitch-mcconnells-health-crisis-is-threatening-a-government-shutdown.html"
        retrieved_at: "2026-07-28T10:30:26+00:00"
  - type: "pm_response"
    notes: "Kalshi binary; the 15% reading suggests the health news has registered some probability uplift but remains well below majority pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "theweek.in: How US Senator Mitch McConnell's health crisis Is threatening a govern"
    url: "https://www.theweek.in/news/world/2026/07/28/how-us-senator-mitch-mcconnells-health-crisis-is-threatening-a-government-shutdown.html"
    published_at: "2026-07-28T00:00:00.000Z"
    retrieved_at: "2026-07-28T10:30:26+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
