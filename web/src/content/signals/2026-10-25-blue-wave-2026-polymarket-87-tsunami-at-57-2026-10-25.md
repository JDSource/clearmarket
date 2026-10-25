---
signal_id: "CMSIG2026102506"
signal_slug: "blue-wave-2026-polymarket-87-tsunami-at-57-2026-10-25"
headline: "Blue wave 2026: Polymarket 87%, tsunami at 57%"
semantic_title: "Blue wave in 2026 stays heavily favored on Polymarket"
telemetry: "Polymarket 87%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-25T07:02:00.000Z"
event_id: "CM-EVT-4N4F192YB2"
event_slug: "blue-wave-in-2026"
event_question: "Will there be a blue wave in 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xed4fd09a24f20a3afc1d722ace811fffff3cffd9a56a3fbffc47f4d3d47a88ed"
  question_raw: "Blue wave in 2026?"
  current_price: 0.87
  volume_24h_usd: 1303.538572
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-30T00:00:00Z"
bullets:
  - "Polymarket prices an 87% chance of a blue wave in 2026, while Kalshi's blue tsunami contract (CM-EVT-6CY3Y4C610) sits lower at 57%."
  - "The framing of the midterms as a referendum on the Trump administration is consistent with strong Democratic market odds, though the definition gap between 'wave' and 'tsunami' explains the spread."
  - "The 30-point gap between Polymarket's blue wave (87%) and Kalshi's blue tsunami (57%) likely reflects definitional thresholds, tsunami implying a larger seat-gain threshold."
  - "Polymarket's Democrats-win-all-four-core-Senate-races contract (CM-EVT-P54SDG6NP7) sits at 62%, the tightest constraint on the full wave scenario."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "A Guardian analysis frames the US midterms as one of four pivotal global elections in 10 days where democratic norms are at stake, with authoritarian backsliding as the central question."
    publisher: "Julian Borger senior international correspondent"
    published_at: "2026-10-25T07:02:00.000Z"
    source_url: "https://www.theguardian.com/world/ng-interactive/2026/oct/25/ten-days-shake-world-democratic-norms-pivotal-elections-brazil-israel-serbia-us"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Julian Borger senior international correspondent"
        source_url: "https://www.theguardian.com/world/ng-interactive/2026/oct/25/ten-days-shake-world-democratic-norms-pivotal-elections-brazil-israel-serbia-us"
        retrieved_at: "2026-10-25T07:48:12+00:00"
  - type: "pm_response"
    notes: "Polymarket and Kalshi carry separate blue wave and blue tsunami contracts with materially different resolution definitions, producing a 30-point spread worth monitoring for arbitrage signals."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Julian Borger senior international correspondent: Ten days that could shake the world: democratic norms at stake in four"
    url: "https://www.theguardian.com/world/ng-interactive/2026/oct/25/ten-days-shake-world-democratic-norms-pivotal-elections-brazil-israel-serbia-us"
    published_at: "2026-10-25T07:02:00.000Z"
    retrieved_at: "2026-10-25T07:48:12+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
