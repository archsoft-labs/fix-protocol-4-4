[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 17](https://www.onixs.biz/fix-dictionary/4.4/tagNum_17.html)

# FIX 4.4 : ExecID <17> field

**Type:** [String](https://www.onixs.biz/fix-dictionary/4.4/index.html#String)

## Description

Unique identifier of execution message as assigned by sell-side (broker, exchange, ECN) (will be 0 (zero) for [ExecType <150>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_150.html) ='I' (Order Status)).

Uniqueness must be guaranteed within a single trading day or the life of a multi-day order. Firms which accept multi-day orders should consider embedding a date within the [ExecID <17>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_17.html) field to assure uniqueness across days.

(Prior to FIX 4.1 this field was of type int)

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [Trade Capture Report Request <AD>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AD_6568.html)
- [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)
- [Trade Capture Report Ack <AR>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AR_6582.html)
- [Allocation Report <AS>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AS_6583.html)
- [Collateral Request <AX>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AX_6588.html)
- [Collateral Assignment <AY>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AY_6589.html)
- [Collateral Response <AZ>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AZ_6590.html)
- [Collateral Report <BA>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BA_6665.html)
- [Collateral Inquiry <BB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BB_6666.html)
- [Collateral Inquiry Ack <BG>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BG_6671.html)
- [Allocation Instruction <J>](https://www.onixs.biz/fix-dictionary/4.4/msgType_J_74.html)
- [Don't Know Trade <Q>](https://www.onixs.biz/fix-dictionary/4.4/msgType_Q_81.html)

