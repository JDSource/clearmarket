---
signal_id: "CMSIG2026102701"
signal_slug: "oct-fed-funds-upper-bound-seen-at-4-0-4-25-kalshi-ladder-2026-10-27"
headline: "Oct Fed funds upper bound seen at 4.0-4.25%: Kalshi ladder"
semantic_title: "Fed funds upper bound stays near 4.0-4.25 percent after Oct meeting"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-27T00:00:00.000Z"
event_id: "CM-EVT-MR57HVWJT3"
event_slug: "kxfed-26dec"
event_question: "Oct 2026 Fed funds upper bound"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXFED-26DEC-T4.25"
  question_raw: "Will the upper bound of the federal funds rate be above 4.25% following the Fed's Dec 9, 2026 meeting?"
  current_price: 0.1
  volume_24h_usd: 193.42
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve Board of Governors"
  resolves_at: "2026-12-16T19:05:00Z"
bullets:
  - "Kalshi ladder pins the October 2026 Fed funds upper bound in the 4.0-4.25% range, pricing 84% above 4.0% but only 10% above 4.25%."
  - "The CNBC survey's 93% pause consensus aligns with the ladder distribution; volume on this contract rose 274x day over day, signaling heavy fresh attention."
  - "The sharp drop from 84% at the 4.0% strike to 10% at 4.25% confirms the market treats a hold at 4.0-4.25% as the near-certain outcome this week."
  - "A companion Kalshi ladder (CM-EVT-6BS28TS762) implies the upper bound near 3.75-4.0%, suggesting a slight divergence in strike calibration worth monitoring against the December hike narrative."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A CNBC Fed Survey shows 93% of respondents expect a pause at the October meeting, with 76% anticipating a hike at the December meeting."
    publisher: "Steve Liesman"
    published_at: "2026-10-27T00:00:00.000Z"
    source_url: "https://www.cnbc.com/2026/10/27/federal-reserve-rate-hike-timing-expectations.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Steve Liesman"
        source_url: "https://www.cnbc.com/2026/10/27/federal-reserve-rate-hike-timing-expectations.html"
        retrieved_at: "2026-10-27T13:54:00+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder volume surged 274x day over day, reflecting concentrated pre-decision positioning consistent with the consensus pause call."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Steve Liesman: Federal Reserve rate hikes are coming, but not this week: CNBC survey"
    url: "https://www.cnbc.com/2026/10/27/federal-reserve-rate-hike-timing-expectations.html"
    published_at: "2026-10-27T00:00:00.000Z"
    retrieved_at: "2026-10-27T13:54:00+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
