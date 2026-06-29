---
signal_id: "CMSIG2026062807"
signal_slug: "scotus-strikes-trump-birthright-citizenship-eo-polymarket-94-2026-06-28"
headline: "SCOTUS strikes Trump birthright citizenship EO: Polymarket 94%"
semantic_title: "SCOTUS Birthright Citizenship EO strike-down nears full pricing"
telemetry: "Polymarket 94%"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-06-28T10:02:35.000Z"
event_id: "CM-EVT-4HHYC680N8"
event_slug: "scotus-strikes-down-trumps-birthright-citizenship-eo"
event_question: "Will SCOTUS strike down Trump's Birthright Citizenship Executive Order?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x12609f33bc603cb234db2af1d502d143587b697bdc479ddb9344401dbf987914"
  question_raw: "SCOTUS strikes down Trump's Birthright Citizenship EO?"
  current_price: 0.936
  volume_24h_usd: 216.129031
  arbitration_model: "uma_oracle"
  resolution_source: "whitehouse.gov"
  resolves_at: "2026-08-31T00:00:00Z"
bullets:
  - "Polymarket prices SCOTUS striking down Trump's birthright citizenship executive order at 94%, near certainty."
  - "Companion Kalshi contract on the order coming into effect by December 31 sits at just 7%, consistent with a near-certain strike-down read."
  - "The 94% and 7% reads together imply markets see essentially no path to the order surviving, even with delayed implementation."
  - "Resolves via whitehouse.gov; the question turns on whether the EO is formally implemented, not just left in legal limbo."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The Supreme Court is expected to rule imminently on Trump's birthright citizenship executive order, one of the most anticipated cases of the term."
    publisher: "Thomson Reuters"
    published_at: "2026-06-28T10:02:35.000Z"
    source_url: "https://95kqds.com/2026/06/28/as-supreme-courts-term-nears-its-end-three-major-trump-rulings-due/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Thomson Reuters"
        source_url: "https://95kqds.com/2026/06/28/as-supreme-courts-term-nears-its-end-three-major-trump-rulings-due/"
        retrieved_at: "2026-06-29T12:28:56+00:00"
  - type: "pm_response"
    notes: "Polymarket's 94% strike-down and Kalshi's 7% implementation rate are tightly coherent, reflecting a strong cross-venue consensus."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Thomson Reuters: As Supreme Court’s term nears its end, three major Trump rulings due |"
    url: "https://95kqds.com/2026/06/28/as-supreme-courts-term-nears-its-end-three-major-trump-rulings-due/"
    published_at: "2026-06-28T10:02:35.000Z"
    retrieved_at: "2026-06-29T12:28:56+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
