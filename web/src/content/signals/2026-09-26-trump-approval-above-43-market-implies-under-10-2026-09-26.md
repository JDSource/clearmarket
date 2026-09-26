---
signal_id: "CMSIG2026092605"
signal_slug: "trump-approval-above-43-market-implies-under-10-2026-09-26"
headline: "Trump approval above 43%: market implies under 10%"
semantic_title: "Trump approval above 43% priced as unlikely"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-26T00:00:00.000Z"
event_id: "CM-EVT-VWW9FTFB33"
event_slug: "kxtrumpapprovalyear-26dec31"
event_question: "Trump approval rating threshold"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPAPPROVALYEAR-26DEC31-43"
  question_raw: "Will Donald Trump's approval rating on approval rating be above 43% during Dec 2025 to Dec 2026 according to VoteHub?"
  current_price: 0.08
  volume_24h_usd: 1.88
  arbitration_model: "kalshi_staff"
  resolution_source: "<polling organization>"
  resolves_at: "2027-01-07T12:00:00Z"
bullets:
  - "The approval rating ladder prices only 8% on Trump clearing 43% approval, implying the market-consensus range sits well below that level."
  - "New polling showing Trump at historic lows aligns directly with the market's sub-43% implied range, with no divergence between news and pricing."
  - "The companion ladder (CM-EVT-0DMSQTKVX3) implies a market-consensus floor near 33-37%, consistent with polls showing broad erosion even among Republicans."
  - "Resolution uses an approval-rating aggregator; the distribution spread between 33% and 43% reflects genuine uncertainty about how low ratings can fall, not just where they are today."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Multiple polls show President Trump's approval ratings sinking to new lows, driven by declining GOP support and deteriorating views on the economy ahead of the midterms."
    publisher: "thehill.com"
    published_at: "2026-09-26T00:00:00.000Z"
    source_url: "https://thehill.com/homenews/administration/6112712-trump-approval-ratings-midterm-elections/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "thehill.com"
        source_url: "https://thehill.com/homenews/administration/6112712-trump-approval-ratings-midterm-elections/"
        retrieved_at: "2026-09-26T12:39:23+00:00"
  - type: "pm_response"
    notes: "Ladder distribution across both contracts indicates the market sees Trump's approval range as 33-43%, with new polling providing concurrent confirmation."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "thehill.com: Donald Trump's sinking approval sparks concerns for GOP ahead of midte"
    url: "https://thehill.com/homenews/administration/6112712-trump-approval-ratings-midterm-elections/"
    published_at: "2026-09-26T00:00:00.000Z"
    retrieved_at: "2026-09-26T12:39:23+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
