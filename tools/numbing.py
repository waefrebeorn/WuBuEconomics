#!/usr/bin/env python3
"""numbing.py — the electrical numbing, modeled across generations.

~ WuBuEconomics ~ ECO-6 filing.

The science (filed ECO-6.5/.6): acute stress ACTIVATES the dopamine
system; chronic exposure produces compensatory DOWNREGULATION (Koob's
opponent-process model) — fewer D2 receptors, blunted reward, a
hypodopaminergic brain. Stress also accelerates biological aging:
telomere shortening (Epel & Blackburn, PNAS 2004), epigenetic clock
acceleration, DNA damage.

This tool models a generation's reward sensitivity (1.0 = fully
sensitive) as chronic stress accumulates, with optional protective
factors (omega-3, exercise, sleep) that slow — but do not stop —
the downregulation. It compares three worlds:

  --calm    : low stress, protected  -> mild numbing
  --modern  : rising stress (ECO-5 four inflations) -> deep numbing
  --nexus   : pacifier economy, accelerated stress -> structural numbing

Usage:
  numbing.py --calm    --gens 5
  numbing.py --modern  --gens 5
  numbing.py --nexus   --gens 5
"""
import argparse
import math

# baseline reward sensitivity (fraction of full sensitivity)
BASE = 1.0


def world_params(mode: str) -> tuple:
    """(stress_per_gen, protection, label)"""
    if mode == "calm":
        return 0.06, 0.85, "CALM — low stress, protected (omega-3, work, sleep)"
    if mode == "modern":
        return 0.16, 0.55, "MODERN — four inflations, partial protection"
    return 0.26, 0.30, "NEXUS — pacifier economy, accelerated stress"


def run(mode: str, gens: int) -> dict:
    stress, protection, label = world_params(mode)
    sensitivity = BASE
    history = []

    for g in range(1, gens + 1):
        # stress erodes sensitivity; protection slows but never stops it
        erosion = stress * (1.0 - protection)  # protection is a dampener
        sensitivity = max(0.05, sensitivity - erosion)
        # brain age acceleration: epigenetic-style, compounds with stress
        bio_age_extra = 2.0 * stress * g * (1.0 - protection * 0.5)
        history.append({
            "gen": g,
            "sensitivity": sensitivity,
            "bio_extra": bio_age_extra,
        })

    return {
        "mode": mode,
        "label": label,
        "gens": gens,
        "history": history,
        "final_sensitivity": history[-1]["sensitivity"],
        "final_bio_extra": history[-1]["bio_extra"],
        "numbed": history[-1]["sensitivity"] < 0.5,
    }


def report(res: dict) -> None:
    print(f"\n=== {res['mode'].upper()} — {res['label']} ===")
    print(f"{'gen':>3} {'reward sens.':>12} {'bio-age extra':>13}  state")
    for h in res["history"]:
        bar = "#" * int(h["sensitivity"] * 30)
        state = "numbing" if h["sensitivity"] < 0.7 else "intact"
        if h["sensitivity"] < 0.4:
            state = "EMACIATED"
        print(f"{h['gen']:>3} {h['sensitivity']:>12.2f} {h['bio_extra']:>13.1f}  {bar} {state}")
    verdict = (
        "STRUCTURALLY NUMBED — the reward system is downregulated; "
        "even protection cannot fully reverse it (filed: receptor "
        "downregulation is structural)."
        if res["numbed"]
        else "still sensitive — the numbing is mild; protection held."
    )
    print(f"\nverdict: {verdict}")
    print(f"filed: 'there are just certain elements that electrically cause")
    print(f"numbing' — Koob opponent-process, Volkow imaging, Epel/Blackburn.")


def main() -> int:
    p = argparse.ArgumentParser(description="numbing.py — the electrical numbing, modeled")
    p.add_argument("--calm", action="store_true")
    p.add_argument("--modern", action="store_true")
    p.add_argument("--nexus", action="store_true")
    p.add_argument("--gens", type=int, default=5)
    args = p.parse_args()

    if args.calm:
        report(run("calm", args.gens))
    elif args.nexus:
        report(run("nexus", args.gens))
    else:
        report(run("modern", args.gens))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
