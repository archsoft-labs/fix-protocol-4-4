[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 231](https://www.onixs.biz/fix-dictionary/4.4/tagNum_231.html)

# FIX 4.4 : ContractMultiplier <231> field

**Type:** [float](https://www.onixs.biz/fix-dictionary/4.4/index.html#float)

## Description

Specifies the ratio or multiply factor to convert from "nominal" units (e.g. contracts) to total units (e.g. shares) (e.g. 1.0, 100, 1000, etc). Applicable For Fixed Income, Convertible Bonds, Derivatives, etc.

In general quantities for all calsses should be expressed in the basic unit of the instrument, e.g. shares for equities, norminal or par amount for bonds, currency for foreign exchange. When quantity is expressed in contracts, e.g. financing transactions and bond trade reporting, ContractMutliplier should contain the number of units in one contract and can be omitted if the multiplier is the default amount for the instrument, i.e. 1,000 par of bonds, 1,000,000 par for financing transactions.

## Used In

- [<Instrument>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_Instrument.html)

