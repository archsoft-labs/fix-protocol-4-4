[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 447](https://www.onixs.biz/fix-dictionary/4.4/tagNum_447.html)

# FIX 4.4 : PartyIDSource <447> field

**Type:** [char](https://www.onixs.biz/fix-dictionary/4.4/index.html#char)

## Description

Identifies class or source of the [PartyID <448>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_448.html) value. Required if [PartyID <448>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_448.html) is specified. Note: applicable values depend upon [PartyRole <452>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_452.html) specified.

See [Appendix 6-G: Use of <Parties> Component Block](https://www.onixs.biz/fix-dictionary/4.4/app_6_g.html)

Valid values:

Applicable to all PartyRoles unless otherwise specified:

B = BIC (Bank Identification Code—Swift managed) code (ISO 9362 – See [Appendix 6-B](https://www.onixs.biz/fix-dictionary/4.4/app_6_b.html))

C = Generally accepted market participant identifier (e.g. NASD mnemonic)

D = Proprietary/Custom code

E = ISO [Country <421>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_421.html) Code

F = Settlement Entity Location (note if Local Market Settlement use "E = ISO Country Code") (see [Appendix 6-G](https://www.onixs.biz/fix-dictionary/4.4/app_6_g.html) for valid values)

G = MIC (ISO 10383 - Market Identifier Code) (See [Appendix 6-C](https://www.onixs.biz/fix-dictionary/4.4/app_6_c.html))

H = CSD participant/member code (e.g. Euroclear, DTC, CREST or Kassenverein number)

For [PartyRole <452>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_452.html)="Investor ID" and for Equities:

1 = Korean Investor ID

2 = Taiwanese Qualified Foreign Investor ID QFII / FID

3 = Taiwanese Trading Account

4 = Malaysian Central Depository (MCD) number

5 = Chinese B Share (Shezhen and Shanghai)

See Volume 4: "Example Usage of PartyRole="Investor ID"

For [PartyRole <452>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_452.html)="Investor ID" and for CIV:

6 = UK National Insurance or Pension Number

7 = US Social Security Number

8 = US Employer Identification Number

9 = Australian Business Number

A = Australian Tax File Number

For [PartyRole <452>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_452.html)="Broker of Credit":

I = Directed broker three character acronym as defined in ISITC "ETC Best Practice" guidelines document

## Used In

- [<Parties>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_Parties.html)

