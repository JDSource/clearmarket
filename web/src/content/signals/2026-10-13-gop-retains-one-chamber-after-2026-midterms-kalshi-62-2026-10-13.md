---
signal_id: "CMSIG2026101306"
signal_slug: "gop-retains-one-chamber-after-2026-midterms-kalshi-62-2026-10-13"
headline: "GOP retains one chamber after 2026 midterms: Kalshi 62%"
semantic_title: "Republicans holding at least one chamber stays near 62%"
telemetry: "Kalshi 62%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-13T00:00:00.000Z"
event_id: "CM-EVT-T5VXKJT451"
event_slug: "kxbalancepowercombo-27feb"
event_question: "Will Republicans control at least one chamber of Congress after the 2026 midterm elections?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBALANCEPOWERCOMBO-27FEB-DD"
  question_raw: "Will House Control be Democratic AND Senate Control be Democratic for Feb 2027?"
  current_price: 0.62
  volume_24h_usd: 30935.42
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "The Kalshi contract prices 62% on Republicans controlling at least one chamber of Congress after the 2026 midterms."
  - "Trump's Alaska rally and the Guilfoyle resignation underscore GOP concern about retaining Congress, consistent with a market short of full conviction at 62%."
  - "A companion Kalshi contract (CM-EVT-CRMKQSR4R6) prices 91% on a new Montana senator being elected, flagging one competitive seat already likely to flip."
  - "Resolves via Bureau of Labor Statistics per the named source, though the operative data is the congressional election outcome on November 3."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump traveled to Alaska to campaign for Republican Senator Dan Sullivan while Ambassador Kimberly Guilfoyle resigned amid allegations of improper conduct, signaling GOP anxiety before November 3."
    publisher: "apnews.com"
    published_at: "2026-10-13T00:00:00.000Z"
    source_url: "https://apnews.com/article/trump-corruption-election-putin-zacharia-aa4ec095692c57a851a942c0f21624f7"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "apnews.com"
        source_url: "https://apnews.com/article/trump-corruption-election-putin-zacharia-aa4ec095692c57a851a942c0f21624f7"
        retrieved_at: "2026-10-16T07:47:56+00:00"
  - type: "pm_response"
    notes: "Kalshi at 62% places Republicans as modest favorites to hold at least one chamber, reflecting competitive midterm conditions rather than a foregone outcome."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "apnews.com: The Latest: Ambassador Kimberly Guilfoyle resigns, vows to challenge a"
    url: "https://apnews.com/article/trump-corruption-election-putin-zacharia-aa4ec095692c57a851a942c0f21624f7"
    published_at: "2026-10-13T00:00:00.000Z"
    retrieved_at: "2026-10-16T07:47:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
