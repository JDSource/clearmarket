---
signal_id: "CMSIG2026100808"
signal_slug: "2026-midterms-held-as-scheduled-polymarket-99-2026-10-08"
headline: "2026 midterms held as scheduled: Polymarket 99%"
semantic_title: "Midterm elections proceeding as scheduled near fully priced in"
telemetry: "Polymarket 99%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-08T00:00:00.000Z"
event_id: "CM-EVT-99YJSN2LN7"
event_slug: "will-the-2026-midterm-elections-happen-as-scheduled"
event_question: "Will the 2026 Midterm Elections happen as scheduled?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd93366079fab7bcb8a03705969822056b76226a48fd5bb7b1475a5b186cf6f07"
  question_raw: "Will the 2026 Midterm Elections happen as scheduled?"
  current_price: 0.99
  volume_24h_usd: 12389.575295
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket prediction market prices the 2026 midterm elections happening as scheduled at 99%."
  - "Trump's explicit pledge not to attack Iran before the midterms removes the most acute near-term disruption risk; the 99% level is consistent with that signal."
  - "Iran's retaliatory missile strikes against Bahrain and Kuwait (Story 28) represent a live escalation risk, but the market has not priced any meaningful disruption probability."
  - "Resolution via uma_oracle; any official postponement or cancellation of the November 3 elections would be required for a NO settlement."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Trump said the US will not attack Iran before the November 3 midterm elections, removing one scenario that could have disrupted the electoral calendar."
    publisher: "Barak Ravid"
    published_at: "2026-10-08T00:00:00.000Z"
    source_url: "https://www.axios.com/2026/10/08/trump-iran-strikes-midterm-elections"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Barak Ravid"
        source_url: "https://www.axios.com/2026/10/08/trump-iran-strikes-midterm-elections"
        retrieved_at: "2026-10-10T07:47:51+00:00"
  - type: "pm_response"
    notes: "Polymarket at 99%; resolves via uma_oracle on whether the elections occur on the scheduled date."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Barak Ravid: Trump: US won't attack Iran before midterms"
    url: "https://www.axios.com/2026/10/08/trump-iran-strikes-midterm-elections"
    published_at: "2026-10-08T00:00:00.000Z"
    retrieved_at: "2026-10-10T07:47:51+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
