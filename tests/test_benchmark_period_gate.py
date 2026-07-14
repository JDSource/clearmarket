#!/usr/bin/env python3
"""
Regression suite for the benchmark_drift period-match gate (spot-vs-forward defect,
shipped 2026-06-26 / 07-01 / 07-13 — see worklog). Deterministic, no API key needed.

The frozen case is the real 2026-07-13 wire: FRED CPIAUCNS latest obs = May 2026
(obs date 2026-05-01, published value 4.2%) while KXCPIYOY-26JUN-T3.9 closed
2026-07-14 on the June release. A trailing print cannot contradict a forward
forecast; the gate must refuse that candidate.
"""
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from gen_benchmark_drift import resolves_on_current_print

FAILS = []
def check(name, got, want):
    ok = got == want
    print(("PASS" if ok else "FAIL"), name, f"(got {got}, want {want})")
    if not ok: FAILS.append(name)

# 1. THE 2026-07-13 CPI WIRE (frozen regression case): June contract vs May print -> refuse.
check("cpi_june_contract_vs_may_print_refused",
      resolves_on_current_print("2026-07-14T12:29:00Z", "2026-05-01", "monthly"), False)

# 2. Same-print monthly market: contract closing on the May release (~Jun 10) vs May obs -> allow.
check("cpi_may_contract_vs_may_print_allowed",
      resolves_on_current_print("2026-06-10T12:29:00Z", "2026-05-01", "monthly"), True)

# 3. Quarterly (GDP): Q2 advance release (~Jul 30) vs Q2 obs (2026-04-01) -> allow.
check("gdp_q2_contract_vs_q2_obs_allowed",
      resolves_on_current_print("2026-07-30T14:00:00Z", "2026-04-01", "quarterly"), True)

# 4. Quarterly forward: Q3 contract (~Oct 30 close) vs Q2 obs -> refuse.
check("gdp_q3_contract_vs_q2_obs_refused",
      resolves_on_current_print("2026-10-30T14:00:00Z", "2026-04-01", "quarterly"), False)

# 5. Daily/spot series (fed funds target, 10yr yield) are always current.
check("daily_series_always_current",
      resolves_on_current_print("2026-12-31T00:00:00Z", "2026-07-13", "daily"), True)

# 6. Fail closed: missing close date, missing obs date, unknown periodicity -> refuse.
check("missing_close_refused", resolves_on_current_print("", "2026-05-01", "monthly"), False)
check("missing_obs_refused", resolves_on_current_print("2026-06-10", "", "monthly"), False)
check("unknown_periodicity_refused", resolves_on_current_print("2026-06-10", "2026-05-01", "weekly"), False)
check("garbage_date_refused", resolves_on_current_print("not-a-date", "2026-05-01", "monthly"), False)

if FAILS:
    print(f"\n{len(FAILS)} failure(s):", ", ".join(FAILS)); sys.exit(1)
print("\nall period-gate checks passed")
