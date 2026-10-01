---
signal_id: "CMSIG2026092906"
signal_slug: "republicans-hold-one-chamber-after-midterms-kalshi-61-2026-09-29"
headline: "Republicans hold one chamber after midterms: Kalshi 61%"
semantic_title: "Republican chamber control odds stay near 60% despite poll drag"
telemetry: "Kalshi 61%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-29T00:00:00.000Z"
event_id: "CM-EVT-T5VXKJT451"
event_slug: "kxbalancepowercombo-27feb"
event_question: "Will Republicans control at least one chamber of Congress after the 2026 midterm elections?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBALANCEPOWERCOMBO-27FEB-DD"
  question_raw: "Will House Control be Democratic AND Senate Control be Democratic for Feb 2027?"
  current_price: 0.61
  volume_24h_usd: 23089.24
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices Republican control of at least one chamber at 61%, remaining modestly favored despite the reported polling headwinds."
  - "Polling showing a Democratic enthusiasm boost has not driven the Kalshi contract below 50%, so the market does not yet see a Democratic sweep as the base case."
  - "Polymarket's NC-04 House contract (CM-EVT-NWW6JR41T9) sits at 96% for the Democratic candidate, showing strong race-level pricing in a key district."
  - "Resolution requires Library of Congress certification; the gap between 61% chamber-level and 96% district-level pricing reflects House-vs-Senate split scenarios."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Polls found that Trump's midterm convention boosted Democratic enthusiasm, with roughly seven in ten voters citing Trump as a factor in their vote."
    publisher: "independent.co.uk"
    published_at: "2026-09-29T00:00:00.000Z"
    source_url: "https://www.independent.co.uk/news/world/americas/us-politics/trump-midterm-convention-democrats-lead-republicans-b3058286.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "independent.co.uk"
        source_url: "https://www.independent.co.uk/news/world/americas/us-politics/trump-midterm-convention-democrats-lead-republicans-b3058286.html"
        retrieved_at: "2026-10-01T07:47:27+00:00"
  - type: "pm_response"
    notes: "Kalshi holds near 61% on overall Republican chamber control; individual district Polymarket contracts show more decisive race-level pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "independent.co.uk: Trump held a midterm convention to rally Republican voters - but Democ"
    url: "https://www.independent.co.uk/news/world/americas/us-politics/trump-midterm-convention-democrats-lead-republicans-b3058286.html"
    published_at: "2026-09-29T00:00:00.000Z"
    retrieved_at: "2026-10-01T07:47:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
