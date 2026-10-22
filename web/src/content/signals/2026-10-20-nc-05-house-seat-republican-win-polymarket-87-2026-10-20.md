---
signal_id: "CMSIG2026102007"
signal_slug: "nc-05-house-seat-republican-win-polymarket-87-2026-10-20"
headline: "NC-05 House seat Republican win: Polymarket 87%"
semantic_title: "Republican holds NC-05 House seat stays heavily favored"
telemetry: "Polymarket 87%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-20T00:00:00.000Z"
event_id: "CM-EVT-1WW8223651"
event_slug: "nc-05-house-election-winner"
event_question: "Will the NC-05 House seat be won by a Republican in the 2026 election?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xc4f1456dc523bfe110e6a2afc7c2144ef3925650e78fa826d2211ddae6763a3d"
  question_raw: "Will the Republican Party win the NC-05 House seat?"
  current_price: 0.87
  volume_24h_usd: 9.89
  arbitration_model: "uma_oracle"
  resolves_at: "2026-11-03T00:00:00Z"
bullets:
  - "Polymarket prices a Republican win in North Carolina's 5th Congressional District at 87%, a strong favorite reading ahead of the November 3 midterms."
  - "Trump's in-state rally reinforces but does not move the already heavy Republican advantage the market has priced into the NC-05 seat."
  - "Companion Polymarket contracts in nearby North Carolina districts, NC-03 at 81% Republican (CM-EVT-MCNRMD34V7) and NC-07 at 80% Republican (CM-EVT-9L1SW3NVQ0), show a consistent statewide lean."
  - "Resolves via UMA oracle on election night or certified results; all three NC contracts show the market pricing a Republican sweep of contested state districts."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump campaigned in North Carolina as part of a final GOP midterm push, with $5,000 checks deployed as a turnout tool even as some Republican voters expressed skepticism."
    publisher: "The Associated Press"
    published_at: "2026-10-20T00:00:00.000Z"
    source_url: "https://apnews.com/article/trump-ukraine-zelenskyy-congress-midterm-elections-a298dcb9327bbad29c0bcc9e61955edb"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "The Associated Press"
        source_url: "https://apnews.com/article/trump-ukraine-zelenskyy-congress-midterm-elections-a298dcb9327bbad29c0bcc9e61955edb"
        retrieved_at: "2026-10-22T07:47:56+00:00"
  - type: "pm_response"
    notes: "Polymarket NC-05 contract at 87%; NC-03 at 81% and NC-07 at 80% form a coherent statewide Republican pricing cluster, consistent with Trump's defensive-rally framing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "The Associated Press: The Latest: Trump to campaign in North Carolina as part of final GOP p"
    url: "https://apnews.com/article/trump-ukraine-zelenskyy-congress-midterm-elections-a298dcb9327bbad29c0bcc9e61955edb"
    published_at: "2026-10-20T00:00:00.000Z"
    retrieved_at: "2026-10-22T07:47:56+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
