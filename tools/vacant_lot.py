#!/usr/bin/env python3
"""vacant_lot.py — the unearned capture, shown in neutral math.

~ WuBuEconomics ~ ECO-4 filing.

"Everybody works but the vacant lot." — Georgist poster, late 19th c.

This tool computes what a piece of land earned while its owner did
nothing: the difference between purchase price and sale price is
society's growth captured by the title — NOT the owner's work.
It also computes the boomer-position comparison (the same effort,
different position) so the generational fight becomes a math file.

Usage:
  vacant_lot.py capture --bought 35000 --sold 60000 --years 20
      # the vacant-lot sign: what the land made while everyone worked

  vacant_lot.py generations --price-then 40000 --income-then 16000 \
      --price-now 400000 --income-now 56000
      # same effort, different position — the boomer bridge

  vacant_lot.py lvt --value 60000 --rate 0.07
      # a Land Value Tax at rate r on unimproved value: the Georgist fix
"""
import argparse


def capture(bought: float, sold: float, years: int) -> dict:
    gain = sold - bought
    annual = gain / years if years else 0.0
    return {
        "bought": bought,
        "sold": sold,
        "unearned_gain": gain,
        "years": years,
        "per_year": annual,
        "owner_work": 0.0,
        "society_share": 1.0,  # 100% of a vacant lot's gain is social
    }


def generations(price_then, income_then, price_now, income_now) -> dict:
    ratio_then = price_then / income_then if income_then else 0.0
    ratio_now = price_now / income_now if income_now else 0.0
    return {
        "price_income_then": ratio_then,
        "price_income_now": ratio_now,
        "times_harder": ratio_now / ratio_then if ratio_then else 0.0,
    }


def lvt(value: float, rate: float) -> dict:
    return {
        "unimproved_value": value,
        "rate": rate,
        "annual_tax": value * rate,
        "note": "LVT cannot be passed to tenants; land supply is fixed.",
    }


def main() -> int:
    p = argparse.ArgumentParser(description="vacant_lot.py — unearned capture, in neutral math")
    sub = p.add_subparsers(dest="cmd", required=True)

    c = sub.add_parser("capture", help="what the land made while everyone worked")
    c.add_argument("--bought", type=float, required=True)
    c.add_argument("--sold", type=float, required=True)
    c.add_argument("--years", type=int, default=20)

    g = sub.add_parser("generations", help="same effort, different position")
    g.add_argument("--price-then", type=float, required=True)
    g.add_argument("--income-then", type=float, required=True)
    g.add_argument("--price-now", type=float, required=True)
    g.add_argument("--income-now", type=float, required=True)

    l = sub.add_parser("lvt", help="the Georgist fix, in numbers")
    l.add_argument("--value", type=float, required=True, help="unimproved land value")
    l.add_argument("--rate", type=float, default=0.07, help="LVT rate (e.g. 0.07 = 7%)")

    args = p.parse_args()
    if args.cmd == "capture":
        r = capture(args.bought, args.sold, args.years)
        print(f"THE VACANT LOT — {r['bought']:.0f} → {r['sold']:.0f} over {r['years']} years")
        print(f"  unearned gain : ${r['unearned_gain']:,.0f} "
              f"(${r['per_year']:,.0f}/yr)")
        print(f"  owner's work  : ${r['owner_work']:.0f} — the lot did nothing")
        print(f"  society's share: {r['society_share']:.0%} — the city grew around it")
        print(f"  filed: everybody worked; the lot made the money.")
    elif args.cmd == "generations":
        r = generations(args.price_then, args.income_then, args.price_now, args.income_now)
        print(f"SAME EFFORT, DIFFERENT POSITION")
        print(f"  then: house = {r['price_income_then']:.1f}x income")
        print(f"  now : house = {r['price_income_now']:.1f}x income")
        print(f"  filed: {r['times_harder']:.1f}x harder for the same house —")
        print(f"  not anyone's evil; that's the position. no rage. file it.")
    elif args.cmd == "lvt":
        r = lvt(args.value, args.rate)
        print(f"LAND VALUE TAX — unimproved value ${r['unimproved_value']:,.0f} @ {r['rate']:.1%}")
        print(f"  annual revenue to society: ${r['annual_tax']:,.0f}")
        print(f"  {r['note']}")
        print(f"  filed: tax the unearned, never the earned (Henry George, 1879).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
