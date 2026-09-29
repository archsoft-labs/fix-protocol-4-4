[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 167](https://www.onixs.biz/fix-dictionary/4.4/tagNum_167.html)

# FIX 4.4 : SecurityType <167> field

**Type:** [String](https://www.onixs.biz/fix-dictionary/4.4/index.html#String)

## Description

Indicates type of security. See also the [Product <460>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_460.html) and [CFICode <461>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_461.html) fields. It is recommended that [CFICode <461>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_461.html) be used instead of [SecurityType <167>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_167.html) for non-Fixed Income instruments.

Example values (grouped by [Product <460>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_460.html) field value)

(Note: additional values may be used by mutual agreement of the counterparties):

AGENCY

- EUSUPRA = Euro Supranational Coupons *

- FAC = Federal Agency Coupon

- FADN = Federal Agency Discount Note

- PEF = Private Export Funding *

- SUPRA = USD Supranational Coupons *

- * Identify the Issuer in the [Issuer <106>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_106.html) field

~~COMMODITY~~

- ~~FUT = Future~~

- ~~OPT = Option~~

*** REPLACED values - See: 
 [Appendix 6-F: 4.Replaced Field Enumerations for Futures and Options for SecurityType (tag 167) with CFICode (tag 461) [replaced in FIX 4.3]](https://www.onixs.biz/fix-dictionary/4.4/app_6_f.html#4) ***

Note: COMMODITY Product includes Bond, Interest Rate, Currency, Currency Spot Options, Crops/Grains, Foodstuffs, Livestock, Fibers, Lumber/Rubber, Oil/Gas/Electricity, Precious/Major Metal, and Industrial Metal. Use [CFICode <461>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_461.html) for more granular definition if necessary.

CORPORATE

- CORP = Corporate Bond

- CPP = Corporate Private Placement

- CB = Convertible Bond

- DUAL = Dual Currency

- EUCORP = Euro Corporate Bond

- XLINKD = Indexed Linked

- STRUCT = Structured Notes

- YANK = Yankee Corporate Bond

CURRENCY

- FOR = Foreign Exchange Contract

EQUITY

- CS = Common Stock

- PS = Preferred Stock

WAR

- Warrant now is listed under Municipals for consistency with Bloomberg fixed income product types. For equity warrants - use the [CFICode <461>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_461.html) instead.

GOVERNMENT

- BRADY = Brady Bond

- EUSOV = Euro Sovereigns *

- TBOND = US Treasury Bond

- TINT = Interest strip from any bond or note

- TIPS = Treasury Inflation Protected Securities

- TCAL = Principal strip of a callable bond or note

- TPRN = Principal strip from a non-callable bond or note

- UST = US Treasury Note (deprecated value, use "**TNOTE**")

- USTB = US Treasury Bill (deprecated value, use "**TBILL**")

- TNOTE = US Treasury Note

- TBILL = US Treasury Bill

- * Identify the Issuer Name in [Issuer <106>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_106.html)

FINANCING

- REPO = Repurchase

- FORWARD = Forward

- BUYSELL = Buy Sellback

- SECLOAN = Securities Loan

- SECPLEDGE = Securities Pledge

INDEX

Note: "Indices" includes: Stock, Index Spot Options, Commodity, Physical Index Options, Share/Ratio, and Spreads. For index types use the [CFICode <461>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_461.html).

LOAN

- TERM = Term Loan

- RVLV = Revolver Loan

- RVLVTRM = Revolver/Term Loan

- BRIDGE = Bridge Loan

- LOFC = Letter of Credit

- SWING = Swing Line Facility

- DINP = Debtor in Possession

- DEFLTED = Defaulted

- WITHDRN = Withdrawn

- REPLACD = Replaced

- MATURED = Matured

- AMENDED = Amended & Restated

- RETIRED = Retired

MONEYMARKET

- BA = Bankers Acceptance

- BN = Bank Notes

- BOX = Bill of Exchanges

- CD = Certificate of Deposit

- CL = Call Loans

- CP = Commercial Paper

- DN = Deposit Notes

- EUCD = Euro Certificate of Deposit

- EUCP = Euro Commercial Paper

- LQN = Liquidity Note

- MTN = Medium Term Notes

- ONITE = Overnight

- PN = Promissory Note

- PZFJ = Plazos Fijos

- STN = Short Term Loan Note

- TD = Time Deposit

- XCN = Extended Comm Note

- YCD = Yankee Certificate of Deposit

MORTGAGE

- ABS = Asset-backed Securities

- CMBS = Corp. Mortgage-backed Securities

- CMO = Collateralized Mortgage Obligation

- IET = IOETTE Mortgage

- MBS = Mortgage-backed Securities

- MIO = Mortgage Interest Only

- MPO = Mortgage Principal Only

- MPP = Mortgage Private Placement

- MPT = Miscellaneous Pass-through

- PFAND = Pfandbriefe *

- TBA = To be Announced

- * Identify the Issuer Name in [Issuer <106>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_106.html)

MUNICIPAL

- AN = Other Anticipation Notes (BAN, GAN, etc.)

- COFO = Certificate of Obligation

- COFP = Certificate of Participation

- GO = General Obligation Bonds

- MT = Mandatory Tender

- RAN = Revenue Anticipation Note

- REV = Revenue Bonds

- SPCLA = Special Assessment

- SPCLO = Special Obligation

- SPCLT = Special Tax

- TAN = Tax Anticipation Note

- TAXA = Tax Allocation

- TECP = Tax Exempt Commercial Paper

- TRAN = Tax & Revenue Anticipation Note

- VRDN = Variable Rate Demand Note

- WAR = Warrant

OTHER

- MF = Mutual Fund (i.e. any kind of open-ended "Collective Investment Vehicle")

- MLEG = Multi-leg instrument (e.g. options strategy or futures spread. [CFICode <461>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_461.html) can be used to identify if options-based, futures-based, etc.)

- NONE = No Security Type

- ? = "Wildcard" entry (used on [Security Definition Request <c>](https://www.onixs.biz/fix-dictionary/4.4/msgType_c_99.html) message)

**NOTE: Additional values may be used by mutual agreement of the counterparties)**

## Used In

- [<Instrument>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_Instrument.html)
- [Allocation Report Ack <AT>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AT_6584.html)
- [Settlement Instruction Request <AV>](https://www.onixs.biz/fix-dictionary/4.4/msgType_AV_6586.html)
- [Allocation Instruction Ack <P>](https://www.onixs.biz/fix-dictionary/4.4/msgType_P_80.html)
- [Settlement Instructions <T>](https://www.onixs.biz/fix-dictionary/4.4/msgType_T_84.html)
- [Security Type Request <v>](https://www.onixs.biz/fix-dictionary/4.4/msgType_v_118.html)
- [Security Types <w>](https://www.onixs.biz/fix-dictionary/4.4/msgType_w_119.html)

