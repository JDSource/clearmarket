---
signal_id: "CMSIG2026111707"
signal_slug: "china-invades-taiwan-by-dec-31-polymarket-2-2026-11-17"
headline: "China invades Taiwan by Dec 31: Polymarket 2%"
semantic_title: "China invading Taiwan by year-end stays near zero"
telemetry: "Polymarket 2%"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-11-17T02:19:54.000Z"
event_id: "CM-EVT-4Y672MJHD0"
event_slug: "will-china-invade-taiwan-before-2027"
event_question: "Will China invade Taiwan by the end of 2026?"
primary_market:
  platform: "polymarket"
  platform_market_id: "0xd9fb1184af0064e5e34b129f5b79afa5a17b7e32f2953ab05efed82315fee6d4"
  question_raw: "Will China invade Taiwan by end of 2026?"
  current_price: 0.017
  volume_24h_usd: 229321.15941899992
  arbitration_model: "uma_oracle"
  resolves_at: "2026-12-31T00:00:00Z"
bullets:
  - "The Polymarket contract puts 2% odds on China invading Taiwan by December 31, 2026, resolving via UMA oracle."
  - "The APEC summit and Trump-Xi bilateral meeting are the highest-profile diplomatic engagements of the year; the market treats the summit as de-escalatory, not a trigger for military action."
  - "A companion Polymarket contract on a China-Japan military clash before 2027 sits at 3%, consistent with a low-but-nonzero regional conflict tail across both markets."
  - "Resolution via UMA oracle by December 31; Taiwan's status is explicitly on the APEC agenda per reports, making the next 48-72 hours a key observation window for any probability shift."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active polymarket market"
    story: "World leaders gathered for APEC and ASEAN summits in Shenzhen, with Trump attending ahead of historic trilateral talks with Xi Jinping and Vladimir Putin."
    publisher: "Mark Saunokonoko"
    published_at: "2026-11-17T02:19:54.000Z"
    source_url: "https://www.theguardian.com/world/live/2026/nov/17/asean-apec-summit-2026-live-updates-trump-xi-putin-meeting-schedule-latest-news?page=with%3Ablock-6afbb5668f08d5d6e898f451"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "Mark Saunokonoko"
        source_url: "https://www.theguardian.com/world/live/2026/nov/17/asean-apec-summit-2026-live-updates-trump-xi-putin-meeting-schedule-latest-news?page=with%3Ablock-6afbb5668f08d5d6e898f451"
        retrieved_at: "2026-11-17T07:48:04+00:00"
  - type: "pm_response"
    notes: "Polymarket contract resolves via UMA oracle by December 31, 2026; the Trump-Xi Shenzhen meeting is the most significant near-term news catalyst for this contract."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "Mark Saunokonoko: World leaders gather for Apec and Asean summits ahead of Trump-Xi-Puti"
    url: "https://www.theguardian.com/world/live/2026/nov/17/asean-apec-summit-2026-live-updates-trump-xi-putin-meeting-schedule-latest-news?page=with%3Ablock-6afbb5668f08d5d6e898f451"
    published_at: "2026-11-17T02:19:54.000Z"
    retrieved_at: "2026-11-17T07:48:04+00:00"
field_provenance:
  pm_data: "polymarket_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
