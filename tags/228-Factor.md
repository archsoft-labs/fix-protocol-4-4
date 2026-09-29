[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 228](https://www.onixs.biz/fix-dictionary/4.4/tagNum_228.html)

# FIX 4.4 : Factor <228> field

**Type:** [float](https://www.onixs.biz/fix-dictionary/4.4/index.html#float)

## Description

For Fixed Income: Amorization Factor for deriving Current face from Original face for ABS or MBS securities, note the fraction may be greater than, equal to or less than 1. In TIPS securities this is the Inflation index.

Qty * [Factor <228>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_228.html) * [Price <44>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_44.html) = Gross Trade Amount

For Derivatives: Contract Value Factor by which price must be adjusted to determine the true nominal value of one futures/options contract.

(Qty * [Price <44>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_44.html)) * [Factor <228>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_228.html) = Nominal Value

(Note tag # was reserved in FIX 4.1, added in FIX 4.3)

## Used In

- [<Instrument>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_Instrument.html)

