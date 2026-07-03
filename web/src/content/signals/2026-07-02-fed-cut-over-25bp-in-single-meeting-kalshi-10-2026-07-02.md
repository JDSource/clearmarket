---
signal_id: "CMSIG2026070202"
signal_slug: "fed-cut-over-25bp-in-single-meeting-kalshi-10-2026-07-02"
headline: "Fed cut over 25bp in single meeting: Kalshi 10%"
semantic_title: "Jumbo Fed cut pricing holds firm at deeply discounted levels"
telemetry: "Kalshi 10%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-02T18:30:59.957Z"
event_id: "CM-EVT-RWRZ1R3SD6"
event_slug: "kxlargecut-26"
event_question: "Will the Federal Reserve cut interest rates by more than 25 basis points in a single action this year?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXLARGECUT-26"
  question_raw: "Will the Fed cut rates more than 25 bps in 2026?"
  current_price: 0.098
  volume_24h_usd: 2115.19
  arbitration_model: "kalshi_staff"
  resolution_source: "Federal Reserve"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The Kalshi prediction market puts only 10% on the Fed cutting by more than 25 basis points in any single meeting."
  - "Despite a sharply weak jobs print, the market is not pricing an emergency or outsized cut, consistent with ongoing inflation concerns limiting the Fed's room."
  - "The weak-jobs plus high-inflation backdrop described in reporting gives the Fed no clear mandate for aggressive easing, and the 10% reading reflects that bind."
  - "The Kalshi ladder CM-EVT-MR57HVWJT3 implies the funds rate stays in the 3.75-4.00% range, making a jumbo cut appear inconsistent with current pricing across both contracts."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "June payrolls came in at 57,000 against a 113,000 consensus, prompting analysts to label it a Fed nightmare of weak jobs plus high inflation."
    publisher: "investing.com"
    published_at: "2026-07-02T18:30:59.957Z"
    source_url: "https://www.investing.com/analysis/feds-nightmare-scenario-has-arrived-weak-jobs-high-inflation-200683221"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "investing.com"
        source_url: "https://www.investing.com/analysis/feds-nightmare-scenario-has-arrived-weak-jobs-high-inflation-200683221"
        retrieved_at: "2026-07-03T10:32:12+00:00"
  - type: "pm_response"
    notes: "Kalshi binary contract resolving via Federal Reserve; at 10%, the market is firmly skeptical of any oversized single-meeting cut."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "investing.com: Fed’s Nightmare Scenario Has Arrived: Weak Jobs, High Inflation | Inve"
    url: "https://www.investing.com/analysis/feds-nightmare-scenario-has-arrived-weak-jobs-high-inflation-200683221"
    published_at: "2026-07-02T18:30:59.957Z"
    retrieved_at: "2026-07-03T10:32:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
