---
signal_id: "CMSIG2026102605"
signal_slug: "dems-win-us-senate-polymarket-66-2026-10-26"
headline: "Dems win US Senate: Polymarket 66%"
semantic_title: "Democrats favored but short of lock on US Senate control in 2026"
telemetry: "Polymarket 66%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-26T17:00:00.000Z"
event_id: "CM-EVT-M9WJY06T90"
event_slug: "which-party-will-win-the-senate-in-2026"
event_question: "Which party will win control of the U.S. Senate in the 2026 election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x307a1ed89d60b61002dd5bbf00e1408c5ed2ab3fcdb056191ca7ef9bc34d38f3"
  question_raw: "Will the Democratic Party control the Senate after the 2026 Midterm elections?"
  current_price: 0.66
  volume_24h_usd: 93471.99000900002
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices Democratic Senate control at 66%, a meaningful lean but well short of the 90% the same venue-equivalent shows for the House."
  - "Al Jazeera analysis highlighting competitive Senate races is consistent with the market's incomplete pricing of a Democratic sweep."
  - "The 34% Republican retention probability in the Senate reflects genuine uncertainty in key state races like Texas (Paxton vs. Talarico) described in companion coverage."
  - "Resolution via UMA oracle on Polymarket; final seat certification, not election-night projections, settles the contract."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Al Jazeera maps and charts show November 3 midterms will decide which party controls Congress for the second half of Trump's presidency."
    publisher: "Alia Chughtai, Hoda Sherif"
    published_at: "2026-10-26T17:00:00.000Z"
    source_url: "https://www.aljazeera.com/news/2026/10/26/us-midterm-elections-2026-in-maps-and-charts"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Alia Chughtai, Hoda Sherif"
        source_url: "https://www.aljazeera.com/news/2026/10/26/us-midterm-elections-2026-in-maps-and-charts"
        retrieved_at: "2026-10-27T07:48:12+00:00"
  - type: "pm_response"
    notes: "Polymarket's 66% on Democratic Senate control is the softest of the three chamber-control contracts, tracking the competitive map identified in Al Jazeera's midterm preview."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Alia Chughtai, Hoda Sherif: US midterm elections 2026 in maps and charts"
    url: "https://www.aljazeera.com/news/2026/10/26/us-midterm-elections-2026-in-maps-and-charts"
    published_at: "2026-10-26T17:00:00.000Z"
    retrieved_at: "2026-10-27T07:48:12+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
