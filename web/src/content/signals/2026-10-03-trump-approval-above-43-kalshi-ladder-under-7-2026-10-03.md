---
signal_id: "CMSIG2026100304"
signal_slug: "trump-approval-above-43-kalshi-ladder-under-7-2026-10-03"
headline: "Trump approval above 43%: Kalshi ladder under 7%"
semantic_title: "Trump approval odds slip below 43 percent threshold"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-03T00:00:00.000Z"
event_id: "CM-EVT-VWW9FTFB33"
event_slug: "kxtrumpapprovalyear-26dec31"
event_question: "Donald Trump approval rating threshold (43%)"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPAPPROVALYEAR-26DEC31-43"
  question_raw: "Will Donald Trump's approval rating on approval rating be above 43% during Dec 2025 to Dec 2026 according to VoteHub?"
  current_price: 0.07
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "<polling organization>"
  resolves_at: "2027-01-07T12:00:00Z"
bullets:
  - "Kalshi ladder prices only 7% probability that Trump's approval rating clears 43%, with all higher strikes at 6% or below."
  - "A 5-point net approval improvement after the Israel-Iran ceasefire has not moved the market materially above the low-single-digit range for the 43% threshold."
  - "The companion Kalshi contract on Trump approval by December 31, 2026 sits at 12% for a 'below threshold' outcome, suggesting the market sees limited upside for approval through year-end."
  - "Resolution uses a named polling organization; the specific pollster and methodology will determine whether the ceasefire bounce is captured in the settlement read."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Trump's net approval improved 5 points over the past week following a ceasefire agreement between Israel and Iran, but the Morning Consult survey suggests overall approval remains subdued."
    publisher: "links.morningconsult.com"
    published_at: "2026-10-03T00:00:00.000Z"
    source_url: "https://links.morningconsult.com/s/vb/W-d8JY9vfRSwvrXaYYc_ModFKt3LZBaWuwnqbjqj5dMb62cAl3riVlUvKGu8WGoQevqfx82w4pW-9il39xCXa3YSuEC-LxGxQLHywtd2lY5RH0NaPblurxaLBwIPymHIUzEV8kmyjTY_N4SZXWjMaVGd_0i8dvrLPk27MA/FOTGo__hMmjdo9q2kEQw0UPyI58QyTri/25"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "links.morningconsult.com"
        source_url: "https://links.morningconsult.com/s/vb/W-d8JY9vfRSwvrXaYYc_ModFKt3LZBaWuwnqbjqj5dMb62cAl3riVlUvKGu8WGoQevqfx82w4pW-9il39xCXa3YSuEC-LxGxQLHywtd2lY5RH0NaPblurxaLBwIPymHIUzEV8kmyjTY_N4SZXWjMaVGd_0i8dvrLPk27MA/FOTGo__hMmjdo9q2kEQw0UPyI58QyTri/25"
        retrieved_at: "2026-10-03T07:47:35+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder and companion contract both signal the market sees Trump approval staying well below 43%, despite the short-term geopolitical boost."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "links.morningconsult.com: source article"
    url: "https://links.morningconsult.com/s/vb/W-d8JY9vfRSwvrXaYYc_ModFKt3LZBaWuwnqbjqj5dMb62cAl3riVlUvKGu8WGoQevqfx82w4pW-9il39xCXa3YSuEC-LxGxQLHywtd2lY5RH0NaPblurxaLBwIPymHIUzEV8kmyjTY_N4SZXWjMaVGd_0i8dvrLPk27MA/FOTGo__hMmjdo9q2kEQw0UPyI58QyTri/25"
    published_at: "2026-10-03T00:00:00.000Z"
    retrieved_at: "2026-10-03T07:47:35+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
