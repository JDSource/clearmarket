---
signal_id: "CMSIG2026062403"
signal_slug: "iran-war-powers-bill-enacted-by-june-30-polymarket-10-2026-06-24"
headline: "Iran war powers bill enacted by June 30: Polymarket 10%"
semantic_title: "Iran war powers resolution passage odds anchored near zero"
telemetry: "Polymarket 10%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-24T03:50:50.000Z"
event_id: "CM-EVT-KF5S4BY541"
event_slug: "congress-passes-iran-war-powers-resolution-by-june-30"
event_question: "Will Congress pass an Iran war powers resolution by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xcb3c2e94aefd13bb09a72fdf74d44fa7b2ebe437b863e0621831c020bfd4ed4d"
  question_raw: "Congress passes Iran war powers resolution by June 30?"
  current_price: 0.099
  volume_24h_usd: 583.491014
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices congressional passage of an Iran war powers resolution by June 30 at only 10%, despite the Senate vote succeeding."
  - "The market distinguishes a congressional vote from enacted law, Trump's veto threat is the dominant risk the price reflects."
  - "The Senate's rare rebuke of a sitting president is politically significant but the market treats veto override as highly unlikely before month-end."
  - "Resolves via Polymarket uma_oracle; a presidential signature or veto-proof override would be required for a YES resolution."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US Senate joined the House in voting to direct President Trump to halt military action against Iran, but the resolution still faces a presidential veto threat."
    publisher: "Patricia Zengerle, Reuters"
    published_at: "2026-06-24T03:50:50.000Z"
    source_url: "https://www.navytimes.com/news/pentagon-congress/2026/06/24/us-senate-joins-house-in-voting-to-halt-iran-war/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Patricia Zengerle, Reuters"
        source_url: "https://www.navytimes.com/news/pentagon-congress/2026/06/24/us-senate-joins-house-in-voting-to-halt-iran-war/"
        retrieved_at: "2026-06-25T10:38:54+00:00"
  - type: "pm_response"
    notes: "Polymarket at 10% treats the Senate vote as a political signal, not a path to enacted law, given the veto threat."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Patricia Zengerle, Reuters: US Senate joins House in voting to halt Iran war"
    url: "https://www.navytimes.com/news/pentagon-congress/2026/06/24/us-senate-joins-house-in-voting-to-halt-iran-war/"
    published_at: "2026-06-24T03:50:50.000Z"
    retrieved_at: "2026-06-25T10:38:54+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
