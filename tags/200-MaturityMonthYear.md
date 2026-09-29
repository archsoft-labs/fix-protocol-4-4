[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 200](https://www.onixs.biz/fix-dictionary/4.4/tagNum_200.html)

# FIX 4.4 : MaturityMonthYear <200> field

**Type:** [MonthYear](https://www.onixs.biz/fix-dictionary/4.4/index.html#MonthYear)

## Description

Can be used with standardized derivatives vs. the [MaturityDate <541>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_541.html) field. Month and Year of the maturity (used for standardized futures and options).

Format:

YYYYMM (i.e. 199903)

YYYYMMDD (20030323)

YYYYMMwN (200303w1) for week

A specific date or can be appended to the [MaturityMonthYear <200>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_200.html). For instance, if multiple standard products exist that mature in the same Year and Month, but actually mature at a different time, a value can be appended, such as "w1" or "w2" to indicate week 1 as opposed to week 2 expiration. Likewise, the date (01-31) can be appended to indicate a specific expiration (maturity date).

## Used In

- [<Instrument>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_Instrument.html)

