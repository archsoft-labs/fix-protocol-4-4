[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 762](https://www.onixs.biz/fix-dictionary/4.4/tagNum_762.html)

# FIX 4.4 : SecuritySubType <762> field

**Type:** [String](https://www.onixs.biz/fix-dictionary/4.4/index.html#String)

## Description

Sub-type qualification/identification of the [SecurityType <167>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_167.html) (e.g. for SecurityType="REPO").

Example values:

General = General Collateral (for [SecurityType <167>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_167.html)="REPO")

For [SecurityType <167>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_167.html)="MLEG" markets can provide the name of the option or futures strategy, such as Calendar, Vertical, Butterfly, etc.

NOTE: Additional values may be used by mutual agreement of the counterparties

## Used In

- [<Instrument>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_Instrument.html)
- [Security Type Request <v>](https://www.onixs.biz/fix-dictionary/4.4/msgType_v_118.html)
- [Security Types <w>](https://www.onixs.biz/fix-dictionary/4.4/msgType_w_119.html)
- [Derivative Security List Request <z>](https://www.onixs.biz/fix-dictionary/4.4/msgType_z_122.html)

