[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 13](https://www.onixs.biz/fix-dictionary/4.4/tagNum_13.html)

# FIX 4.4 : CommType <13> field

**Type:** [char](https://www.onixs.biz/fix-dictionary/4.4/index.html#char)

## Description

[Commission <12>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_12.html) type

Valid values:

1 = per unit (implying shares, par, currency, etc)

2 = percentage

3 = absolute (total monetary amount)

4 = (for CIV buy orders) percentage waived - cash discount

5 = (for CIV buy orders) percentage waived - enhanced units

6 = points per bond or or contract [Supply [ContractMultiplier <231>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_231.html) in the [<Instrument>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_Instrument.html) component block if the object security is denominated in a size other than the industry default - 1000 par for bonds.]

## Used In

- [<CommissionData>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_CommissionData.html)
- [Quote Status Report <AI>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AI_6573.html)
- [Quote Response <AJ>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AJ_6574.html)
- [Quote <S>](https://www.onixs.biz/fix-dictionary/4.4/msgType_S_83.html)

