---
signal_id: "CMSIG2026070708"
signal_slug: "ukraine-russia-peace-deal-before-2027-polymarket-20-2026-07-07"
headline: "Ukraine-Russia peace deal before 2027: Polymarket 20%"
semantic_title: "Ukraine-Russia peace deal before 2027 pricing holds at low consensus"
telemetry: "Polymarket 20%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-07T09:28:47.000Z"
event_id: "CM-EVT-DCQYWYX424"
event_slug: "ukraine-signs-peace-deal-with-russia-before-2027"
event_question: "Will Ukraine sign a peace deal with Russia before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x4167e22670f31e5f93d132f78108f3fae809bd15cadf78983eff096845ed1415"
  question_raw: "Ukraine signs peace deal with Russia before 2027?"
  current_price: 0.2
  volume_24h_usd: 4918.67937
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a 20% probability Ukraine signs a peace deal with Russia before 2027."
  - "Active Ukrainian drone strikes on Moscow run directly counter to Trump's 'getting closer' optimism; the 20% reading reflects the market absorbing both signals without conviction."
  - "A companion Polymarket contract on Zelensky leaving the Ukrainian presidency by end of 2026 sits at 10%, indicating markets do not see leadership change as a near-term peace catalyst."
  - "Polymarket resolves via UMA oracle; a signed peace agreement is required, not a ceasefire or framework announcement, setting a high bar for the 20% to pay out."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Ukraine launched dozens of drones targeting Moscow as Zelensky vowed more strikes, while Trump separately said a war resolution is getting closer after talks with Putin and Zelensky."
    publisher: "ABC News"
    published_at: "2026-07-07T09:28:47.000Z"
    source_url: "https://abcnews.com/International/dozens-ukrainian-drones-target-moscow-mayor-zelenskyy-vows/story?id=134540012"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ABC News"
        source_url: "https://abcnews.com/International/dozens-ukrainian-drones-target-moscow-mayor-zelenskyy-vows/story?id=134540012"
        retrieved_at: "2026-07-07T10:52:00+00:00"
  - type: "pm_response"
    notes: "Polymarket UMA oracle resolves on a signed deal, not a ceasefire; the 20% pricing reflects the gap between diplomatic optimism and active military escalation."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ABC News: Dozens of Ukrainian drones target Moscow, mayor says, as Zelenskyy vow"
    url: "https://abcnews.com/International/dozens-ukrainian-drones-target-moscow-mayor-zelenskyy-vows/story?id=134540012"
    published_at: "2026-07-07T09:28:47.000Z"
    retrieved_at: "2026-07-07T10:52:00+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
