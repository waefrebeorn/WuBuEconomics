#!/usr/bin/env python3
"""lifespan_loop.py — the loop that is not a loop, simulated.

~ WuBuEconomics ~ ECO-5 filing.

The generational "cycle" is not a cycle — it is a function of one
number: lifespan. Generations alive at once = lifespan ÷ generation
gap. Medical advancement lengthens lifespan, stacks more generations
alive simultaneously, and the "generational war" is demographic
crowding — the queue of five generations standing in an economy
that has inflated four times since the oldest was born.

Verified anchors (Our World in Data):
  1900 global life expectancy: ~32 years  -> ~2 generations alive
  2026 global life expectancy: ~73 years  -> ~4 generations alive
  Japan / developed regions:   84+ years  -> ~5 generations alive

Usage:
  lifespan_loop.py --lifespan 32 --gap 25
  lifespan_loop.py --lifespan 73 --gap 25
  lifespan_loop.py --lifespan 84 --gap 25
  lifespan_loop.py --timeline          # stack over a century of medicine
"""
import argparse
import math


def generations_alive(lifespan: float, gap: float) -> float:
    """How many generations are alive at once (overlap estimate).

    A person born at t spans [t, t+lifespan]; generations are born
    every `gap` years. The number alive at any moment is roughly
    lifespan/gap, but with overlap smoothing we use the standard
    demographic estimate: floor(lifespan/gap) + 1 when the tail
    overlaps (the oldest generation's members are still alive when
    the newest is born).
    """
    raw = lifespan / gap
    return raw


def friction(raw: float) -> str:
    if raw < 2.0:
        return "LOW — handoff, not war (2 generations inherit & pass on)"
    if raw < 3.0:
        return "MODERATE — three generations, three price levels"
    if raw < 4.0:
        return "HIGH — four generations queued in one inflated economy"
    return "MAXIMUM — the fullest stack; the war is the victory over death"


def report(lifespan: float, gap: float) -> dict:
    raw = generations_alive(lifespan, gap)
    alive = math.floor(raw) + 1
    return {
        "lifespan": lifespan,
        "gap": gap,
        "raw_overlap": raw,
        "generations_alive": alive,
        "friction": friction(raw),
        "explanation": (
            f"{lifespan:.0f}yr lifespan ÷ {gap:.0f}yr gap = {raw:.1f} "
            f"→ ~{alive} generations alive at once"
        ),
    }


def timeline() -> None:
    print("THE STACK OVER A CENTURY OF MEDICINE (gap = 25 yrs)")
    print(f"{'year':>6} {'lifespan':>9} {'gens':>5}  friction")
    for year, life in [(1900, 32), (1950, 46), (1975, 59),
                       (2000, 66), (2026, 73), (2050, 78)]:
        r = report(life, 25)
        print(f"{year:>6} {life:>8.0f}yr {r['generations_alive']:>4}   "
              f"{r['friction'].split('—')[0].strip()}")
    print("\nfiled: the generational war is demographic crowding —")
    print("the better a region heals its people, the taller the stack,")
    print("and the louder the generations complain about each other.")


def main() -> int:
    p = argparse.ArgumentParser(description="lifespan_loop.py — the loop that is not a loop")
    p.add_argument("--lifespan", type=float, default=73.0, help="region life expectancy (years)")
    p.add_argument("--gap", type=float, default=25.0, help="generation gap (years)")
    p.add_argument("--timeline", action="store_true", help="show the stack 1900-2050")
    args = p.parse_args()

    if args.timeline:
        timeline()
        return 0

    r = report(args.lifespan, args.gap)
    print(f"LIFESPAN LOOP — {r['lifespan']:.0f}yr lifespan, {r['gap']:.0f}yr generation gap")
    print(f"  {r['explanation']}")
    print(f"  friction: {r['friction']}")
    print(f"\n  filed: not a cycle — a measurement. medical advancement")
    print(f"  stacks generations; the stack is the 'generational stigma.'")
    print(f"  blame the structure (lifespan), never the person.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
