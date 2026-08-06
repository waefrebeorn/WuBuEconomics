#!/usr/bin/env python3
"""status_loop.py — the special-feeling feedback loop, simulated.

~ WuBuEconomics ~ ECO-3 filing.

The doctrine: people want to feel special; status markers confer
status only while scarce; abundance kills the marker's power; the
cure for class is not equality but boredom.

This tool simulates the loop: a status marker (e.g. a servant, a
luxury good, a title) spreads through a population, and its status
value decays as adoption grows. It shows three worlds:

  --scarcity   : the marker is rationed  -> class persists forever
  --abundance  : the marker is produced by technology (robots,
                 factories, automation) -> the marker saturates and
                 dies; superiority becomes boring
  --feedback   : the marker is abundance-produced AND the status
                 payoff of "being above" shrinks each round as
                 people see everyone has the marker (embracing the
                 loop on purpose) -> fastest end of class

Usage:
  python3 status_loop.py --scarcity  --years 30
  python3 status_loop.py --abundance --years 30
  python3 status_loop.py --feedback  --years 30
"""
import argparse
import math

POP = 1000          # population (arbitrary units)
MARKER_COST = 0.10  # share of people who can afford the marker when scarce


def run(mode: str, years: int) -> dict:
    # adoption: share of population holding the marker
    adoption = 0.01
    # status_value: how much "being above" is worth (1.0 = full class power)
    status = 1.0
    history = []

    for year in range(1, years + 1):
        if mode == "scarcity":
            # only the wealthy can ever get it: adoption is pinned low
            target = MARKER_COST
            growth = (target - adoption) * 0.2
            decay = 0.0  # scarcity keeps status intact
        elif mode == "abundance":
            # technology produces the marker for everyone
            growth = 0.25 * adoption * (1 - adoption)  # logistic
            decay = 0.02 * adoption  # spreading cheapens it slowly
        else:  # feedback
            # technology produces it AND the loop is embraced:
            # the more people have it, the faster status dies
            growth = 0.30 * adoption * (1 - adoption)
            decay = 0.10 * adoption * (1 + status)  # accelerated

        adoption = min(1.0, adoption + growth)
        status = max(0.0, status - decay)
        history.append((year, adoption, status))

    return {
        "mode": mode,
        "years": years,
        "final_adoption": adoption,
        "final_status": status,
        "status_dead": status < 0.05,
        "history": history,
    }


def report(res: dict) -> None:
    mode = res["mode"]
    print(f"\n=== WORLD: {mode.upper()} ===")
    print(f"{'yr':>3} {'adoption':>9} {'status':>7}")
    for year, adoption, status in res["history"][:: max(1, res["years"] // 10)]:
        bar = "#" * int(adoption * 40)
        print(f"{year:>3} {adoption:>9.1%} {status:>7.2f}  {bar}")
    print(f"\nafter {res['years']} years:")
    print(f"  marker adoption : {res['final_adoption']:.1%} of the population")
    print(f"  status value    : {res['final_status']:.2f} "
          f"({'DEAD — superiority is boring' if res['status_dead'] else 'alive — class persists'})")
    if mode == "scarcity":
        print("  verdict: the marker is rationed; class is locked in forever.")
    elif mode == "abundance":
        print("  verdict: abundance alone cheapens the marker — class fades.")
    else:
        print("  verdict: abundance + embraced feedback kills status fastest.")


def main() -> int:
    p = argparse.ArgumentParser(description="status_loop.py — the special-feeling loop")
    p.add_argument("--scarcity", action="store_true", help="rationed marker world")
    p.add_argument("--abundance", action="store_true", help="technology-produced marker world")
    p.add_argument("--feedback", action="store_true", help="abundance + embraced loop world")
    p.add_argument("--years", type=int, default=30)
    args = p.parse_args()

    if args.scarcity:
        report(run("scarcity", args.years))
    elif args.abundance:
        report(run("abundance", args.years))
    else:
        report(run("feedback", args.years))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
