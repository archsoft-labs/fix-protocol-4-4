[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 752](https://www.onixs.biz/fix-dictionary/4.4/tagNum_752.html)

# FIX 4.4 : SideMultiLegReportingType <752> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Used to indicate if the side being reported on [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html) represents a leg of a multileg instrument or a single security.

Valid values:

1 = Single Security (default if not specified)

2 = Individual leg of a multileg security

3 = Multileg security

## Used In

- [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)

