---
signal_id: "CMSIG2026060208"
signal_slug: "trump-approval-above-43-kalshi-ladder-implies-43-2026-06-02"
headline: "Trump approval above 43%: Kalshi ladder implies <43%"
semantic_title: "Consensus anchors Trump approval below 43 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-02T00:00:00.000Z"
event_id: "CM-EVT-VWW9FTFB33"
event_slug: "kxtrumpapprovalyear-26dec31"
event_question: "Trump approval rating"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPAPPROVALYEAR-26DEC31-43"
  question_raw: "Will Donald Trump's approval rating on approval rating be above 43% during Dec 2025 to Dec 2026 according to VoteHub?"
  current_price: 0.25
  volume_24h_usd: 1.64
  arbitration_model: "kalshi_staff"
  resolves_at: "2027-01-07T12:00:00Z"
bullets:
  - "Kalshi ladder puts only 25% probability on Trump's approval rising above 43% in the measured window."
  - "Economist/YouGov poll showing new approval lows on inflation and Iran is consistent with this bearish distribution."
  - "Companion downside ladder (CM-EVT-0DMSQTKVX3) prices 99% on approval staying below 40%, narrowing the expected range to roughly 33-43%."
  - "Resolves via named approval-rating data source; the ladder is calibrated to a specific polling methodology, not an average of averages."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "An Economist/YouGov poll showed Trump's approval hitting new lows on inflation and the Iran war."
    publisher: "David Montgomery   Senior data journalist"
    published_at: "2026-06-02T00:00:00.000Z"
    source_url: "https://yougov.com/en-us/articles/54886-donald-trump-approval-new-lows-inflation-iran-ai-e-jean-carroll-may-29-june-1-2026-economist-yougov-poll"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "David Montgomery   Senior data journalist"
        source_url: "https://yougov.com/en-us/articles/54886-donald-trump-approval-new-lows-inflation-iran-ai-e-jean-carroll-may-29-june-1-2026-economist-yougov-poll"
        retrieved_at: "2026-06-04T03:24:20+00:00"
  - type: "pm_response"
    notes: "Kalshi's approval ladder at 25% above 43% aligns with fresh poll lows driven by Iran and inflation headwinds."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "David Montgomery   Senior data journalist: Trump approval hits new lows on inflation and Iran, AI, E. Jean Carrol"
    url: "https://yougov.com/en-us/articles/54886-donald-trump-approval-new-lows-inflation-iran-ai-e-jean-carroll-may-29-june-1-2026-economist-yougov-poll"
    published_at: "2026-06-02T00:00:00.000Z"
    retrieved_at: "2026-06-04T03:24:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
