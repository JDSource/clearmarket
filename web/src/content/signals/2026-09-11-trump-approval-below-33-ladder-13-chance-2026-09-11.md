---
signal_id: "CMSIG2026091103"
signal_slug: "trump-approval-below-33-ladder-13-chance-2026-09-11"
headline: "Trump approval below 33%: ladder 13% chance"
semantic_title: "Trump approval odds below 33 percent stay low"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-11T08:31:19.596Z"
event_id: "CM-EVT-0DMSQTKVX3"
event_slug: "kxtrumpapprovalbelow-26dec31"
event_question: "Trump approval rating floor (ladder, below)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPAPPROVALBELOW-26DEC31-33"
  question_raw: "Will Donald Trump's approval rating on approval rating be below 33% during Dec 2025 to Dec 2026 according to VoteHub?"
  current_price: 0.13
  volume_24h_usd: 10.17
  arbitration_model: "kalshi_staff"
  resolution_source: "<polling organization>"
  resolves_at: "2027-01-07T12:00:00Z"
bullets:
  - "Ladder prices only 13% chance the approval rating drops below 33%, implying the market-implied floor is in the 33-37% range."
  - "The ABC/WaPo/Ipsos poll showing 66% wrong-track sentiment is consistent with depressed approval but not a collapse below 33%."
  - "A companion binary, Polymarket CM-EVT-VNTLCWF6Y5 at 1% on the 2026 approval rating resolution, signals extremely low odds of a broader approval bounce."
  - "Resolution uses the named approval-rating tracker cited in the contract; the ladder settles based on whether the reading crosses specified thresholds."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "An ABC News/Washington Post/Ipsos poll finds two-thirds of Americans say the country is headed in the wrong direction, with concerns over the economy and Iran denting Trump's approval."
    publisher: "ABC News"
    published_at: "2026-09-11T08:31:19.596Z"
    source_url: "https://abcnews.com/Politics/thirds-americans-country-headed-wrong-direction-abc-newswashington/story?id=132583099"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "ABC News"
        source_url: "https://abcnews.com/Politics/thirds-americans-country-headed-wrong-direction-abc-newswashington/story?id=132583099"
        retrieved_at: "2026-09-11T12:32:20+00:00"
  - type: "pm_response"
    notes: "Ladder and Polymarket binary both point to low but not collapsing approval; cross-venue read is internally consistent."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "ABC News: Two-thirds of Americans say country is headed in the wrong direction:"
    url: "https://abcnews.com/Politics/thirds-americans-country-headed-wrong-direction-abc-newswashington/story?id=132583099"
    published_at: "2026-09-11T08:31:19.596Z"
    retrieved_at: "2026-09-11T12:32:20+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
