---
signal_id: "CMSIG2026083002"
signal_slug: "aug-unemployment-rate-seen-4-1-4-2-kalshi-ladder-2026-08-30"
headline: "Aug unemployment rate seen 4.1-4.2%: Kalshi ladder"
semantic_title: "August unemployment odds cluster near 4.1 to 4.2 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-30T00:00:00.000Z"
event_id: "CM-EVT-CN1M891289"
event_slug: "kxu3-26aug"
event_question: "U-3 unemployment rate, August 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXU3-26AUG-T4.2"
  question_raw: "Will the unemployment rate (U-3) be above 4.2% in August?"
  current_price: 0.26
  volume_24h_usd: 1051.7
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-12-04T14:00:00Z"
bullets:
  - "Kalshi ladder puts 57% odds on U-3 above 4.1% and 26% on above 4.2%, implying the market central estimate sits in the 4.1-4.2% band."
  - "The 85% probability above 3.9% and 57% above 4.1% are consistent with a labor market that is softening at the margin but not breaking down."
  - "Fortune's 'functionally unemployed' framing aligns with the ladder's fat tail above 4.2% (remaining 26%), suggesting markets are not dismissing a worse read."
  - "The sharp drop in probability from 85% at 3.9% to 26% at 4.2% shows the Kalshi contract treats a sharp deterioration above 4.2% as an unlikely but non-trivial risk."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fortune reports the official jobless rate has been falling but the count of functionally unemployed Americans is climbing, highlighting a gap between headline and broader labor market health."
    publisher: "Jason Ma"
    published_at: "2026-08-30T00:00:00.000Z"
    source_url: "https://fortune.com/2026/08/30/jobless-rate-labor-market-economy-full-employment-functionally-unemployed/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jason Ma"
        source_url: "https://fortune.com/2026/08/30/jobless-rate-labor-market-economy-full-employment-functionally-unemployed/"
        retrieved_at: "2026-08-31T15:47:21+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via FRED, giving a clean, unambiguous official data source for settlement."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jason Ma: The official jobless rate has been falling. But the number of 'functio"
    url: "https://fortune.com/2026/08/30/jobless-rate-labor-market-economy-full-employment-functionally-unemployed/"
    published_at: "2026-08-30T00:00:00.000Z"
    retrieved_at: "2026-08-31T15:47:21+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
