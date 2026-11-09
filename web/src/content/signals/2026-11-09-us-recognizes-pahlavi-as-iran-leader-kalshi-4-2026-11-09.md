---
signal_id: "CMSIG2026110908"
signal_slug: "us-recognizes-pahlavi-as-iran-leader-kalshi-4-2026-11-09"
headline: "US recognizes Pahlavi as Iran leader: Kalshi 4%"
semantic_title: "Reza Pahlavi recognized as Iran leader by 2026 stays near zero"
telemetry: "Kalshi 4%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-09T01:42:17.000Z"
event_id: "CM-EVT-SY50TZ6672"
event_slug: "kxrecogpersoniran-26"
event_question: "Will the United States recognize Reza Pahlavi as the leader of Iran by 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXRECOGPERSONIRAN-26"
  question_raw: "Will the United States recognize Reza Pahlavi as the leader of Iran in 2026?"
  current_price: 0.041
  volume_24h_usd: 29.18
  arbitration_model: "kalshi_staff"
  resolution_source: "ABC"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "The Kalshi contract prices only a 4% chance the US recognizes Reza Pahlavi as Iran's leader before the end of 2026, with volume up 3,247% day over day."
  - "The massive volume surge signals the claim is drawing significant fresh attention, even as the probability remains very low."
  - "Trump's diplomatic engagement with Qatar on Iran and signaling of openness to a deal are inconsistent with a regime-change recognition path."
  - "Resolution via ABC News reporting; the volume spike likely reflects speculative interest rather than any credible intelligence of a policy shift."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump met Qatar's prime minister to advance Iran diplomacy as efforts to end the Iran war face significant hurdles."
    publisher: "Yahoo"
    published_at: "2026-11-09T01:42:17.000Z"
    source_url: "https://www.yahoo.com/news/politics/articles/trump-meet-qatars-prime-minister-014217445.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Yahoo"
        source_url: "https://www.yahoo.com/news/politics/articles/trump-meet-qatars-prime-minister-014217445.html"
        retrieved_at: "2026-11-09T07:47:40+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via ABC News; the volume surge is a notable signal but the 4% pricing firmly discounts regime-change recognition in 2026."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Yahoo: Trump to meet Qatar's prime minister as Iran diplomacy faces hurdles"
    url: "https://www.yahoo.com/news/politics/articles/trump-meet-qatars-prime-minister-014217445.html"
    published_at: "2026-11-09T01:42:17.000Z"
    retrieved_at: "2026-11-09T07:47:40+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
