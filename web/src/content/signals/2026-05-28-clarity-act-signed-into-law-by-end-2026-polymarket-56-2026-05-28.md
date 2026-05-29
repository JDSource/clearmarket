---
signal_id: "CMSIG2026052806"
signal_slug: "clarity-act-signed-into-law-by-end-2026-polymarket-56-2026-05-28"
headline: "Clarity Act signed into law by end-2026: Polymarket 56%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-05-28T01:21:04.000Z"
event_id: "CM-EVT-ZXN47LV744"
event_slug: "clarity-act-signed-into-law-in-2026"
event_question: "Will the Clarity Act be signed into law by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9cb23d04b2ded06147482076688b69b487a8d982c63ebdda2ab3678cf27cf390"
  question_raw: "Clarity Act signed into law in 2026?"
  current_price: 0.56
  volume_24h_usd: 3186.318228
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "The Polymarket contract on the Clarity Act being signed into law by end of 2026 sits at 56%, a bare majority that reflects genuine uncertainty about whether legislative action will follow Trump's public pledge."
  - "Trump's vow to deliver a permanent crypto market-structure law is directionally consistent with the 56% reading, but the market is not pricing high confidence -- suggesting prediction-market participants see meaningful risk that Congressional action stalls or the bill's form changes materially before enactment."
  - "The Republican reconciliation difficulties highlighted in Story 14 (a separate $70 billion package stalled over an anti-weaponization fund dispute) provide concrete context for why the market assigns only slim-majority odds despite executive-branch enthusiasm for crypto legislation."
  - "SEC Chair Paul Atkins publicly declaring the era of stifling innovation over (Story 39) is a regulatory complement to Trump's pledge, but neither executive rhetoric nor regulatory posture directly accelerates Congressional passage -- the Polymarket contract at 56% reflects that distinction."
  - "The Polymarket contract resolves via uma_oracle; resolution requires the Clarity Act specifically to be signed into law, meaning a presidential executive order on crypto or a different crypto bill would not satisfy resolution conditions."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "President Donald Trump vowed to cement a durable US crypto market-structure law and pledged his administration would never let crypto down, promising a framework that cannot be undone by future administrations."
    publisher: "Kevin Helms"
    published_at: "2026-05-28T01:21:04.000Z"
    source_url: "https://news.bitcoin.com/trump-vows-crypto-market-structure-law-that-cannot-be-undone/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Kevin Helms"
        source_url: "https://news.bitcoin.com/trump-vows-crypto-market-structure-law-that-cannot-be-undone/"
        retrieved_at: "2026-05-29T21:01:04+00:00"
  - type: "pm_response"
    notes: "Polymarket at 56% on the Clarity Act by year-end captures the gap between Trump's stated intent and the legislative calendar; no companion contract on a 2027 timeline is available in the provided data for term-structure comparison."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Kevin Helms: Trump Vows Crypto Market Structure Law That 'Cannot Be Undone'"
    url: "https://news.bitcoin.com/trump-vows-crypto-market-structure-law-that-cannot-be-undone/"
    published_at: "2026-05-28T01:21:04.000Z"
    retrieved_at: "2026-05-29T21:01:04+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
