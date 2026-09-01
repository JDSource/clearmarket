---
signal_id: "CMSIG2026083103"
signal_slug: "sept-unemployment-rate-seen-4-1-4-2-ladder-2026-08-31"
headline: "Sept unemployment rate seen 4.1-4.2%: ladder"
semantic_title: "Unemployment rate seen holding near 4.1 to 4.2 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-31T00:00:00.000Z"
event_id: "CM-EVT-720DZC17Y9"
event_slug: "kxu3-26sep"
event_question: "U-3 unemployment rate September 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26SEP-T4.2"
  question_raw: "Will the unemployment rate (U-3) be above 4.2% in September?"
  current_price: 0.48
  volume_24h_usd: 99.29
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "The prediction market ladder implies the September U-3 unemployment rate in the 4.1-4.2% range: 68% above 4.1% but only 48% above 4.2%."
  - "A strong payrolls print backing Warsh is consistent with the market keeping unemployment near 4.1-4.2%, not a material softening."
  - "The companion ladder on peak unemployment (CM-EVT-RBY62SKLC0) prices only 20% above 4.5% before 2027, suggesting markets do not see a near-term spike."
  - "The tight range between 4.1% and 4.2% as the modal outcome leaves little room for a labor-market deterioration narrative to gain traction."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The August jobs report preview highlighted a robust payrolls rebound that is seen backing Warsh's view that the labor market supports tighter policy."
    publisher: "top1markets.com"
    published_at: "2026-08-31T00:00:00.000Z"
    source_url: "https://www.top1markets.com/news/august-2026-jobs-report-nfp-preview"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "top1markets.com"
        source_url: "https://www.top1markets.com/news/august-2026-jobs-report-nfp-preview"
        retrieved_at: "2026-09-01T13:00:06+00:00"
  - type: "pm_response"
    notes: "Ladder market pins September unemployment near 4.1-4.2%; the peak-unemployment companion at 20% above 4.5% closes off recession scenarios."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "top1markets.com: August 2026 Jobs Report Preview: Date, Forecasts, and Why a Weak NFP N"
    url: "https://www.top1markets.com/news/august-2026-jobs-report-nfp-preview"
    published_at: "2026-08-31T00:00:00.000Z"
    retrieved_at: "2026-09-01T13:00:06+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
