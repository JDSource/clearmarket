---
signal_id: "CMSIG2026092104"
signal_slug: "gop-holds-at-least-one-chamber-kalshi-64-2026-09-21"
headline: "GOP holds at least one chamber: Kalshi 64%"
semantic_title: "Republicans holding Congress odds stay near 50%"
telemetry: "Kalshi 64%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-21T07:46:31.893Z"
event_id: "CM-EVT-T5VXKJT451"
event_slug: "kxbalancepowercombo-27feb"
event_question: "Will Republicans control at least one chamber of Congress after the 2026 midterm elections?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBALANCEPOWERCOMBO-27FEB-DD"
  question_raw: "Will House Control be Democratic AND Senate Control be Democratic for Feb 2027?"
  current_price: 0.64
  volume_24h_usd: 60540.82
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "The Kalshi contract on Republicans controlling at least one chamber after the 2026 midterms prices at 64%."
  - "The NBC poll showing voter dissatisfaction with Trump's economic management is only partially reflected; the market still gives Republicans a clear edge at 64%."
  - "The 64% reading suggests the market is weighing Republican cash advantages and Democratic unpopularity against unfavorable presidential approval ratings."
  - "Resolves via Bureau of Labor Statistics, though the named source appears to be a placeholder; actual resolution would be official congressional certification."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "An NBC News poll finds most voters say Trump has hurt the economy, creating a difficult environment for Republicans, though the Democratic Party remains unpopular and the congressional race is tighter than the first Trump midterm."
    publisher: "NBC News"
    published_at: "2026-09-21T07:46:31.893Z"
    source_url: "https://www.nbcnews.com/politics/2026-election/poll-voters-say-trump-hurt-economy-competitive-midterm-election-looms-rcna597868"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "NBC News"
        source_url: "https://www.nbcnews.com/politics/2026-election/poll-voters-say-trump-hurt-economy-competitive-midterm-election-looms-rcna597868"
        retrieved_at: "2026-09-23T07:47:29+00:00"
  - type: "pm_response"
    notes: "Kalshi prices Republicans holding at least one congressional chamber at 64%, a moderate lean that does not fully reflect the bearish poll signals for the GOP."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "NBC News: Poll: Most voters say Trump has hurt the economy as competitive midter"
    url: "https://www.nbcnews.com/politics/2026-election/poll-voters-say-trump-hurt-economy-competitive-midterm-election-looms-rcna597868"
    published_at: "2026-09-21T07:46:31.893Z"
    retrieved_at: "2026-09-23T07:47:29+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
