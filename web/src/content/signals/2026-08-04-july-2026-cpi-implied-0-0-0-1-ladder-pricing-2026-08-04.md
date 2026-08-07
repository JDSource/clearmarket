---
signal_id: "CMSIG2026080402"
signal_slug: "july-2026-cpi-implied-0-0-0-1-ladder-pricing-2026-08-04"
headline: "July 2026 CPI implied 0.0%-0.1%: ladder pricing"
semantic_title: "July CPI stays near zero in market pricing"
telemetry: "Kalshi ladder"
category_tag: "PRE_EVENT_PRICING"
detection_path: "news_cycle"
pre_news_classification: "pre_news"
published_at: "2026-08-04T00:00:00.000Z"
event_id: "CM-EVT-HVKDYMRT39"
event_slug: "kxcpi-26jul"
event_question: "July 2026 CPI monthly change"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXCPI-26JUL-T0.1"
  question_raw: "Will CPI rise more than 0.1% in July 2026?"
  current_price: 0.25
  volume_24h_usd: 275.9
  arbitration_model: "kalshi_staff"
  resolution_source: "Bureau of Labor Statistics"
  resolves_at: "2026-11-11T13:56:00Z"
bullets:
  - "Prediction market ladder prices July 2026 CPI in the 0.0%-0.1% range, with 61% probability above 0.0% and only 25% above 0.1%."
  - "Kansas City Fed President Jeff Schmid called inflation 'too high' and 'worrisome,' but the ladder's near-zero monthly read is not consistent with a renewed inflation surge."
  - "The sharp drop from 61% above 0.0% to 25% above 0.1% signals the market sees only a modest positive print as the modal outcome, not a hot number."
  - "Schmid's call for tighter policy finds little support in this distribution; the ladder implies CPI trajectory that would not obviously justify the rate hikes he endorsed."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "BNY flagged the upcoming July CPI print as the second key Fed input alongside NFP, with inflation trajectory shaping the rate path."
    publisher: "fxstreet.com"
    published_at: "2026-08-04T00:00:00.000Z"
    source_url: "https://www.fxstreet.com/news/us-dollar-nfp-and-inflation-mix-complicate-fed-path-bny-202608040915"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "fxstreet.com"
        source_url: "https://www.fxstreet.com/news/us-dollar-nfp-and-inflation-mix-complicate-fed-path-bny-202608040915"
        retrieved_at: "2026-08-07T08:53:43+00:00"
  - type: "pm_response"
    notes: "Ladder distribution from prediction market strikes; no single-venue binary price available; resolution tied to BLS CPI release."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "fxstreet.com: US Dollar: NFP and inflation mix complicate Fed path, BNY"
    url: "https://www.fxstreet.com/news/us-dollar-nfp-and-inflation-mix-complicate-fed-path-bny-202608040915"
    published_at: "2026-08-04T00:00:00.000Z"
    retrieved_at: "2026-08-07T08:53:43+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
