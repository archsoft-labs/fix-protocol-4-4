[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 586](https://www.onixs.biz/fix-dictionary/4.4/tagNum_586.html)

# FIX 4.4 : OrigOrdModTime <586> field

**Type:** [UTCTimestamp](https://www.onixs.biz/fix-dictionary/4.4/index.html#UTCTimestamp)

## Description

The most recent (or current) modification [TransactTime <60>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_60.html) reported on an [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html) for the order.

The [OrigOrdModTime <586>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_586.html) is provided as an optional field on [Order Cancel Request <F>](https://www.onixs.biz/fix-dictionary/4.4/msgType_F_70.html) and [Order Cancel/Replace Requests <G>](https://www.onixs.biz/fix-dictionary/4.4/msgType_G_71.html) to identify that the state of the order has not changed since the request was issued.

This is provided to support markets similar to Eurex and A/C/E.

## Used In

- [Order Cancel Reject <9>](https://www.onixs.biz/fix-dictionary/4.4/msgType_9_9.html)
- [Multileg Order Cancel/Replace <AC>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AC_6567.html)
- [Order Cancel Request <F>](https://www.onixs.biz/fix-dictionary/4.4/msgType_F_70.html)
- [Order Cancel/Replace Request <G>](https://www.onixs.biz/fix-dictionary/4.4/msgType_G_71.html)
- [Cross Order Cancel/Replace Request <t>](https://www.onixs.biz/fix-dictionary/4.4/msgType_t_116.html)
- [Cross Order Cancel Request <u>](https://www.onixs.biz/fix-dictionary/4.4/msgType_u_117.html)

