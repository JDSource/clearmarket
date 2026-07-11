---
signal_id: "CMSIG2026071006"
signal_slug: "housing-investment-restriction-law-kalshi-100-2026-07-10"
headline: "Housing investment restriction law: Kalshi 100%"
semantic_title: "Institutional housing investment bill nears full resolution pricing"
telemetry: "Kalshi 100%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "lagging"
published_at: "2026-07-10T15:53:35.000Z"
event_id: "CM-EVT-HH1QMWSWC1"
event_slug: "kxhfhousing-27"
event_question: "Will legislation restricting institutional single-family home investment become law? (multi-deadline series, 2026-2027)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHFHOUSING-27"
  question_raw: "Will a bill become law taxing or banning hedge funds from owning homes before election day?"
  current_price: 0.996
  volume_24h_usd: 9462.91
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-01-08T15:00:00Z"
bullets:
  - "The Kalshi contract on legislation restricting institutional single-family home investment becoming law is priced at 100%, with trading volume up 64x day over day."
  - "The bill's automatic enactment via the ten-day pocket-unsigned rule is now confirmed, making this a resolved or near-resolved event; the 100% price reflects that certainty."
  - "The volume surge of 64x suggests traders rushed to close or settle positions following the confirmed enactment news, not to open new directional bets."
  - "Resolves via Library of Congress legislative record; the resolution source will confirm enactment date, with no veto or pocket-veto ambiguity remaining."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The bipartisan housing bill restricting institutional single-family home investment became law automatically after Trump refused to sign it in protest over the absence of a GOP voter ID provision."
    publisher: "Chantelle Lee"
    published_at: "2026-07-10T15:53:35.000Z"
    source_url: "https://time.com/article/2026/07/10/housing-bill-trump/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Chantelle Lee"
        source_url: "https://time.com/article/2026/07/10/housing-bill-trump/"
        retrieved_at: "2026-07-11T09:24:13+00:00"
  - type: "pm_response"
    notes: "Kalshi contract at 100% with 64x volume surge indicates the market has fully absorbed the enactment confirmation; new positions at this level carry no remaining directional edge."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Chantelle Lee: The Bipartisan Housing Bill Is Set to Become Law, Despite Trump’s Refu"
    url: "https://time.com/article/2026/07/10/housing-bill-trump/"
    published_at: "2026-07-10T15:53:35.000Z"
    retrieved_at: "2026-07-11T09:24:13+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
