---
signal_id: "CMSIG2026112005"
signal_slug: "us-ukraine-security-guarantee-by-dec-31-polymarket-6-2026-11-20"
headline: "US Ukraine security guarantee by Dec 31: Polymarket 6%"
semantic_title: "US security guarantee for Ukraine by year-end stays unlikely"
telemetry: "Polymarket 6%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-20T08:44:00.000Z"
event_id: "CM-EVT-VT4J8XSQN3"
event_slug: "us-agrees-to-give-ukraine-security-guarantee-by-december-31"
event_question: "Will the U.S. agree to give Ukraine a security guarantee by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x26ed26fd53ec238c80afee64b55e098e4c8f7e0b64f332ff6713fd3b504ab350"
  question_raw: "U.S. agrees to give Ukraine security guarantee by December 31? "
  current_price: 0.057
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket prices a 6% chance the US agrees to give Ukraine a security guarantee by December 31, resolved via UMA oracle."
  - "The US envoy's statement that Russia is open to NATO-style guarantees is a significant diplomatic signal, but Polymarket is not pricing it as a near-term outcome."
  - "The companion contract on Ukraine ceding territory to Russia by 2026 sits at just 2%, suggesting markets see a frozen stalemate rather than any deal."
  - "Resolution requires a formal US commitment to Ukraine's security, a high bar given Congressional dynamics with Democrats taking power in weeks."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The US said Russia is open to NATO-style security guarantees for Ukraine following the Trump-Putin trilateral summit, with envoy Jared Kushner briefing reporters after a Coalition of the Willing summit."
    publisher: "Associated Press"
    published_at: "2026-11-20T08:44:00.000Z"
    source_url: "https://www.dailysabah.com/world/europe/us-says-russia-open-to-nato-style-security-guarantees-for-ukraine"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Associated Press"
        source_url: "https://www.dailysabah.com/world/europe/us-says-russia-open-to-nato-style-security-guarantees-for-ukraine"
        retrieved_at: "2026-11-23T07:47:39+00:00"
  - type: "pm_response"
    notes: "Polymarket's 6% on a US security guarantee resolves via UMA oracle; diplomatic language from the summit is not translating into market conviction."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Associated Press: US says Russia open to NATO-style security guarantees for Ukraine | Da"
    url: "https://www.dailysabah.com/world/europe/us-says-russia-open-to-nato-style-security-guarantees-for-ukraine"
    published_at: "2026-11-20T08:44:00.000Z"
    retrieved_at: "2026-11-23T07:47:39+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
