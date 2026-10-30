---
signal_id: "CMSIG2026102906"
signal_slug: "alaska-gov-senate-gop-combo-kalshi-3-2026-10-29"
headline: "Alaska Gov-Senate GOP combo: Kalshi 3%"
semantic_title: "Alaska Governor-Senate GOP combo stays near zero odds"
telemetry: "Kalshi 3%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-29T07:02:00.000Z"
event_id: "CM-EVT-09C696KZH3"
event_slug: "kxaksengovcombo-26nov"
event_question: "Alaska Governor-Senate combo"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXAKSENGOVCOMBO-26NOV-REPDEM"
  question_raw: "Will Alaska Governor winner be Republican party and Alaska Senate winner be Democratic party?"
  current_price: 0.03
  volume_24h_usd: 265.08
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-11-03T15:00:00Z"
bullets:
  - "The Kalshi contract on a Republican Alaska Governor-Senate combo sits at just 3%, even as federal subpoenas roil the race."
  - "Trading volume on this contract rose 8,669% day over day, indicating the DOJ subpoenas and Peltola investigation headlines are drawing heavy market attention."
  - "Despite the political turbulence, the market is not repricing toward a Republican sweep in Alaska, the probability holds near zero."
  - "The Kalshi contract on a new senator being elected in Alaska (CM-EVT-KQWMXB6NX7) sits at 31%, suggesting the market sees some Democratic vulnerability but not a full Republican flip."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Justice Department issued subpoenas in Alaska days before the midterms, amid a campaign investigation and calls for prosecution of Democratic Senate candidate Mary Peltola."
    publisher: "Bridget Brown, Michael Warren, Luena Rodriguez-Feo Vileira, Carley Petesch, Lisa Marie Pane"
    published_at: "2026-10-29T07:02:00.000Z"
    source_url: "https://apnews.com/live/trump-midterm-elections-news-updates-10-29-2026"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Bridget Brown, Michael Warren, Luena Rodriguez-Feo Vileira, Carley Petesch, Lisa Marie Pane"
        source_url: "https://apnews.com/live/trump-midterm-elections-news-updates-10-29-2026"
        retrieved_at: "2026-10-30T07:48:00+00:00"
  - type: "pm_response"
    notes: "Kalshi prices the Alaska Republican sweep at 3% despite a dramatic volume spike, indicating the DOJ news drew attention without shifting consensus odds."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Bridget Brown, Michael Warren, Luena Rodriguez-Feo Vileira, Carley Petesch, Lisa Marie Pane: Justice Department issues subpoenas in California, Alaska | AP News"
    url: "https://apnews.com/live/trump-midterm-elections-news-updates-10-29-2026"
    published_at: "2026-10-29T07:02:00.000Z"
    retrieved_at: "2026-10-30T07:48:00+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
