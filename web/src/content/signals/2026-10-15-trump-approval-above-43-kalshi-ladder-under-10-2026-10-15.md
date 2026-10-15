---
signal_id: "CMSIG2026101506"
signal_slug: "trump-approval-above-43-kalshi-ladder-under-10-2026-10-15"
headline: "Trump approval above 43%: Kalshi ladder under 10%"
semantic_title: "Trump approval above 43 percent stays a long shot near year-end"
telemetry: "Kalshi ladder"
category_tag: "MOMENTUM_REPRICING"
detection_path: "news_cycle"
pre_news_classification: "concurrent"
published_at: "2026-10-15T12:38:35.000Z"
event_id: "CM-EVT-VWW9FTFB33"
event_slug: "kxtrumpapprovalyear-26dec31"
event_question: "Trump approval rating level"
primary_market:
  platform: "kalshi"
  platform_market_id: "KXTRUMPAPPROVALYEAR-26DEC31-43"
  question_raw: "Will Donald Trump's approval rating on approval rating be above 43% during Dec 2025 to Dec 2026 according to VoteHub?"
  current_price: 0.031
  volume_24h_usd: 0.0
  arbitration_model: "kalshi_staff"
  resolution_source: "<polling organization>"
  resolves_at: "2027-01-07T12:00:00Z"
bullets:
  - "Kalshi ladder prices Trump approval above 43% at only 3%, above 44% at 8%, implying a market-implied range well below 43%."
  - "The AP-NORC polling showing majority dissatisfaction on economy and foreign policy is fully consistent with sub-43% approval pricing."
  - "The companion Kalshi contract (CM-EVT-0DMSQTKVX3) prices Trump approval below a threshold by December 31 at 12%, suggesting the market sees limited upside."
  - "The Polymarket contract on Trump ceasing to be president before 2027 (CM-EVT-ZW6ZK09DB1) sits at 4%, so low approval is priced as persistent but not destabilizing."
atomic_claims:
  - type: "news_event"
    significance:
      threshold: 5
      threshold_unit: "rank"
      passed: true
      reason: "surfaced in the daily Exa news-cycle scan; mechanically matched to an active kalshi market"
    story: "An AP-NORC poll found a strong majority of voters believe President Donald Trump is failing on domestic and foreign policy ahead of November midterms."
    publisher: "The Associated Press"
    published_at: "2026-10-15T12:38:35.000Z"
    source_url: "https://apnews.com/article/trump-inflation-economy-democrats-zacharia-ukraine-18131f88e983086649e6bf9928cb50f5"
    field_provenance:
      story:
        tier: "mediated"
        method: "exa_search"
        source: "The Associated Press"
        source_url: "https://apnews.com/article/trump-inflation-economy-democrats-zacharia-ukraine-18131f88e983086649e6bf9928cb50f5"
        retrieved_at: "2026-10-15T13:02:56+00:00"
  - type: "pm_response"
    notes: "Kalshi ladder resolves via polling organization; distribution implies current approval is stuck well below the 43% threshold with limited recovery priced in."
    field_provenance:
      notes:
        tier: "editorial"
        method: "llm_judge_cm_signal_v1"
sources:
  - label: "The Associated Press: The Latest: AP-NORC poll: Strong majority of voters believes Trump is"
    url: "https://apnews.com/article/trump-inflation-economy-democrats-zacharia-ukraine-18131f88e983086649e6bf9928cb50f5"
    published_at: "2026-10-15T12:38:35.000Z"
    retrieved_at: "2026-10-15T13:02:56+00:00"
field_provenance:
  pm_data: "kalshi_api"
  news_context: "exa_search"
  editorial_judgment: "cm_signal_llm_judge"
---

Surfaced by the daily news-cycle scan (Exa retrieval, Claude ranking): one of the day's significant stories, matched to the ClearMarket event pricing it. News-cycle wires publish on coverage, not editorial selection.
