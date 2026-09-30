---
signal_id: "CMSIG2026093005"
signal_slug: "us-embassy-reopens-in-iran-kalshi-4-2026-09-30"
headline: "US embassy reopens in Iran: Kalshi 4%"
semantic_title: "US embassy reopening in Iran stays a long shot at 4 percent"
telemetry: "Kalshi 4%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-30T00:00:00.000Z"
event_id: "CM-EVT-34SYT4T2T1"
event_slug: "kxiranembassy-27"
event_question: "Will the United States reopen its embassy in Iran?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXIRANEMBASSY-27"
  question_raw: "Will the US reopen its embassy in Iran before Jan 1, 2027?"
  current_price: 0.038
  volume_24h_usd: 0.39
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The Kalshi prediction market puts only 4% on the United States reopening its embassy in Iran, resolving via The New York Times."
  - "Backchannel ceasefire talks via Qatar are an early-stage signal; the market treats full diplomatic normalization as a very distant outcome even as talks resume."
  - "The Polymarket contract on Iran withdrawing from the NPT before 2027 sits at 10%, suggesting the market sees nuclear escalation as more likely than full diplomatic rapprochement."
  - "Embassy reopening requires sustained agreement well beyond a ceasefire; the named resolution source is The New York Times confirmation, not a government announcement alone."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "US and Iranian officials separately spoke with Qatari mediators exploring a ceasefire and reopening of the Strait of Hormuz after seven months of conflict."
    publisher: "Thomson Reuters"
    published_at: "2026-09-30T00:00:00.000Z"
    source_url: "https://www.republicworld.com/world-news/wrapup-1-us-iran-separately-talk-with-mediators-in-latest-bid-to-end-war-2026-09-30-137961"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Thomson Reuters"
        source_url: "https://www.republicworld.com/world-news/wrapup-1-us-iran-separately-talk-with-mediators-in-latest-bid-to-end-war-2026-09-30-137961"
        retrieved_at: "2026-09-30T07:47:19+00:00"
  - type: "pm_response"
    notes: "Kalshi at 4% puts long odds on embassy reopening despite active backchannel talks, signaling the market expects at most a limited ceasefire, not normalized relations."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Thomson Reuters: After 7 Months Of War, US And Iran Reopen Backchannel For Ceasefire |"
    url: "https://www.republicworld.com/world-news/wrapup-1-us-iran-separately-talk-with-mediators-in-latest-bid-to-end-war-2026-09-30-137961"
    published_at: "2026-09-30T00:00:00.000Z"
    retrieved_at: "2026-09-30T07:47:19+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
