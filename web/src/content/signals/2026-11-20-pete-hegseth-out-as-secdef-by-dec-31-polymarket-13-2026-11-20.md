---
signal_id: "CMSIG2026112008"
signal_slug: "pete-hegseth-out-as-secdef-by-dec-31-polymarket-13-2026-11-20"
headline: "Pete Hegseth out as SecDef by Dec 31: Polymarket 13%"
semantic_title: "Hegseth out as Defense Secretary by year-end stays a long shot at 13 percent"
telemetry: "Polymarket 13%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-20T18:39:30.000Z"
event_id: "CM-EVT-JWSH7Q94S8"
event_slug: "pete-hegseth-out-as-secretary-of-defense-by-december-31"
event_question: "Will Pete Hegseth be out as Secretary of Defense by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x0fcfcfc35d71424c0693c717d2e3bc9b8992910835d124d80cd2f01498f1d3dc"
  question_raw: "Pete Hegseth out as Secretary of Defense by December 31?"
  current_price: 0.13
  volume_24h_usd: 16281.612429
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a 13% chance Secretary of Defense Pete Hegseth is out of his role by December 31, resolves via UMA oracle."
  - "The 13% price reflects some market doubt about Hegseth's tenure but falls well short of majority odds, putting his removal firmly in long-shot territory."
  - "The earlier July 31 deadline contract (CM-EVT-4P9HVH2J97) carries no price, so the term structure between the two deadlines cannot be computed from available data."
  - "Trump's approval of Army explosive detonation over environmental objections, as reported alongside the Hegseth coverage, signals an administration comfortable with controversy rather than one trimming cabinet risk."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The Seattle Times roundup of Trump administration political news included ongoing coverage of cabinet stability and environmental controversies."
    publisher: "seattletimes.com"
    published_at: "2026-11-20T18:39:30.000Z"
    source_url: "https://www.seattletimes.com/nation-world/nation-politics/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "seattletimes.com"
        source_url: "https://www.seattletimes.com/nation-world/nation-politics/"
        retrieved_at: "2026-11-21T07:47:41+00:00"
  - type: "pm_response"
    notes: "Polymarket contract on Hegseth's departure resolves via UMA oracle; the 13% is the only priced read on cabinet stability from provided data."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "seattletimes.com: Nation & World Politics | The Seattle Times"
    url: "https://www.seattletimes.com/nation-world/nation-politics/"
    published_at: "2026-11-20T18:39:30.000Z"
    retrieved_at: "2026-11-21T07:47:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
