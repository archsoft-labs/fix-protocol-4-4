[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 636](https://www.onixs.biz/fix-dictionary/4.4/tagNum_636.html)

# FIX 4.4 : WorkingIndicator <636> field

**Type:** [Boolean](https://www.onixs.biz/fix-dictionary/4.4/index.html#Boolean)

## Description

Indicates if the order is currently being worked. Applicable only for [OrdStatus <39>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_39.html) = 'New'. For open outcry markets this indicates that the order is being worked in the crowd. For electronic markets it indicates that the order has transitioned from a contingent order to a market order.

Valid values:

Y = Order is currently being worked

N = Order has been accepted but not yet in a working state

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [Order Cancel Reject <9>](https://www.onixs.biz/fix-dictionary/4.4/msgType_9_9.html)
- [List Status <N>](https://www.onixs.biz/fix-dictionary/4.4/msgType_N_78.html)

