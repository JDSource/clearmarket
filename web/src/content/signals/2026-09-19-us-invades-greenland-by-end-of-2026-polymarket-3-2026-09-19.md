---
signal_id: "CMSIG2026091908"
signal_slug: "us-invades-greenland-by-end-of-2026-polymarket-3-2026-09-19"
headline: "US invades Greenland by end of 2026: Polymarket 3%"
semantic_title: "US invasion of Greenland by end of 2026 stays a long shot"
telemetry: "Polymarket 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-19T00:00:00.000Z"
event_id: "CM-EVT-TJWVR9PXN5"
event_slug: "will-the-us-invade-greenland-in-2026"
event_question: "Will the U.S. invade Greenland by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xe723e5e63c14e387c03cb37b11d79fa88f46a302503175b56cd9f68ecbc00a20"
  question_raw: "Will the U.S. invade Greenland in 2026?"
  current_price: 0.03
  volume_24h_usd: 485.05
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract prices only a 3% chance the US invades Greenland by end of 2026."
  - "The trilateral diplomatic agreement announced September 18 is consistent with the market's near-zero invasion probability; the market appears to have priced a negotiated outcome."
  - "The companion Polymarket contract on a US-Denmark military clash before 2027 sits at 2%, reinforcing that armed conflict is treated as a tail scenario."
  - "Resolves via uma_oracle; the Greenland independence vote contract at 4% for 2026 suggests the market sees neither military nor democratic resolution this year."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US, Denmark, and Greenland announced a diplomatic agreement on the Arctic territory on September 18, 2026, marking a de-escalation from earlier confrontational posturing."
    publisher: "Aamer Madhani and Ben Finley         Sept. 18, 2026  6:58 PM PT"
    published_at: "2026-09-19T00:00:00.000Z"
    source_url: "https://www.latimes.com/world-nation/story/2026-09-18/u-s-denmark-greenland-hail-agreement-on-arctic-territory"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Aamer Madhani and Ben Finley         Sept. 18, 2026  6:58 PM PT"
        source_url: "https://www.latimes.com/world-nation/story/2026-09-18/u-s-denmark-greenland-hail-agreement-on-arctic-territory"
        retrieved_at: "2026-09-19T07:47:13+00:00"
  - type: "pm_response"
    notes: "Polymarket at 3% is consistent with a diplomatic resolution; the agreement reported September 18 aligns with rather than surprises the current pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Aamer Madhani and Ben Finley         Sept. 18, 2026  6:58 PM PT: U.S., Denmark and Greenland hail agreement on the Arctic territory - L"
    url: "https://www.latimes.com/world-nation/story/2026-09-18/u-s-denmark-greenland-hail-agreement-on-arctic-territory"
    published_at: "2026-09-19T00:00:00.000Z"
    retrieved_at: "2026-09-19T07:47:13+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
