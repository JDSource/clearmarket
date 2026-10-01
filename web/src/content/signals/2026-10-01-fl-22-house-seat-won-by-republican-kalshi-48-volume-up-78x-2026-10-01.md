---
signal_id: "CMSIG2026100105"
signal_slug: "fl-22-house-seat-won-by-republican-kalshi-48-volume-up-78x-2026-10-01"
headline: "FL-22 House seat won by Republican: Kalshi 48%, volume up 78x"
semantic_title: "Florida House District 22 GOP win sits near 50 percent"
telemetry: "Kalshi 48%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-01T00:00:00.000Z"
event_id: "CM-EVT-J5NV8SJXP4"
event_slug: "kxhouserace-fl22-26"
event_question: "Will the Florida House District 22 seat be won by a Republican in the next election?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXHOUSERACE-FL22-26-R"
  question_raw: "Will Republican win the House race for FL-22?"
  current_price: 0.48
  volume_24h_usd: 10.08
  arbitration_model: "kalshi_staff"
  resolution_source: "Library of Congress"
  resolves_at: "2027-01-04T17:00:00Z"
bullets:
  - "Kalshi prices a Republican win in Florida House District 22 at 48%, effectively a coin-flip with a slight lean to Democrats."
  - "Trading volume on this contract jumped 78.9 times day-over-day, the sharpest single-contract volume move in the political batch, signaling new attention on this race."
  - "Trump and Vance targeting deep-red areas to boost enthusiasm is consistent with a party defending seats it would normally expect to hold safely."
  - "A companion Kalshi contract on the Florida 25th House seat sits at 73% for a Republican win, highlighting significant intra-state variation in competitiveness."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump and Vance are campaigning in deep-red areas to shore up Republican enthusiasm ahead of November midterms."
    publisher: "MICHELLE L. PRICE Associated Press"
    published_at: "2026-10-01T00:00:00.000Z"
    source_url: "https://abcnews.com/Politics/wireStory/trump-vance-hit-campaign-trail-deep-red-areas-136909791"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "MICHELLE L. PRICE Associated Press"
        source_url: "https://abcnews.com/Politics/wireStory/trump-vance-hit-campaign-trail-deep-red-areas-136909791"
        retrieved_at: "2026-10-01T15:03:15+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via Library of Congress; the near-50% pricing and 79x volume surge make FL-22 the single most actively repriced political contract in today's batch."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "MICHELLE L. PRICE Associated Press: Trump and Vance hit the campaign trail in deep-red areas where GOP can"
    url: "https://abcnews.com/Politics/wireStory/trump-vance-hit-campaign-trail-deep-red-areas-136909791"
    published_at: "2026-10-01T00:00:00.000Z"
    retrieved_at: "2026-10-01T15:03:15+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
