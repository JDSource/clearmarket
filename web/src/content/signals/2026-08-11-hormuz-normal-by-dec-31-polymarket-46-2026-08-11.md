---
signal_id: "CMSIG2026081108"
signal_slug: "hormuz-normal-by-dec-31-polymarket-46-2026-08-11"
headline: "Hormuz normal by Dec 31: Polymarket 46%"
semantic_title: "BRICS Hormuz mediation leaves reopening odds near even"
telemetry: "Polymarket 46%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-08-11T05:48:24.201Z"
event_id: "CM-EVT-LCPV825X09"
event_slug: "strait-of-hormuz-traffic-returns-to-normal-by-december-31"
event_question: "Will Strait of Hormuz traffic return to normal by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x5c79dfde05559b79a9cb9f7c4187e4d49632dd042572ae676952f812732591cc"
  question_raw: "Strait of Hormuz traffic returns to normal by December 31?"
  current_price: 0.46
  volume_24h_usd: 61071.808274999996
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices Strait of Hormuz traffic returning to normal by December 31 at 46%, nearly balanced."
  - "BRICS multilateral pressure and Oman-led talks add a diplomatic track, but the market at 46% does not assign a clear edge to any pathway."
  - "Trump's sanctions pivot on Iran (story 13) runs counter to the diplomatic momentum, explaining why odds remain below 50% despite active mediation efforts."
  - "Kalshi's US Iran embassy reopening contract at 7% (CM-EVT-34SYT4T2T1) implies traffic normalization, if it happens, will precede any full diplomatic restoration."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "India and China are rallying BRICS to support Oman-led talks to resolve the Strait of Hormuz crisis as an alternative to US diplomacy."
    publisher: "South China Morning Post"
    published_at: "2026-08-11T05:48:24.201Z"
    source_url: "https://www.scmp.com/week-asia/politics/article/3363590/brics-stiffest-test-can-india-china-rally-bloc-resolve-strait-hormuz-crisis"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "South China Morning Post"
        source_url: "https://www.scmp.com/week-asia/politics/article/3363590/brics-stiffest-test-can-india-china-rally-bloc-resolve-strait-hormuz-crisis"
        retrieved_at: "2026-08-11T08:49:29+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; 46% reflects genuine multipath uncertainty between US sanctions pressure and BRICS-Oman diplomatic track."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "South China Morning Post: Can India and China rally Brics to ease Strait of Hormuz tensions?"
    url: "https://www.scmp.com/week-asia/politics/article/3363590/brics-stiffest-test-can-india-china-rally-bloc-resolve-strait-hormuz-crisis"
    published_at: "2026-08-11T05:48:24.201Z"
    retrieved_at: "2026-08-11T08:49:29+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
