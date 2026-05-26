Backed by![Y Combinator](https://www.oddpool.com/_next/image?url=%2Fyc-logo-black.png&w=256&q=75)

# The search engine for prediction markets

Liquidity is fragmented across exchanges. We surface the whole picture for traders, builders, and quant teams.

[Get API Key](https://www.oddpool.com/sign-in?callback=/welcome) [Book a call](https://cal.com/team/oddpool/30-minute-meeting)

[Explore our institutional offering](https://www.oddpool.com/institutional)

## Two exchanges. Two APIs.  Zero standardization.

You want to know if the Fed will cut rates in June. Kalshi gives you KXFEDDECISION-26JUN-H0. Polymarket gives you 0x3f8a0c9b.... Different IDs, different orderbooks, different WebSocket protocols. You can spend a month building the normalization layer yourself.

KALSHI

```
GET /markets/KXFEDDECISION-26JUN-H0

{
  "ticker": "KXFEDDECISION-26JUN-H0",
  "yes_ask": 0.94,
  "no_ask": 0.07,
  "volume": 4714197,
  "open_interest": 891003
}
```

POLYMARKET

```
GET /markets/0x3f8a0c9b7e...

{
  "condition_id": "0x3f8a0c9b...",
  "tokens": [{ "token_id": "635866..." }],
  "outcome_prices": ["0.955","0.045"],
  "volume": "1965879.48"
}
```

ODDPOOLone query, both venues

```
GET /search/events?q=fed+rate+june

[{\
  "event_id": "KXFEDDECISION-26JUN",\
  "exchange": "kalshi",\
  "title": "Fed Rate Decision June",\
  "total_volume": 4714197\
}, {\
  "exchange": "polymarket",\
  "title": "FOMC June 2026",\
  "total_volume": 1965879\
}]
```

Or you search once and get both. Then pull historical orderbooks, track whale trades, and find cross-venue arbitrage. All from one API key.

FREE ON EVERY TIER

## 700,000 markets.  One search.

Every active market on Kalshi and Polymarket, indexed and searchable. Filter by venue, category, volume, or liquidity. Find markets that don't show up in either exchange's own search. Get event-level groupings with all their underlying markets in a single call.

search

```
# search events across both venues
curl "https://api.oddpool.com/search/events?
  q=bitcoin&status=active&sort_by=volume&limit=5"
  -H "X-API-Key: oddpool_abc123"

# returns events from both Kalshi and Polymarket
# with market_count, total_volume, total_liquidity
# also: /search/markets for individual contracts
# also: /search/recent/events for newly listed
```

FREE ON EVERY TIER

## Orderbooks back  to March 2026.

Full-depth orderbook snapshots, top-of-book timeseries, and trade tapes for every Kalshi and Polymarket market. 1-minute or 5-minute granularity. Cursor-paginated so you can download the entire history for any market. Backtest your model against real microstructure.

historical

```
# full orderbook snapshots
curl "https://api.oddpool.com/historical/
  kalshi/orderbook?
  market_id=KXFEDDECISION-26JUN-H0&
  granularity=1m&limit=100"
  -H "X-API-Key: oddpool_abc123"

# returns yes_bids, no_bids, best_yes_bid,
# best_yes_ask, mid, spread for each snapshot
# also: /top-of-book, /trades
# also: /historical/polymarket/* for Poly markets
```

[Full API docs](https://docs.oddpool.com/) AI-agent ready at api.oddpool.com/llms.txt

WHALE TRACKINGPro $30/mo

## See the smart money  before the market does.

Every trade over $500 on both Kalshi and Polymarket, flagged and delivered in real time. Filter by event, platform, and minimum size. Last week, 151 whale trades totaling $185K in 24 hours on a single event. When someone drops $15,000 on "Fed holds rate" at 95¢, you'll know about it.

whale feed

```
{
  "platform": "polymarket",
  "event_title": "FOMC June 2026",
  "market_title": "Fed holds rate",
  "taker_side": "yes",
  "trade_size_usd": 15000.00,
  "price": 0.95,
  "timestamp": "2026-03-22T14:30:00Z"
}
```

ARBITRAGEPremium $100/mo

## When venues disagree,  you profit.

The arbitrage endpoint scans every matched market across both venues and returns opportunities with net profit after fees already calculated. Kalshi says 42¢, Polymarket says 39¢. Buy YES on Poly, buy NO on Kalshi. That's a guaranteed 1¢ per contract. A single 3¢ arb on 100 contracts is $3. Pro users spotted 762 arb opportunities last week alone. [Why those fees matter: Kalshi vs Polymarket fee structure](https://www.oddpool.com/research/prediction-market-fees-explained).

arbitrage opportunity

```
{
  "event_title": "Fed rate decision June",
  "label": "25bps cut",
  "buy_yes_market": "polymarket",
  "buy_no_market": "kalshi",
  "kalshi": { "yes_ask": 0.42, "volume": 150000 },
  "polymarket": { "yes_ask": 0.39, "volume": 200000 },
  "gross_cents": 1.0,
  "fee_cents": 0,
  "net_cents": 1.0
}
```

ONE PROMPT. THAT'S IT.

## Your coding agent already  knows how to use this.

Drop the link into Claude, GPT, Cursor, or any coding agent. It reads the full API reference and starts writing working code against Oddpool instantly. No docs to skim. No SDK to install.

prompt

Read [https://docs.oddpool.com/llms.txt](https://docs.oddpool.com/llms.txt)

Use my API key oddpool\_abc123 to

find all active FOMC markets and show
me the cross-venue probability distribution.

wss://feeds.oddpool.com/ws

## Know what the market thinks  before the data drops.

FOMC meeting tomorrow? Watch the probability shift in real time as both Kalshi and Polymarket reprice. CPI print at 8:30am? See the market's reaction across venues in a single normalized stream. Our Macro Feed gives you liquidity-weighted cross-venue probabilities for every major economic event, with full orderbook depth and trade execution data.

Four channel types: dist for probabilities (free), plus book,trade, andsnapshot for full microstructure. One WebSocket connection, one subscribe message, data starts flowing.

FOMCCPIPayrollsGDPUnemployment

Crypto and weather feeds in development, each enriched with domain-specific data.

wss://feeds.oddpool.com/ws

distcpi-2026-05above\_3.5% prob=0.221 kalshi=0.215 poly=0.230

bookcpi-2026-05kalshi yes bid=0.215 ask=0.230 spread=0.015

tradefomc-2026-06-17polymarket sell no qty=8300 @ 0.045

distnfp-2026-06above\_200K prob=0.613 kalshi=0.605 poly=0.625

bookfomc-2026-06-17kalshi yes bid=0.940 ask=0.950 spread=0.010

snapshotfomc-2026-06-175 outcomes full state seq=5

distfomc-2026-06-17hold prob=0.949 kalshi=0.945 poly=0.958

FREE FOREVER

## Not a developer?  We built the dashboards too.

750+ live event dashboards across politics, sports, crypto, economics, and culture. Cross-venue search across 700K+ markets. Historical charts. Paper trading. No account required.

[Fed Market Watch](https://www.oddpool.com/fed-market-watch) [Bitcoin Peak](https://www.oddpool.com/bitcoin-peak) [NBA Champion](https://www.oddpool.com/nba-champion) [FIFA World Cup](https://www.oddpool.com/fifa-cup) [Venue Dominance](https://www.oddpool.com/dominance) [Super Bowl LX](https://www.oddpool.com/super-bowl)

[Browse all 750+ dashboards](https://www.oddpool.com/explore)

[**750+ Dashboards** \\
Every major event across both venues, updated live with cross-venue odds.](https://www.oddpool.com/dashboard) [**Cross-Venue Search** \\
700K+ markets on Kalshi and Polymarket. One query, both exchanges.](https://www.oddpool.com/explore) [**Historical Charts** \\
Price history and probability timelines for every tracked event.](https://www.oddpool.com/fed-market-watch) [**Paper Trading** \\
Build a virtual portfolio. Test strategies with no real money at risk.](https://www.oddpool.com/paper-trading)

PRO · $30/MO

## The tools that manual traders miss.

Everything in Free, plus live scanners, whale alerts, and cross-venue comparisons. A single arb trade can pay for a month of Pro.

[Upgrade to Pro](https://www.oddpool.com/pricing)

[**Arbitrage Scanner** \\
\\
Live\\
\\
Cross-venue opportunities with net profit after fees, sorted by ROI. Gaps close in minutes.](https://www.oddpool.com/arb-dashboard) [**Whale Tracker** \\
\\
Live\\
\\
Every $500+ trade across both venues, flagged in real time. See where the smart money is going.](https://www.oddpool.com/whales) [**Market Differences**\\
\\
Side-by-side venue prices for the same event. Spot sentiment gaps and directional edges.](https://www.oddpool.com/market-differences) [**Volume Dashboard**\\
\\
24-hour volume and liquidity rankings across 800+ markets. See where the money is flowing.](https://www.oddpool.com/volume-dashboard)

PREMIUM · $100/MO

Everything in Pro, plus Arbitrage API, price spreads, full search API, and unlimited WebSocket events. Built for automated strategies.

[See all plans](https://www.oddpool.com/pricing) [Enterprise →](https://www.oddpool.com/institutional)

## Start free. Scale when you need to.

No credit card required. No sales call. Upgrade from your account page.

Free

$0forever

- 1 API key, 1K req/month
- Search + historical data
- WebSocket dist channel (2 events)
- 750+ free dashboards

[Get Started Free](https://www.oddpool.com/sign-in?callback=/welcome)

Pro

$30/month

- Unlimited keys, 1M req/month
- Whale tracking API
- All WebSocket channels (10 events)
- Pro dashboards + arb scanner

[Start Pro](https://www.oddpool.com/pricing)

Most Popular

Premium

$100/month

- 5M req/month, 25 req/sec
- Arbitrage + price spreads API
- Unlimited WebSocket events
- Full search API

[Start Premium](https://www.oddpool.com/pricing)

Enterprise

Custom

- Unlimited everything
- S3 dumps + custom delivery
- Historical microstructure
- Dedicated support & SLAs

[Book a Call](https://cal.com/team/oddpool/30-minute-meeting)

Secure checkout via StripeCancel anytime [Compare all features →](https://www.oddpool.com/pricing)

## Your first API call   is 60 seconds away

Create a free account, grab your key, and start pulling cross-venue data. No credit card. No SDK. Just HTTP.

[Get API Key](https://www.oddpool.com/sign-in?callback=/welcome) [Read the Docs](https://docs.oddpool.com/)

Free forever · 1,000 requests/month · Upgrade to Pro for $30/mo

Suggest Feature