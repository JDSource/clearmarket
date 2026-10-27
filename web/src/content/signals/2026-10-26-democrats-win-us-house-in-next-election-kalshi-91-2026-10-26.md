---
signal_id: "CMSIG2026102605"
signal_slug: "democrats-win-us-house-in-next-election-kalshi-91-2026-10-26"
headline: "Democrats win US House in next election: Kalshi 91%"
semantic_title: "Democrats taking the House builds toward heavily favored pricing"
telemetry: "Kalshi 91%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-26T20:47:39.000Z"
event_id: "CM-EVT-FV8MR86S63"
event_slug: "controlh-2026"
event_question: "Will the Democratic Party win the U.S. House in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "CONTROLH-2026-D"
  question_raw: "Will Democrats win the House in 2026?"
  current_price: 0.906
  volume_24h_usd: 418418.06
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "The Kalshi prediction market prices an 91% probability that Democrats win the U.S. House in the next election."
  - "The Axios framing of a busy global news week including U.S. midterms is consistent with the heavily Democrat-favored House pricing."
  - "The companion Kalshi contract on Republicans holding at least one chamber (CM-EVT-T5VXKJT451) sits at 64%, implying the Senate is seen as the more likely remaining Republican firewall."
  - "Resolves via the Library of Congress per the named resolution source following certified House election results after November 3."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Axios reports Democrats are eyeing strong midterm prospects with focus on Israel elections, Venezuela, and U.S. congressional races simultaneously."
    publisher: "axios.com"
    published_at: "2026-10-26T20:47:39.000Z"
    source_url: "https://www.axios.com/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "axios.com"
        source_url: "https://www.axios.com/"
        retrieved_at: "2026-10-27T13:54:00+00:00"
  - type: "pm_response"
    notes: "Kalshi at 91% is one of the strongest House calls in the current cycle, consistent with multiple reports describing GOP midterm woes."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "axios.com: Axios - Breaking news, U.S. news and politics, and local news"
    url: "https://www.axios.com/"
    published_at: "2026-10-26T20:47:39.000Z"
    retrieved_at: "2026-10-27T13:54:00+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
