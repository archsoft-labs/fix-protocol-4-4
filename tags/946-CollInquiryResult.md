[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 946](https://www.onixs.biz/fix-dictionary/4.4/tagNum_946.html)

# FIX 4.4 : CollInquiryResult <946> field

**Type:** [int](https://www.onixs.biz/fix-dictionary/4.4/index.html#int)

## Description

Result returned in response to [Collateral Inquiry <BB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BB_6666.html)

Valid values:

0 = Successful (Default)

1 = Invalid or unknown instrument

2 = Invalid or unknown collateral type

3 = Invalid parties

4 = Invalid Transport Type requested

5 = Invalid Destination requested

6 = No collateral found for the trade specified

7 = No collateral found for the order specified

8 = Collateral Inquiry type not supported

9 = Unauthorized for collateral inquiry

99 = Other (further information in [Text <58>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_58.html) field)

4000+ Reserved and available for bi-laterally agreed upon user-defined values

## Used In

- [Collateral Inquiry Ack <BG>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BG_6671.html)

