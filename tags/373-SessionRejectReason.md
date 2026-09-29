[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 373](https://www.onixs.biz/fix-dictionary/4.4/tagNum_373.html)

# FIX 4.4 : SessionRejectReason <373> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Code to identify reason for a session-level [Reject <3>](https://www.onixs.biz/fix-dictionary/4.4/msgType_3_3.html) message.

Valid values:

0 = Invalid tag number

1 = Required tag missing

2 = Tag not defined for this message type

3 = Undefined Tag

4 = Tag specified without a value

5 = Value is incorrect (out of range) for this tag

6 = Incorrect data format for value

7 = Decryption problem

8 = [Signature <89>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_89.html) problem

9 = CompID problem

10 = [SendingTime <52>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_52.html) accuracy problem

11 = Invalid [MsgType <35>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_35.html)

12 = XML Validation error

13 = Tag appears more than once

14 = Tag specified out of required order

15 = Repeating group fields out of order

16 = Incorrect NumInGroup count for repeating group

17 = Non "Data" value includes field delimiter (<SOH> character)

99 = Other

## Used In

- [Reject <3>](https://www.onixs.biz/fix-dictionary/4.4/msgType_3_3.html)

