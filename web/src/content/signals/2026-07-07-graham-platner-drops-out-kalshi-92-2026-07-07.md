---
signal_id: "CMSIG2026070705"
signal_slug: "graham-platner-drops-out-kalshi-92-2026-07-07"
headline: "Graham Platner drops out: Kalshi 92%"
semantic_title: "Graham Platner dropout consensus hardens near full pricing"
telemetry: "Kalshi 92%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-07T10:00:04.000Z"
event_id: "CM-EVT-5YRQP7DDC2"
event_slug: "kxplatnerdropout-26"
event_question: "Will Graham Platner drop out?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPLATNERDROPOUT-26"
  question_raw: "Will Graham Platner drop out of the 2026 United States Senate election in Maine before Jul 14, 2026?"
  current_price: 0.916
  volume_24h_usd: 864358.64
  arbitration_model: "kalshi_staff"
  resolution_source: "Fox News"
  resolves_at: "2026-07-14T14:00:00Z"
bullets:
  - "Kalshi prices a 92% probability that Graham Platner will drop out of the Maine Senate race, resolving via Fox News."
  - "Multiple news outlets report Democrats have already abandoned Platner following the sexual assault allegation, consistent with the near-certainty the market assigns to his exit."
  - "The companion Senate majority contract (CM-EVT-M9WJY06T90 on Polymarket) prices Democrats' Senate control chances at only 45%, reflecting how pivotal Maine was to their path."
  - "Kalshi contract resolves via Fox News reporting of a confirmed Platner withdrawal; the 92% price suggests the market is treating departure as near-certain but not yet officially confirmed."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A sexual assault allegation against Maine Democratic Senate candidate Graham Platner has prompted Democrats to abandon him, imperiling the party's narrow path to a Senate majority."
    publisher: "foxnews.com"
    published_at: "2026-07-07T10:00:04.000Z"
    source_url: "https://www.foxnews.com/politics/four-months-midterms-12-races-determine-senate-majority"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "foxnews.com"
        source_url: "https://www.foxnews.com/politics/four-months-midterms-12-races-determine-senate-majority"
        retrieved_at: "2026-07-08T10:13:38+00:00"
  - type: "pm_response"
    notes: "Kalshi contract at 92% is tightly aligned with news of Democratic abandonment of the candidate; resolution awaits Fox News confirmation of a formal withdrawal."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "foxnews.com: The 2026 midterm races that could flip Senate control | Fox News"
    url: "https://www.foxnews.com/politics/four-months-midterms-12-races-determine-senate-majority"
    published_at: "2026-07-07T10:00:04.000Z"
    retrieved_at: "2026-07-08T10:13:38+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
