---
signal_id: "CMSIG2026102805"
signal_slug: "dems-win-any-texas-statewide-in-2026-kalshi-74-2026-10-28"
headline: "Dems win any Texas statewide in 2026: Kalshi 74%"
semantic_title: "Democrats winning any Texas statewide race stays near 75 percent odds"
telemetry: "Kalshi 74%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-28T03:00:00.000Z"
event_id: "CM-EVT-NQQNC9S0P9"
event_slug: "kxanydemwintexas-26nov03"
event_question: "Will Democrats win any statewide election in Texas in 2026?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXANYDEMWINTEXAS-26NOV03"
  question_raw: "Will the number of Democrats who win a statewide election in Texas in 2026 be above 0?"
  current_price: 0.74
  volume_24h_usd: 160.87
  arbitration_model: "kalshi_staff"
  resolution_source: "The Source Agencies are"
  resolves_at: "2027-11-02T14:00:00Z"
bullets:
  - "Kalshi prices 74% on Democrats winning at least one statewide election in Texas in 2026."
  - "Dueling rally coverage underscores a genuinely competitive Texas Senate race, and the 74% probability reflects markets treating a Democratic win as more likely than not."
  - "At 74%, the market goes further than typical political commentary, which frames this as a long-shot opportunity rather than a probable outcome."
  - "Resolves via named Source Agencies; the Texas Senate race is the primary catalyst, but any statewide win qualifies."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Democrat James Talarico and President Donald Trump held dueling Texas Senate rallies, with Democrats calling the race their best Texas chance in a generation."
    publisher: "Natasha Korecki, Peter Nicholas"
    published_at: "2026-10-28T03:00:00.000Z"
    source_url: "https://www.nbcnews.com/politics/2026-election/james-talarico-faces-trump-dueling-texas-rallies-elections-final-days-rcna605629"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Natasha Korecki, Peter Nicholas"
        source_url: "https://www.nbcnews.com/politics/2026-election/james-talarico-faces-trump-dueling-texas-rallies-elections-final-days-rcna605629"
        retrieved_at: "2026-10-28T07:49:08+00:00"
  - type: "pm_response"
    notes: "Kalshi at 74% is a notably high probability for Democratic Texas success; the contract's broad definition (any statewide win) may be driving the elevated pricing relative to individual race odds."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Natasha Korecki, Peter Nicholas: James Talarico faces off against Trump in dueling Texas rallies in ele"
    url: "https://www.nbcnews.com/politics/2026-election/james-talarico-faces-trump-dueling-texas-rallies-elections-final-days-rcna605629"
    published_at: "2026-10-28T03:00:00.000Z"
    retrieved_at: "2026-10-28T07:49:08+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
