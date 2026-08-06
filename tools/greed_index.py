#!/usr/bin/env python3
"""greed_index.py — locate greed, flag illegal action, anticipate malice.

~ WuBuEconomics ~ ECO-8 filing.

The Greed Index = Capture + Nexus + Malice (0-300).

  Capture : unearned value concentration (ECO-4 Georgism; rent,
            speculation, monopoly, extraction) — 0..100
  Nexus   : the seam — vertical integration with moral insulation
            (ECO-6; clean inside, slave-like outside) — 0..100
  Malice  : malicious compliance risk (citizenship migration,
            gaming the scores, buying the Bureau) — 0..100

Bands: 0-99 FILED (observed, logged, watched with love)
       100-199 WATCHED (spotlight intensifies, WBI-1 monitoring)
       200+ FLAGGED (ledger publishes; illegal action goes to Bureau)

The Index is published, never enforced — the space is powerless
(GOV-1.4). The spotlight is the sanction.

Usage:
  greed_index.py --capture 40 --nexus 30 --malice 20
  greed_index.py --capture 95 --nexus 90 --malice 95
"""
import argparse


def band(total: float) -> str:
    if total < 100:
        return "FILED — observed, logged, watched with love"
    if total < 200:
        return "WATCHED — spotlight intensifies; WBI-1 monitoring"
    return "FLAGGED — the ledger publishes; illegal action goes to the Bureau"


def verdict(total: float) -> str:
    if total < 100:
        return "no action — the Index observes and files."
    if total < 200:
        return "the spotlight brightens; the actor is invited to file (the off-ramp)."
    return ("the ledger publishes; malicious compliance is anticipated — "
            "the space answers with better service (ECO-7), never force.")


def main() -> int:
    p = argparse.ArgumentParser(description="greed_index.py — locate the greed")
    p.add_argument("--capture", type=float, required=True, help="capture score 0-100")
    p.add_argument("--nexus", type=float, required=True, help="nexus score 0-100")
    p.add_argument("--malice", type=float, required=True, help="malice score 0-100")
    args = p.parse_args()

    total = args.capture + args.nexus + args.malice
    print(f"GREED INDEX: {total:.0f}/300")
    print(f"  capture : {args.capture:.0f}/100  (unearned value concentration, ECO-4)")
    print(f"  nexus   : {args.nexus:.0f}/100  (the seam, clean inside/dirty outside, ECO-6)")
    print(f"  malice  : {args.malice:.0f}/100  (malicious compliance risk)")
    print(f"  band    : {band(total)}")
    print(f"  response: {verdict(total)}")
    print(f"\nfiled: the Index is published, never enforced.")
    print(f"the space has no authority — only the spotlight.")
    print(f"you cannot buy a ledger that doesn't erase.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
