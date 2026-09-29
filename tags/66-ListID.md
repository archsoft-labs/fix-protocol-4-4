[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 66](https://www.onixs.biz/fix-dictionary/4.4/tagNum_66.html)

# FIX 4.4 : ListID <66> field

**Type:** [String](https://www.onixs.biz/fix-dictionary/4.4/index.html#String)

## Description

Unique identifier for list as assigned by institution, used to associate multiple individual orders. Uniqueness must be guaranteed within a single trading day. Firms which generate multi-day orders should consider embedding a date within the [ListID <66>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_66.html) field to assure uniqueness across days.

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [Order Cancel Reject <9>](https://www.onixs.biz/fix-dictionary/4.4/msgType_9_9.html)
- [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)
- [Confirmation <AK>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AK_6575.html)
- [Allocation Report <AS>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AS_6583.html)
- [Confirmation Request <BH>](https://www.onixs.biz/fix-dictionary/4.4/msgType_BH_6672.html)
- [New Order List <E>](https://www.onixs.biz/fix-dictionary/4.4/msgType_E_69.html)
- [Order Cancel Request <F>](https://www.onixs.biz/fix-dictionary/4.4/msgType_F_70.html)
- [Order Cancel/Replace Request <G>](https://www.onixs.biz/fix-dictionary/4.4/msgType_G_71.html)
- [Allocation Instruction <J>](https://www.onixs.biz/fix-dictionary/4.4/msgType_J_74.html)
- [Bid Request <k>](https://www.onixs.biz/fix-dictionary/4.4/msgType_k_107.html)
- [List Cancel Request <K>](https://www.onixs.biz/fix-dictionary/4.4/msgType_K_75.html)
- [Bid Response <l>](https://www.onixs.biz/fix-dictionary/4.4/msgType_l_108.html)
- [List Execute <L>](https://www.onixs.biz/fix-dictionary/4.4/msgType_L_76.html)
- [List Strike Price <m>](https://www.onixs.biz/fix-dictionary/4.4/msgType_m_109.html)
- [List Status Request <M>](https://www.onixs.biz/fix-dictionary/4.4/msgType_M_77.html)
- [List Status <N>](https://www.onixs.biz/fix-dictionary/4.4/msgType_N_78.html)

