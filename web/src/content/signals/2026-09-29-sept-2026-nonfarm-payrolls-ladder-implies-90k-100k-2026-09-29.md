---
signal_id: "CMSIG2026092901"
signal_slug: "sept-2026-nonfarm-payrolls-ladder-implies-90k-100k-2026-09-29"
headline: "Sept 2026 nonfarm payrolls: ladder implies 90K-100K"
semantic_title: "September jobs market prices in solid positive print"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-09-29T00:00:00.000Z"
event_id: "CM-EVT-MZQH465PC3"
event_slug: "kxpayrolls-26sep"
event_question: "September 2026 nonfarm payrolls"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXPAYROLLS-26SEP-T100000"
  question_raw: "Will above 100000 jobs be added in September 2026?"
  current_price: 0.48
  volume_24h_usd: 1404.05
  arbitration_model: "kalshi_staff"
  resolution_source: "BLS"
  resolves_at: "2027-01-01T14:00:00Z"
bullets:
  - "Prediction market ladder puts 57% on above 90K jobs and 48% on above 100K, implying a central estimate near 90K-100K for September 2026."
  - "Fed Governor Michael S. Barr's hawkish rate-hike signal is broadly consistent with a labor market still adding jobs, not contracting."
  - "The 27% probability above 125K shows the market is not pricing a blowout print; tail risk skews to the downside."
  - "Resolution via Bureau of Labor Statistics Employment Situation report; any benchmark revision could shift the ladder distribution materially."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "Fed Governor Michael S. Barr said more rate hikes are likely needed to curb inflation, signaling ongoing tightening pressure on the labor market."
    publisher: "Ann Saphir"
    published_at: "2026-09-29T00:00:00.000Z"
    source_url: "https://www.reuters.com/business/feds-barr-says-more-rate-hikes-likely-be-needed-curb-inflation-2026-09-29/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Ann Saphir"
        source_url: "https://www.reuters.com/business/feds-barr-says-more-rate-hikes-likely-be-needed-curb-inflation-2026-09-29/"
        retrieved_at: "2026-09-30T07:47:19+00:00"
  - type: "pm_response"
    notes: "Ladder prediction market prices a positive but moderate September payrolls print, consistent with Barr's still-resilient labor market framing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Ann Saphir: Fed's Barr says more rate hikes likely to be needed to curb inflation"
    url: "https://www.reuters.com/business/feds-barr-says-more-rate-hikes-likely-be-needed-curb-inflation-2026-09-29/"
    published_at: "2026-09-29T00:00:00.000Z"
    retrieved_at: "2026-09-30T07:47:19+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
