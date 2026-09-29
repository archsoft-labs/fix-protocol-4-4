[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 126](https://www.onixs.biz/fix-dictionary/4.4/tagNum_126.html)

# FIX 4.4 : ExpireTime <126> field

**Type:** [UTCTimestamp](https://www.onixs.biz/fix-dictionary/4.4/index.html#UTCTimestamp)

## Description

Time/Date of order expiration (always expressed in UTC (Universal Time Coordinated, also known as "GMT")

The meaning of expiration is specific to the context where the field is used.

- For orders, this is the expiration time of a 'Good Till Date' [TimeInForce <59>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_59.html).

- For Quotes - this is the expiration of the quote.

- Expiration time is provided across the quote message dialog to control the length of time of the overall quoting process.

- For collateral requests, this is the time by which collateral must be assigned.

- For collateral assignments, this is the time by which a response to the assignment is expected.

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [New Order Multileg <AB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AB_6566.html)
- [Multileg Order Cancel/Replace <AC>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AC_6567.html)
- [Quote Request Reject <AG>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AG_6571.html)
- [Quote Status Report <AI>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AI_6573.html)
- [Settlement Instruction Request <AV>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AV_6586.html)
- [Collateral Request <AX>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AX_6588.html)
- [Collateral Assignment <AY>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AY_6589.html)
- [New Order Single <D>](https://www.onixs.biz/fix-dictionary/4.4/msgType_D_68.html)
- [New Order List <E>](https://www.onixs.biz/fix-dictionary/4.4/msgType_E_69.html)
- [Order Cancel/Replace Request <G>](https://www.onixs.biz/fix-dictionary/4.4/msgType_G_71.html)
- [Quote Request <R>](https://www.onixs.biz/fix-dictionary/4.4/msgType_R_82.html)
- [New Order Cross <s>](https://www.onixs.biz/fix-dictionary/4.4/msgType_s_115.html)
- [Cross Order Cancel/Replace Request <t>](https://www.onixs.biz/fix-dictionary/4.4/msgType_t_116.html)
- [Settlement Instructions <T>](https://www.onixs.biz/fix-dictionary/4.4/msgType_T_84.html)
- [Market Data - Snapshot/Full Refresh <W>](https://www.onixs.biz/fix-dictionary/4.4/msgType_W_87.html)
- [Market Data - Incremental Refresh <X>](https://www.onixs.biz/fix-dictionary/4.4/msgType_X_88.html)

