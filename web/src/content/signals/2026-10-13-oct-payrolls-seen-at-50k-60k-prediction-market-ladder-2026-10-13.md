---
signal_id: "CMSIG2026101303"
signal_slug: "oct-payrolls-seen-at-50k-60k-prediction-market-ladder-2026-10-13"
headline: "Oct payrolls seen at 50K-60K: prediction market ladder"
semantic_title: "October payrolls implied range holds at 50K to 60K jobs"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-13T00:00:00.000Z"
event_id: "CM-EVT-6CSLHX0K76"
event_slug: "kxpayrolls-26oct"
event_question: "October 2026 nonfarm payrolls added"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26OCT-T60000"
  question_raw: "Will above 60000 jobs be added in October 2026?"
  current_price: 0.43
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-02-05T15:00:00Z"
bullets:
  - "The prediction market ladder implies October payrolls in the 50K-60K range: 56% above 50K but only 43% above 60K."
  - "The September miss of 29K (Story 3) is lagging news; the market prices October at a modest recovery, not a sustained collapse."
  - "The 86% probability above zero shows the market firmly rejects an outright contraction in October despite the September shock."
  - "Resolution uses the BLS Employment Situation report; single-month payroll prints are often revised, which may explain the market's above-zero confidence."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Atlanta Fed noted September nonfarm payrolls rose only 29,000, flagging broad labor market softness beyond health care."
    publisher: "Lei Fang Research Economist, Associate Adviser"
    published_at: "2026-10-13T00:00:00.000Z"
    source_url: "https://www.atlantafed.org/research-and-data/publications/policy-hub-macroblog/2026/10/13/beyond-health-care-has-labor-market-improvement-broadened-in-2026"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Lei Fang Research Economist, Associate Adviser"
        source_url: "https://www.atlantafed.org/research-and-data/publications/policy-hub-macroblog/2026/10/13/beyond-health-care-has-labor-market-improvement-broadened-in-2026"
        retrieved_at: "2026-10-14T07:47:32+00:00"
  - type: "pm_response"
    notes: "Prediction market ladder; the implied 50K-60K range represents a partial bounce from September's weak print but remains well below trend."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Lei Fang Research Economist, Associate Adviser: Beyond Health Care: Has Labor Market Improvement Broadened in 2026? -"
    url: "https://www.atlantafed.org/research-and-data/publications/policy-hub-macroblog/2026/10/13/beyond-health-care-has-labor-market-improvement-broadened-in-2026"
    published_at: "2026-10-13T00:00:00.000Z"
    retrieved_at: "2026-10-14T07:47:32+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
