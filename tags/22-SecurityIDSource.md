[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 22](https://www.onixs.biz/fix-dictionary/4.4/tagNum_22.html)

# FIX 4.4 : SecurityIDSource <22> field

**Type:** [String](https://www.onixs.biz/fix-dictionary/4.4/index.html#String)

## Description

Identifies class or source of the [SecurityID <48>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_48.html) value. Required if [SecurityID <48>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_48.html) is specified.

Valid values:

1 = CUSIP

2 = SEDOL

3 = QUIK

4 = ISIN number

5 = RIC code

6 = ISO [Currency <15>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_15.html) Code

7 = ISO [Country <421>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_421.html) Code

8 = Exchange Symbol

9 = Consolidated Tape Association (CTA) Symbol (SIAC CTS/CQS line format)

A = Bloomberg Symbol

B = Wertpapier

C = Dutch

D = Valoren

E = Sicovam

F = Belgian

G = "Common" (Clearstream and Euroclear)

H = Clearing House / Clearing Organization

I = ISDA/FpML Product Specification

J = Options Price Reporting Authority

100+ are reserved for private security identifications

## Used In

- [<Instrument>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_Instrument.html)

