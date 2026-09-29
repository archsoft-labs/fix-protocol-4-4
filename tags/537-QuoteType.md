[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 537](https://www.onixs.biz/fix-dictionary/4.4/tagNum_537.html)

# FIX 4.4 : QuoteType <537> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Identifies the type of quote.

Valid values:

0 = Indicative

1 = Tradeable

2 = Restricted Tradeable

3 = Counter (tradable)

An indicative quote is used to inform a counterparty of a market. An indicative quote does not result directly in a trade.

A tradeable quote is submitted to a market and will result directly in a trade against other orders and quotes in a market.

A restricted tradeable quote is submitted to a market and within a certain restriction (possibly based upon price or quantity) will automatically trade against orders. Order that do not comply with restrictions are sent to the quote issuer who can choose to accept or decline the order.

A counter quote is used in the negotiation model. See Volume 7 - "Product: Fixed Income" for example usage.

## Used In

- [Quote Request Reject <AG>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AG_6571.html)
- [RFQ Request <AH>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AH_6572.html)
- [Quote Status Report <AI>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AI_6573.html)
- [Quote Response <AJ>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AJ_6574.html)
- [Mass Quote Acknowledgement <b>](https://www.onixs.biz/fix-dictionary/4.4/msgType_b_98.html)
- [Mass Quote <i>](https://www.onixs.biz/fix-dictionary/4.4/msgType_i_105.html)
- [Quote Request <R>](https://www.onixs.biz/fix-dictionary/4.4/msgType_R_82.html)
- [Quote <S>](https://www.onixs.biz/fix-dictionary/4.4/msgType_S_83.html)

