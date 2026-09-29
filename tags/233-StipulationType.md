[← Back to FIX 4.4 fields index](../README.md)

> Source: [OnixS FIX 4.4 — tag 233](https://www.onixs.biz/fix-dictionary/4.4/tagNum_233.html)

# FIX 4.4 : StipulationType <233> field

**Type:** [String](https://www.onixs.biz/fix-dictionary/4.4/index.html#String)

## Description

For Fixed Income. Type of Stipulation.

Values include:

AMT = AMT (y/n)

AUTOREINV = Auto Reinvestment at <rate> or better

BANKQUAL = Bank qualified (y/n)

BGNCON = Bargain Conditions (see [StipulationValue <234>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_234.html) for values)

COUPON = Coupon range

CURRENCY = ISO [Currency <15>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_15.html) code

CUSTOMDATE = Custom start/end date

GEOG = Geographics and % Range (ex. 234=CA 0-80 [minimum of 80% California assets])

HAIRCUT = Valuation discount

INSURED = Insured (y/n)

ISSUE = Year or Year/Month of Issue (ex. 234=2002/09)

ISSUER = [Issuer <106>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_106.html)'s ticker

ISSUESIZE = issue size range

LOOKBACK = Lookback days

LOT = Explicit lot identifier

LOTVAR = Lot Variance (value in percent maximum over- or under-allocation allowed)

MAT = Maturity Year and Month

MATURITY = Maturity range

MAXSUBS = Maximum substitutions (Repo)

MINQTY = Minimum quantity

MININCR = Minimum increment

MINDNOM = Minimum denomination

PAYFREQ = Payment frequency, calendar

PIECES = Number of Pieces

PMAX = Pools Maximum

PPM = Pools per Million

PPL = Pools per Lot

PPT = Pools per Trade

PRICE = Price range

PRICEFREQ = Pricing frequency

PROD = Production Year

PROTECT = Call protection

PURPOSE = Purpose

PXSOURCE = [Benchmark <219>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_219.html) price source

RATING = Rating source and range

REDEMPTION = Type of redemption - values are: NonCallable, Callable, Prefunded, EscrowedToMaturity, Putable, Convertible

RESTRICTED = Restricted (y/n)

SECTOR = Market sector

SECTYPE = [SecurityType <167>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_167.html) included or excluded

STRUCT = Structure

SUBSFREQ = Substitutions frequency (Repo)

SUBSLEFT = Substitutions left (Repo)

TEXT = Freeform text

TRDVAR = Trade Variance (value in percent maximum over- or under-allocation allowed)

WAC = Weighted Average Coupon: value in percent (exact or range) plus 'Gross' or 'Net' of servicing spread (the default) (ex. 234=6.5- Net [minimum of 6.5% net of servicing fee])

WAL = Weighted Average Life Coupon: value in percent (exact or range)

WALA = Weighted Average Loan Age: value in months (exact or range)

WAM = Weighted Average Maturity : value in months (exact or range)

WHOLE = Whole [Pool <691>](https://www.onixs.biz/fix-dictionary/4.4/tagNum_691.html) (y/n)

YIELD = Yield range

**or the following Prepayment Speeds:**

SMM = Single Monthly Mortality

CPR = Constant Prepayment Rate

CPY = Constant Prepayment Yield

CPP = Constant Prepayment Penalty

ABS = Absolute Prepayment Speed

MPR = Monthly Prepayment Rate

PSA = % of BMA Prepayment Curve

PPC = % of Prospectus Prepayment Curve

MHP = % of Manufactured Housing Prepayment Curve

HEP = final CPR of Home Equity Prepayment Curve

Other types may be used by mutual agreement of the counterparties.

(Note tag # was reserved in FIX 4.1, added in FIX 4.3)

## Used In

- [<Stipulations>](https://www.onixs.biz/fix-dictionary/4.4/compBlock_Stipulations.html)

