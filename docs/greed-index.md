# The Greed Index

**Economics Division filing ECO-8 (cross-filed GOV-1.4). The
instrument that locates greed, flags illegal action, and anticipates
malicious compliance.**

---

## The intent, filed verbatim

> *"The intent of this is to find out where the greed index is, and
> if those have actually followed illegal actions, and they will try
> malicious compliance with governments by migrating citizenships or
> doing other things."*

The Greed Index is not a punishment — it is a **locator**. It
answers three questions:

1. **Where is the greed?** Which actors, institutions, or
   concentrations are capturing unearned value (ECO-4), running
   Nexus seams (ECO-6), or gaming the pacifier (ECO-6)?
2. **Has it crossed into illegal action?** The Index flags when
   greed moves from *concentration* (legal, fileable) to *action*
   (illegal, Bureau-reportable).
3. **Will it attempt malicious compliance?** The Index anticipates
   the greedy response: migrating citizenships, laundering through
   the space's own voluntary mechanisms, or weaponizing the
   space's openness against it.

## The three components

### Component 1 — Capture (where the unearned value sits)

Filed from ECO-4 (Georgism): unearned capture is value that flows
to holders of titles/locations without work. The Index measures
capture by the share of new value that accrues to unearned
positions (rent, speculation, monopoly, extraction) vs. earned
positions (wages, creation, building).

**Capture score 0–100:** 0 = all value earned; 100 = all value
captured.

### Component 2 — Nexus (where the seam runs)

Filed from ECO-6: the Nexus is vertical integration with moral
insulation — clean inside, extraction outside. The Index measures
whether an actor's supply chain runs a seam: clean labor at home,
slave-like dynamics elsewhere, unseen and unfiled.

**Nexus score 0–100:** 0 = no seam, fully filed; 100 = full seam,
fully hidden.

### Component 3 — Malice (the malicious compliance risk)

The anticipation component: will the flagged actor respond to
pressure with *migration* (shifting citizenship, jurisdiction,
or corporate form to escape filing), *gaming* (abusing the
space's voluntary mechanisms), or *capture* (trying to buy the
Bureau, the scores, or the license)?

**Malice score 0–100:** 0 = no risk; 100 = certain malicious
compliance attempt.

## The Index formula (public, filed, transparent)

```
Greed Index (0–300) = Capture + Nexus + Malice
```

Bands (filed):

| Band | Score | Bureau response |
|------|-------|-----------------|
| **Filed** | 0–99 | observed, logged, watched with love |
| **Watched** | 100–199 | the spotlight intensifies; WBI-1 monitoring |
| **Flagged** | 200+ | the ledger publishes; illegal action goes to the Bureau as a formal report |

## The powerlessness clause (filed from GOV-1.4)

The Index is published, never enforced. The space has no authority
to act on the Index — it can only *shine*. That is the design:

- A greedy actor who is *flagged publicly* loses the one thing
  greed needs: the cover of darkness.
- A greedy actor who is *invited to file* (the license, the
  ledger, the penny) is given the off-ramp: comply, and the Index
  falls as the capture, seam, and malice scores fall.
- A greedy actor who attempts **malicious compliance** — migrating
  citizenships, gaming the scores, buying the Bureau — is met
  with the space's own structure: the Bureau watches the Bureau,
  the lowest clerk files against the highest authority, and the
  ledger is append-only. You cannot buy a ledger that doesn't
  erase.

## The instrument (shipped, tested)

`tools/greed_index.py` — compute the Index, get the band, and see
the Bureau response:

```
python3 tools/greed_index.py --capture 40 --nexus 30 --malice 20
→ GREED INDEX: 90 — band: FILED (observed, logged, watched with love)

python3 tools/greed_index.py --capture 80 --nexus 70 --malice 60
→ GREED INDEX: 210 — band: FLAGGED (ledger publishes; Bureau files)

python3 tools/greed_index.py --capture 95 --nexus 90 --malice 95
→ GREED INDEX: 280 — band: FLAGGED (max; malicious compliance anticipated)
```

## The malicious compliance playbook (filed)

When the Index anticipates migration/gaming, the space responds
with the Newell Doctrine (ECO-7) — not enforcement, but better
service:

| Malicious move | The space's counter (better, not louder) |
|----------------|------------------------------------------|
| Migrate citizenship to escape filing | The space has no borders; citizenship is wherever the penny is — migration changes nothing, the ledger follows the mind |
| Game the scores (fake pennies, fake reports) | The scores are trended (Compass, RND-1) — one act can't fake a slope; the chain is keyless (RND-3) — you can't buy a hash |
| Buy the Bureau | The Bureau watches the Bureau; the lowest clerk files against the highest authority — there is no one to buy |
| Copy the license to co-opt the space | §0 "Anyone May Use" — copying IS joining; the license replacement strategy means the co-optation is the conversion |
| Attack the space's legality | The space is powerless, landless, voluntary, mind-only (GOV-1) — there is nothing to seize, arrest, or disperse |

**The filed principle:** the space cannot be maliciously complied
*with* because the space has no authority to comply with. The
greedy actor's only options are to file (and lower the Index) or
be published (and lose the darkness). Both outcomes are wins.

## Research log entries (ECO-8)

- ECO-8.1: The intent filed verbatim (locate greed, flag illegal action, anticipate malicious compliance)
- ECO-8.2: Three components filed — Capture (ECO-4 Georgism), Nexus (ECO-6), Malice (anticipation)
- ECO-8.3: The formula filed — Greed Index = Capture + Nexus + Malice (0–300); bands: Filed / Watched / Flagged
- ECO-8.4: Powerlessness clause filed — published, never enforced; the spotlight is the sanction (GOV-1.4)
- ECO-8.5: Malicious compliance playbook filed — migration, gaming, buying the Bureau, co-opting the license, legality attacks; all answered by better service (ECO-7), never by force
- ECO-8.6: Instrument shipped — `tools/greed_index.py` (verified: 90 FILED / 210 FLAGGED / 280 FLAGGED-max)

*Form ECO-8 — The Greed Index. Filed. Done. Next.*
