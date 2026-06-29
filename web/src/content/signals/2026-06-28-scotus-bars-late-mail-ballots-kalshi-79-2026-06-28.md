---
signal_id: "CMSIG2026062805"
signal_slug: "scotus-bars-late-mail-ballots-kalshi-79-2026-06-28"
headline: "SCOTUS bars late mail ballots: Kalshi 79%"
semantic_title: "SCOTUS mail ballot bar consensus hardens near 80 percent"
telemetry: "Kalshi 79%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-28T23:54:12.000Z"
event_id: "CM-EVT-8NWCS8ZRW8"
event_slug: "kxwatsonrnc"
event_question: "Will the Supreme Court of the United States bar the counting of mail ballots received after Election Day?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXWATSONRNC"
  question_raw: "Will SCOTUS bar counting mail ballots received after Election Day?"
  current_price: 0.79
  volume_24h_usd: 1474.76
  arbitration_model: "kalshi_staff"
  resolution_source: "Supreme Court"
  resolves_at: "2026-08-01T14:00:00Z"
bullets:
  - "Kalshi prices the Supreme Court barring counting of mail ballots received after Election Day at 79%, resolving via Supreme Court."
  - "Lower court blocking of Trump's mail voting order is consistent with a drawn-out legal battle reaching the Supreme Court, where the market prices a likely bar."
  - "The appeals court block on Michigan voter data access adds to a pattern of lower court resistance, but markets price SCOTUS as ultimately siding differently."
  - "No companion contract with a clean price is available to form a spread, but 79% reflects a strong majority conviction on the SCOTUS outcome."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A federal court halted Trump's executive order limiting voting by mail, adding to a string of judicial losses for the administration on election rule changes."
    publisher: "Jonathan Shorman"
    published_at: "2026-06-28T23:54:12.000Z"
    source_url: "https://www.homelandsecuritynewswire.com/dr20260629-trump-order-limiting-voting-by-ma-il-halted-by-federal-court"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jonathan Shorman"
        source_url: "https://www.homelandsecuritynewswire.com/dr20260629-trump-order-limiting-voting-by-ma-il-halted-by-federal-court"
        retrieved_at: "2026-06-29T01:46:24+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via Supreme Court ruling; 79% reflects market belief that lower court blocks precede eventual SCOTUS resolution favoring the bar."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jonathan Shorman: Trump Order Limiting Voting by Ma il Halted by Federal Court  | Homela"
    url: "https://www.homelandsecuritynewswire.com/dr20260629-trump-order-limiting-voting-by-ma-il-halted-by-federal-court"
    published_at: "2026-06-28T23:54:12.000Z"
    retrieved_at: "2026-06-29T01:46:24+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
