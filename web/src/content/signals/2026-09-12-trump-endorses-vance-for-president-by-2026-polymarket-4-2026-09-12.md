---
signal_id: "CMSIG2026091204"
signal_slug: "trump-endorses-vance-for-president-by-2026-polymarket-4-2026-09-12"
headline: "Trump endorses Vance for president by 2026: Polymarket 4%"
semantic_title: "Trump endorsing Vance for president before 2027 stays a long shot"
telemetry: "Polymarket 4%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-12T00:00:00.000Z"
event_id: "CM-EVT-VYGG3P41R5"
event_slug: "will-trump-endorse-jd-vance-for-president-before-2027"
event_question: "Will Trump endorse JD Vance for president before 2027?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9c414cb64000dc7645b2bba8d7586746f3ddb1cfd1b564769188b81cd63ad667"
  question_raw: "Will Trump endorse JD Vance for president before 2027?"
  current_price: 0.04
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts only 4% on Trump endorsing JD Vance for president before 2027, treating the outcome as a clear long shot."
  - "Vance's high-profile Dallas convention role generated successor speculation, but the market is not pricing a Trump endorsement as remotely likely in this window."
  - "The Polymarket contract on Trump ceasing to be president before 2027 sits at 6%, so the low Vance endorsement odds are consistent with a market that expects Trump to remain in office and retain optionality."
  - "Polymarket resolves via UMA oracle; early endorsement would require a Trump public statement explicitly backing Vance for the presidency before calendar year-end."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Vice President JD Vance played a prominent midterm surrogate role at the Dallas GOP convention, fueling succession speculation."
    publisher: "Steve Contorno"
    published_at: "2026-09-12T00:00:00.000Z"
    source_url: "https://www.cnn.com/2026/09/12/politics/jd-vance-midterm-elections-trump-rubio"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Steve Contorno"
        source_url: "https://www.cnn.com/2026/09/12/politics/jd-vance-midterm-elections-trump-rubio"
        retrieved_at: "2026-09-12T11:56:19+00:00"
  - type: "pm_response"
    notes: "Polymarket at 4% prices the endorsement as effectively a tail risk, not a base case despite Vance's elevated midterm profile."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Steve Contorno: JD Vance embraces tricky role as Trump’s midterm messenger, and poten"
    url: "https://www.cnn.com/2026/09/12/politics/jd-vance-midterm-elections-trump-rubio"
    published_at: "2026-09-12T00:00:00.000Z"
    retrieved_at: "2026-09-12T11:56:19+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
