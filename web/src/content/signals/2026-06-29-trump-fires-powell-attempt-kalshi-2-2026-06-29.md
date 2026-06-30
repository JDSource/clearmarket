---
signal_id: "CMSIG2026062905"
signal_slug: "trump-fires-powell-attempt-kalshi-2-2026-06-29"
headline: "Trump fires Powell attempt: Kalshi 2%"
semantic_title: "Trump firing Fed Chair Powell consensus holds near zero"
telemetry: "Kalshi 2%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-06-29T14:25:18.000Z"
event_id: "CM-EVT-TMHG8WLK69"
event_slug: "kxtryfirepowell-26may12"
event_question: "Will Trump attempt to fire Powell as Federal Reserve Chair or Governor?"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRYFIREPOWELL-26MAY12-GOV2"
  question_raw: "Will the President try to fire the Jerome Powell as either Chair of the Board of Governors of the Federal Reserve System or Member of the Board of Governors of the Federal Reserve System before Jan 1, 2027?"
  current_price: 0.025
  volume_24h_usd: 46.34
  arbitration_model: "kalshi_staff"
  resolution_source: "ABC"
  resolves_at: "2027-01-01T15:00:00Z"
bullets:
  - "Kalshi prediction market prices only 2% odds that Trump will attempt to fire Fed Chair Jerome Powell as Chair or Governor."
  - "The Supreme Court ruling explicitly protecting Fed governors from presidential removal is consistent with the near-zero Kalshi probability on a Powell firing attempt."
  - "The companion Polymarket contract (CM-EVT-L2GSTD8DB5) at 99% on presidential firing of FTC commissioners shows the court drew a sharp line at the Fed specifically."
  - "Resolves via ABC News confirmation of a Trump attempt; the court's carve-out for the Fed makes the resolution bar even less likely to be cleared."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "The Supreme Court ruled that President Trump cannot fire Federal Reserve Governor Lisa Cook, carving out the central bank from a broader ruling allowing presidential removal of independent agency heads."
    publisher: "nbcdfw.com"
    published_at: "2026-06-29T14:25:18.000Z"
    source_url: "https://www.nbcdfw.com/news/national-international/supreme-court-rules-lisa-cook-federal-reserve-trump/3999187/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "nbcdfw.com"
        source_url: "https://www.nbcdfw.com/news/national-international/supreme-court-rules-lisa-cook-federal-reserve-trump/3999187/"
        retrieved_at: "2026-06-30T10:54:27+00:00"
  - type: "pm_response"
    notes: "Kalshi contract resolves via ABC News; the Cook ruling directly reduces the legal pathway that would have emboldened a Powell removal attempt, consistent with the 2% pricing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "nbcdfw.com: Supreme Court rules Trump can’t fire Federal Reserve governor Cook, N"
    url: "https://www.nbcdfw.com/news/national-international/supreme-court-rules-lisa-cook-federal-reserve-trump/3999187/"
    published_at: "2026-06-29T14:25:18.000Z"
    retrieved_at: "2026-06-30T10:54:27+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
