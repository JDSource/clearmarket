---
signal_id: "CMSIG2026071807"
signal_slug: "bitcoin-above-100k-by-dec-31-cm-ladder-12-2026-07-18"
headline: "Bitcoin above $100K by Dec 31: CM ladder 12%"
semantic_title: "Bitcoin above dollar 100K by year-end wavers at thin 12 percent"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-07-18T08:54:00.000Z"
event_id: "CM-EVT-0MWN62PNG9"
event_slug: "kxbtcmaxy-26dec31"
event_question: "Bitcoin price by Dec 31, 2026"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBTCMAXY-26DEC31-99999.99"
  question_raw: "Will Bitcoin be above $99,999.99 by Dec 31, 2026 at 11:59 PM ET?"
  current_price: 0.12
  volume_24h_usd: 278.35
  arbitration_model: "kalshi_staff"
  resolution_source: "CF Benchmarks"
  resolves_at: "2027-01-31T04:59:00Z"
bullets:
  - "The ClearMarket ladder prices Bitcoin above $100K by December 31 at only 12%, with probability collapsing further at higher strikes."
  - "A rebound to $64K after the AI-driven selloff leaves Bitcoin well below the $100K threshold, consistent with the market's skeptical distribution."
  - "The ladder shows near-zero probability above $110K (7%), implying the market sees $100K as a hard ceiling for the year-end scenario."
  - "Resolves at December 31, 2026 close via the specified Bitcoin price source in the contract."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Bitcoin rebounded to $64K after an AI-competition-led selloff triggered a broader crypto rout, with the Kimi K3 model beating Claude and GPT in coding benchmarks hitting semiconductor and crypto markets."
    publisher: "economictimes.indiatimes.com"
    published_at: "2026-07-18T08:54:00.000Z"
    source_url: "https://economictimes.indiatimes.com/markets/cryptocurrency/bitcoin-rebounds-to-64k-after-ai-led-selloff-triggers-crypto-rout-heres-what-experts-say/articleshow/132476886.cms"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "economictimes.indiatimes.com"
        source_url: "https://economictimes.indiatimes.com/markets/cryptocurrency/bitcoin-rebounds-to-64k-after-ai-led-selloff-triggers-crypto-rout-heres-what-experts-say/articleshow/132476886.cms"
        retrieved_at: "2026-07-18T09:20:01+00:00"
  - type: "pm_response"
    notes: "ClearMarket ladder at 12% above $100K reflects broad market skepticism that the current $64K level can sustain a 56% rally by year-end."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "economictimes.indiatimes.com: Bitcoin rebounds to $64K after AI-led selloff triggers crypto rout. He"
    url: "https://economictimes.indiatimes.com/markets/cryptocurrency/bitcoin-rebounds-to-64k-after-ai-led-selloff-triggers-crypto-rout-heres-what-experts-say/articleshow/132476886.cms"
    published_at: "2026-07-18T08:54:00.000Z"
    retrieved_at: "2026-07-18T09:20:01+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
