---
signal_id: "CMSIG2026062406"
signal_slug: "proof-of-citizenship-for-federal-voter-registration-kalshi-1-2026-06-24"
headline: "Proof of citizenship for federal voter registration: Kalshi 15%"
semantic_title: "Proof-of-citizenship voter registration fractures against passage"
telemetry: "Kalshi 15%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-24T15:28:58.000Z"
event_id: "CM-EVT-G8CYMWNWC6"
event_slug: "kxelectionbill"
event_question: "Will proof of citizenship be required for federal voter registration?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXELECTIONBILL-27JAN01"
  question_raw: "Will legislation that requires proof of U.S. citizenship as a condition of registering to vote in federal elections become law before Jan 1, 2027?"
  current_price: 0.15
  volume_24h_usd: 46.86
  arbitration_model: "kalshi_staff"
  resolution_source: "White House"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prices only 15% on proof of citizenship becoming a federal voter registration requirement, resolving via the White House."
  - "Trump's threat to hold the housing bill hostage over the SAVE Act is not moving the market; 15% reflects the Senate vote-count obstacle reported in news coverage."
  - "A separate story (Story 14) reports Trump subsequently caved and agreed to transmit the housing bill without the SAVE Act passing, consistent with the low 15% market price."
  - "Resolves via White House confirmation of a signed law or executive order; the market is pricing the SAVE Act as a negotiating tool, not a likely legislative outcome."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump linked his signature on a bipartisan housing bill to Congress passing the SAVE Act, which would require proof of citizenship for federal voter registration, but the bill lacks Senate votes."
    publisher: "nbcnewyork.com"
    published_at: "2026-06-24T15:28:58.000Z"
    source_url: "https://www.nbcnewyork.com/news/national-international/trump-housing-bill-voter-id/6517594/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "nbcnewyork.com"
        source_url: "https://www.nbcnewyork.com/news/national-international/trump-housing-bill-voter-id/6517594/"
        retrieved_at: "2026-06-27T10:02:20+00:00"
  - type: "pm_response"
    notes: "Kalshi contract on proof-of-citizenship voter registration requirement; the 15% price is consistent with the reported Senate vote-count failure and Trump's subsequent cave on the housing bill linkage."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "nbcnewyork.com: Trump won’t sign housing bill without Congress passing voter ID, NBC"
    url: "https://www.nbcnewyork.com/news/national-international/trump-housing-bill-voter-id/6517594/"
    published_at: "2026-06-24T15:28:58.000Z"
    retrieved_at: "2026-06-27T10:02:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
