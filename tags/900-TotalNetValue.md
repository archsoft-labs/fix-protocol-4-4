[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 900](https://www.onixs.biz/fix-dictionary/4.4/tagNum_900.html)

# FIX 4.4 : TotalNetValue <900> field

**Type:** [Amt](https://www.onixs.biz/fix-dictionary/4.4/index.html#Amt)

## Description

TotalNetValue is determined as follows:

At the initial collateral assignment [TotalNetValue <900>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_900.html) is the sum of ([UnderlyingStartValue <884>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_884.html) * (1-haircut)).

In a collateral substitution [TotalNetValue <900>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_900.html) is the sum of ([UnderlyingCurrentValue <885>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_885.html) * (1-haircut)).

## Used In

- [Collateral Request <AX>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AX_6588.html)
- [Collateral Assignment <AY>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AY_6589.html)
- [Collateral Response <AZ>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AZ_6590.html)
- [Collateral Report <BA>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BA_6665.html)
- [Collateral Inquiry <BB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BB_6666.html)

