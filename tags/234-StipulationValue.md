[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 234](https://www.onixs.biz/fix-dictionary/4.4/tagNum_234.html)

# FIX 4.4 : StipulationValue <234> field

**Type:** [String](https://www.onixs.biz/fix-dictionary/4.4/index.html#String)

## Description

For Fixed Income. Value of stipulation.

The expression can be an absolute single value or a combination of values and logical operators:

< value

> value

<= value

>= value

value

value1 - value2

value1 OR value2

value1 AND value2

YES

NO

Bargain conditions recognized by the London Stock Exchange - to be used when [StipulationType <233>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_233.html) = "BGNCON".

CD = Special cum Dividend

XD = Special ex Dividend

CC = Special cum Coupon

XC = Special ex Coupon

CB = Special cum Bonus

XB = Special ex Bonus

CR = Special cum Rights

XR = Special ex Rights

CP = Special cum Capital Repayments

XP = Special ex Capital Repayments

CS = Cash Settlement

SP = Special Price

TR = Report for European Equity Market Securities in accordance with Chapter 8 of the Rules.

GD = Guaranteed Delivery

Values for [StipulationType <233>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_233.html) = "PXSOURCE":

BB GENERIC

BB FAIRVALUE

BROKERTEC

ESPEED

GOVPX

HILLIARD FARBER

ICAP

TRADEWEB

TULLETT LIBERTY

If a particular side of the market is wanted append /BID /OFFER or /MID.

plus appropriate combinations of the above and other expressions by mutual agreement of the counterparties.

Examples: ">=60", ".25", "ORANGE OR CONTRACOSTA", etc.

(Note tag # was reserved in FIX 4.1, added in FIX 4.3)

## Used In

- [<Stipulations>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_Stipulations.html)

