---
signal_id: "CMSIG2026102502"
signal_slug: "gop-holds-one-congress-chamber-after-midterms-kalshi-65-2026-10-25"
headline: "GOP holds one Congress chamber after midterms: Kalshi 65%"
semantic_title: "Republicans holding at least one chamber stays near 65 percent odds"
telemetry: "Kalshi 65%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-25T00:00:00.000Z"
event_id: "CM-EVT-T5VXKJT451"
event_slug: "kxbalancepowercombo-27feb"
event_question: "Will Republicans control at least one chamber of Congress after the 2026 midterm elections?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBALANCEPOWERCOMBO-27FEB-DD"
  question_raw: "Will House Control be Democratic AND Senate Control be Democratic for Feb 2027?"
  current_price: 0.65
  volume_24h_usd: 36292.1
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi puts 65% odds on Republicans controlling at least one chamber of Congress after the 2026 midterms."
  - "The story ties the Fed hold directly to midterm timing, but the Kalshi contract shows Republicans as clear but not overwhelming favorites."
  - "A companion Kalshi contract puts 75% on Republicans holding more governorships than Democrats, suggesting broader GOP strength at the state level than in Congress."
  - "Resolution depends on certified election results per Bureau of Labor Statistics designation as resolution source, with any contested races potentially delaying settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Fed is expected to hold rates steady at its October meeting, days ahead of the U.S. midterm elections, with political pressure cited as a backdrop."
    publisher: "thenationaltimes.au"
    published_at: "2026-10-25T00:00:00.000Z"
    source_url: "https://www.thenationaltimes.au/Politics/797937-fed-expected-to-hold-rates-steady-days-ahead-of-us-midterms.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "thenationaltimes.au"
        source_url: "https://www.thenationaltimes.au/Politics/797937-fed-expected-to-hold-rates-steady-days-ahead-of-us-midterms.html"
        retrieved_at: "2026-10-25T12:56:07+00:00"
  - type: "pm_response"
    notes: "Kalshi prices a 65% GOP congressional probability, with the governorship contract at 75% showing a cross-market spread that implies more state-level confidence than federal."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "thenationaltimes.au: The National Times - Fed expected to hold rates steady days ahead of U"
    url: "https://www.thenationaltimes.au/Politics/797937-fed-expected-to-hold-rates-steady-days-ahead-of-us-midterms.html"
    published_at: "2026-10-25T00:00:00.000Z"
    retrieved_at: "2026-10-25T12:56:07+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
