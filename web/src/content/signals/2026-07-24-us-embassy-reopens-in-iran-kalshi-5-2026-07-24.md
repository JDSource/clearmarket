---
signal_id: "CMSIG2026072406"
signal_slug: "us-embassy-reopens-in-iran-kalshi-5-2026-07-24"
headline: "US embassy reopens in Iran: Kalshi 5%"
semantic_title: "US embassy reopening in Iran stays a heavy long shot at 5%"
telemetry: "Kalshi 5%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-24T00:00:00.000Z"
event_id: "CM-EVT-34SYT4T2T1"
event_slug: "kxiranembassy-27"
event_question: "Will the United States reopen its embassy in Iran?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXIRANEMBASSY-27"
  question_raw: "Will the US reopen its embassy in Iran before Jan 1, 2027?"
  current_price: 0.051
  volume_24h_usd: 19.18
  arbitration_model: "kalshi_staff"
  resolution_source: "The New York Times"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices only 5% on the US reopening its embassy in Iran, a strong diplomatic normalization marker that the market firmly rejects."
  - "Iran's rejection of the Iraqi-brokered ceasefire proposal is fully consistent with the near-zero embassy probability; the market sees no diplomatic off-ramp in sight."
  - "Polymarket (CM-EVT-WD982793G1) prices a 29% chance the US invades Iran outright before 2027, this higher probability on escalation versus the 5% on normalization illustrates the market's asymmetric war-scenario lean."
  - "Kalshi resolves via The New York Times; embassy reopening is a lagging diplomatic indicator that requires ceasefire, deal, and formal restoration of relations, all currently near zero probability."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Iran rejected a US ceasefire proposal conveyed by Iraqi Prime Minister Ali al-Zaidi after his meeting with President Donald Trump, as strikes continued for a 13th night."
    publisher: "timesnownews.com"
    published_at: "2026-07-24T00:00:00.000Z"
    source_url: "https://www.timesnownews.com/world/middle-east/trumps-ceasefire-bid-collapses-iran-rejects-iraqi-brokered-us-proposal-article-155160592"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "timesnownews.com"
        source_url: "https://www.timesnownews.com/world/middle-east/trumps-ceasefire-bid-collapses-iran-rejects-iraqi-brokered-us-proposal-article-155160592"
        retrieved_at: "2026-07-24T10:13:15+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via The New York Times; the 5% price is directionally consistent with all Iran-deal and Hormuz markets in this dataset."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "timesnownews.com: Trump's Ceasefire Bid Collapses: Iran Rejects Iraqi-Brokered US Propos"
    url: "https://www.timesnownews.com/world/middle-east/trumps-ceasefire-bid-collapses-iran-rejects-iraqi-brokered-us-proposal-article-155160592"
    published_at: "2026-07-24T00:00:00.000Z"
    retrieved_at: "2026-07-24T10:13:15+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
