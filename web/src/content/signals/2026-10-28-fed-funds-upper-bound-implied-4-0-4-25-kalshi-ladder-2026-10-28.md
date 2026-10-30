---
signal_id: "CMSIG2026102801"
signal_slug: "fed-funds-upper-bound-implied-4-0-4-25-kalshi-ladder-2026-10-28"
headline: "Fed funds upper bound implied 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds rate seen near 4.0, 4.25% after October hold"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-28T18:04:42.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Federal funds rate upper bound post-October meeting"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.03
  volume_24h_usd: 54.89
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder prices the post-October Fed funds upper bound firmly in the 4.00, 4.25% range: 74% above 4.00%, collapsing to just 3% above 4.25%."
  - "The Fed held steady as reported, consistent with the 99% pricing at every strike through 3.75%, the hold itself was fully priced in."
  - "The sharp drop from 74% to 3% between the 4.00% and 4.25% strikes signals the market sees exactly one more 25bp hike as the base case, likely December."
  - "Trading volume on this Kalshi contract surged 75,618% day over day, a strong signal the October decision and December hike expectations are drawing intense fresh attention."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Federal Reserve held its benchmark rate steady at roughly 3.9% at the October meeting, with investors widely expecting a hike at the December meeting."
    publisher: "Scott Horsley"
    published_at: "2026-10-28T18:04:42.000Z"
    source_url: "https://www.npr.org/2026/10/28/nx-s1-6020425/federal-reserve-interest-rates-inflation"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Scott Horsley"
        source_url: "https://www.npr.org/2026/10/28/nx-s1-6020425/federal-reserve-interest-rates-inflation"
        retrieved_at: "2026-10-30T07:48:00+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder on the federal funds upper bound shows a tight consensus around one more hike, with extreme volume spike confirming the Fed decision drove heavy contract activity."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Scott Horsley: Fed holds interest rates steady despite stubborn inflation : NPR"
    url: "https://www.npr.org/2026/10/28/nx-s1-6020425/federal-reserve-interest-rates-inflation"
    published_at: "2026-10-28T18:04:42.000Z"
    retrieved_at: "2026-10-30T07:48:00+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
