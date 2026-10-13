---
signal_id: "CMSIG2026101307"
signal_slug: "trump-approval-above-43-ladder-under-3-probability-2026-10-13"
headline: "Trump approval above 43%: ladder under 3% probability"
semantic_title: "Trump approval rating priced below 43 percent by markets"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-13T00:00:00.000Z"
event_id: "CM-EVT-VWW9FTFB33"
event_slug: "kxtrumpapprovalyear-26dec31"
event_question: "Trump approval rating threshold"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPAPPROVALYEAR-26DEC31-43"
  question_raw: "Will Donald Trump's approval rating on approval rating be above 43% during Dec 2025 to Dec 2026 according to VoteHub?"
  current_price: 0.031
  volume_24h_usd: 10.06
  arbitration_model: "kalshi_staff"
  resolution_source: "<polling organization>"
  resolves_at: "2027-01-07T12:00:00Z"
bullets:
  - "Prediction market ladder prices only 3% odds Trump's approval rating exceeds 43%, implying the market consensus sits well below that threshold."
  - "The AP-NORC poll showing majority disapproval aligns with the ladder's sub-43% implied range, with the market not pricing any near-term approval recovery."
  - "A companion Kalshi contract on Trump's approval rating at December 31, 2026 sitting below a threshold is priced at 11%, adding a longer-dated consistent signal."
  - "Resolution tracks a named polling organization's approval figure; the current distribution prices a sustained low-approval environment through year-end."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A new AP-NORC poll finds most Americans believe Donald Trump is profiting off the presidency unethically and is focused more on his wealth than helping ordinary people."
    publisher: "apnews.com"
    published_at: "2026-10-13T00:00:00.000Z"
    source_url: "https://apnews.com/article/ethics-trump-family-crypto-conflicts-poll-1222b8ee41ccff5b23dcd41efdac34ff"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/ethics-trump-family-crypto-conflicts-poll-1222b8ee41ccff5b23dcd41efdac34ff"
        retrieved_at: "2026-10-13T15:32:34+00:00"
  - type: "pm_response"
    notes: "Prediction market ladder prices Trump approval above 43% at just 3%, consistent with broad polling weakness shown in the AP-NORC survey."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: Trump says he cares for Americans. They think he's more focused on his"
    url: "https://apnews.com/article/ethics-trump-family-crypto-conflicts-poll-1222b8ee41ccff5b23dcd41efdac34ff"
    published_at: "2026-10-13T00:00:00.000Z"
    retrieved_at: "2026-10-13T15:32:34+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
