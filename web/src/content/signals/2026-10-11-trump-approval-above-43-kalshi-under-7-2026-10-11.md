---
signal_id: "CMSIG2026101103"
signal_slug: "trump-approval-above-43-kalshi-under-7-2026-10-11"
headline: "Trump approval above 43%: Kalshi under 7%"
semantic_title: "Trump approval odds stay heavily below 43 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-11T00:00:00.000Z"
event_id: "CM-EVT-VWW9FTFB33"
event_slug: "kxtrumpapprovalyear-26dec31"
event_question: "Trump approval rating threshold"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPAPPROVALYEAR-26DEC31-43"
  question_raw: "Will Donald Trump's approval rating on approval rating be above 43% during Dec 2025 to Dec 2026 according to VoteHub?"
  current_price: 0.069
  volume_24h_usd: 78.25
  arbitration_model: "kalshi_staff"
  resolution_source: "<polling organization>"
  resolves_at: "2027-01-07T12:00:00Z"
bullets:
  - "Kalshi ladder puts only 7% odds on Trump's approval rating exceeding 43%, with every higher strike (44%-50%) at 6% or below."
  - "Near-record-low consumer sentiment driven by Middle East cost-of-living pressures aligns with the market's heavily negative approval pricing."
  - "Pew Research separately reported Trump approval at 30%, far below even the 43% threshold the market already prices as a long shot."
  - "Companion Kalshi contract on Trump approval ending 2026 below threshold sits at 8%, suggesting the market sees little chance of a recovery by year-end."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US consumer sentiment slumped further in early October as rising living costs tied to the Middle East conflict deepened household frustration ahead of midterms."
    publisher: "Reuters"
    published_at: "2026-10-11T00:00:00.000Z"
    source_url: "https://www.nst.com.my/business/economy/2026/10/1552962/us-consumer-sentiment-near-record-low-frustration-over-economy"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Reuters"
        source_url: "https://www.nst.com.my/business/economy/2026/10/1552962/us-consumer-sentiment-near-record-low-frustration-over-economy"
        retrieved_at: "2026-10-11T14:35:49+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder; the implied range below 43% is consistent across all ladder strikes, making this one of the most lopsided approval distributions in the data set."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Reuters: US consumer sentiment near record low as frustration over economy moun"
    url: "https://www.nst.com.my/business/economy/2026/10/1552962/us-consumer-sentiment-near-record-low-frustration-over-economy"
    published_at: "2026-10-11T00:00:00.000Z"
    retrieved_at: "2026-10-11T14:35:49+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
