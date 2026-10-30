---
signal_id: "CMSIG2026102903"
signal_slug: "alaska-gov-senate-combo-kalshi-4-volume-up-87x-2026-10-29"
headline: "Alaska Gov-Senate combo: Kalshi 4%, volume up 87x"
semantic_title: "Alaska governor-Senate split combo stays a long shot"
telemetry: "Kalshi 4%"
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
  current_price: 0.04
  volume_24h_usd: 36.26
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-11-03T15:00:00Z"
bullets:
  - "Kalshi prices the Alaska governor-Senate party-combo outcome at just 4%, keeping it a heavy long shot despite late-race drama."
  - "Trading volume on this Kalshi contract surged 8,669% day-over-day, signaling a sharp spike in attention around the DOJ subpoena and Peltola controversy."
  - "A separate Kalshi contract on Alaska electing a new senator sits at 31%, suggesting the market sees incumbent retention as more likely than a flip."
  - "Kalshi resolves via United States Congress certification of results; late-breaking DOJ subpoenas alone do not change the resolution mechanic."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Justice Department issued pre-election subpoenas in Alaska as Democrat Mary Peltola denied ballot controversy accusations in the Senate race."
    publisher: "Bridget Brown, Michael Warren, Luena Rodriguez-Feo Vileira, Carley Petesch, Lisa Marie Pane"
    published_at: "2026-10-29T07:02:00.000Z"
    source_url: "https://apnews.com/live/trump-midterm-elections-news-updates-10-29-2026"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Bridget Brown, Michael Warren, Luena Rodriguez-Feo Vileira, Carley Petesch, Lisa Marie Pane"
        source_url: "https://apnews.com/live/trump-midterm-elections-news-updates-10-29-2026"
        retrieved_at: "2026-10-30T14:47:28+00:00"
  - type: "pm_response"
    notes: "The 87x volume surge on the Alaska combo contract is the strongest attention signal in this news cycle, but the 4% price shows the market is not pricing in a dramatic outcome shift."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Bridget Brown, Michael Warren, Luena Rodriguez-Feo Vileira, Carley Petesch, Lisa Marie Pane: Justice Department issues subpoenas in California, Alaska | AP News"
    url: "https://apnews.com/live/trump-midterm-elections-news-updates-10-29-2026"
    published_at: "2026-10-29T07:02:00.000Z"
    retrieved_at: "2026-10-30T14:47:28+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
