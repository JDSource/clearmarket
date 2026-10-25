---
signal_id: "CMSIG2026102505"
signal_slug: "dems-win-senate-control-2026-polymarket-67-2026-10-25"
headline: "Dems win Senate control 2026: Polymarket 67%"
semantic_title: "Democrats stay favored to win Senate control in 2026"
telemetry: "Polymarket 67%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-25T02:00:00.000Z"
event_id: "CM-EVT-M9WJY06T90"
event_slug: "which-party-will-win-the-senate-in-2026"
event_question: "Which party will win control of the U.S. Senate in the 2026 election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x307a1ed89d60b61002dd5bbf00e1408c5ed2ab3fcdb056191ca7ef9bc34d38f3"
  question_raw: "Will the Democratic Party control the Senate after the 2026 Midterm elections?"
  current_price: 0.67
  volume_24h_usd: 72579.791255
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket puts 67% odds on Democrats winning Senate control in the 2026 election, resolving via UMA oracle."
  - "Obama's active campaign presence on economic and foreign policy grounds is consistent with a Democratic advantage in Senate races, as the market currently prices."
  - "The Polymarket contract at 67% aligns with the Iowa Senate race Kalshi contract (CM-EVT-R8V0583H75) at 59% for the Republican candidate, a key battleground where Dems need to hold."
  - "Resolution via UMA oracle after official election results; the November 2026 midterms are priced at 87% to occur on schedule per Kalshi (CM-EVT-HT9T7KMRT5)."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Former President Barack Obama is actively campaigning for Democrats ahead of the November midterms, attacking the Trump administration on the Iran war and consumer prices."
    publisher: "Max Matza"
    published_at: "2026-10-25T02:00:00.000Z"
    source_url: "https://www.bbc.com/news/articles/cmj6jwe1j1gjo"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Max Matza"
        source_url: "https://www.bbc.com/news/articles/cmj6jwe1j1gjo"
        retrieved_at: "2026-10-25T07:48:12+00:00"
  - type: "pm_response"
    notes: "Polymarket carries the Senate control contract at 67% for Democrats; Kalshi's individual race contracts provide a cross-check on the competitive map."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Max Matza: Obama attacks Trump as he campaigns for Democrats ahead of midterm ele"
    url: "https://www.bbc.com/news/articles/cmj6jwe1j1gjo"
    published_at: "2026-10-25T02:00:00.000Z"
    retrieved_at: "2026-10-25T07:48:12+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
