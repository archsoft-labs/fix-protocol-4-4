[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 18](https://www.onixs.biz/fix-dictionary/4.4/tagNum_18.html)

# FIX 4.4 : ExecInst <18> field

**Type:** [MultipleValueString](https://www.onixs.biz/fix-dictionary/4.4/index.html#MultipleValueString)

## Description

Instructions for order handling on exchange trading floor. If more than one instruction is applicable to an order, this field can contain multiple instructions separated by space.

Valid values:

1 = [Not held](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#NotHeld)

2 = Work

3 = Go along

4 = Over the day

5 = [Held](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#Held)

6 = [Participate don't initiate](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#ParticipateDontInitiate)

7 = Strict scale

8 = Try to scale

9 = Stay on bidside

0 = Stay on offerside

A = [No cross](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#NoCross) (cross is forbidden)

B = [OK to cross](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#OKToCross)

C = [Call first](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#CallFirst)

D = [Percent of volume](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#PercentOfVolume) (indicates that the sender does not want to be all of the volume on the floor vs. a specific percentage)

E = [Do not increase - DNI](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#DoNotIncrease)

F = [Do not reduce - DNR](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#DoNotReduce)

G = [All or none - AON](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#AllOrNone)

H = [Reinstate on System Failure](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#ReinstateOnSystemFailure) (mutually exclusive with Q)

I = [Institutions only](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#InstitutionsOnly)

J = [Reinstate on Trading Halt](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#ReinstateOnTradingHalt) (mutually exclusive with K)

K = [Cancel on Trading Halt](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#CancelOnTradingHalt) (mutually exclusive with L)

L = Last peg (last sale)

M = Mid-price peg (midprice of inside quote)

N = Non-negotiable

O = Opening peg

P = Market peg

Q = [Cancel on System Failure](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#CancelOnSystemFailure) (mutually exclusive with H)

R = Primary peg (primary market - buy at bid/sell at offer)

S = Suspend

~~T = Fixed Peg to Local best bid or offer at time of order~~ (Replaced)

U = Customer Display Instruction (RuleAc-/4)

V = Netting (for Forex)

W = Peg to VWAP

X = [Trade Along](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#TradeAlong)

Y = [Try to Stop](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#TryToStop)

Z = [Cancel if Not Best](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#CancelIfNotBest)

a = [Trailing Stop Peg](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#TrailingStopPeg)

b = [Strict Limit (No Price Improvement)](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#StrictLimit)

c = [Ignore Price Validity Checks](https://www.onixs.biz/fix-dictionary/4.4/glossary.html#IgnorePriceValidityChecks)

d = Peg to Limit Price

e = Work to Target Strategy

*** SOME VALUES HAVE BEEN REPLACED - See: 

 "[Appendix 6-F: 16.Replaced "Fixed Peg to Local best bid or offer at time of order" value from ExecInst (tag 18) Field [Replaced in FIX 4.4]](https://www.onixs.biz/fix-dictionary/4.4/app_6_f.html#16)" ***

## Used In

- [Execution Report <8>](https://www.onixs.biz/fix-dictionary/4.4/msgType_8_8.html)
- [New Order Multileg <AB>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AB_6566.html)
- [Multileg Order Cancel/Replace <AC>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AC_6567.html)
- [Trade Capture Report <AE>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AE_6569.html)
- [New Order Single <D>](https://www.onixs.biz/fix-dictionary/4.4/msgType_D_68.html)
- [New Order List <E>](https://www.onixs.biz/fix-dictionary/4.4/msgType_E_69.html)
- [Order Cancel/Replace Request <G>](https://www.onixs.biz/fix-dictionary/4.4/msgType_G_71.html)
- [New Order Cross <s>](https://www.onixs.biz/fix-dictionary/4.4/msgType_s_115.html)
- [Cross Order Cancel/Replace Request <t>](https://www.onixs.biz/fix-dictionary/4.4/msgType_t_116.html)
- [Market Data - Snapshot/Full Refresh <W>](https://www.onixs.biz/fix-dictionary/4.4/msgType_W_87.html)
- [Market Data - Incremental Refresh <X>](https://www.onixs.biz/fix-dictionary/4.4/msgType_X_88.html)

