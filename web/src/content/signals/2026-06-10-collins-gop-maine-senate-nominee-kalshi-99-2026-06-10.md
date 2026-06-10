---
signal_id: "CMSIG2026061008"
signal_slug: "collins-gop-maine-senate-nominee-kalshi-99-2026-06-10"
headline: "Collins GOP Maine Senate nominee: Kalshi 99%"
semantic_title: "Collins as Maine GOP Senate nominee fully absorbed into pricing"
telemetry: "Kalshi 99%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-06-10T02:11:22.000Z"
event_id: "CM-EVT-FJC909J0Z4"
event_slug: "kxsenatemer-26"
event_question: "Will Susan Collins be the Republican nominee for the Senate in Maine?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXSENATEMER-26-SCOL"
  question_raw: "Will Susan Collins be the Republican nominee for the Senate in Maine?"
  current_price: 0.99
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "Republican Party"
  resolves_at: "2026-11-03T15:00:00Z"
bullets:
  - "Kalshi prices Susan Collins as the Republican Senate nominee for Maine at 99%, reflecting the primary result as a near-done resolution."
  - "Platner's primary win confirms the Collins matchup; the 99% is fully consistent with Collins having secured her own nomination on the same night."
  - "The broader Senate control question is priced separately: Kalshi puts Republicans winning the Senate at 79% (CM-EVT-S6Y29BSL46 Kansas race), with Maine as one of the competitive seats that shapes that outcome."
  - "Resolves via Republican Party official nominee designation; no credible challenger remaining after primary night makes this effectively settled."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Democrat Graham Platner won the Maine Democratic primary, setting up a high-stakes November Senate race against Republican incumbent Susan Collins."
    publisher: "yahoo.com"
    published_at: "2026-06-10T02:11:22.000Z"
    source_url: "https://www.yahoo.com/news/politics/articles/graham-platner-win-maine-democratic-014446949.html"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "yahoo.com"
        source_url: "https://www.yahoo.com/news/politics/articles/graham-platner-win-maine-democratic-014446949.html"
        retrieved_at: "2026-06-10T11:36:47+00:00"
  - type: "pm_response"
    notes: "Kalshi's 99% on Collins as GOP nominee is lagging the primary result, functioning as a settlement-pending price rather than a forward signal; the live question now is the general-election outcome."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "yahoo.com: Graham Platner to win Maine Democratic Senate primary and face Sen. Su"
    url: "https://www.yahoo.com/news/politics/articles/graham-platner-win-maine-democratic-014446949.html"
    published_at: "2026-06-10T02:11:22.000Z"
    retrieved_at: "2026-06-10T11:36:47+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
