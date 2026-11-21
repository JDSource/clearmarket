---
signal_id: "CMSIG2026111905"
signal_slug: "u-s-security-guarantee-for-ukraine-by-dec-31-polymarket-6-2026-11-19"
headline: "U.S. security guarantee for Ukraine by Dec 31: Polymarket 6%"
semantic_title: "U.S. security guarantee for Ukraine stays near long-shot pricing at 6 percent"
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
  current_price: 0.057
  volume_24h_usd: 27.370438
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices only a 6% chance the U.S. formally agrees to give Ukraine a security guarantee by December 31, resolves via UMA oracle."
  - "Kushner's claim that Russia is comfortable with NATO-like guarantees is a constructive signal, but the market is treating it as far from a done deal by year-end."
  - "The companion contract on Ukraine agreeing not to join NATO before 2027 (Polymarket CM-EVT-S5MX1GCV08) sits at just 1%, showing the market sees neither side of the security architecture resolving quickly."
  - "The near-term June 30 deadline contract (CM-EVT-XJ07DRZ1S1) carries no price, leaving the December contract as the only live read on this guarantee question."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "Jared Kushner said he believes Russia is comfortable with NATO-like security guarantees for Ukraine, raising the prospect of a formal U.S. commitment."
    publisher: "Bridget Brown, Sylvia Hui, Bernard McGhee, Luena Rodriguez-Feo Vileira, Anjalie Tandon"
    published_at: "2026-11-19T04:59:00.000Z"
    source_url: "https://apnews.com/live/trump-xi-putin-china-politics-news-updates-11-19-2026"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Bridget Brown, Sylvia Hui, Bernard McGhee, Luena Rodriguez-Feo Vileira, Anjalie Tandon"
        source_url: "https://apnews.com/live/trump-xi-putin-china-politics-news-updates-11-19-2026"
        retrieved_at: "2026-11-21T07:47:41+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle; Kushner's statement is concurrent with the 6% price, which is not moving toward higher probability despite the diplomatic framing."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Bridget Brown, Sylvia Hui, Bernard McGhee, Luena Rodriguez-Feo Vileira, Anjalie Tandon: Kushner says he believes Russia is ‘comfortable’ with NATO-like securi"
    url: "https://apnews.com/live/trump-xi-putin-china-politics-news-updates-11-19-2026"
    published_at: "2026-11-19T04:59:00.000Z"
    retrieved_at: "2026-11-21T07:47:41+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
