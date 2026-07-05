---
signal_id: "CMSIG2026070505"
signal_slug: "trump-attends-nato-summit-polymarket-99-2026-07-05"
headline: "Trump attends NATO Summit: Polymarket 99%"
semantic_title: "Trump NATO summit attendance nears full pricing"
telemetry: "Polymarket 99%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-05T02:47:27.000Z"
event_id: "CM-EVT-FD56H0NQ25"
event_slug: "will-trump-attend-nato-summit-279"
event_question: "Will Donald Trump attend NATO Summit?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x71ee9c148f0e2b386ba959aca5954c5e6c428695bf1a5fca0af9194f40487758"
  question_raw: "Will Donald Trump attend NATO Summit?"
  current_price: 0.989
  volume_24h_usd: 7163.753250999999
  arbitration_model: "uma_oracle"
  resolves_at: "2026-07-08T00:00:00Z"
bullets:
  - "Polymarket prices a 99% probability that Trump attends the NATO Summit, resolved via UMA oracle."
  - "Trading volume on this Polymarket contract surged 2,721% day over day, with the Trump-Putin call and summit framing driving fresh positioning to near-certainty."
  - "At 99%, the market treats Trump's NATO attendance as a near-done fact; the diplomatic activity around the summit is consistent with, not in tension with, that pricing."
  - "Despite near-certain attendance, the companion Polymarket contract on a Ukraine peace deal (CM-EVT-DCQYWYX424) sits at only 18%, showing the market separates showing up from delivering a deal."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Russia says Trump reaffirmed readiness to help end the Ukraine war in a call with Putin, with the NATO summit in Ankara as the backdrop for settlement discussions."
    publisher: "aa.com.tr"
    published_at: "2026-07-05T02:47:27.000Z"
    source_url: "https://www.aa.com.tr/en/russia-ukraine-war/russia-says-trump-reaffirmed-readiness-to-help-end-ukraine-war-in-phone-call-with-putin/3986393"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "aa.com.tr"
        source_url: "https://www.aa.com.tr/en/russia-ukraine-war/russia-says-trump-reaffirmed-readiness-to-help-end-ukraine-war-in-phone-call-with-putin/3986393"
        retrieved_at: "2026-07-05T10:07:52+00:00"
  - type: "pm_response"
    notes: "Polymarket binary contract resolving via UMA oracle; exceptional volume spike confirms the Trump-Putin call elevated this contract to maximum attention."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "aa.com.tr: Russia says Trump 'reaffirmed readiness' to help end Ukraine war in ph"
    url: "https://www.aa.com.tr/en/russia-ukraine-war/russia-says-trump-reaffirmed-readiness-to-help-end-ukraine-war-in-phone-call-with-putin/3986393"
    published_at: "2026-07-05T02:47:27.000Z"
    retrieved_at: "2026-07-05T10:07:52+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
