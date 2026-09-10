---
signal_id: "CMSIG2026091001"
signal_slug: "august-cpi-implied-near-0-3-0-4-ladder-after-ppi-undershoot-2026-09-10"
headline: "August CPI implied near 0.3-0.4%: ladder after PPI undershoot"
semantic_title: "August CPI near flat stays the market call after PPI miss"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-10T00:00:00.000Z"
event_id: "CM-EVT-D057W6W251"
event_slug: "kxcpi-26aug"
event_question: "August 2026 CPI month-on-month change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26AUG-T0.4"
  question_raw: "Will CPI rise more than 0.4% in August 2026?"
  current_price: 0.13
  volume_24h_usd: 717.18
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-12-11T13:56:00Z"
bullets:
  - "The CPI ladder prices the August 2026 month-on-month change in the 0.3-0.4% range: 97% above 0.1%, but only 59% above 0.3% and 13% above 0.4%."
  - "August PPI came in at -0.1% versus +0.3% expected; the CPI ladder's implied range is notably above the PPI print, suggesting markets see CPI as still positive despite the producer-price shock."
  - "The mismatch between a deep PPI undershoot and a CPI ladder still centered near 0.3% points to a services/shelter wedge keeping consumer inflation stickier than wholesale prices."
  - "The Kalshi contract on whether the Federal Reserve will raise rates in 2026 sits at 76%, a cross-check on whether Friday's CPI would need to deliver a second consecutive surprise to shift that terminal rate view."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "August PPI fell 0.1% month-on-month versus a +0.3% consensus, dramatically undershooting and collapsing near-term rate-hike odds ahead of Friday's CPI print."
    publisher: "PomiNews"
    published_at: "2026-09-10T00:00:00.000Z"
    source_url: "https://pomegra.io/news/august-ppi-falls-01-rate-hike-odds-collapse"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "PomiNews"
        source_url: "https://pomegra.io/news/august-ppi-falls-01-rate-hike-odds-collapse"
        retrieved_at: "2026-09-10T12:39:52+00:00"
  - type: "pm_response"
    notes: "The CPI ladder carries priced strikes from -0.4% through 1.0% and resolves on the Bureau of Labor Statistics August CPI release; no single strike dominates above 0.3%."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "PomiNews: August PPI Falls 0.1%, Rate-Hike Odds Collapse | Pomegra News"
    url: "https://pomegra.io/news/august-ppi-falls-01-rate-hike-odds-collapse"
    published_at: "2026-09-10T00:00:00.000Z"
    retrieved_at: "2026-09-10T12:39:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
