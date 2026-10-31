---
signal_id: "CMSIG2026103005"
signal_slug: "gop-holds-more-governorships-after-midterms-kalshi-84-2026-10-30"
headline: "GOP holds more governorships after midterms: Kalshi 84%"
semantic_title: "Republicans stay heavily favored to hold more governorships"
telemetry: "Kalshi 84%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-30T15:00:00.000Z"
event_id: "CM-EVT-4DFCBXLZN6"
event_slug: "kxgovwins-27jan01"
event_question: "Will Republicans hold more governorships than Democrats after the midterms?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXGOVWINS-27JAN01-R-50"
  question_raw: "Will the difference between the number of Republican governors and the number of Democratic governors be between -50 and -1 governors after the 2026 midterms?"
  current_price: 0.84
  volume_24h_usd: 11655.8
  arbitration_model: "kalshi_staff"
  resolution_source: "the Statistical Review of World Energy"
  resolves_at: "2027-04-01T15:00:00Z"
bullets:
  - "Kalshi prices Republicans holding more governorships than Democrats after the 2026 midterms at 84%, with trading volume up 4,689% day-over-day."
  - "The surge in trading volume signals fresh market attention as Election Day approaches, consistent with the AP's crossroads framing."
  - "Multiple companion Kalshi governor contracts, Alabama at 93%, Pennsylvania at 98%, Oklahoma at 90%, anchor the GOP's structural advantage in the tally."
  - "Resolution via the Statistical Review of World Energy (named source); final governorship counts determined by official state election results."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "AP and PBS report both parties at a crossroads as midterms approach, with GOP gubernatorial dominance under scrutiny."
    publisher: "Steve Peoples, Associated Press"
    published_at: "2026-10-30T15:00:00.000Z"
    source_url: "https://www.pbs.org/newshour/politics/a-midterm-crossroads-for-both-parties-eyeing-the-beginning-of-the-end-of-the-trump-era"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Steve Peoples, Associated Press"
        source_url: "https://www.pbs.org/newshour/politics/a-midterm-crossroads-for-both-parties-eyeing-the-beginning-of-the-end-of-the-trump-era"
        retrieved_at: "2026-10-31T07:48:23+00:00"
  - type: "pm_response"
    notes: "Kalshi's 84% with a 47.9x volume spike is the clearest signal of late-cycle conviction on Republican gubernatorial dominance heading into Election Day."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Steve Peoples, Associated Press: A midterm crossroads for both parties eyeing the beginning of the end"
    url: "https://www.pbs.org/newshour/politics/a-midterm-crossroads-for-both-parties-eyeing-the-beginning-of-the-end-of-the-trump-era"
    published_at: "2026-10-30T15:00:00.000Z"
    retrieved_at: "2026-10-31T07:48:23+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
