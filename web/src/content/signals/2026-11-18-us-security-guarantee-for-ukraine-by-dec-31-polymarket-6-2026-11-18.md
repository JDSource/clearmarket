---
signal_id: "CMSIG2026111805"
signal_slug: "us-security-guarantee-for-ukraine-by-dec-31-polymarket-6-2026-11-18"
headline: "US security guarantee for Ukraine by Dec 31: Polymarket 6%"
semantic_title: "US security guarantee for Ukraine by year-end stays near zero"
telemetry: "Polymarket 6%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-18T04:08:08.000Z"
event_id: "CM-EVT-VT4J8XSQN3"
event_slug: "us-agrees-to-give-ukraine-security-guarantee-by-december-31"
event_question: "Will the U.S. agree to give Ukraine a security guarantee by December 31?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0x26ed26fd53ec238c80afee64b55e098e4c8f7e0b64f332ff6713fd3b504ab350"
  question_raw: "U.S. agrees to give Ukraine security guarantee by December 31? "
  current_price: 0.063
  volume_24h_usd: 0.0
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "Polymarket puts 6% odds on the US agreeing to a formal security guarantee for Ukraine by December 31, 2026, resolved via UMA oracle."
  - "With Ukraine not represented at the Shenzhen trilateral and the agenda focused on nuclear arms control and trade, the Polymarket contract's near-zero pricing is consistent with the diplomatic setup."
  - "A shorter-horizon companion contract asking if the US agrees to a guarantee by June 30 has no active price, but the December contract at 6% already implies the market sees no near-term path."
  - "Resolution requires a formal US agreement to provide Ukraine a security guarantee; Rubio comments on potential Trump-Kim talks and APEC optics do not meet that threshold."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "The Trump-Xi-Putin trilateral at APEC in Shenzhen is expected to cover the Ukraine war, nuclear arms control, and trade, with Zelensky not present."
    publisher: "Express Global Desk"
    published_at: "2026-11-18T04:08:08.000Z"
    source_url: "https://indianexpress.com/article/world/world-news-live-updates-trump-china-us-tech-outages-first-xi-putin-meet-apec-qeshm-island-hormuz-russia-ukraine-10967706/"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Express Global Desk"
        source_url: "https://indianexpress.com/article/world/world-news-live-updates-trump-china-us-tech-outages-first-xi-putin-meet-apec-qeshm-island-hormuz-russia-ukraine-10967706/"
        retrieved_at: "2026-11-18T07:48:08+00:00"
  - type: "pm_response"
    notes: "Polymarket at 6% on a year-end US security guarantee for Ukraine signals deep skepticism despite high-profile multilateral diplomacy at APEC Shenzhen."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Express Global Desk: World News Live Updates: Trump heads to China amid US tech outages for"
    url: "https://indianexpress.com/article/world/world-news-live-updates-trump-china-us-tech-outages-first-xi-putin-meet-apec-qeshm-island-hormuz-russia-ukraine-10967706/"
    published_at: "2026-11-18T04:08:08.000Z"
    retrieved_at: "2026-11-18T07:48:08+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
