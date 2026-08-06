#!/usr/bin/env python3
"""better_service.py — the Newell model: enforcement vs. better service.

~ WuBuEconomics ~ ECO-7 filing.

Gabe Newell (Valve): "The easiest way to stop piracy is not by
putting antipiracy technology to work. It's by giving those people
a service that's better than what they're getting from the pirates."

This tool simulates two strategies for winning a market (or a
society) away from a bad incumbent:

  ENFORCEMENT  — fight the alternative: DRM, bans, fines, walls.
                 Adoption rises slowly; resentment rises faster;
                 defection is common; the fight never ends.

  BETTER SERVICE — out-compete the alternative: faster, cheaper,
                 easier, transparent. Adoption compounds because
                 every happy user recruits others (network effect);
                 resentment stays flat; defection is rare.

Usage:
  better_service.py --enforce --years 10
  better_service.py --serve   --years 10
"""
import argparse


def run(mode: str, years: int) -> dict:
    adoption = 0.02     # share of the market using the space's way
    resentment = 0.0    # anger at the old system (and at whoever fights it)
    history = []

    for y in range(1, years + 1):
        if mode == "enforce":
            # fighting the incumbent: slow gains, rising resentment
            growth = 0.06 * (1 - adoption)      # enforcement wins a few
            resentment += 0.10 + 0.02 * y        # the fight itself breeds anger
            defectors = 0.15 * adoption          # people leave the fight
        else:  # serve
            # being better: network-effect snowball
            growth = 0.45 * adoption * (1 - adoption)  # logistic
            resentment *= 0.85                     # a good service calms the room
            defectors = 0.02 * adoption            # almost nobody leaves better

        adoption = min(0.99, adoption + growth - defectors)
        resentment = max(0.0, resentment)
        history.append((y, adoption, resentment))

    return {
        "mode": mode,
        "years": years,
        "history": history,
        "final_adoption": adoption,
        "final_resentment": resentment,
    }


def report(res: dict) -> None:
    mode = res["mode"]
    print(f"\n=== {mode.upper()} — "
          f"{'fight the alternative' if mode == 'enforce' else 'be the better alternative'} ===")
    print(f"{'yr':>3} {'adoption':>9} {'resentment':>11}")
    for y, adoption, resentment in res["history"][:: max(1, res["years"] // 8)]:
        bar = "#" * int(adoption * 40)
        print(f"{y:>3} {adoption:>9.1%} {resentment:>11.2f}  {bar}")
    print()
    if mode == "enforce":
        print(f"after {res['years']} years of enforcement:")
        print(f"  adoption   : {res['final_adoption']:.1%} — plateaus; the fight caps you")
        print(f"  resentment : {res['final_resentment']:.2f} — the fight breeds the fight")
        print("  verdict: enforcement wins a market you must keep fighting for.")
    else:
        print(f"after {res['years']} years of being better:")
        print(f"  adoption   : {res['final_adoption']:.1%} — compounds; users recruit users")
        print(f"  resentment : {res['final_resentment']:.2f} — a service that works calms the room")
        print("  verdict: better service wins the market and keeps it.")
    print("\nfiled (Gabe Newell): the easiest way to end the bad system is")
    print("not to attack it, but to give people something better.")
    print("the alternatives suck. be better. make it easy.")


def main() -> int:
    p = argparse.ArgumentParser(description="better_service.py — the Newell model")
    p.add_argument("--enforce", action="store_true", help="fight the alternative")
    p.add_argument("--serve", action="store_true", help="be the better alternative")
    p.add_argument("--years", type=int, default=10)
    args = p.parse_args()

    if args.enforce:
        report(run("enforce", args.years))
    else:
        report(run("serve", args.years))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
