---
signal_id: "CMSIG2026061104"
signal_slug: "us-iran-nuclear-deal-by-june-30-polymarket-28-2026-06-11"
headline: "US-Iran nuclear deal by June 30: Polymarket 28%"
semantic_title: "US-Iran nuclear deal by June 30 wavers at 28 percent"
telemetry: "Polymarket 28%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-11T22:55:24.000Z"
event_id: "CM-EVT-LG47Z78CF2"
event_slug: "us-iran-nuclear-deal-by-june-30"
event_question: "Will the US and Iran reach a nuclear deal by June 30?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xa70fc3695a65833b91b45df6db6015096f3e1471b70352ca411b4209010e7633"
  question_raw: "US-Iran nuclear deal by June 30?"
  current_price: 0.28
  volume_24h_usd: 207316.77510300005
  arbitration_model: "uma_oracle"
  resolves_at: "2026-06-30T00:00:00Z"
bullets:
  - "Polymarket prices only 28% on the US and Iran reaching a nuclear deal by June 30, despite Trump's claims of imminent agreement."
  - "The market is not embracing Trump's optimism, Tehran's public denial that anything is finalized keeps the probability well below 50% for the near-term deadline."
  - "The July 31 horizon contract (CM-EVT-Y2L01CWLW3) sits at 45%, capturing the spread between Trump's weekend-deal rhetoric and the market's skepticism about the June 30 cutoff."
  - "Resolves via UMA oracle; a signed, publicly confirmed nuclear agreement between the US and Iran must be documented before June 30 to settle YES."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "President Trump called off threatened new Iran strikes and claimed a deal was imminent, while Tehran insisted nothing was finalized."
    publisher: "pbs.org"
    published_at: "2026-06-11T22:55:24.000Z"
    source_url: "https://www.pbs.org/newshour/show/trump-calls-off-threatened-strikes-says-deal-with-iran-is-close"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "pbs.org"
        source_url: "https://www.pbs.org/newshour/show/trump-calls-off-threatened-strikes-says-deal-with-iran-is-close"
        retrieved_at: "2026-06-12T11:42:07+00:00"
  - type: "pm_response"
    notes: "Polymarket contract at 28% is in clear tension with Trump's public claims of a near-done deal, reflecting the market fading the presidential optimism signal."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "pbs.org: Trump calls off threatened strikes, says deal with Iran is close | PBS"
    url: "https://www.pbs.org/newshour/show/trump-calls-off-threatened-strikes-says-deal-with-iran-is-close"
    published_at: "2026-06-11T22:55:24.000Z"
    retrieved_at: "2026-06-12T11:42:07+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
