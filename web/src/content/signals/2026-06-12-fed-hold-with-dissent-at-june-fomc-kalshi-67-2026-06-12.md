---
signal_id: "CMSIG2026061206"
signal_slug: "fed-hold-with-dissent-at-june-fomc-kalshi-67-2026-06-12"
headline: "Fed hold with dissent at June FOMC: Kalshi 67%"
semantic_title: "Fed hold with at least one dissent at June meeting wavers near two-thirds"
telemetry: "Kalshi 67%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-12T16:54:27.000Z"
event_id: "CM-EVT-MZGHWX20T0"
event_slug: "kxfedcombo-26jun"
event_question: "Will the Federal Reserve hold rates at 4.25%-4.50% with at least one dissent at its June 2026 meeting?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFEDCOMBO-26JUN-0-0"
  question_raw: "Will Federal Funds Rate Decision be No change AND Dissents be 0 for Jun 2026?"
  current_price: 0.67
  volume_24h_usd: 238.04
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-06-17T19:00:00Z"
bullets:
  - "Kalshi prices the Fed holding at 4.25-4.50% with at least one dissent at the June meeting at 67%."
  - "Warsh arriving at a divided Fed with inflation at 4.2% and political pressure for cuts is directly consistent with elevated dissent probability."
  - "At 67%, the market prices a hold with dissent as more likely than not, but leaves meaningful room for a unanimous hold or a surprise move."
  - "Resolution is via Bureau of Labor Statistics; note the resolution source appears to be a mismatch with the actual Fed decision, and that edge case could affect settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "New Fed Chair Kevin Warsh steps into a divided FOMC as Trump pushes for cuts and May inflation hits 4.2%, a three-year high."
    publisher: "mpamag.com"
    published_at: "2026-06-12T16:54:27.000Z"
    source_url: "https://www.mpamag.com/us/mortgage-industry/market-updates/warsh-walks-into-a-divided-fed-as-a-bare-knuckle-fight-begins-for-monetary-policy/578775"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "mpamag.com"
        source_url: "https://www.mpamag.com/us/mortgage-industry/market-updates/warsh-walks-into-a-divided-fed-as-a-bare-knuckle-fight-begins-for-monetary-policy/578775"
        retrieved_at: "2026-06-15T13:51:44+00:00"
  - type: "pm_response"
    notes: "Kalshi at 67% reflects the market pricing internal Fed division as the base case, consistent with reported bare-knuckle fight framing around monetary policy."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "mpamag.com: Warsh walks into a divided Fed as a 'bare-knuckle fight' begins for mo"
    url: "https://www.mpamag.com/us/mortgage-industry/market-updates/warsh-walks-into-a-divided-fed-as-a-bare-knuckle-fight-begins-for-monetary-policy/578775"
    published_at: "2026-06-12T16:54:27.000Z"
    retrieved_at: "2026-06-15T13:51:44+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
