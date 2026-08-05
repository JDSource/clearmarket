---
signal_id: "CMSIG2026080407"
signal_slug: "gop-controls-one-chamber-post-midterms-kalshi-42-2026-08-04"
headline: "GOP controls one chamber post-midterms: Kalshi 42%"
semantic_title: "Republican Congress control after 2026 midterms holds below 50%"
telemetry: "Kalshi 42%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-04T00:00:00.000Z"
event_id: "CM-EVT-T5VXKJT451"
event_slug: "kxbalancepowercombo-27feb"
event_question: "Will Republicans control at least one chamber of Congress after the 2026 midterm elections?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXBALANCEPOWERCOMBO-27FEB-DD"
  question_raw: "Will House Control be Democratic AND Senate Control be Democratic for Feb 2027?"
  current_price: 0.42
  volume_24h_usd: 45221.85
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2027-02-01T15:00:00Z"
bullets:
  - "Kalshi contract puts only 42% odds on Republicans controlling at least one chamber of Congress after the 2026 midterms."
  - "The below-50% pricing is consistent with the narrative of Trump political headwinds, though the market is not strongly pricing a Democratic sweep."
  - "El-Sayed's progressive primary win in Michigan adds a data point on Democratic enthusiasm in a key battleground state."
  - "Resolves via Bureau of Labor Statistics, note: this appears to be an unusual resolution source for an election contract; traders should verify the resolution mechanic carefully."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Analysis suggests a string of Trump setbacks could give Democrats an edge in the 2026 midterm elections."
    publisher: "Jeff Mordock"
    published_at: "2026-08-04T00:00:00.000Z"
    source_url: "https://www.washingtontimes.com/news/2026/aug/4/string-setbacks-trump-threatens-also-give-democrats-edge-midterm/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Jeff Mordock"
        source_url: "https://www.washingtontimes.com/news/2026/aug/4/string-setbacks-trump-threatens-also-give-democrats-edge-midterm/"
        retrieved_at: "2026-08-05T10:30:51+00:00"
  - type: "pm_response"
    notes: "Kalshi at 42% is the only priced chamber-control contract in this batch; resolution source listed as Bureau of Labor Statistics, which warrants scrutiny."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Jeff Mordock: String of setbacks for Trump threatens to also give Democrats edge in"
    url: "https://www.washingtontimes.com/news/2026/aug/4/string-setbacks-trump-threatens-also-give-democrats-edge-midterm/"
    published_at: "2026-08-04T00:00:00.000Z"
    retrieved_at: "2026-08-05T10:30:51+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
