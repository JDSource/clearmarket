---
signal_id: "CMSIG2026101605"
signal_slug: "fl-25-house-seat-won-by-dems-kalshi-81-vol-surge-2026-10-16"
headline: "FL-25 House seat won by Dems: Kalshi 81%, vol surge"
semantic_title: "Democrats winning Florida 25th House seat stays favored"
telemetry: "Kalshi 81%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-16T00:00:00.000Z"
event_id: "CM-EVT-Q8F4815M66"
event_slug: "kxhouserace-fl25-26"
event_question: "Will the Florida 25th House seat be won in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-FL25-26-D"
  question_raw: "Will Democratic win the House race for FL-25?"
  current_price: 0.81
  volume_24h_usd: 661.19
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi puts 81% on Democrats winning Florida's 25th congressional district House seat, a heavily favored position."
  - "Trading volume on this contract surged 27,119% day over day, a 272x increase, signaling a sharp influx of fresh attention to this race."
  - "The volume spike alongside an 81% Democratic probability is consistent with the AP reporting of Republicans pulling resources from front-line districts."
  - "Resolves via Library of Congress; the FL-09 House seat on Kalshi (CM-EVT-DZ1HCD1GF9) sits at 71% for Democrats, reinforcing a broad Florida trend in the prediction markets."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "GOP strategy is shifting as Republicans retreat from front-line districts, with Trump aides bracing for midterm losses."
    publisher: "Nancy Cook"
    published_at: "2026-10-16T00:00:00.000Z"
    source_url: "https://www.washingtonpost.com/politics/2026/10/16/trump-aides-brace-white-house-turmoil-midterm-losses-loom/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Nancy Cook"
        source_url: "https://www.washingtonpost.com/politics/2026/10/16/trump-aides-brace-white-house-turmoil-midterm-losses-loom/"
        retrieved_at: "2026-10-16T12:59:00+00:00"
  - type: "pm_response"
    notes: "Kalshi contract; the 272x volume surge is the single strongest activity signal in this batch and is the key market read on GOP retreat news."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Nancy Cook: Trump aides brace for White House turmoil as midterm losses loom - The"
    url: "https://www.washingtonpost.com/politics/2026/10/16/trump-aides-brace-white-house-turmoil-midterm-losses-loom/"
    published_at: "2026-10-16T00:00:00.000Z"
    retrieved_at: "2026-10-16T12:59:00+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
