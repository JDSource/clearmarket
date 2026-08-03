---
signal_id: "CMSIG2026080305"
signal_slug: "blanche-ag-confirmation-kalshi-76-2026-08-03"
headline: "Blanche AG confirmation: Kalshi 76%"
semantic_title: "Todd Blanche Senate confirmation stays favored at 76 percent"
telemetry: "Kalshi 76%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-03T00:00:00.000Z"
event_id: "CM-EVT-NY76DC3G68"
event_slug: "kxagconf-26"
event_question: "Will Todd Blanche be confirmed?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAGCONF-26JUN05-SEP01"
  question_raw: "Will Trump's first announced Attorney General pick be confirmed as Attorney General before Sep 1, 2026?"
  current_price: 0.76
  volume_24h_usd: 16840.63
  arbitration_model: "kalshi_staff"
  resolution_source: "U.S. Senate"
  resolves_at: "2026-09-08T14:00:00Z"
bullets:
  - "Kalshi prices Blanche confirmation at 76%, a clear but not overwhelming majority, resolves via U.S. Senate vote."
  - "Blanche's rescission of the fund was a direct concession to Senators Thom Tillis and John Cornyn, removing the primary stated obstacle to their support."
  - "The companion Kalshi vote-count ladder (CM-EVT-GMWVVJJ4S2) pins implied vote total at 49-50, consistent with a narrow but successful confirmation."
  - "Kalshi resolves via the official U.S. Senate confirmation vote; failure to hold the 50-vote floor would settle the contract NO."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Acting Attorney General Todd Blanche rescinded Trump's $1.8 billion anti-weaponization fund after Republican senators threatened to block his confirmation."
    publisher: "cbsnews.com"
    published_at: "2026-08-03T00:00:00.000Z"
    source_url: "https://www.cbsnews.com/news/todd-blanche-anti-weaponization-fund-order/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "cbsnews.com"
        source_url: "https://www.cbsnews.com/news/todd-blanche-anti-weaponization-fund-order/"
        retrieved_at: "2026-08-03T11:18:40+00:00"
  - type: "pm_response"
    notes: "Kalshi at 76% on confirmation; the vote-count ladder at 49-50 implied votes cross-validates a tight but likely passage scenario."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "cbsnews.com: Acting Attorney General Todd Blanche issues order rescinding \"anti-wea"
    url: "https://www.cbsnews.com/news/todd-blanche-anti-weaponization-fund-order/"
    published_at: "2026-08-03T00:00:00.000Z"
    retrieved_at: "2026-08-03T11:18:40+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
