---
signal_id: "CMSIG2026101601"
signal_slug: "core-cpi-above-2-kalshi-ladder-implies-2-8-2-9-2026-10-16"
headline: "Core CPI above 2%: Kalshi ladder implies 2.8-2.9%"
semantic_title: "Core CPI above 2 percent stays near full pricing"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-16T00:00:00.000Z"
event_id: "CM-EVT-BXDL61HVR9"
event_slug: "kxcpicoreyoy-26nov"
event_question: "Core CPI year-over-year rate"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPICOREYOY-26NOV-T2.9"
  question_raw: "Will the rate of core CPI inflation be above 2.9% for the year ending in November 2026?"
  current_price: 0.3
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-12-17T15:00:00Z"
bullets:
  - "Kalshi ladder prices the core CPI year-over-year rate in the 2.8-2.9% range: 55% above 2.8%, only 30% above 2.9%."
  - "TD Economics reported core CPI at 2.6%; the Kalshi distribution is consistent with expectations of continued drift higher toward 2.8-2.9%."
  - "The 78% probability above 2.6% aligns with the current print, suggesting markets anticipated this level and are pricing modest further acceleration."
  - "The Kalshi contract at only 8% for core CPI falling below 2.2% in 2026 confirms the ladder read: a return to near-target inflation is heavily discounted."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "TD Economics reported headline CPI accelerated to 3.7% and core CPI to 2.6% in the latest reading, with NFIB, Beige Book, and PPI data all pointing to building price pressures."
    publisher: "economics.td.com"
    published_at: "2026-10-16T00:00:00.000Z"
    source_url: "https://economics.td.com/us-weekly-bottom-line"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "economics.td.com"
        source_url: "https://economics.td.com/us-weekly-bottom-line"
        retrieved_at: "2026-10-18T12:25:52+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder on core CPI year-over-year spans 2.0% to 3.5% strikes; implied central tendency sits firmly in the 2.8-2.9% band."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "economics.td.com: TD Economics - Weekly Bottom Line"
    url: "https://economics.td.com/us-weekly-bottom-line"
    published_at: "2026-10-16T00:00:00.000Z"
    retrieved_at: "2026-10-18T12:25:52+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
