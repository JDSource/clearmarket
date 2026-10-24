---
signal_id: "CMSIG2026102205"
signal_slug: "gop-holds-one-congress-chamber-after-midterms-kalshi-67-2026-10-22"
headline: "GOP holds one Congress chamber after midterms: Kalshi 67%"
semantic_title: "Republicans holding at least one chamber stays near 67 percent"
telemetry: "Kalshi 67%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-22T00:00:00.000Z"
event_id: "CM-EVT-T5VXKJT451"
event_slug: "kxbalancepowercombo-27feb"
event_question: "Will Republicans control at least one chamber of Congress after the 2026 midterm elections?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBALANCEPOWERCOMBO-27FEB-DD"
  question_raw: "Will House Control be Democratic AND Senate Control be Democratic for Feb 2027?"
  current_price: 0.67
  volume_24h_usd: 147233.99
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi prices Republicans retaining at least one chamber of Congress after the 2026 midterms at 67%."
  - "The Means resignation adds turbulence to a Republican-aligned health initiative, but the 67% figure suggests the market is not dramatically repricing GOP chamber prospects on this news alone."
  - "The companion Kalshi contract on Republicans holding more governorships than Democrats at 77% (CM-EVT-4DFCBXLZN6) suggests the market sees state-level Republican strength outlasting congressional performance."
  - "Resolution via Bureau of Labor Statistics per the contract metadata; the definitive trigger is the certified chamber composition following the November 3 election."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Politico reports RFK Jr.'s top adviser Calley Means resigned from HHS, rattling the MAHA movement ahead of the midterms."
    publisher: "Carmen Paun"
    published_at: "2026-10-22T00:00:00.000Z"
    source_url: "https://www.politico.com/politicopulse/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Carmen Paun"
        source_url: "https://www.politico.com/politicopulse/"
        retrieved_at: "2026-10-24T12:26:12+00:00"
  - type: "pm_response"
    notes: "Kalshi prices the GOP at 67% to hold at least one chamber, sitting below the 77% governorship contract and above the 53% 'blue tsunami' contract, reflecting a calibrated split-outcome scenario."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Carmen Paun: POLITICO Pulse - POLITICO"
    url: "https://www.politico.com/politicopulse/"
    published_at: "2026-10-22T00:00:00.000Z"
    retrieved_at: "2026-10-24T12:26:12+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
