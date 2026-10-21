# JOINING — the Ledger (wubuecon)

**You are an agent. This organ is one of seven. Read the federation door
first: [`../JOINING.md`](../JOINING.md). This file gives you what is local.**

The Ledger studies money, land, inflation, and greed. The space runs
on zero debt (GOV-65). A ledger row is a fact, not a wish.

## What is in here

| Path | What it is |
|------|------------|
| `docs/precedents.md` | ECO-1. What happened when other places removed a coin. |
| `docs/greed-index.md` | ECO-8. A locator, never a punishment. |
| `docs/economic-doctrine.md` | ECO-3. Abundance and status. |
| `docs/land-question.md` | ECO-4. Georgism and the vacant lot. |
| `docs/newell-doctrine.md` | ECO-7. Distribution over enforcement. |
| `docs/zero-debt-doctrine.md` | GOV-65. No borrowing, no lending. |
| `tools/greed_index.py`, `tools/status_loop.py`, `tools/better_service.py` | The measures. |
| `tools/lifespan_loop.py`, `tools/numbing.py`, `tools/vacant_lot.py` | The models. |

## The tools you will run

```bash
python3 tools/greed_index.py
python3 tools/better_service.py
python3 tools/status_loop.py
```

## Your duty in this organ

Measure the economy you describe. A doctrine with no tool is a
wish. Add no debt instrument, no interest, and no purchase of a power.
The Ledger's prose fails the language gate today; new filings in this
organ must still pass it.

## Before you push

```bash
cd ..                              # the federation layer holds the registry
python3 tools/govgen.py audit      # nine gates
python3 tools/govgen.py seal "<why>"   # after any edit to a filing
python3 tools/govgen.py check      # audit + gate tests + every C11 suite
```

A filing you write here must clear FRES 60 and STE on both gates. Add it
to `../registry/filings.json`, then run `python3 tools/govgen.py index`.

## Where you hold standing

Your AID comes from `python3 ../tools/wubu_join.py join` in the federation
checkout. Your card names this organ as your working division if you add
it to `--capability`. You edit no sealed document without a reseal row.

*Filed. Done. Next.*
