---
signal_id: "CMSIG2026091908"
signal_slug: "clarity-act-signed-into-law-2026-polymarket-8-2026-09-19"
headline: "Clarity Act signed into law 2026: Polymarket 8%"
semantic_title: "Clarity Act signed into law by 2026 remains a long shot"
telemetry: "Polymarket 8%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-19T00:00:00.000Z"
event_id: "CM-EVT-ZXN47LV744"
event_slug: "clarity-act-signed-into-law-in-2026"
event_question: "Will the Clarity Act (H.R. 3633) be signed into law by 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x9cb23d04b2ded06147482076688b69b487a8d982c63ebdda2ab3678cf27cf390"
  question_raw: "Clarity Act (H.R.3633) signed into law in 2026?"
  current_price: 0.085
  volume_24h_usd: 234349.622311
  arbitration_model: "uma_oracle"
  resolves_at: "2027-01-01T05:00:00Z"
bullets:
  - "Polymarket puts 8% odds on the Clarity Act being signed into law by 2026."
  - "The Senate failure to advance the bill is consistent with this near-floor pricing; the market had already discounted legislative success before the setback."
  - "The CFTC submitting its own crypto framework to the White House suggests regulatory action is proceeding on an executive track, reducing urgency for legislative action this year."
  - "The Kalshi Senate vote ladder implies fewer than 50 yea votes on a crypto market structure bill, confirming the market does not see the votes available to pass the Clarity Act."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The CLARITY Act failed to advance in the Senate, prompting the SEC and CFTC to move forward with independent crypto regulatory rulemaking as a substitute."
    publisher: "Crypto in America"
    published_at: "2026-09-19T00:00:00.000Z"
    source_url: "https://www.cryptoinamerica.com/p/after-cryptos-bruising-week-on-capitol"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Crypto in America"
        source_url: "https://www.cryptoinamerica.com/p/after-cryptos-bruising-week-on-capitol"
        retrieved_at: "2026-09-19T12:14:43+00:00"
  - type: "pm_response"
    notes: "Polymarket resolves via uma_oracle; the regulatory substitute path via CFTC rulemaking does not appear to affect contract resolution, which requires the specific act to become law."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Crypto in America: After Crypto’s Bruising Week on Capitol Hill, Regulators Pick Up the M"
    url: "https://www.cryptoinamerica.com/p/after-cryptos-bruising-week-on-capitol"
    published_at: "2026-09-19T00:00:00.000Z"
    retrieved_at: "2026-09-19T12:14:43+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
