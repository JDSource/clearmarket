---
signal_id: "CMSIG2026090107"
signal_slug: "us-recognizes-pahlavi-as-iran-leader-kalshi-6-2026-09-01"
headline: "US recognizes Pahlavi as Iran leader: Kalshi 6%"
semantic_title: "US recognition of Reza Pahlavi as Iran leader stays a long shot"
telemetry: "Kalshi 6%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-01T00:00:00.000Z"
event_id: "CM-EVT-SY50TZ6672"
event_slug: "kxrecogpersoniran-26"
event_question: "Will the United States recognize Reza Pahlavi as the leader of Iran by 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXRECOGPERSONIRAN-26"
  question_raw: "Will the United States recognize Reza Pahlavi as the leader of Iran in 2026?"
  current_price: 0.06
  volume_24h_usd: 51.33
  arbitration_model: "kalshi_staff"
  resolution_source: "ABC"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices only 6% on the United States recognizing Reza Pahlavi as the leader of Iran by 2026, resolving via ABC."
  - "Pezeshkian's conditional ceasefire offer implies Iranian leadership is engaged diplomatically, making a US pivot to regime-change recognition even less likely near-term."
  - "The companion Kalshi contract on the US reopening its embassy in Iran sits at 2%, reinforcing that markets see no normalization path in sight."
  - "The 6% Pahlavi recognition price and 2% embassy reopening price together bracket the full range of US-Iran rapprochement scenarios as remote."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Iranian President Masoud Pezeshkian said Iran would return to a ceasefire agreement if the United States does, suggesting conditional de-escalation."
    publisher: "The Associated Press"
    published_at: "2026-09-01T00:00:00.000Z"
    source_url: "https://www.thestar.com/news/world/middle-east/iran-s-president-says-iran-would-return-to-ceasefire-agreement-if-us-does-and-other-mideast-news/article_29f0dd0f-9230-5daf-b7c2-c19185764e40.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "The Associated Press"
        source_url: "https://www.thestar.com/news/world/middle-east/iran-s-president-says-iran-would-return-to-ceasefire-agreement-if-us-does-and-other-mideast-news/article_29f0dd0f-9230-5daf-b7c2-c19185764e40.html"
        retrieved_at: "2026-09-01T13:00:06+00:00"
  - type: "pm_response"
    notes: "Kalshi at 6% on Pahlavi recognition; the 2% embassy-reopening contract closes off any diplomatic normalization scenario in the market's implied distribution."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "The Associated Press: Iran's president says Iran would return to ceasefire agreement if U.S."
    url: "https://www.thestar.com/news/world/middle-east/iran-s-president-says-iran-would-return-to-ceasefire-agreement-if-us-does-and-other-mideast-news/article_29f0dd0f-9230-5daf-b7c2-c19185764e40.html"
    published_at: "2026-09-01T00:00:00.000Z"
    retrieved_at: "2026-09-01T13:00:06+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
