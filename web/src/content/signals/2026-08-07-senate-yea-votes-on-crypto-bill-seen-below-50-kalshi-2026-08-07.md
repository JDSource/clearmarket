---
signal_id: "CMSIG2026080708"
signal_slug: "senate-yea-votes-on-crypto-bill-seen-below-50-kalshi-2026-08-07"
headline: "Senate Yea votes on crypto bill seen below 50: Kalshi"
semantic_title: "Senate Yea votes on crypto bill seen below 50"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-07T00:00:00.000Z"
event_id: "CM-EVT-CSYS5KPXK6"
event_slug: "kxvoteclarity-26may16"
event_question: "Senate Yea votes on crypto market structure bill"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXVOTECLARITY-26MAY16-T50"
  question_raw: "How many Senate members will vote Yea on a crypto market structure bill (as defined in KXCRYPTOSTRUCTURE)?"
  current_price: 0.4
  volume_24h_usd: 98.16
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi ladder prices Senate Yea votes on a crypto market structure bill below 50: only 40% chance of reaching 50 votes, 32% at 55, dropping to 7% at 66."
  - "The CLARITY Act delay until September is consistent with the sub-50 vote implied range, suggesting the market already doubted passage before the delay was confirmed."
  - "Trump's public praise for Bitcoin alongside the delay adds political complexity; Senate Majority Leader John Thune faces a separate Kalshi contract at 45% on Trump calling for his removal."
  - "Resolution via vote tally from the Senate Parliamentarian as named source; the threshold for passage (50 vs. 60 for cloture) is itself a settlement ambiguity."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "A Senate vote on the CLARITY Act crypto market structure bill was delayed until September after Republican lawmakers had expected it to proceed."
    publisher: "Mathew Di Salvo"
    published_at: "2026-08-07T00:00:00.000Z"
    source_url: "https://bitcoinmagazine.com/news/clarity-act-vote-delayed-trump-bitcoin"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Mathew Di Salvo"
        source_url: "https://bitcoinmagazine.com/news/clarity-act-vote-delayed-trump-bitcoin"
        retrieved_at: "2026-08-10T09:14:34+00:00"
  - type: "pm_response"
    notes: "Kalshi's ladder puts long odds against the crypto bill reaching a filibuster-proof majority, with the September delay reinforcing the market's cautious pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Mathew Di Salvo: Clarity Act Delayed Until September, Trump Praises Bitcoin"
    url: "https://bitcoinmagazine.com/news/clarity-act-vote-delayed-trump-bitcoin"
    published_at: "2026-08-07T00:00:00.000Z"
    retrieved_at: "2026-08-10T09:14:34+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
