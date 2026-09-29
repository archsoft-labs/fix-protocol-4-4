[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 47](https://www.onixs.biz/fix-dictionary/4.4/tagNum_47.html)

# FIX 4.4 : Rule80A(No Longer Used) <47> field

**Type:** [char](https://www.onixs.biz/fix-dictionary/4.4/index.html#char)

## Description

No longer used as of FIX.4.4. Included here for reference to prior versions.

See [Appendix 6-F: 12.Removed Deprecated Field: Rule80A (tag 47) [Deprecated and Replaced in FIX 4.3, Removed in FIX 4.4]](https://www.onixs.biz/fix-dictionary/4.4/app_6_f.html#12)

Note that the name of this field is changing to [OrderCapacity <528>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_528.html) as Rule80A is a very US market-specific term. Other world markets need to convey similar information, however, often a subset of the US values. See VOLUME 4 - "OrderCapacity and OrderRestrictions (formerly Rule80A) Usage by Market" for market-specific usage of this field.

Valid values:

A = Agency single order

B = Short exempt transaction (refer to A type)

C = Program Order, non-index arb, for Member firm/org

D = Program Order, index arb, for Member firm/org

E = Short Exempt Transaction for Principal (was incorrectly identified in the FIX spec as "Registered Equity Market Maker trades")

F = Short exempt transaction (refer to W type)

H = Short exempt transaction (refer to I type)

I = Individual Investor, single order

J = Program Order, index arb, for individual customer

K = Program Order, non-index arb, for individual customer

L = Short exempt transaction for member competing market-maker affiliated with the firm clearing the trade (refer to P and O types)

M = Program Order, index arb, for other member

N = Program Order, non-index arb, for other member

O = Proprietary transactions for competing market-maker that is affiliated with the clearing member (was incorrectly identified in the FIX spec as "Competing dealer trades")

P = Principal

R = Transactions for the account of a non-member competing market maker (was incorrectly identified in the FIX spec as "Competing dealer trades")

S = Specialist trades

T = Transactions for the account of an unaffiliated member's competing market maker (was incorrectly identified in the FIX spec as "Competing dealer trades")

U = Program Order, index arb, for other agency

W = All other orders as agent for other member

X = Short exempt transaction for member competing market-maker not affiliated with the firm clearing the trade (refer to W and T types)

Y = Program Order, non-index arb, for other agency

Z = Short exempt transaction for non-member competing market-maker (refer to A and R types)

