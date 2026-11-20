---
signal_id: "CMSIG2026111904"
signal_slug: "us-security-guarantee-for-ukraine-by-dec-31-polymarket-6-2026-11-19"
headline: "US security guarantee for Ukraine by Dec 31: Polymarket 6%"
semantic_title: "US security guarantee for Ukraine by year-end priced as unlikely"
telemetry: "Polymarket 6%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-19T04:59:00.000Z"
event_id: "CM-EVT-VT4J8XSQN3"
event_slug: "us-agrees-to-give-ukraine-security-guarantee-by-december-31"
event_question: "Will the U.S. agree to give Ukraine a security guarantee by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x26ed26fd53ec238c80afee64b55e098e4c8f7e0b64f332ff6713fd3b504ab350"
  question_raw: "U.S. agrees to give Ukraine security guarantee by December 31? "
  current_price: 0.064
  volume_24h_usd: 426.31579
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only 6% on the US agreeing to give Ukraine a formal security guarantee by December 31, 2026."
  - "Kushner's optimistic framing is not reflected in the market, which treats a binding US commitment before year-end as highly unlikely."
  - "A shorter-horizon companion contract (CM-EVT-XJ07DRZ1S1) on a guarantee by June 30 has no published price, but would imply an even lower ceiling."
  - "Resolves via UMA oracle; the trigger is a formal US agreement, not diplomatic statements or summit communiques."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Jared Kushner said Russia is comfortable with NATO-like security guarantees for Ukraine, raising hopes for a deal framework after the Trump-Putin-Xi summit."
    publisher: "Bridget Brown, Sylvia Hui, Bernard McGhee, Luena Rodriguez-Feo Vileira, Anjalie Tandon"
    published_at: "2026-11-19T04:59:00.000Z"
    source_url: "https://apnews.com/live/trump-xi-putin-china-politics-news-updates-11-19-2026"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Bridget Brown, Sylvia Hui, Bernard McGhee, Luena Rodriguez-Feo Vileira, Anjalie Tandon"
        source_url: "https://apnews.com/live/trump-xi-putin-china-politics-news-updates-11-19-2026"
        retrieved_at: "2026-11-20T07:47:31+00:00"
  - type: "pm_response"
    notes: "Polymarket at 6% is fading the Kushner optimism; the market sees near-term deal completion as a long shot despite diplomatic momentum."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Bridget Brown, Sylvia Hui, Bernard McGhee, Luena Rodriguez-Feo Vileira, Anjalie Tandon: Kushner says he believes Russia is ‘comfortable’ with NATO-like securi"
    url: "https://apnews.com/live/trump-xi-putin-china-politics-news-updates-11-19-2026"
    published_at: "2026-11-19T04:59:00.000Z"
    retrieved_at: "2026-11-20T07:47:31+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
