# FIX Protocol 4.4 — Fields by Tag

> FIX 4.4 field dictionary containing the tag, field name, and description.
>
> Source: [OnixS / FIX 4.4 field dictionary](https://www.onixs.biz/fix-dictionary/4.4/fields_by_tag.html).

**Total fields extracted:** 953

| Tag | Field | Description |
|---:|---|---|
| [1](tags/1-Account.md) | [Account](tags/1-Account.md) | Account mnemonic as agreed between buy and sell sides, e.g. broker and institution or investor/intermediary and fund manager. |
| [2](tags/2-AdvId.md) | [AdvId](tags/2-AdvId.md) | Unique identifier of Advertisement (7) message. |
| [3](tags/3-AdvRefID.md) | [AdvRefID](tags/3-AdvRefID.md) | Reference identifier used with CANCEL and REPLACE transaction types. |
| [4](tags/4-AdvSide.md) | [AdvSide](tags/4-AdvSide.md) | Broker's side of advertised trade |
| [5](tags/5-AdvTransType.md) | [AdvTransType](tags/5-AdvTransType.md) | Identifies Advertisement (7) message transaction type |
| [6](tags/6-AvgPx.md) | [AvgPx](tags/6-AvgPx.md) | Calculated average price of all fills on this order. |
| [7](tags/7-BeginSeqNo.md) | [BeginSeqNo](tags/7-BeginSeqNo.md) | Message sequence number of first message in range to be resent |
| [8](tags/8-BeginString.md) | [BeginString](tags/8-BeginString.md) | Identifies beginning of new message and protocol version. ALWAYS FIRST FIELD IN MESSAGE. (Always unencrypted) |
| [9](tags/9-BodyLength.md) | [BodyLength](tags/9-BodyLength.md) | Message length, in bytes, is verified by counting the number of characters in the message following the BodyLength (9) field up to, and including, the delimiter immediately preceding the CheckSum (10) field. ALWAYS SECOND FIELD IN MESSAGE. (Always unencrypted) For example, for message 8=FIX 4.4^9=5^35=0^10=10^, the BodyLength is 5 for 35=0^ |
| [10](tags/10-CheckSum.md) | [CheckSum](tags/10-CheckSum.md) | Three bytes, simple checksum (see Volume 2: "Checksum Calculation" for description). ALWAYS LAST FIELD IN MESSAGE; i.e. serves, with the trailing <SOH>, as the end-of-message delimiter. Always defined as three characters. (Always unencrypted). |
| [11](tags/11-ClOrdID.md) | [ClOrdID](tags/11-ClOrdID.md) | Unique identifier for Order as assigned by the buy-side (institution, broker, intermediary etc.) (identified by SenderCompID (49) or OnBehalfOfCompID (115) as appropriate). Uniqueness must be guaranteed within a single trading day. Firms, particularly those which electronically submit multi-day orders, trade globally or throughout market close periods, should ensure uniqueness across days, for example by embedding a date within the ClOrdID (11) field. |
| [12](tags/12-Commission.md) | [Commission](tags/12-Commission.md) | Commission. Note if CommType <13> is percentage, Commission <12> of 5% should be represented as .05. |
| [13](tags/13-CommType.md) | [CommType](tags/13-CommType.md) | Commission <12> type. |
| [14](tags/14-CumQty.md) | [CumQty](tags/14-CumQty.md) | Total quantity (e.g. number of shares) filled. |
| [15](tags/15-Currency.md) | [Currency](tags/15-Currency.md) | Identifies currency used for price. Absence of this field is interpreted as the default for the security. It is recommended that systems provide the currency value whenever possible. See Appendix 6-A: Valid Currency Codes for information on obtaining valid values. |
| [16](tags/16-EndSeqNo.md) | [EndSeqNo](tags/16-EndSeqNo.md) | Message sequence number of last message in range to be resent. If request is for a single message BeginSeqNo <7> = EndSeqNo <16>. If request is for all messages subsequent to a particular message, EndSeqNo <16> = 0 (representing infinity). |
| [17](tags/17-ExecID.md) | [ExecID](tags/17-ExecID.md) | Unique identifier of execution message as assigned by sell-side (broker, exchange, ECN) (will be 0 (zero) for ExecType <150> ='I' (Order Status)). |
| [18](tags/18-ExecInst.md) | [ExecInst](tags/18-ExecInst.md) | Instructions for order handling on exchange trading floor. If more than one instruction is applicable to an order, this field can contain multiple instructions separated by space. |
| [19](tags/19-ExecRefID.md) | [ExecRefID](tags/19-ExecRefID.md) | Reference identifier used with Trade Cancel and Trade Correct execution types. |
| [20](tags/20-ExecTransType-replaced.md) | [ExecTransType (replaced)](tags/20-ExecTransType-replaced.md) | No longer used as of FIX 4.3. Included here for reference to prior versions. |
| [21](tags/21-HandlInst.md) | [HandlInst](tags/21-HandlInst.md) | Instructions for order handling on Broker trading floor |
| [22](tags/22-SecurityIDSource.md) | [SecurityIDSource](tags/22-SecurityIDSource.md) | Identifies class or source of the SecurityID (48) value. Required if SecurityID (48) is specified. |
| [23](tags/23-IOIid.md) | [IOIid](tags/23-IOIid.md) | Unique identifier of IOI <6> message. |
| [24](tags/24-IOIOthSvc-no-longer-used.md) | [IOIOthSvc  (no longer used)](tags/24-IOIOthSvc-no-longer-used.md) | No longer used as of FIX 4.2. Included here for reference to prior versions. |
| [25](tags/25-IOIQltyInd.md) | [IOIQltyInd](tags/25-IOIQltyInd.md) | Relative quality of indication |
| [26](tags/26-IOIRefID.md) | [IOIRefID](tags/26-IOIRefID.md) | Reference identifier used with CANCEL and REPLACE, transaction types. |
| [27](tags/27-IOIQty.md) | [IOIQty](tags/27-IOIQty.md) | Quantity (e.g. number of shares) in numeric form or relative size. |
| [28](tags/28-IOITransType.md) | [IOITransType](tags/28-IOITransType.md) | Identifies IOI <6> message transaction type. |
| [29](tags/29-LastCapacity.md) | [LastCapacity](tags/29-LastCapacity.md) | Broker capacity in order execution |
| [30](tags/30-LastMkt.md) | [LastMkt](tags/30-LastMkt.md) | Market of execution for last fill, or an indication of the market where an order was routed |
| [31](tags/31-LastPx.md) | [LastPx](tags/31-LastPx.md) | Price of this (last) fill. |
| [32](tags/32-LastQty.md) | [LastQty](tags/32-LastQty.md) | Quantity (e.g. shares) bought/sold on this (last) fill. |
| [33](tags/33-LinesOfText.md) | [LinesOfText](tags/33-LinesOfText.md) | Identifies number of lines of text body |
| [34](tags/34-MsgSeqNum.md) | [MsgSeqNum](tags/34-MsgSeqNum.md) | Integer message sequence number. |
| [35](tags/35-MsgType.md) | [MsgType](tags/35-MsgType.md) | Defines message type. ALWAYS THIRD FIELD IN MESSAGE. (Always unencrypted) |
| [36](tags/36-NewSeqNo.md) | [NewSeqNo](tags/36-NewSeqNo.md) | New sequence number |
| [37](tags/37-OrderID.md) | [OrderID](tags/37-OrderID.md) | Unique identifier for Order as assigned by sell-side (broker, exchange, ECN). Uniqueness must be guaranteed within a single trading day. Firms which accept multi-day orders should consider embedding a date within the OrderID (37) field to assure uniqueness across days. |
| [38](tags/38-OrderQty.md) | [OrderQty](tags/38-OrderQty.md) | Quantity ordered. This represents the number of shares for equities or par, face or nominal value for FI instruments. |
| [39](tags/39-OrdStatus.md) | [OrdStatus](tags/39-OrdStatus.md) | Identifies current status of order. |
| [40](tags/40-OrdType.md) | [OrdType](tags/40-OrdType.md) | Order type. |
| [41](tags/41-OrigClOrdID.md) | [OrigClOrdID](tags/41-OrigClOrdID.md) | ClOrdID (11) of the previous order (NOT the initial order of the day) as assigned by the institution, used to identify the previous order in cancel and cancel/replace requests. |
| [42](tags/42-OrigTime.md) | [OrigTime](tags/42-OrigTime.md) | Time of message origination (always expressed in UTC (Universal Time Coordinated, also known as "GMT")) |
| [43](tags/43-PossDupFlag.md) | [PossDupFlag](tags/43-PossDupFlag.md) | Indicates possible retransmission of message with this sequence number |
| [44](tags/44-Price.md) | [Price](tags/44-Price.md) | Price per unit of quantity (e.g. per share) |
| [45](tags/45-RefSeqNum.md) | [RefSeqNum](tags/45-RefSeqNum.md) | Reference message sequence number |
| [46](tags/46-RelatdSym-no-longer-used.md) | [RelatdSym  (no longer used)](tags/46-RelatdSym-no-longer-used.md) | No longer used as of FIX 4.3. Included here for reference to prior versions. |
| [47](tags/47-Rule80A-No-Longer-Used.md) | [Rule80A(No Longer Used)](tags/47-Rule80A-No-Longer-Used.md) | No longer used as of FIX.4.4. Included here for reference to prior versions. |
| [48](tags/48-SecurityID.md) | [SecurityID](tags/48-SecurityID.md) | Security identifier value of SecurityIDSource <22> type (e.g. CUSIP, SEDOL, ISIN, etc). Requires SecurityIDSource <22>. |
| [49](tags/49-SenderCompID.md) | [SenderCompID](tags/49-SenderCompID.md) | Assigned value used to identify firm sending message. |
| [50](tags/50-SenderSubID.md) | [SenderSubID](tags/50-SenderSubID.md) | Assigned value used to identify specific message originator (desk, trader, etc.) |
| [51](tags/51-SendingDate-no-longer-used.md) | [SendingDate  (no longer used)](tags/51-SendingDate-no-longer-used.md) | No longer used. Included here for reference to prior versions. |
| [52](tags/52-SendingTime.md) | [SendingTime](tags/52-SendingTime.md) | Time of message transmission (always expressed in UTC (Universal Time Coordinated, also known as "GMT") |
| [53](tags/53-Quantity.md) | [Quantity](tags/53-Quantity.md) | Overall/total quantity (e.g. number of shares) |
| [54](tags/54-Side.md) | [Side](tags/54-Side.md) | Side of order |
| [55](tags/55-Symbol.md) | [Symbol](tags/55-Symbol.md) | Ticker symbol. Common, "human understood" representation of the security. SecurityID (48) value can be specified if no symbol exists (e.g. non-exchange traded Collective Investment Vehicles). |
| [56](tags/56-TargetCompID.md) | [TargetCompID](tags/56-TargetCompID.md) | Assigned value used to identify receiving firm. |
| [57](tags/57-TargetSubID.md) | [TargetSubID](tags/57-TargetSubID.md) | Assigned value used to identify specific individual or unit intended to receive message. "ADMIN" reserved for administrative messages not intended for a specific user. |
| [58](tags/58-Text.md) | [Text](tags/58-Text.md) | Free format text string |
| [59](tags/59-TimeInForce.md) | [TimeInForce](tags/59-TimeInForce.md) | Specifies how long the order remains in effect. Absence of this field is interpreted as DAY. NOTE not applicable to CIV Orders. |
| [60](tags/60-TransactTime.md) | [TransactTime](tags/60-TransactTime.md) | Time of execution/order creation (expressed in UTC (Universal Time Coordinated, also known as "GMT"). |
| [61](tags/61-Urgency.md) | [Urgency](tags/61-Urgency.md) | Urgency flag |
| [62](tags/62-ValidUntilTime.md) | [ValidUntilTime](tags/62-ValidUntilTime.md) | Indicates expiration time of indication message (always expressed in UTC (Universal Time Coordinated, also known as "GMT"). |
| [63](tags/63-SettlType.md) | [SettlType](tags/63-SettlType.md) | Indicates order settlement period. If present, SettlDate <64> overrides this field. If both SettlType <63> and SettlDate <64> are omitted, the default for SettlType <63> is '0' (Regular). |
| [64](tags/64-SettlDate.md) | [SettlDate](tags/64-SettlDate.md) | Specific date of trade settlement (SettlementDate) in YYYYMMDD format. |
| [65](tags/65-SymbolSfx.md) | [SymbolSfx](tags/65-SymbolSfx.md) | Additional information about the security (e.g. preferred, warrants, etc.). Note also see SecurityType <167>. |
| [66](tags/66-ListID.md) | [ListID](tags/66-ListID.md) | Unique identifier for list as assigned by institution, used to associate multiple individual orders. Uniqueness must be guaranteed within a single trading day. Firms which generate multi-day orders should consider embedding a date within the ListID (66) field to assure uniqueness across days. |
| [67](tags/67-ListSeqNo.md) | [ListSeqNo](tags/67-ListSeqNo.md) | Sequence of individual order within list (i.e. ListSeqNo <67> of TotNoOrders <68>, 2 of 25, 3 of 25, . . . ). |
| [68](tags/68-TotNoOrders.md) | [TotNoOrders](tags/68-TotNoOrders.md) | Total number of list order entries across all messages. Should be the sum of all NoOrders <73> in each message that has repeating list order entries related to the same ListID <66>. Used to support fragmentation. |
| [69](tags/69-ListExecInst.md) | [ListExecInst](tags/69-ListExecInst.md) | Free format text message containing list handling and execution instructions. |
| [70](tags/70-AllocID.md) | [AllocID](tags/70-AllocID.md) | Unique identifier for allocation message. |
| [71](tags/71-AllocTransType.md) | [AllocTransType](tags/71-AllocTransType.md) | Identifies allocation transaction type |
| [72](tags/72-RefAllocID.md) | [RefAllocID](tags/72-RefAllocID.md) | Reference identifier to be used with AllocTransType <71> = 'Replace' or 'Cancel'. |
| [73](tags/73-NoOrders.md) | [NoOrders](tags/73-NoOrders.md) | Indicates number of orders to be combined for average pricing and allocation. |
| [74](tags/74-AvgPxPrecision.md) | [AvgPxPrecision](tags/74-AvgPxPrecision.md) | Indicates number of decimal places to be used for average pricing. Absence of this field indicates that default precision arranged by the broker/institution is to be used. |
| [75](tags/75-TradeDate.md) | [TradeDate](tags/75-TradeDate.md) | Indicates date of trade referenced in this message in YYYYMMDD format. Absence of this field indicates current day (expressed in local time at place of trade). |
| [76](tags/76-ExecBroker-replaced.md) | [ExecBroker (replaced)](tags/76-ExecBroker-replaced.md) | No longer used as of FIX 4.3. Included here for reference to prior versions. |
| [77](tags/77-PositionEffect.md) | [PositionEffect](tags/77-PositionEffect.md) | Indicates whether the resulting position after a trade should be an opening position or closing position. Used for omnibus accounting - where accounts are held on a gross basis instead of being netted together. |
| [78](tags/78-NoAllocs.md) | [NoAllocs](tags/78-NoAllocs.md) | Number of repeating AllocAccount <79>/AllocPrice <366> entries. |
| [79](tags/79-AllocAccount.md) | [AllocAccount](tags/79-AllocAccount.md) | Sub-account mnemonic |
| [80](tags/80-AllocQty.md) | [AllocQty](tags/80-AllocQty.md) | Quantity to be allocated to specific sub-account |
| [81](tags/81-ProcessCode.md) | [ProcessCode](tags/81-ProcessCode.md) | Processing code for sub-account. Absence of this field in AllocAccount <79> / AllocPrice <366> /AllocQty <80> / ProcessCode <81> instance indicates regular trade. |
| [82](tags/82-NoRpts.md) | [NoRpts](tags/82-NoRpts.md) | Total number of reports within series. |
| [83](tags/83-RptSeq.md) | [RptSeq](tags/83-RptSeq.md) | Sequence number of message within report series. |
| [84](tags/84-CxlQty.md) | [CxlQty](tags/84-CxlQty.md) | Total quantity canceled for this order. |
| [85](tags/85-NoDlvyInst.md) | [NoDlvyInst](tags/85-NoDlvyInst.md) | Number of delivery instruction fields in repeating group. |
| [86](tags/86-DlvyInst-no-longer-used.md) | [DlvyInst (no longer used)](tags/86-DlvyInst-no-longer-used.md) | Free format text field to indicate delivery instructions |
| [87](tags/87-AllocStatus.md) | [AllocStatus](tags/87-AllocStatus.md) | Identifies status of allocation. |
| [88](tags/88-AllocRejCode.md) | [AllocRejCode](tags/88-AllocRejCode.md) | Identifies reason for rejection. |
| [89](tags/89-Signature.md) | [Signature](tags/89-Signature.md) | Electronic signature |
| [90](tags/90-SecureDataLen.md) | [SecureDataLen](tags/90-SecureDataLen.md) | Length of encrypted message |
| [91](tags/91-SecureData.md) | [SecureData](tags/91-SecureData.md) | Actual encrypted data stream |
| [92](tags/92-BrokerOfCredit-replaced.md) | [BrokerOfCredit (replaced)](tags/92-BrokerOfCredit-replaced.md) | No longer used as of FIX 4.3. Included here for reference to prior versions. |
| [93](tags/93-SignatureLength.md) | [SignatureLength](tags/93-SignatureLength.md) | Number of bytes in Signature <89> field. |
| [94](tags/94-EmailType.md) | [EmailType](tags/94-EmailType.md) | Email <C> message type. |
| [95](tags/95-RawDataLength.md) | [RawDataLength](tags/95-RawDataLength.md) | Number of bytes in raw data field. |
| [96](tags/96-RawData.md) | [RawData](tags/96-RawData.md) | Unformatted raw data, can include bitmaps, word processor documents, etc. |
| [97](tags/97-PossResend.md) | [PossResend](tags/97-PossResend.md) | Indicates that message may contain information that has been sent under another sequence number. |
| [98](tags/98-EncryptMethod.md) | [EncryptMethod](tags/98-EncryptMethod.md) | Method of encryption. |
| [99](tags/99-StopPx.md) | [StopPx](tags/99-StopPx.md) | Price per unit of quantity (e.g. per share) |
| [100](tags/100-ExDestination.md) | [ExDestination](tags/100-ExDestination.md) | Execution destination as defined by institution when order is entered. |
| [102](tags/102-CxlRejReason.md) | [CxlRejReason](tags/102-CxlRejReason.md) | Code to identify reason for cancel rejection. |
| [103](tags/103-OrdRejReason.md) | [OrdRejReason](tags/103-OrdRejReason.md) | Code to identify reason for order rejection. |
| [104](tags/104-IOIQualifier.md) | [IOIQualifier](tags/104-IOIQualifier.md) | Code to qualify IOI use. |
| [105](tags/105-WaveNo-no-longer-used.md) | [WaveNo (no longer used)](tags/105-WaveNo-no-longer-used.md) | No longer used as of FIX 4.3. Included here for reference to prior versions. |
| [106](tags/106-Issuer.md) | [Issuer](tags/106-Issuer.md) | Name of security issuer (e.g. International Business Machines, GNMA). |
| [107](tags/107-SecurityDesc.md) | [SecurityDesc](tags/107-SecurityDesc.md) | Security description. |
| [108](tags/108-HeartBtInt.md) | [HeartBtInt](tags/108-HeartBtInt.md) | Heartbeat <0> interval (seconds). |
| [109](tags/109-ClientID-replaced.md) | [ClientID (replaced)](tags/109-ClientID-replaced.md) | No longer used as of FIX 4.3. Included here for reference to prior versions. |
| [110](tags/110-MinQty.md) | [MinQty](tags/110-MinQty.md) | Minimum quantity of an order to be executed. |
| [111](tags/111-MaxFloor.md) | [MaxFloor](tags/111-MaxFloor.md) | Maximum quantity (e.g. number of shares) within an order to be shown on the exchange floor at any given time. |
| [112](tags/112-TestReqID.md) | [TestReqID](tags/112-TestReqID.md) | Identifier included in Test Request (1) message to be returned in resulting Heartbeat (0) |
| [113](tags/113-ReportToExch.md) | [ReportToExch](tags/113-ReportToExch.md) | Identifies party of trade responsible for exchange reporting. |
| [114](tags/114-LocateReqd.md) | [LocateReqd](tags/114-LocateReqd.md) | Indicates whether the broker is to locate the stock in conjunction with a short sell order. |
| [115](tags/115-OnBehalfOfCompID.md) | [OnBehalfOfCompID](tags/115-OnBehalfOfCompID.md) | Assigned value used to identify firm originating message if the message was delivered by a third party i.e. the third party firm identifier would be delivered in the SenderCompID (49) field and the firm originating the message in this field. |
| [116](tags/116-OnBehalfOfSubID.md) | [OnBehalfOfSubID](tags/116-OnBehalfOfSubID.md) | Assigned value used to identify specific message originator (i.e. trader) if the message was delivered by a third party |
| [117](tags/117-QuoteID.md) | [QuoteID](tags/117-QuoteID.md) | Unique identifier for quote |
| [118](tags/118-NetMoney.md) | [NetMoney](tags/118-NetMoney.md) | Total amount due as the result of the transaction (e.g. for Buy order - principal + commission + fees) reported in currency of execution. |
| [119](tags/119-SettlCurrAmt.md) | [SettlCurrAmt](tags/119-SettlCurrAmt.md) | Total amount due expressed in settlement currency (includes the effect of the forex transaction) |
| [120](tags/120-SettlCurrency.md) | [SettlCurrency](tags/120-SettlCurrency.md) | Currency code of settlement denomination. |
| [121](tags/121-ForexReq.md) | [ForexReq](tags/121-ForexReq.md) | Indicates request for forex accommodation trade to be executed along with security transaction. |
| [122](tags/122-OrigSendingTime.md) | [OrigSendingTime](tags/122-OrigSendingTime.md) | Original time of message transmission (always expressed in UTC (Universal Time Coordinated, also known as "GMT") when transmitting orders as the result of a resend request. |
| [123](tags/123-GapFillFlag.md) | [GapFillFlag](tags/123-GapFillFlag.md) | Indicates that the Sequence Reset (4) message is replacing administrative or application messages which will not be resent. |
| [124](tags/124-NoExecs.md) | [NoExecs](tags/124-NoExecs.md) | No of execution repeating group entries to follow. |
| [125](tags/125-CxlType-no-longer-used.md) | [CxlType (no longer used)](tags/125-CxlType-no-longer-used.md) | No longer used. Included here for reference to prior versions. |
| [126](tags/126-ExpireTime.md) | [ExpireTime](tags/126-ExpireTime.md) | Time/Date of order expiration (always expressed in UTC (Universal Time Coordinated, also known as "GMT"). |
| [127](tags/127-DKReason.md) | [DKReason](tags/127-DKReason.md) | Reason for execution rejection. |
| [128](tags/128-DeliverToCompID.md) | [DeliverToCompID](tags/128-DeliverToCompID.md) | Assigned value used to identify the firm targeted to receive the message if the message is delivered by a third party i.e. the third party firm identifier would be delivered in the TargetCompID (56) field and the ultimate receiver firm ID in this field. |
| [129](tags/129-DeliverToSubID.md) | [DeliverToSubID](tags/129-DeliverToSubID.md) | Assigned value used to identify specific message recipient (i.e. trader) if the message is delivered by a third party |
| [130](tags/130-IOINaturalFlag.md) | [IOINaturalFlag](tags/130-IOINaturalFlag.md) | Indicates that IOI <6> is the result of an existing agency order or a facilitation position resulting from an agency order, not from principal trading or order solicitation activity. |
| [131](tags/131-QuoteReqID.md) | [QuoteReqID](tags/131-QuoteReqID.md) | Unique identifier for quote request. |
| [132](tags/132-BidPx.md) | [BidPx](tags/132-BidPx.md) | Bid price/rate |
| [133](tags/133-OfferPx.md) | [OfferPx](tags/133-OfferPx.md) | Offer price/rate |
| [134](tags/134-BidSize.md) | [BidSize](tags/134-BidSize.md) | Quantity of bid |
| [135](tags/135-OfferSize.md) | [OfferSize](tags/135-OfferSize.md) | Quantity of offer |
| [136](tags/136-NoMiscFees.md) | [NoMiscFees](tags/136-NoMiscFees.md) | Number of repeating groups of miscellaneous fees |
| [137](tags/137-MiscFeeAmt.md) | [MiscFeeAmt](tags/137-MiscFeeAmt.md) | Miscellaneous fee value |
| [138](tags/138-MiscFeeCurr.md) | [MiscFeeCurr](tags/138-MiscFeeCurr.md) | Currency <15> of miscellaneous fee. |
| [139](tags/139-MiscFeeType.md) | [MiscFeeType](tags/139-MiscFeeType.md) | Indicates type of miscellaneous fee. |
| [140](tags/140-PrevClosePx.md) | [PrevClosePx](tags/140-PrevClosePx.md) | Previous closing price of security. |
| [141](tags/141-ResetSeqNumFlag.md) | [ResetSeqNumFlag](tags/141-ResetSeqNumFlag.md) | Indicates that the both sides of the FIX session should reset sequence numbers. |
| [142](tags/142-SenderLocationID.md) | [SenderLocationID](tags/142-SenderLocationID.md) | Assigned value used to identify specific message originator's location (i.e. geographic location and/or desk, trader) |
| [143](tags/143-TargetLocationID.md) | [TargetLocationID](tags/143-TargetLocationID.md) | Assigned value used to identify specific message destination's location (i.e. geographic location and/or desk, trader) |
| [144](tags/144-OnBehalfOfLocationID.md) | [OnBehalfOfLocationID](tags/144-OnBehalfOfLocationID.md) | Assigned value used to identify specific message originator's location (i.e. geographic location and/or desk, trader) if the message was delivered by a third party |
| [145](tags/145-DeliverToLocationID.md) | [DeliverToLocationID](tags/145-DeliverToLocationID.md) | Assigned value used to identify specific message recipient's location (i.e. geographic location and/or desk, trader) if the message was delivered by a third party |
| [146](tags/146-NoRelatedSym.md) | [NoRelatedSym](tags/146-NoRelatedSym.md) | Specifies the number of repeating symbols specified. |
| [147](tags/147-Subject.md) | [Subject](tags/147-Subject.md) | The subject of an Email <C> message. |
| [148](tags/148-Headline.md) | [Headline](tags/148-Headline.md) | The headline of a News <B> message. |
| [149](tags/149-URLLink.md) | [URLLink](tags/149-URLLink.md) | A URI (Uniform Resource Identifier) or URL (Uniform Resource Locator) link to additional information (i.e. http://en.wikipedia.org/wiki/Uniform_Resource_Locator ). See " Appendix 6-B FIX Fields Based Upon Other Standards " of FIX. |
| [150](tags/150-ExecType.md) | [ExecType](tags/150-ExecType.md) | Describes the specific Execution Report (i.e. Pending Cancel) while OrdStatus <39> will always identify the current order status (i.e. Partially Filled). |
| [151](tags/151-LeavesQty.md) | [LeavesQty](tags/151-LeavesQty.md) | Quantity open for further execution. If the OrdStatus <39> is 'Canceled', 'DoneForTheDay', 'Expired', 'Calculated', or' Rejected' (in which case the order is no longer active) then LeavesQty <151> could be 0, otherwise LeavesQty <151> = OrderQty <38> - CumQty <14>. |
| [152](tags/152-CashOrderQty.md) | [CashOrderQty](tags/152-CashOrderQty.md) | Specifies the approximate order quantity desired in total monetary units vs. as tradeable units (e.g. number of shares). The broker or fund manager (for CIV orders) would be responsible for converting and calculating a tradeable unit (e.g. share) quantity (OrderQty <38>) based upon this amount to be used for the actual order and subsequent messages. |
| [153](tags/153-AllocAvgPx.md) | [AllocAvgPx](tags/153-AllocAvgPx.md) | AvgPx <6> for a specific AllocAccount <79>. |
| [154](tags/154-AllocNetMoney.md) | [AllocNetMoney](tags/154-AllocNetMoney.md) | NetMoney (118) for a specific AllocAccount (79) |
| [155](tags/155-SettlCurrFxRate.md) | [SettlCurrFxRate](tags/155-SettlCurrFxRate.md) | Foreign exchange rate used to compute SettlCurrAmt (119) from Currency (15) to SettlCurrency (120) |
| [156](tags/156-SettlCurrFxRateCalc.md) | [SettlCurrFxRateCalc](tags/156-SettlCurrFxRateCalc.md) | Specifies whether or not SettlCurrFxRate (155) should be multiplied or divided. |
| [157](tags/157-NumDaysInterest.md) | [NumDaysInterest](tags/157-NumDaysInterest.md) | Number of Days of Interest for convertible bonds and fixed income. Note value may be negative. |
| [158](tags/158-AccruedInterestRate.md) | [AccruedInterestRate](tags/158-AccruedInterestRate.md) | The amount the buyer compensates the seller for the portion of the next coupon interest payment the seller has earned but will not receive from the issuer because the issuer will send the next coupon payment to the buyer. Accrued Interest Rate is the annualized Accrued Interest amount divided by the purchase price of the bond. |
| [159](tags/159-AccruedInterestAmt.md) | [AccruedInterestAmt](tags/159-AccruedInterestAmt.md) | Amount of Accrued Interest for convertible bonds and fixed income |
| [160](tags/160-SettlInstMode.md) | [SettlInstMode](tags/160-SettlInstMode.md) | Indicates mode used for Settlement Instructions <T> message. |
| [161](tags/161-AllocText.md) | [AllocText](tags/161-AllocText.md) | Free format text related to a specific AllocAccount <79>. |
| [162](tags/162-SettlInstID.md) | [SettlInstID](tags/162-SettlInstID.md) | Unique identifier for Settlement Instruction. |
| [163](tags/163-SettlInstTransType.md) | [SettlInstTransType](tags/163-SettlInstTransType.md) | Settlement Instructions <T> message transaction type. |
| [164](tags/164-EmailThreadID.md) | [EmailThreadID](tags/164-EmailThreadID.md) | Unique identifier for an email thread (new and chain of replies) |
| [165](tags/165-SettlInstSource.md) | [SettlInstSource](tags/165-SettlInstSource.md) | Indicates source of Settlement Instructions <T>. |
| [166](tags/166-SettlLocation-replaced.md) | [SettlLocation (replaced)](tags/166-SettlLocation-replaced.md) | No longer used as of FIX 4.3. Included here for reference to prior versions. |
| [167](tags/167-SecurityType.md) | [SecurityType](tags/167-SecurityType.md) | Indicates type of security. See also the Product (460) and CFICode (461) fields. It is recommended that CFICode (461) be used instead of SecurityType (167) for non-Fixed Income instruments. |
| [168](tags/168-EffectiveTime.md) | [EffectiveTime](tags/168-EffectiveTime.md) | Time the details within the message should take effect (always expressed in UTC (Universal Time Coordinated, also known as "GMT"). |
| [169](tags/169-StandInstDbType.md) | [StandInstDbType](tags/169-StandInstDbType.md) | Identifies the Standing Instruction database used |
| [170](tags/170-StandInstDbName.md) | [StandInstDbName](tags/170-StandInstDbName.md) | Name of the Standing Instruction database represented with StandInstDbType (169) (i.e. the Global Custodian's name). |
| [171](tags/171-StandInstDbID.md) | [StandInstDbID](tags/171-StandInstDbID.md) | Unique identifier used on the Standing Instructions database for the Standing Instructions to be referenced. |
| [172](tags/172-SettlDeliveryType.md) | [SettlDeliveryType](tags/172-SettlDeliveryType.md) | Identifies type of settlement |
| [173](tags/173-SettlDepositoryCode-replaced.md) | [SettlDepositoryCode (replaced)](tags/173-SettlDepositoryCode-replaced.md) | No longer used as of FIX 4.4. Included here for reference to prior versions. |
| [174](tags/174-SettlBrkrCode-replaced.md) | [SettlBrkrCode (replaced)](tags/174-SettlBrkrCode-replaced.md) | No longer used as of FIX 4.4. Included here for reference to prior versions. |
| [175](tags/175-SettlInstCode-replaced.md) | [SettlInstCode (replaced)](tags/175-SettlInstCode-replaced.md) | No longer used as of FIX 4.4. Included here for reference to prior versions. |
| [176](tags/176-SecuritySettlAgentName-replaced.md) | [SecuritySettlAgentName (replaced)](tags/176-SecuritySettlAgentName-replaced.md) | No longer used as of FIX 4.4. Included here for reference to prior versions. |
| [177](tags/177-SecuritySettlAgentCode-replaced.md) | [SecuritySettlAgentCode (replaced)](tags/177-SecuritySettlAgentCode-replaced.md) | No longer used as of FIX 4.4. Included here for reference to prior versions. |
| [178](tags/178-SecuritySettlAgentAcctNum-replaced.md) | [SecuritySettlAgentAcctNum (replaced)](tags/178-SecuritySettlAgentAcctNum-replaced.md) | No longer used as of FIX 4.4. Included here for reference to prior versions. |
| [179](tags/179-SecuritySettlAgentAcctName-replaced.md) | [SecuritySettlAgentAcctName (replaced)](tags/179-SecuritySettlAgentAcctName-replaced.md) | No longer used as of FIX 4.4. Included here for reference to prior versions. |
| [180](tags/180-SecuritySettlAgentContactName-replaced.md) | [SecuritySettlAgentContactName (replaced)](tags/180-SecuritySettlAgentContactName-replaced.md) | No longer used as of FIX 4.4. Included here for reference to prior versions. |
| [181](tags/181-SecuritySettlAgentContactPhone-replaced.md) | [SecuritySettlAgentContactPhone (replaced)](tags/181-SecuritySettlAgentContactPhone-replaced.md) | No longer used as of FIX 4.4. Included here for reference to prior versions. |
| [182](tags/182-CashSettlAgentName-replaced.md) | [CashSettlAgentName (replaced)](tags/182-CashSettlAgentName-replaced.md) | No longer used as of FIX 4.4. Included here for reference to prior versions. |
| [183](tags/183-CashSettlAgentCode-replaced.md) | [CashSettlAgentCode (replaced)](tags/183-CashSettlAgentCode-replaced.md) | No longer used as of FIX 4.4. Included here for reference to prior versions. |
| [184](tags/184-CashSettlAgentAcctNum-replaced.md) | [CashSettlAgentAcctNum (replaced)](tags/184-CashSettlAgentAcctNum-replaced.md) | No longer used as of FIX 4.4. Included here for reference to prior versions. |
| [185](tags/185-CashSettlAgentAcctName-replaced.md) | [CashSettlAgentAcctName (replaced)](tags/185-CashSettlAgentAcctName-replaced.md) | No longer used as of FIX 4.4. Included here for reference to prior versions. |
| [186](tags/186-CashSettlAgentContactName-replaced.md) | [CashSettlAgentContactName (replaced)](tags/186-CashSettlAgentContactName-replaced.md) | No longer used as of FIX 4.4. Included here for reference to prior versions. |
| [187](tags/187-CashSettlAgentContactPhone-replaced.md) | [CashSettlAgentContactPhone (replaced)](tags/187-CashSettlAgentContactPhone-replaced.md) | No longer used as of FIX 4.4. Included here for reference to prior versions. |
| [188](tags/188-BidSpotRate.md) | [BidSpotRate](tags/188-BidSpotRate.md) | Bid F/X spot rate. |
| [189](tags/189-BidForwardPoints.md) | [BidForwardPoints](tags/189-BidForwardPoints.md) | Bid F/X forward points added to spot rate. May be a negative value. |
| [190](tags/190-OfferSpotRate.md) | [OfferSpotRate](tags/190-OfferSpotRate.md) | Offer F/X spot rate. |
| [191](tags/191-OfferForwardPoints.md) | [OfferForwardPoints](tags/191-OfferForwardPoints.md) | Offer F/X forward points added to spot rate. May be a negative value. |
| [192](tags/192-OrderQty2.md) | [OrderQty2](tags/192-OrderQty2.md) | OrderQty (38) of the future part of a F/X swap order. |
| [193](tags/193-SettDate2.md) | [SettDate2](tags/193-SettDate2.md) | SettDate <64> of the future part of a F/X swap order. |
| [194](tags/194-LastSpotRate.md) | [LastSpotRate](tags/194-LastSpotRate.md) | F/X spot rate. |
| [195](tags/195-LastForwardPoints.md) | [LastForwardPoints](tags/195-LastForwardPoints.md) | F/X forward points added to LastSpotRate <194>. May be a negative value. |
| [196](tags/196-AllocLinkID.md) | [AllocLinkID](tags/196-AllocLinkID.md) | Can be used to link two different Allocation messages (each with unique AllocID <70> together, i.e. for F/X "Netting" or "Swaps". Should be unique. |
| [197](tags/197-AllocLinkType.md) | [AllocLinkType](tags/197-AllocLinkType.md) | Identifies the type of Allocation linkage when AllocLinkID <196> is used. |
| [198](tags/198-SecondaryOrderID.md) | [SecondaryOrderID](tags/198-SecondaryOrderID.md) | Assigned by the party which accepts the order. Can be used to provide the OrderID (37) used by an exchange or executing system. |
| [199](tags/199-NoIOIQualifiers.md) | [NoIOIQualifiers](tags/199-NoIOIQualifiers.md) | Number of repeating groups of IOIQualifiers <104>. |
| [200](tags/200-MaturityMonthYear.md) | [MaturityMonthYear](tags/200-MaturityMonthYear.md) | Can be used with standardized derivatives vs. the MaturityDate (541) field. Month and Year of the maturity (used for standardized futures and options). |
| [201](tags/201-PutOrCall-replaced.md) | [PutOrCall (replaced)](tags/201-PutOrCall-replaced.md) | No longer used as of FIX 4.3. Included here for reference to prior versions. |
| [202](tags/202-StrikePrice.md) | [StrikePrice](tags/202-StrikePrice.md) | Strike Price for an Option. |
| [203](tags/203-CoveredOrUncovered.md) | [CoveredOrUncovered](tags/203-CoveredOrUncovered.md) | Used for derivative products, such as options |
| [204](tags/204-CustomerOrFirm-replaced.md) | [CustomerOrFirm (replaced)](tags/204-CustomerOrFirm-replaced.md) | No longer used as of FIX 4.3. Included here for reference to prior versions. |
| [205](tags/205-MaturityDay-replaced.md) | [MaturityDay (replaced)](tags/205-MaturityDay-replaced.md) | No longer used as of FIX 4.3. Included here for reference to prior versions. |
| [206](tags/206-OptAttribute.md) | [OptAttribute](tags/206-OptAttribute.md) | Can be used for SecurityType (167) =OPT to identify a particular security. Valid values vary by SecurityExchange: For Exchanges: DTB (Frankfurt), HKSE (Hong Kong), and SOFFEX (Zurich) 0-9 = single digit "version" number assigned by exchange following capital adjustments (0=current, 1=prior, 2=prior to 1, etc). |
| [207](tags/207-SecurityExchange.md) | [SecurityExchange](tags/207-SecurityExchange.md) | Market used to help identify a security. |
| [208](tags/208-NotifyBrokerOfCredit.md) | [NotifyBrokerOfCredit](tags/208-NotifyBrokerOfCredit.md) | Indicates whether or not details should be communicated to BrokerOfCredit <92> (i.e. step-in broker). |
| [209](tags/209-AllocHandlInst.md) | [AllocHandlInst](tags/209-AllocHandlInst.md) | Indicates how the receiver (i.e. third party) of Allocation message should handle/process the account details. |
| [210](tags/210-MaxShow.md) | [MaxShow](tags/210-MaxShow.md) | Maximum quantity (e.g. number of shares) within an order to be shown to other customers (i.e. sent via an IOI <6>). |
| [211](tags/211-PegOffsetValue.md) | [PegOffsetValue](tags/211-PegOffsetValue.md) | Amount (signed) added to the peg for a pegged order in the context of the PegOffsetType (836) |
| [212](tags/212-XmlDataLen.md) | [XmlDataLen](tags/212-XmlDataLen.md) | Length of the XmlData (213) data block. |
| [213](tags/213-XmlData.md) | [XmlData](tags/213-XmlData.md) | Actual XML data stream (e.g. FIXML). See approriate XML reference (e.g. FIXML). Note: may contain embedded SOH characters. |
| [214](tags/214-SettlInstRefID.md) | [SettlInstRefID](tags/214-SettlInstRefID.md) | Reference identifier for the SettlInstID <162> with 'Cancel' and 'Replace' SettlInstTransType <163> transaction types. |
| [215](tags/215-NoRoutingIDs.md) | [NoRoutingIDs](tags/215-NoRoutingIDs.md) | Number of repeating groups of RoutingID (217) and RoutingType (216) values. |
| [216](tags/216-RoutingType.md) | [RoutingType](tags/216-RoutingType.md) | Indicates the type of RoutingID (217) specified. |
| [217](tags/217-RoutingID.md) | [RoutingID](tags/217-RoutingID.md) | Assigned value used to identify a specific routing destination. |
| [218](tags/218-Spread.md) | [Spread](tags/218-Spread.md) | For Fixed Income. Either Swap Spread or Spread to Benchmark depending upon the order type. |
| [219](tags/219-Benchmark-no-longer-used.md) | [Benchmark (no longer used)](tags/219-Benchmark-no-longer-used.md) | No longer used. Included here for reference to prior versions. |
| [220](tags/220-BenchmarkCurveCurrency.md) | [BenchmarkCurveCurrency](tags/220-BenchmarkCurveCurrency.md) | Identifies currency used for benchmark curve. See "Appendix 6-A: Valid Currency Codes" for information on obtaining valid values. |
| [221](tags/221-BenchmarkCurveName.md) | [BenchmarkCurveName](tags/221-BenchmarkCurveName.md) | Name of benchmark curve. |
| [222](tags/222-BenchmarkCurvePoint.md) | [BenchmarkCurvePoint](tags/222-BenchmarkCurvePoint.md) | Point on benchmark curve. Free form values: e.g. "1Y", "7Y", "INTERPOLATED". |
| [223](tags/223-CouponRate.md) | [CouponRate](tags/223-CouponRate.md) | The rate of interest that, when multiplied by the principal, par value, or face value of a bond, provides the currency amount of the periodic interest payment. The coupon is always cited, along with maturity, in any quotation of a bond's price. |
| [224](tags/224-CouponPaymentDate.md) | [CouponPaymentDate](tags/224-CouponPaymentDate.md) | Date interest is to be paid. Used in identifying Corporate Bond issues. |
| [225](tags/225-IssueDate.md) | [IssueDate](tags/225-IssueDate.md) | The date on which a bond or stock offering is issued. It may or may not be the same as the effective date (DatedDate <873>) or the date on which interest begins to accrue (InterestAccrualDate <874>). |
| [226](tags/226-RepurchaseTerm.md) | [RepurchaseTerm](tags/226-RepurchaseTerm.md) | DEPRECATED FIELD - See Appendix 6-E: 5.Deprecated various FIX 4.3-introduced "Repo" Fields [deprecated in FIX 4.4] . |
| [227](tags/227-RepurchaseRate.md) | [RepurchaseRate](tags/227-RepurchaseRate.md) | DEPRECATED FIELD - See Appendix 6-E: 5.Deprecated various FIX 4.3-introduced "Repo" Fields [deprecated in FIX 4.4] . |
| [228](tags/228-Factor.md) | [Factor](tags/228-Factor.md) | For Fixed Income: Amorization Factor for deriving Current face from Original face for ABS or MBS securities, note the fraction may be greater than, equal to or less than 1. In TIPS securities this is the Inflation index. |
| [229](tags/229-TradeOriginationDate.md) | [TradeOriginationDate](tags/229-TradeOriginationDate.md) | Used with Fixed Income for Muncipal New Issue Market. Agreement in principal between counter-parties prior to actual trade date. |
| [230](tags/230-ExDate.md) | [ExDate](tags/230-ExDate.md) | The date when a distribution of interest is deducted from a securities assets or set aside for payment to bondholders. On the ex-date, the securities price drops by the amount of the distribution (plus or minus any market activity). |
| [231](tags/231-ContractMultiplier.md) | [ContractMultiplier](tags/231-ContractMultiplier.md) | Specifies the ratio or multiply factor to convert from "nominal" units (e.g. contracts) to total units (e.g. shares) (e.g. 1.0, 100, 1000, etc). Applicable For Fixed Income, Convertible Bonds, Derivatives, etc. |
| [232](tags/232-NoStipulations.md) | [NoStipulations](tags/232-NoStipulations.md) | Number of stipulation entries |
| [233](tags/233-StipulationType.md) | [StipulationType](tags/233-StipulationType.md) | For Fixed Income. Type of Stipulation. |
| [234](tags/234-StipulationValue.md) | [StipulationValue](tags/234-StipulationValue.md) | For Fixed Income. Value of stipulation. |
| [235](tags/235-YieldType.md) | [YieldType](tags/235-YieldType.md) | Type of yield. |
| [236](tags/236-Yield.md) | [Yield](tags/236-Yield.md) | Yield percentage. |
| [237](tags/237-TotalTakedown.md) | [TotalTakedown](tags/237-TotalTakedown.md) | The price at which the securities are distributed to the different members of an underwriting group for the primary market in Municipals, total gross underwriter's spread. |
| [238](tags/238-Concession.md) | [Concession](tags/238-Concession.md) | Provides the reduction in price for the secondary market in Muncipals. |
| [239](tags/239-RepoCollateralSecurityType.md) | [RepoCollateralSecurityType](tags/239-RepoCollateralSecurityType.md) | DEPRECATED FIELD - See Appendix 6-E: 5.Deprecated various FIX 4.3-introduced "Repo" Fields [deprecated in FIX 4.4] . |
| [240](tags/240-RedemptionDate.md) | [RedemptionDate](tags/240-RedemptionDate.md) | DEPRECATED FIELD - See Appendix 6-E: 3.Deprecated Instrument-affiliated "RedemptionDate" Fields: RedemptionDate (240), UnderlyingRedemptionDate (247), and LegRedemptionDate (254) [deprecated in FIX 4.4] . |
| [241](tags/241-UnderlyingCouponPaymentDate.md) | [UnderlyingCouponPaymentDate](tags/241-UnderlyingCouponPaymentDate.md) | Underlying security's CouponPaymentDate. See CouponPaymentDate (224) field for description |
| [242](tags/242-UnderlyingIssueDate.md) | [UnderlyingIssueDate](tags/242-UnderlyingIssueDate.md) | Underlying security's IssueDate. See IssueDate (225) field for description |
| [243](tags/243-UnderlyingRepoCollateralSecurityType.md) | [UnderlyingRepoCollateralSecurityType](tags/243-UnderlyingRepoCollateralSecurityType.md) | DEPRECATED FIELD - See Appendix 6-E: 5.Deprecated various FIX 4.3-introduced "Repo" Fields [deprecated in FIX 4.4] . |
| [244](tags/244-UnderlyingRepurchaseTerm.md) | [UnderlyingRepurchaseTerm](tags/244-UnderlyingRepurchaseTerm.md) | DEPRECATED FIELD - See Appendix 6-E: 5.Deprecated various FIX 4.3-introduced "Repo" Fields [deprecated in FIX 4.4] . |
| [245](tags/245-UnderlyingRepurchaseRate.md) | [UnderlyingRepurchaseRate](tags/245-UnderlyingRepurchaseRate.md) | DEPRECATED FIELD - See Appendix 6-E: 5.Deprecated various FIX 4.3-introduced "Repo" Fields [deprecated in FIX 4.4] . |
| [246](tags/246-UnderlyingFactor.md) | [UnderlyingFactor](tags/246-UnderlyingFactor.md) | Underlying security's Factor. |
| [247](tags/247-UnderlyingRedemptionDate.md) | [UnderlyingRedemptionDate](tags/247-UnderlyingRedemptionDate.md) | DEPRECATED FIELD - See Appendix 6-E: 3.Deprecated Instrument-affiliated "RedemptionDate" Fields: RedemptionDate (240), UnderlyingRedemptionDate (247), and LegRedemptionDate (254) [deprecated in FIX 4.4] . |
| [248](tags/248-LegCouponPaymentDate.md) | [LegCouponPaymentDate](tags/248-LegCouponPaymentDate.md) | Multileg instrument's individual leg security's CouponPaymentDate. See CouponPaymentDate (224) field for description |
| [249](tags/249-LegIssueDate.md) | [LegIssueDate](tags/249-LegIssueDate.md) | Multileg instrument's individual leg security's IssueDate. See IssueDate (225) field for description |
| [250](tags/250-LegRepoCollateralSecurityType.md) | [LegRepoCollateralSecurityType](tags/250-LegRepoCollateralSecurityType.md) | DEPRECATED FIELD - See Appendix 6-E: 5.Deprecated various FIX 4.3-introduced "Repo" Fields [deprecated in FIX 4.4] . |
| [251](tags/251-LegRepurchaseTerm.md) | [LegRepurchaseTerm](tags/251-LegRepurchaseTerm.md) | DEPRECATED FIELD - See Appendix 6-E: 5.Deprecated various FIX 4.3-introduced "Repo" Fields [deprecated in FIX 4.4] . |
| [252](tags/252-LegRepurchaseRate.md) | [LegRepurchaseRate](tags/252-LegRepurchaseRate.md) | DEPRECATED FIELD - See Appendix 6-E: 5.Deprecated various FIX 4.3-introduced "Repo" Fields [deprecated in FIX 4.4] . |
| [253](tags/253-LegFactor.md) | [LegFactor](tags/253-LegFactor.md) | Multileg instrument's individual leg security's Factor. |
| [254](tags/254-LegRedemptionDate.md) | [LegRedemptionDate](tags/254-LegRedemptionDate.md) | DEPRECATED FIELD - See Appendix 6-E: 3.Deprecated Instrument-affiliated "RedemptionDate" Fields: RedemptionDate (240), UnderlyingRedemptionDate (247), and LegRedemptionDate (254) [deprecated in FIX 4.4] . |
| [255](tags/255-CreditRating.md) | [CreditRating](tags/255-CreditRating.md) | An evaluation of a company's ability to repay obligations or its likelihood of not defaulting. These evaluation are provided by Credit Rating Agencies, i.e. S&P, Moody's. |
| [256](tags/256-UnderlyingCreditRating.md) | [UnderlyingCreditRating](tags/256-UnderlyingCreditRating.md) | Underlying security's CreditRating. See CreditRating (255) field for description |
| [257](tags/257-LegCreditRating.md) | [LegCreditRating](tags/257-LegCreditRating.md) | Multileg instrument's individual leg security's CreditRating. See CreditRating (255) field for description |
| [258](tags/258-TradedFlatSwitch.md) | [TradedFlatSwitch](tags/258-TradedFlatSwitch.md) | Driver and part of trade in the event that the Security Master file was wrong at the point of entry |
| [259](tags/259-BasisFeatureDate.md) | [BasisFeatureDate](tags/259-BasisFeatureDate.md) | BasisFeatureDate (259) allows requesting firms within fixed income the ability to request an alternative yield-to-worst, -maturity, -extended or other call. This flows through the confirm process. |
| [260](tags/260-BasisFeaturePrice.md) | [BasisFeaturePrice](tags/260-BasisFeaturePrice.md) | Price for BasisFeatureDate. |
| [262](tags/262-MDReqID.md) | [MDReqID](tags/262-MDReqID.md) | Unique identifier for Market Data Request <V>. |
| [263](tags/263-SubscriptionRequestType.md) | [SubscriptionRequestType](tags/263-SubscriptionRequestType.md) | Subscription Request Type |
| [264](tags/264-MarketDepth.md) | [MarketDepth](tags/264-MarketDepth.md) | Depth of market for Book Snapshot |
| [265](tags/265-MDUpdateType.md) | [MDUpdateType](tags/265-MDUpdateType.md) | Specifies the type of Market Data update. |
| [266](tags/266-AggregatedBook.md) | [AggregatedBook](tags/266-AggregatedBook.md) | Specifies whether or not book entries should be aggregated. |
| [267](tags/267-NoMDEntryTypes.md) | [NoMDEntryTypes](tags/267-NoMDEntryTypes.md) | Number of MDEntryType (269) fields requested. |
| [268](tags/268-NoMDEntries.md) | [NoMDEntries](tags/268-NoMDEntries.md) | Number of entries in Market Data message. |
| [269](tags/269-MDEntryType.md) | [MDEntryType](tags/269-MDEntryType.md) | Type Market Data entry. |
| [270](tags/270-MDEntryPx.md) | [MDEntryPx](tags/270-MDEntryPx.md) | Price of the Market Data Entry. |
| [271](tags/271-MDEntrySize.md) | [MDEntrySize](tags/271-MDEntrySize.md) | Quantity or volume represented by the Market Data Entry. |
| [272](tags/272-MDEntryDate.md) | [MDEntryDate](tags/272-MDEntryDate.md) | Date of Market Data Entry. |
| [273](tags/273-MDEntryTime.md) | [MDEntryTime](tags/273-MDEntryTime.md) | Time of Market Data Entry. |
| [274](tags/274-TickDirection.md) | [TickDirection](tags/274-TickDirection.md) | Direction of the "tick". |
| [275](tags/275-MDMkt.md) | [MDMkt](tags/275-MDMkt.md) | Market posting quote / trade. |
| [276](tags/276-QuoteCondition.md) | [QuoteCondition](tags/276-QuoteCondition.md) | Space-delimited list of conditions describing a quote. |
| [277](tags/277-TradeCondition.md) | [TradeCondition](tags/277-TradeCondition.md) | Space-delimited list of conditions describing a trade |
| [278](tags/278-MDEntryID.md) | [MDEntryID](tags/278-MDEntryID.md) | Unique Market Data Entry identifier. |
| [279](tags/279-MDUpdateAction.md) | [MDUpdateAction](tags/279-MDUpdateAction.md) | Type of Market Data update action. |
| [280](tags/280-MDEntryRefID.md) | [MDEntryRefID](tags/280-MDEntryRefID.md) | Refers to a previous MDEntryID <278>. |
| [281](tags/281-MDReqRejReason.md) | [MDReqRejReason](tags/281-MDReqRejReason.md) | Reason for the rejection of a MarketDataRequest <V>. |
| [282](tags/282-MDEntryOriginator.md) | [MDEntryOriginator](tags/282-MDEntryOriginator.md) | Originator of a Market Data Entry |
| [283](tags/283-LocationID.md) | [LocationID](tags/283-LocationID.md) | Identification of a Market Maker's location |
| [284](tags/284-DeskID.md) | [DeskID](tags/284-DeskID.md) | Identification of a Market Maker's desk |
| [285](tags/285-DeleteReason.md) | [DeleteReason](tags/285-DeleteReason.md) | Reason for deletion. |
| [286](tags/286-OpenCloseSettlFlag.md) | [OpenCloseSettlFlag](tags/286-OpenCloseSettlFlag.md) | Flag that identifies a market data entry. |
| [287](tags/287-SellerDays.md) | [SellerDays](tags/287-SellerDays.md) | Specifies the number of days that may elapse before delivery of the security |
| [288](tags/288-MDEntryBuyer.md) | [MDEntryBuyer](tags/288-MDEntryBuyer.md) | Buying party in a trade |
| [289](tags/289-MDEntrySeller.md) | [MDEntrySeller](tags/289-MDEntrySeller.md) | Selling party in a trade |
| [290](tags/290-MDEntryPositionNo.md) | [MDEntryPositionNo](tags/290-MDEntryPositionNo.md) | Display position of a bid or offer, numbered from most competitive to least competitive, per market side, beginning with 1. |
| [291](tags/291-FinancialStatus.md) | [FinancialStatus](tags/291-FinancialStatus.md) | Identifies a firm's financial status. |
| [292](tags/292-CorporateAction.md) | [CorporateAction](tags/292-CorporateAction.md) | Identifies the type of Corporate Action. |
| [293](tags/293-DefBidSize.md) | [DefBidSize](tags/293-DefBidSize.md) | Default Bid Size. |
| [294](tags/294-DefOfferSize.md) | [DefOfferSize](tags/294-DefOfferSize.md) | Default Offer Size. |
| [295](tags/295-NoQuoteEntries.md) | [NoQuoteEntries](tags/295-NoQuoteEntries.md) | The number of quote entries for a QuoteSet. |
| [296](tags/296-NoQuoteSets.md) | [NoQuoteSets](tags/296-NoQuoteSets.md) | The number of sets of quotes in the message. |
| [297](tags/297-QuoteStatus.md) | [QuoteStatus](tags/297-QuoteStatus.md) | Identifies the status of the quote acknowledgement. |
| [298](tags/298-QuoteCancelType.md) | [QuoteCancelType](tags/298-QuoteCancelType.md) | Identifies the type of quote cancel. |
| [299](tags/299-QuoteEntryID.md) | [QuoteEntryID](tags/299-QuoteEntryID.md) | Uniquely identifies the quote as part of a QuoteSet. |
| [300](tags/300-QuoteRejectReason.md) | [QuoteRejectReason](tags/300-QuoteRejectReason.md) | Reason Quote was rejected:. |
| [301](tags/301-QuoteResponseLevel.md) | [QuoteResponseLevel](tags/301-QuoteResponseLevel.md) | Level of Response requested from receiver of quote messages. |
| [302](tags/302-QuoteSetID.md) | [QuoteSetID](tags/302-QuoteSetID.md) | Unique id for the Quote Set. |
| [303](tags/303-QuoteRequestType.md) | [QuoteRequestType](tags/303-QuoteRequestType.md) | Indicates the type of Quote Request <R> being generated. |
| [304](tags/304-TotNoQuoteEntries.md) | [TotNoQuoteEntries](tags/304-TotNoQuoteEntries.md) | Total number of quotes for the quote set across all messages. Should be the sum of all NoQuoteEntries <295> in each message that has repeating quotes that are part of the same quote set. |
| [305](tags/305-UnderlyingSecurityIDSource.md) | [UnderlyingSecurityIDSource](tags/305-UnderlyingSecurityIDSource.md) | Underlying security's SecurityIDSource. See SecurityIDSource (22) field for description |
| [306](tags/306-UnderlyingIssuer.md) | [UnderlyingIssuer](tags/306-UnderlyingIssuer.md) | Underlying security's Issuer. See Issuer (106) field for description |
| [307](tags/307-UnderlyingSecurityDesc.md) | [UnderlyingSecurityDesc](tags/307-UnderlyingSecurityDesc.md) | Underlying security's SecurityDesc. See SecurityDesc (107) field for description |
| [308](tags/308-UnderlyingSecurityExchange.md) | [UnderlyingSecurityExchange](tags/308-UnderlyingSecurityExchange.md) | Underlying security's SecurityExchange. Can be used to identify the underlying security. |
| [309](tags/309-UnderlyingSecurityID.md) | [UnderlyingSecurityID](tags/309-UnderlyingSecurityID.md) | Underlying security's SecurityID. See SecurityID (48) field for description |
| [310](tags/310-UnderlyingSecurityType.md) | [UnderlyingSecurityType](tags/310-UnderlyingSecurityType.md) | Underlying security's SecurityType. |
| [311](tags/311-UnderlyingSymbol.md) | [UnderlyingSymbol](tags/311-UnderlyingSymbol.md) | Underlying security's Symbol. |
| [312](tags/312-UnderlyingSymbolSfx.md) | [UnderlyingSymbolSfx](tags/312-UnderlyingSymbolSfx.md) | Underlying security's SymbolSfx. See SymbolSfx (65) field for description |
| [313](tags/313-UnderlyingMaturityMonthYear.md) | [UnderlyingMaturityMonthYear](tags/313-UnderlyingMaturityMonthYear.md) | Underlying security's MaturityMonthYear. Can be used with standardized derivatives vs. the UnderlyingMaturityDate (542) field. See MaturityMonthYear (200) field for description |
| [314](tags/314-UnderlyingMaturityDay-replaced.md) | [UnderlyingMaturityDay (replaced)](tags/314-UnderlyingMaturityDay-replaced.md) | No longer used as of FIX 4.3. Included here for reference to prior versions. |
| [315](tags/315-UnderlyingPutOrCall-replaced.md) | [UnderlyingPutOrCall (replaced)](tags/315-UnderlyingPutOrCall-replaced.md) | No longer used as of FIX 4.3. Included here for reference to prior versions. |
| [316](tags/316-UnderlyingStrikePrice.md) | [UnderlyingStrikePrice](tags/316-UnderlyingStrikePrice.md) | Underlying security's StrikePrice. See StrikePrice (202) field for description |
| [317](tags/317-UnderlyingOptAttribute.md) | [UnderlyingOptAttribute](tags/317-UnderlyingOptAttribute.md) | Underlying security's OptAttribute. See OptAttribute (206) field for description |
| [318](tags/318-UnderlyingCurrency.md) | [UnderlyingCurrency](tags/318-UnderlyingCurrency.md) | Underlying security's Currency. See Currency (15) field for description |
| [319](tags/319-RatioQty-replaced.md) | [RatioQty (replaced)](tags/319-RatioQty-replaced.md) | No longer used as of FIX 4.3. Included here for reference to prior versions. |
| [320](tags/320-SecurityReqID.md) | [SecurityReqID](tags/320-SecurityReqID.md) | Unique ID of a Security Definition Request <c>. |
| [321](tags/321-SecurityRequestType.md) | [SecurityRequestType](tags/321-SecurityRequestType.md) | Type of Security Definition Request <c>. |
| [322](tags/322-SecurityResponseID.md) | [SecurityResponseID](tags/322-SecurityResponseID.md) | Unique ID of a Security Definition <d> message. |
| [323](tags/323-SecurityResponseType.md) | [SecurityResponseType](tags/323-SecurityResponseType.md) | Type of Security Definition <d> message response. |
| [324](tags/324-SecurityStatusReqID.md) | [SecurityStatusReqID](tags/324-SecurityStatusReqID.md) | Unique ID of a Security Status Request <e> message. |
| [325](tags/325-UnsolicitedIndicator.md) | [UnsolicitedIndicator](tags/325-UnsolicitedIndicator.md) | Indicates whether or not message is being sent as a result of a subscription request or not. |
| [326](tags/326-SecurityTradingStatus.md) | [SecurityTradingStatus](tags/326-SecurityTradingStatus.md) | Identifies the trading status applicable to the transaction. |
| [327](tags/327-HaltReason.md) | [HaltReason](tags/327-HaltReason.md) | Denotes the reason for the Opening Delay or Trading Halt. |
| [328](tags/328-InViewOfCommon.md) | [InViewOfCommon](tags/328-InViewOfCommon.md) | Indicates whether or not the halt was due to Common Stock trading being halted. |
| [329](tags/329-DueToRelated.md) | [DueToRelated](tags/329-DueToRelated.md) | Indicates whether or not the halt was due to the Related Security being halted. |
| [330](tags/330-BuyVolume.md) | [BuyVolume](tags/330-BuyVolume.md) | Quantity bought. |
| [331](tags/331-SellVolume.md) | [SellVolume](tags/331-SellVolume.md) | Quantity sold. |
| [332](tags/332-HighPx.md) | [HighPx](tags/332-HighPx.md) | Represents an indication of the high end of the price range for a security prior to the open or reopen |
| [333](tags/333-LowPx.md) | [LowPx](tags/333-LowPx.md) | Represents an indication of the low end of the price range for a security prior to the open or reopen |
| [334](tags/334-Adjustment.md) | [Adjustment](tags/334-Adjustment.md) | Identifies the type of adjustment. |
| [335](tags/335-TradSesReqID.md) | [TradSesReqID](tags/335-TradSesReqID.md) | Unique ID of a Trading Session Status <h> message. |
| [336](tags/336-TradingSessionID.md) | [TradingSessionID](tags/336-TradingSessionID.md) | Identifier for Trading Session |
| [337](tags/337-ContraTrader.md) | [ContraTrader](tags/337-ContraTrader.md) | Identifies the trader (e.g. "badge number") of the ContraBroker <375>. |
| [338](tags/338-TradSesMethod.md) | [TradSesMethod](tags/338-TradSesMethod.md) | Method of trading |
| [339](tags/339-TradSesMode.md) | [TradSesMode](tags/339-TradSesMode.md) | Trading Session Mode |
| [340](tags/340-TradSesStatus.md) | [TradSesStatus](tags/340-TradSesStatus.md) | State of the trading session. |
| [341](tags/341-TradSesStartTime.md) | [TradSesStartTime](tags/341-TradSesStartTime.md) | Starting time of the trading session |
| [342](tags/342-TradSesOpenTime.md) | [TradSesOpenTime](tags/342-TradSesOpenTime.md) | Time of the opening of the trading session |
| [343](tags/343-TradSesPreCloseTime.md) | [TradSesPreCloseTime](tags/343-TradSesPreCloseTime.md) | Time of the pre-closed of the trading session |
| [344](tags/344-TradSesCloseTime.md) | [TradSesCloseTime](tags/344-TradSesCloseTime.md) | Closing time of the trading session |
| [345](tags/345-TradSesEndTime.md) | [TradSesEndTime](tags/345-TradSesEndTime.md) | End time of the trading session |
| [346](tags/346-NumberOfOrders.md) | [NumberOfOrders](tags/346-NumberOfOrders.md) | Number of orders in the market. |
| [347](tags/347-MessageEncoding.md) | [MessageEncoding](tags/347-MessageEncoding.md) | Type of message encoding (non-ASCII (non-English) characters) used in a message's "Encoded" fields. |
| [348](tags/348-EncodedIssuerLen.md) | [EncodedIssuerLen](tags/348-EncodedIssuerLen.md) | Byte length of encoded (non-ASCII characters) EncodedIssuer (349) field. |
| [349](tags/349-EncodedIssuer.md) | [EncodedIssuer](tags/349-EncodedIssuer.md) | Encoded (non-ASCII characters) representation of the Issuer <106> field in the encoded format specified via the MessageEncoding <347> field. If used, the ASCII (English) representation should also be specified in the Issuer field. |
| [350](tags/350-EncodedSecurityDescLen.md) | [EncodedSecurityDescLen](tags/350-EncodedSecurityDescLen.md) | Byte length of encoded (non-ASCII characters) EncodedSecurityDesc (351) field. |
| [351](tags/351-EncodedSecurityDesc.md) | [EncodedSecurityDesc](tags/351-EncodedSecurityDesc.md) | Encoded (non-ASCII characters) representation of the SecurityDesc (107) field in the encoded format specified via the MessageEncoding (347) field. If used, the ASCII (English) representation should also be specified in the SecurityDesc (107) field. |
| [352](tags/352-EncodedListExecInstLen.md) | [EncodedListExecInstLen](tags/352-EncodedListExecInstLen.md) | Byte length of encoded (non-ASCII characters) EncodedListExecInst (353) field. |
| [353](tags/353-EncodedListExecInst.md) | [EncodedListExecInst](tags/353-EncodedListExecInst.md) | Encoded (non-ASCII characters) representation of the ListExecInst (69) field in the encoded format specified via the MessageEncoding (347) field. If used, the ASCII (English) representation should also be specified in the ListExecInst (69) field. |
| [354](tags/354-EncodedTextLen.md) | [EncodedTextLen](tags/354-EncodedTextLen.md) | Byte length of encoded (non-ASCII characters) EncodedText (355) field. |
| [355](tags/355-EncodedText.md) | [EncodedText](tags/355-EncodedText.md) | Encoded (non-ASCII characters) representation of the Text (58) field in the encoded format specified via the MessageEncoding (347) field. If used, the ASCII (English) representation should also be specified in the Text (58) field. |
| [356](tags/356-EncodedSubjectLen.md) | [EncodedSubjectLen](tags/356-EncodedSubjectLen.md) | Byte length of encoded (non-ASCII characters) EncodedSubject (357) field. |
| [357](tags/357-EncodedSubject.md) | [EncodedSubject](tags/357-EncodedSubject.md) | Encoded (non-ASCII characters) representation of the Subject (147) field in the encoded format specified via the MessageEncoding (347) field. If used, the ASCII (English) representation should also be specified in the Subject (147) field. |
| [358](tags/358-EncodedHeadlineLen.md) | [EncodedHeadlineLen](tags/358-EncodedHeadlineLen.md) | Byte length of encoded (non-ASCII characters) EncodedHeadline (359) field. |
| [359](tags/359-EncodedHeadline.md) | [EncodedHeadline](tags/359-EncodedHeadline.md) | Encoded (non-ASCII characters) representation of the Headline (148) field in the encoded format specified via the MessageEncoding (347) field. If used, the ASCII (English) representation should also be specified in the Headline (148) field. |
| [360](tags/360-EncodedAllocTextLen.md) | [EncodedAllocTextLen](tags/360-EncodedAllocTextLen.md) | Byte length of encoded (non-ASCII characters) EncodedAllocText (361) field. |
| [361](tags/361-EncodedAllocText.md) | [EncodedAllocText](tags/361-EncodedAllocText.md) | Encoded (non-ASCII characters) representation of the AllocText (161) field in the encoded format specified via the MessageEncoding (347) field. If used, the ASCII (English) representation should also be specified in the AllocText (161) field. |
| [362](tags/362-EncodedUnderlyingIssuerLen.md) | [EncodedUnderlyingIssuerLen](tags/362-EncodedUnderlyingIssuerLen.md) | Byte length of encoded (non-ASCII characters) EncodedUnderlyingIssuer (363) field. |
| [363](tags/363-EncodedUnderlyingIssuer.md) | [EncodedUnderlyingIssuer](tags/363-EncodedUnderlyingIssuer.md) | Encoded (non-ASCII characters) representation of the UnderlyingIssuer (306) field in the encoded format specified via the MessageEncoding (347) field. If used, the ASCII (English) representation should also be specified in the UnderlyingIssuer (306) field. |
| [364](tags/364-EncodedUnderlyingSecurityDescLen.md) | [EncodedUnderlyingSecurityDescLen](tags/364-EncodedUnderlyingSecurityDescLen.md) | Byte length of encoded (non-ASCII characters) EncodedUnderlyingSecurityDesc (365) field. |
| [365](tags/365-EncodedUnderlyingSecurityDesc.md) | [EncodedUnderlyingSecurityDesc](tags/365-EncodedUnderlyingSecurityDesc.md) | Encoded (non-ASCII characters) representation of the UnderlyingSecurityDesc <307> field in the encoded format specified via the MessageEncoding <347> field. If used, the ASCII (English) representation should also be specified in the UnderlyingSecurityeDesc field. |
| [366](tags/366-AllocPrice.md) | [AllocPrice](tags/366-AllocPrice.md) | Executed price for an AllocAccount (79) entry used when using "executed price" vs. "average price" allocations (e.g. Japan). |
| [367](tags/367-QuoteSetValidUntilTime.md) | [QuoteSetValidUntilTime](tags/367-QuoteSetValidUntilTime.md) | Indicates expiration time of this particular QuoteSet (always expressed in UTC (Universal Time Coordinated, also known as "GMT") |
| [368](tags/368-QuoteEntryRejectReason.md) | [QuoteEntryRejectReason](tags/368-QuoteEntryRejectReason.md) | Reason Quote Entry was rejected: |
| [369](tags/369-LastMsgSeqNumProcessed.md) | [LastMsgSeqNumProcessed](tags/369-LastMsgSeqNumProcessed.md) | The last MsgSeqNum (34) value received by the FIX engine and processed by downstream application, such as trading engine or order routing system. Can be specified on every message sent. Useful for detecting a backlog with a counterparty. |
| [370](tags/370-OnBehalfOfSendingTime-no-longer-used.md) | [OnBehalfOfSendingTime (no longer used)](tags/370-OnBehalfOfSendingTime-no-longer-used.md) | No longer used as of FIX.4.4. Included here for reference to prior versions. |
| [371](tags/371-RefTagID.md) | [RefTagID](tags/371-RefTagID.md) | The tag number of the FIX field being referenced. |
| [372](tags/372-RefMsgType.md) | [RefMsgType](tags/372-RefMsgType.md) | The MsgType (35) of the FIX message being referenced. |
| [373](tags/373-SessionRejectReason.md) | [SessionRejectReason](tags/373-SessionRejectReason.md) | Code to identify reason for a session-level Reject (3) message. |
| [374](tags/374-BidRequestTransType.md) | [BidRequestTransType](tags/374-BidRequestTransType.md) | Identifies the Bid Request <k> message type. |
| [375](tags/375-ContraBroker.md) | [ContraBroker](tags/375-ContraBroker.md) | Identifies contra broker. Standard NASD market-maker mnemonic is preferred. |
| [376](tags/376-ComplianceID.md) | [ComplianceID](tags/376-ComplianceID.md) | ID used to represent this transaction for compliance purposes (e.g. OATS reporting). |
| [377](tags/377-SolicitedFlag.md) | [SolicitedFlag](tags/377-SolicitedFlag.md) | Indicates whether or not the order was solicited. |
| [378](tags/378-ExecRestatementReason.md) | [ExecRestatementReason](tags/378-ExecRestatementReason.md) | Code to identify reason for an ExecutionRpt <8> message sent with ExecType <150>='Restated' or used when communicating an unsolicited cancel. |
| [379](tags/379-BusinessRejectRefID.md) | [BusinessRejectRefID](tags/379-BusinessRejectRefID.md) | The value of the business-level "ID" field on the message being referenced. |
| [380](tags/380-BusinessRejectReason.md) | [BusinessRejectReason](tags/380-BusinessRejectReason.md) | Code to identify reason for a Business Message Reject <j> message. |
| [381](tags/381-GrossTradeAmt.md) | [GrossTradeAmt](tags/381-GrossTradeAmt.md) | Total amount traded (e.g. CumQty <14> AvgPx <6>) expressed in units of currency. |
| [382](tags/382-NoContraBrokers.md) | [NoContraBrokers](tags/382-NoContraBrokers.md) | The number of ContraBroker (375) entries. |
| [383](tags/383-MaxMessageSize.md) | [MaxMessageSize](tags/383-MaxMessageSize.md) | Maximum number of bytes supported for a single message. |
| [384](tags/384-NoMsgTypes.md) | [NoMsgTypes](tags/384-NoMsgTypes.md) | Number of MsgTypes <35> in repeating group. |
| [385](tags/385-MsgDirection.md) | [MsgDirection](tags/385-MsgDirection.md) | Specifies the direction of the messsage. |
| [386](tags/386-NoTradingSessions.md) | [NoTradingSessions](tags/386-NoTradingSessions.md) | Number of TradingSessionIDs <336> in repeating group. |
| [387](tags/387-TotalVolumeTraded.md) | [TotalVolumeTraded](tags/387-TotalVolumeTraded.md) | Total volume (quantity) traded. |
| [388](tags/388-DiscretionInst.md) | [DiscretionInst](tags/388-DiscretionInst.md) | Code to identify the price a DiscretionOffsetValue (389) is related to and should be mathematically added to. |
| [389](tags/389-DiscretionOffsetValue.md) | [DiscretionOffsetValue](tags/389-DiscretionOffsetValue.md) | Amount (signed) added to the "related to" price specified via DiscretionInst <388>, in the context of DiscretionOffsetType <842>. |
| [390](tags/390-BidID.md) | [BidID](tags/390-BidID.md) | Unique identifier for Bid Response <l> as assigned by sell-side (broker, exchange, ECN). Uniqueness must be guaranteed within a single trading day. |
| [391](tags/391-ClientBidID.md) | [ClientBidID](tags/391-ClientBidID.md) | Unique identifier for a Bid Request <k> as assigned by institution. Uniqueness must be guaranteed within a single trading day. |
| [392](tags/392-ListName.md) | [ListName](tags/392-ListName.md) | Descriptive name for list order. |
| [393](tags/393-TotNoRelatedSym.md) | [TotNoRelatedSym](tags/393-TotNoRelatedSym.md) | Total number of securities. |
| [394](tags/394-BidType.md) | [BidType](tags/394-BidType.md) | Code to identify the type of Bid Request <k>. |
| [395](tags/395-NumTickets.md) | [NumTickets](tags/395-NumTickets.md) | Total number of tickets. |
| [396](tags/396-SideValue1.md) | [SideValue1](tags/396-SideValue1.md) | Amounts in currency |
| [397](tags/397-SideValue2.md) | [SideValue2](tags/397-SideValue2.md) | Amounts in currency |
| [398](tags/398-NoBidDescriptors.md) | [NoBidDescriptors](tags/398-NoBidDescriptors.md) | Number of BidDescriptor (400) entries. |
| [399](tags/399-BidDescriptorType.md) | [BidDescriptorType](tags/399-BidDescriptorType.md) | Code to identify the type of BidDescriptor <400>. |
| [400](tags/400-BidDescriptor.md) | [BidDescriptor](tags/400-BidDescriptor.md) | BidDescriptor value. Usage depends upon BidDescriptorType <399>. |
| [401](tags/401-SideValueInd.md) | [SideValueInd](tags/401-SideValueInd.md) | Code to identify which "SideValue" the value refers to. SideValue1 <396> and SideValue2 <397> are used as opposed to Buy or Sell so that the basket can be quoted either way as Buy or Sell. |
| [402](tags/402-LiquidityPctLow.md) | [LiquidityPctLow](tags/402-LiquidityPctLow.md) | Liquidity indicator or lower limit if TotNoRelatedSym (393) > 1. Represented as a percentage. |
| [403](tags/403-LiquidityPctHigh.md) | [LiquidityPctHigh](tags/403-LiquidityPctHigh.md) | Upper liquidity indicator if TotNoRelatedSym (393) > 1. Represented as a percentage. |
| [404](tags/404-LiquidityValue.md) | [LiquidityValue](tags/404-LiquidityValue.md) | Value between LiquidityPctLow (402) and LiquidityPctHigh (403) in Currency (15) |
| [405](tags/405-EFPTrackingError.md) | [EFPTrackingError](tags/405-EFPTrackingError.md) | Eg Used in EFP trades 12% (EFP - Exchange for Physical ). Represented as a percentage. |
| [406](tags/406-FairValue.md) | [FairValue](tags/406-FairValue.md) | Used in EFP trades |
| [407](tags/407-OutsideIndexPct.md) | [OutsideIndexPct](tags/407-OutsideIndexPct.md) | Used in EFP trades. Represented as a percentage. |
| [408](tags/408-ValueOfFutures.md) | [ValueOfFutures](tags/408-ValueOfFutures.md) | Used in EFP trades |
| [409](tags/409-LiquidityIndType.md) | [LiquidityIndType](tags/409-LiquidityIndType.md) | Code to identify the type of liquidity indicator. |
| [410](tags/410-WtAverageLiquidity.md) | [WtAverageLiquidity](tags/410-WtAverageLiquidity.md) | Overall weighted average liquidity expressed as a % of average daily volume. Represented as a percentage. |
| [411](tags/411-ExchangeForPhysical.md) | [ExchangeForPhysical](tags/411-ExchangeForPhysical.md) | Indicates whether or not to exchange for phsyical. |
| [412](tags/412-OutMainCntryUIndex.md) | [OutMainCntryUIndex](tags/412-OutMainCntryUIndex.md) | Value of stocks in Currency (15) |
| [413](tags/413-CrossPercent.md) | [CrossPercent](tags/413-CrossPercent.md) | Percentage of program that crosses in Currency <15>. Represented as a percentage. |
| [414](tags/414-ProgRptReqs.md) | [ProgRptReqs](tags/414-ProgRptReqs.md) | Code to identify the desired frequency of progress reports. |
| [415](tags/415-ProgPeriodInterval.md) | [ProgPeriodInterval](tags/415-ProgPeriodInterval.md) | Time in minutes between each ListStatus <N> report sent by SellSide. Zero means don't send status. |
| [416](tags/416-IncTaxInd.md) | [IncTaxInd](tags/416-IncTaxInd.md) | Code to represent whether value is net (inclusive of tax) or gross. |
| [417](tags/417-NumBidders.md) | [NumBidders](tags/417-NumBidders.md) | Indicates the total number of bidders on the list |
| [418](tags/418-BidTradeType.md) | [BidTradeType](tags/418-BidTradeType.md) | Code to represent the type of trade. |
| [419](tags/419-BasisPxType.md) | [BasisPxType](tags/419-BasisPxType.md) | Code to represent the basis price type. |
| [420](tags/420-NoBidComponents.md) | [NoBidComponents](tags/420-NoBidComponents.md) | Indicates the number of list entries. |
| [421](tags/421-Country.md) | [Country](tags/421-Country.md) | ISO Country Code in field |
| [422](tags/422-TotNoStrikes.md) | [TotNoStrikes](tags/422-TotNoStrikes.md) | Total number of strike price entries across all messages. Should be the sum of all NoStrikes <428> in each message that has repeating strike price entries related to the same ListID <66>. Used to support fragmentation. |
| [423](tags/423-PriceType.md) | [PriceType](tags/423-PriceType.md) | Code to represent the price type. |
| [424](tags/424-DayOrderQty.md) | [DayOrderQty](tags/424-DayOrderQty.md) | For GT orders, the OrderQty <38> less all quantity (adjusted for stock splits) that traded on previous days. DayOrderQty <424> = OrderQty <38> - (CumQty <14> - DayCumQty <425>). |
| [425](tags/425-DayCumQty.md) | [DayCumQty](tags/425-DayCumQty.md) | Quantity on a GT order that has traded today. |
| [426](tags/426-DayAvgPx.md) | [DayAvgPx](tags/426-DayAvgPx.md) | The average price for quantity on a GT order that has traded today. |
| [427](tags/427-GTBookingInst.md) | [GTBookingInst](tags/427-GTBookingInst.md) | Code to identify whether to book out executions on a part-filled GT order on the day of execution or to accumulate. |
| [428](tags/428-NoStrikes.md) | [NoStrikes](tags/428-NoStrikes.md) | Number of list strike price entries. |
| [429](tags/429-ListStatusType.md) | [ListStatusType](tags/429-ListStatusType.md) | Code to represent the status type. |
| [430](tags/430-NetGrossInd.md) | [NetGrossInd](tags/430-NetGrossInd.md) | Code to represent whether value is net (inclusive of tax) or gross. |
| [431](tags/431-ListOrderStatus.md) | [ListOrderStatus](tags/431-ListOrderStatus.md) | Code to represent the status of a list order. |
| [432](tags/432-ExpireDate.md) | [ExpireDate](tags/432-ExpireDate.md) | Date of order expiration (last day the order can trade), always expressed in terms of the local market date. The time at which the order expires is determined by the local market's business practices |
| [433](tags/433-ListExecInstType.md) | [ListExecInstType](tags/433-ListExecInstType.md) | Identifies the type of ListExecInst <69>. |
| [434](tags/434-CxlRejResponseTo.md) | [CxlRejResponseTo](tags/434-CxlRejResponseTo.md) | Identifies the type of request that a Cancel Reject <9> is in response to. |
| [435](tags/435-UnderlyingCouponRate.md) | [UnderlyingCouponRate](tags/435-UnderlyingCouponRate.md) | Underlying security's CouponRate. See CouponRate (223) field for description |
| [436](tags/436-UnderlyingContractMultiplier.md) | [UnderlyingContractMultiplier](tags/436-UnderlyingContractMultiplier.md) | Underlying security's ContractMultiplier. See ContractMultiplier (231) field for description |
| [437](tags/437-ContraTradeQty.md) | [ContraTradeQty](tags/437-ContraTradeQty.md) | Quantity traded with the ContraBroker <375>. |
| [438](tags/438-ContraTradeTime.md) | [ContraTradeTime](tags/438-ContraTradeTime.md) | Identifes the time of the trade with the ContraBroker <375>. Always expressed in UTC (Universal Time Coordinated, also known as "GMT"). |
| [439](tags/439-ClearingFirm-replaced.md) | [ClearingFirm (replaced)](tags/439-ClearingFirm-replaced.md) | No longer used as of FIX 4.3. Included here for reference to prior versions. |
| [440](tags/440-ClearingAccount-replaced.md) | [ClearingAccount (replaced)](tags/440-ClearingAccount-replaced.md) | No longer used as of FIX 4.3. Included here for reference to prior versions. |
| [441](tags/441-LiquidityNumSecurities.md) | [LiquidityNumSecurities](tags/441-LiquidityNumSecurities.md) | Number of Securites between LiquidityPctLow <402> and LiquidityPctHigh <403> in Currency <15>. |
| [442](tags/442-MultiLegReportingType.md) | [MultiLegReportingType](tags/442-MultiLegReportingType.md) | Used to indicate what an Execution Report <8> represents (e.g. used with multi-leg securities, such as option strategies, spreads, etc.). |
| [443](tags/443-StrikeTime.md) | [StrikeTime](tags/443-StrikeTime.md) | The time at which current market prices are used to determine the value of a basket. |
| [444](tags/444-ListStatusText.md) | [ListStatusText](tags/444-ListStatusText.md) | Free format text string related to List Status <N>. |
| [445](tags/445-EncodedListStatusTextLen.md) | [EncodedListStatusTextLen](tags/445-EncodedListStatusTextLen.md) | Byte length of encoded (non-ASCII characters) EncodedListStatusText (446) field. |
| [446](tags/446-EncodedListStatusText.md) | [EncodedListStatusText](tags/446-EncodedListStatusText.md) | Encoded (non-ASCII characters) representation of the ListStatusText (444) field in the encoded format specified via the MessageEncoding (347) field. If used, the ASCII (English) representation should also be specified in the ListStatusText (444) field. |
| [447](tags/447-PartyIDSource.md) | [PartyIDSource](tags/447-PartyIDSource.md) | Identifies class or source of the PartyID (448) value. Required if PartyID (448) is specified. Note: applicable values depend upon PartyRole (452) specified. |
| [448](tags/448-PartyID.md) | [PartyID](tags/448-PartyID.md) | Party identifier/code. See PartyIDSource <447> and PartyRole <452>. |
| [449](tags/449-TotalVolumeTradedDate-replaced.md) | [TotalVolumeTradedDate (replaced)](tags/449-TotalVolumeTradedDate-replaced.md) | No longer used as of FIX 4.4. Included here for reference to prior versions. |
| [450](tags/450-TotalVolumeTraded-Time-replaced.md) | [TotalVolumeTraded Time (replaced)](tags/450-TotalVolumeTraded-Time-replaced.md) | No longer used as of FIX 4.4. Included here for reference to prior versions. |
| [451](tags/451-NetChgPrevDay.md) | [NetChgPrevDay](tags/451-NetChgPrevDay.md) | Net change from previous day's closing price vs. last traded price. |
| [452](tags/452-PartyRole.md) | [PartyRole](tags/452-PartyRole.md) | Identifies the type or role of the PartyID (448) specified. |
| [453](tags/453-NoPartyIDs.md) | [NoPartyIDs](tags/453-NoPartyIDs.md) | Number of PartyID <448>, PartyIDSource <447>, and PartyRole <452> entries. |
| [454](tags/454-NoSecurityAltID.md) | [NoSecurityAltID](tags/454-NoSecurityAltID.md) | Number of SecurityAltID (455) entries. |
| [455](tags/455-SecurityAltID.md) | [SecurityAltID](tags/455-SecurityAltID.md) | Alternate Security identifier value for this security of SecurityAltIDSource <456> type (e.g. CUSIP, SEDOL, ISIN, etc). Requires SecurityAltIDSource <456>. |
| [456](tags/456-SecurityAltIDSource.md) | [SecurityAltIDSource](tags/456-SecurityAltIDSource.md) | Identifies class or source of the SecurityAltID (455) value. Required if SecurityAltID (455) is specified. |
| [457](tags/457-NoUnderlyingSecurityAltID.md) | [NoUnderlyingSecurityAltID](tags/457-NoUnderlyingSecurityAltID.md) | Number of UnderlyingSecurityAltID (458) entries. |
| [458](tags/458-UnderlyingSecurityAltID.md) | [UnderlyingSecurityAltID](tags/458-UnderlyingSecurityAltID.md) | Alternate Security identifier value for this underlying security of UnderlyingSecurityAltIDSource <459> type (e.g. CUSIP, SEDOL, ISIN, etc). Requires UnderlyingSecurityAltIDSource <459>. |
| [459](tags/459-UnderlyingSecurityAltIDSource.md) | [UnderlyingSecurityAltIDSource](tags/459-UnderlyingSecurityAltIDSource.md) | Identifies class or source of the UnderlyingSecurityAltID (458) value. Required if UnderlyingSecurityAltID (458) is specified. |
| [460](tags/460-Product.md) | [Product](tags/460-Product.md) | Indicates the type of product the security is associated with. See also the CFICode (461) and SecurityType (167) fields. |
| [461](tags/461-CFICode.md) | [CFICode](tags/461-CFICode.md) | Indicates the type of security using ISO 10962 standard, Classification of Financial Instruments (CFI code) values. ISO 10962 is maintained by ANNA (Association of National Numbering Agencies) acting as Registration Authority. See Appendix 6-B: FIX Fields Based Upon Other Standards. See also the Product <460> and SecurityType <167> fields. It is recommended that CFICode <461> be used instead of SecurityType <167> for non-Fixed Income instruments. |
| [462](tags/462-UnderlyingProduct.md) | [UnderlyingProduct](tags/462-UnderlyingProduct.md) | Underlying security's Product. |
| [463](tags/463-UnderlyingCFICode.md) | [UnderlyingCFICode](tags/463-UnderlyingCFICode.md) | Underlying security's CFICode. |
| [464](tags/464-TestMessageIndicator.md) | [TestMessageIndicator](tags/464-TestMessageIndicator.md) | Indicates whether or not this FIX Session is a "test" vs. "production" connection. Useful for preventing "accidents". |
| [465](tags/465-QuantityType.md) | [QuantityType](tags/465-QuantityType.md) | Designates the type of quantities (e.g. OrderQty (38) ) specified. Used for MBS and TIPS Fixed Income security types. |
| [466](tags/466-BookingRefID.md) | [BookingRefID](tags/466-BookingRefID.md) | Common reference passed to a post-trade booking process (e.g. industry matching utility). |
| [467](tags/467-IndividualAllocID.md) | [IndividualAllocID](tags/467-IndividualAllocID.md) | Unique identifier for a specific NoAllocs <78> repeating group instance (e.g. for an AllocAccount <79>). |
| [468](tags/468-RoundingDirection.md) | [RoundingDirection](tags/468-RoundingDirection.md) | Specifies which direction to round For CIV - indicates whether or not the quantity of shares/units is to be rounded and in which direction where CashOrderQty (152) or (for CIV only) OrderPercent (516) are specified on an order. |
| [469](tags/469-RoundingModulus.md) | [RoundingModulus](tags/469-RoundingModulus.md) | For CIV - a float value indicating the value to which rounding is required. |
| [470](tags/470-CountryOfIssue.md) | [CountryOfIssue](tags/470-CountryOfIssue.md) | ISO Country <421> code of instrument issue (e.g. the country portion typically used in ISIN). Can be used in conjunction with non-ISIN SecurityID <48> (e.g. CUSIP for Municipal Bonds without ISIN) to provide uniqueness. |
| [471](tags/471-StateOrProvinceOfIssue.md) | [StateOrProvinceOfIssue](tags/471-StateOrProvinceOfIssue.md) | A two-character state or province abbreviation. |
| [472](tags/472-LocaleOfIssue.md) | [LocaleOfIssue](tags/472-LocaleOfIssue.md) | Identifies the locale. For Municipal Security Issuers other than state or province. Refer to http://www.atmos.albany.edu/cgi/stagrep-cgi |
| [473](tags/473-NoRegistDtls.md) | [NoRegistDtls](tags/473-NoRegistDtls.md) | The number of registration details on a Registration Instructions <o> message. |
| [474](tags/474-MailingDtls.md) | [MailingDtls](tags/474-MailingDtls.md) | Set of Correspondence address details, possibly including phone, fax, etc. |
| [475](tags/475-InvestorCountryOfResidence.md) | [InvestorCountryOfResidence](tags/475-InvestorCountryOfResidence.md) | The ISO 3166 Country code (2 character) identifying which country the beneficial investor is resident for tax purposes. |
| [476](tags/476-PaymentRef.md) | [PaymentRef](tags/476-PaymentRef.md) | "Settlement Payment Reference" - A free format Payment reference to assist with reconciliation, e.g. a Client and/or Order ID number. |
| [477](tags/477-DistribPaymentMethod.md) | [DistribPaymentMethod](tags/477-DistribPaymentMethod.md) | A code identifying the payment method for a (fractional) distribution. |
| [478](tags/478-CashDistribCurr.md) | [CashDistribCurr](tags/478-CashDistribCurr.md) | Specifies currency to be use for Cash Distributions. See Appendix 6-A: Valid Currency Codes. |
| [479](tags/479-CommCurrency.md) | [CommCurrency](tags/479-CommCurrency.md) | Specifies currency to be use for Commission (12) if the Commission currency is different from the Deal Currency - see Appendix 6-A: "Valid Currency Codes" of FIX Specification. |
| [480](tags/480-CancellationRights.md) | [CancellationRights](tags/480-CancellationRights.md) | For CIV - A one character code identifying whether Cancellation rights/Cooling off period applies. |
| [481](tags/481-MoneyLaunderingStatus.md) | [MoneyLaunderingStatus](tags/481-MoneyLaunderingStatus.md) | A one character code identifying Money laundering status. |
| [482](tags/482-MailingInst.md) | [MailingInst](tags/482-MailingInst.md) | Free format text to specify mailing instruction requirements, e.g. "no third party mailings". |
| [483](tags/483-TransBkdTime.md) | [TransBkdTime](tags/483-TransBkdTime.md) | For CIV A date and time stamp to indicate the time a CIV order was booked by the fund manager. |
| [484](tags/484-ExecPriceType.md) | [ExecPriceType](tags/484-ExecPriceType.md) | For CIV - Identifies how the execution price LastPx (31) was calculated from the fund unit/share price(s) calculated at the fund valuation point. |
| [485](tags/485-ExecPriceAdjustment.md) | [ExecPriceAdjustment](tags/485-ExecPriceAdjustment.md) | For CIV the amount or percentage by which the fund unit/share price was adjusted, as indicated by ExecPriceType (484) |
| [486](tags/486-DateOfBirth.md) | [DateOfBirth](tags/486-DateOfBirth.md) | The date of birth applicable to the individual, e.g. required to open some types of tax-exempt account. |
| [487](tags/487-TradeReportTransType.md) | [TradeReportTransType](tags/487-TradeReportTransType.md) | Identifies Trade Report message transaction type. |
| [488](tags/488-CardHolderName.md) | [CardHolderName](tags/488-CardHolderName.md) | The name of the payment card holder as specified on the card being used for payment. |
| [489](tags/489-CardNumber.md) | [CardNumber](tags/489-CardNumber.md) | The number of the payment card as specified on the card being used for payment. |
| [490](tags/490-CardExpDate.md) | [CardExpDate](tags/490-CardExpDate.md) | The expiry date of the payment card as specified on the card being used for payment. |
| [491](tags/491-CardIssNum.md) | [CardIssNum](tags/491-CardIssNum.md) | The issue number of the payment card as specified on the card being used for payment. This is only applicable to certain types of card. |
| [492](tags/492-PaymentMethod.md) | [PaymentMethod](tags/492-PaymentMethod.md) | A code identifying the Settlement payment method. |
| [493](tags/493-RegistAcctType.md) | [RegistAcctType](tags/493-RegistAcctType.md) | For CIV - a fund manager-defined code identifying which of the fund manager's account types is required. |
| [494](tags/494-Designation.md) | [Designation](tags/494-Designation.md) | Free format text defining the designation to be associated with a holding on the register. Used to identify assets of a specific underlying investor using a common registration, e.g. a broker's nominee or street name. |
| [495](tags/495-TaxAdvantageType.md) | [TaxAdvantageType](tags/495-TaxAdvantageType.md) | For CIV - a code identifying the type of tax exempt account in which purchased shares/units are to be held. |
| [496](tags/496-RegistRejReasonText.md) | [RegistRejReasonText](tags/496-RegistRejReasonText.md) | Text indicating reason(s) why a Registration Instructions <o> has been rejected. |
| [497](tags/497-FundRenewWaiv.md) | [FundRenewWaiv](tags/497-FundRenewWaiv.md) | A one character code identifying whether the Fund based renewal commission is to be waived. |
| [498](tags/498-CashDistribAgentName.md) | [CashDistribAgentName](tags/498-CashDistribAgentName.md) | Name of local agent bank if for cash distributions |
| [499](tags/499-CashDistribAgentCode.md) | [CashDistribAgentCode](tags/499-CashDistribAgentCode.md) | BIC (Bank Identification Code - Swift managed) code of agent bank for cash distributions. |
| [500](tags/500-CashDistribAgentAcctNumber.md) | [CashDistribAgentAcctNumber](tags/500-CashDistribAgentAcctNumber.md) | Account <1> number at agent bank for distributions. |
| [501](tags/501-CashDistribPayRef.md) | [CashDistribPayRef](tags/501-CashDistribPayRef.md) | Free format Payment reference to assist with reconciliation of distributions. |
| [502](tags/502-CashDistribAgentAcctName.md) | [CashDistribAgentAcctName](tags/502-CashDistribAgentAcctName.md) | Name of account at agent bank for distributions. |
| [503](tags/503-CardStartDate.md) | [CardStartDate](tags/503-CardStartDate.md) | The start date of the card as specified on the card being used for payment. |
| [504](tags/504-PaymentDate.md) | [PaymentDate](tags/504-PaymentDate.md) | The date written on a cheque or date payment should be submitted to the relevant clearing system. |
| [505](tags/505-PaymentRemitterID.md) | [PaymentRemitterID](tags/505-PaymentRemitterID.md) | Identifies sender of a payment, e.g. the payment remitter or a customer reference number. |
| [506](tags/506-RegistStatus.md) | [RegistStatus](tags/506-RegistStatus.md) | Registration status as returned by the broker or (for CIV) the fund manager:. |
| [507](tags/507-RegistRejReasonCode.md) | [RegistRejReasonCode](tags/507-RegistRejReasonCode.md) | Reason(s) why Registration Instructions <o> has been rejected. |
| [508](tags/508-RegistRefID.md) | [RegistRefID](tags/508-RegistRefID.md) | Reference identifier for the RegistID <513> with 'Cancel' and 'Replace' RegistTransType <514> transaction types. |
| [509](tags/509-RegistDtls.md) | [RegistDtls](tags/509-RegistDtls.md) | Set of Registration name and address details, possibly including phone, fax etc. |
| [510](tags/510-NoDistribInsts.md) | [NoDistribInsts](tags/510-NoDistribInsts.md) | The number of Distribution Instructions on a Registration Instructions <o> message. |
| [511](tags/511-RegistEmail.md) | [RegistEmail](tags/511-RegistEmail.md) | Email address relating to Registration name and address details |
| [512](tags/512-DistribPercentage.md) | [DistribPercentage](tags/512-DistribPercentage.md) | The amount of each distribution to go to this beneficiary, expressed as a percentage |
| [513](tags/513-RegistID.md) | [RegistID](tags/513-RegistID.md) | Unique identifier of the registration details as assigned by institution or intermediary. |
| [514](tags/514-RegistTransType.md) | [RegistTransType](tags/514-RegistTransType.md) | Identifies Registration Instructions <o> transaction type. |
| [515](tags/515-ExecValuationPoint.md) | [ExecValuationPoint](tags/515-ExecValuationPoint.md) | For CIV - a date and time stamp to indicate the fund valuation point with respect to which a order was priced by the fund manager. |
| [516](tags/516-OrderPercent.md) | [OrderPercent](tags/516-OrderPercent.md) | For CIV specifies the approximate order quantity desired. For a CIV Sale it specifies percentage of investor's total holding to be sold. For a CIV switch/exchange it specifies percentage of investor's cash realised from sales to be re-invested. The executing broker, intermediary or fund manager is responsible for converting and calculating OrderQty (38) in shares/units for subsequent messages. |
| [517](tags/517-OwnershipType.md) | [OwnershipType](tags/517-OwnershipType.md) | The relationship between Registration parties. |
| [518](tags/518-NoContAmts.md) | [NoContAmts](tags/518-NoContAmts.md) | The number of Contract Amount details on an Execution Report (8) message |
| [519](tags/519-ContAmtType.md) | [ContAmtType](tags/519-ContAmtType.md) | Type of ContAmtValue <520>. |
| [520](tags/520-ContAmtValue.md) | [ContAmtValue](tags/520-ContAmtValue.md) | Value of Contract Amount, e.g. a financial amount or percentage as indicated by ContAmtType <519>. |
| [521](tags/521-ContAmtCurr.md) | [ContAmtCurr](tags/521-ContAmtCurr.md) | Specifies currency for the Contract amount if different from the Deal Currency - see " Appendix 6-A; Valid Currency Codes ". |
| [522](tags/522-OwnerType.md) | [OwnerType](tags/522-OwnerType.md) | Identifies the type of owner. |
| [523](tags/523-PartySubID.md) | [PartySubID](tags/523-PartySubID.md) | Sub-identifier (e.g. Clearing Account for PartyRole <452>=Clearing Firm, Locate ID # for PartyRole <452>=Locate/Lending Firm, etc). Not required when using PartyID <448>, PartyIDSource <447>, and PartyRole <452>. |
| [524](tags/524-NestedPartyID.md) | [NestedPartyID](tags/524-NestedPartyID.md) | PartyID value within a nested repeating group. |
| [525](tags/525-NestedPartyIDSource.md) | [NestedPartyIDSource](tags/525-NestedPartyIDSource.md) | PartyIDSource value within a nested repeating group. |
| [526](tags/526-SecondaryClOrdID.md) | [SecondaryClOrdID](tags/526-SecondaryClOrdID.md) | Assigned by the party which originates the order. Can be used to provide the ClOrdID (11) used by an exchange or executing system. |
| [527](tags/527-SecondaryExecID.md) | [SecondaryExecID](tags/527-SecondaryExecID.md) | Assigned by the party which accepts the order. Can be used to provide the ExecID (17) used by an exchange or executing system. |
| [528](tags/528-OrderCapacity.md) | [OrderCapacity](tags/528-OrderCapacity.md) | Designates the capacity of the firm placing the order. |
| [529](tags/529-OrderRestrictions.md) | [OrderRestrictions](tags/529-OrderRestrictions.md) | Restrictions associated with an order. If more than one restriction is applicable to an order, this field can contain multiple instructions separated by space. |
| [530](tags/530-MassCancelRequestType.md) | [MassCancelRequestType](tags/530-MassCancelRequestType.md) | Specifies scope of Order Mass Cancel Request <q>. |
| [531](tags/531-MassCancelResponse.md) | [MassCancelResponse](tags/531-MassCancelResponse.md) | Specifies the action taken by counterparty order handling system as a result of the Order Mass Cancel Request <q>. |
| [532](tags/532-MassCancelRejectReason.md) | [MassCancelRejectReason](tags/532-MassCancelRejectReason.md) | Reason Order Mass Cancel Request <q> was rejected. |
| [533](tags/533-TotalAffectedOrders.md) | [TotalAffectedOrders](tags/533-TotalAffectedOrders.md) | Total number of orders affected by Order Mass Cancel Request <q>. |
| [534](tags/534-NoAffectedOrders.md) | [NoAffectedOrders](tags/534-NoAffectedOrders.md) | Number of affected orders in the repeating group of order ids. |
| [535](tags/535-AffectedOrderID.md) | [AffectedOrderID](tags/535-AffectedOrderID.md) | OrderID <37> of an order affected by a Mass Cancel Request <q>. |
| [536](tags/536-AffectedSecondaryOrderID.md) | [AffectedSecondaryOrderID](tags/536-AffectedSecondaryOrderID.md) | SecondaryOrderID <198> of an order affected by a Mass Cancel Request <q>. |
| [537](tags/537-QuoteType.md) | [QuoteType](tags/537-QuoteType.md) | Identifies the type of quote. |
| [538](tags/538-NestedPartyRole.md) | [NestedPartyRole](tags/538-NestedPartyRole.md) | PartyRole value within a nested repeating group. |
| [539](tags/539-NoNestedPartyIDs.md) | [NoNestedPartyIDs](tags/539-NoNestedPartyIDs.md) | Number of NestedPartyID <524>, NestedPartyIDSource <525>, and NestedPartyRole <538> entries. |
| [540](tags/540-TotalAccruedInterestAmt.md) | [TotalAccruedInterestAmt](tags/540-TotalAccruedInterestAmt.md) | DEPRECATED FIELD - See Appendix 6-E: 1.Deprecated Field: TotalAccruedInterestAmt (tag 540) [deprecated in FIX 4.4] . |
| [541](tags/541-MaturityDate.md) | [MaturityDate](tags/541-MaturityDate.md) | Date of maturity. |
| [542](tags/542-UnderlyingMaturityDate.md) | [UnderlyingMaturityDate](tags/542-UnderlyingMaturityDate.md) | Underlying security's maturity date. See MaturityDate (541) field for description |
| [543](tags/543-InstrRegistry.md) | [InstrRegistry](tags/543-InstrRegistry.md) | The location at which records of ownership are maintained for this instrument, and at which ownership changes must be recorded. |
| [544](tags/544-CashMargin.md) | [CashMargin](tags/544-CashMargin.md) | Identifies whether an order is a margin order or a non-margin order. This is primarily used when sending orders to Japanese exchanges to indicate sell margin or buy to cover. The same tag could be assigned also by buy-side to indicate the intent to sell or buy margin and the sell-side to accept or reject (base on some validation criteria) the margin request. |
| [545](tags/545-NestedPartySubID.md) | [NestedPartySubID](tags/545-NestedPartySubID.md) | PartySubID value within a nested repeating group. |
| [546](tags/546-Scope.md) | [Scope](tags/546-Scope.md) | Defines the scope of a data element. |
| [547](tags/547-MDImplicitDelete.md) | [MDImplicitDelete](tags/547-MDImplicitDelete.md) | Defines how a server handles distribution of a truncated book. Defaults to broker option. |
| [548](tags/548-CrossID.md) | [CrossID](tags/548-CrossID.md) | Identifier for a cross order. Must be unique during a given trading day. Recommend that firms use the order date as part of the CrossID <548> for Good Till Cancel (GT) orders. |
| [549](tags/549-CrossType.md) | [CrossType](tags/549-CrossType.md) | Type of cross being submitted to a market |
| [550](tags/550-CrossPrioritization.md) | [CrossPrioritization](tags/550-CrossPrioritization.md) | Indicates if one side or the other of a cross order should be prioritized. |
| [551](tags/551-OrigCrossID.md) | [OrigCrossID](tags/551-OrigCrossID.md) | CrossID <548> of the previous cross order (NOT the initial cross order of the day) as assigned by the institution, used to identify the previous cross order in Cross Order Cancel Request <u> and Cross Order Cancel/Replace Request <t>. |
| [552](tags/552-NoSides.md) | [NoSides](tags/552-NoSides.md) | Number of Side (54) repeating group instances. |
| [553](tags/553-Username.md) | [Username](tags/553-Username.md) | Userid or username. |
| [554](tags/554-Password.md) | [Password](tags/554-Password.md) | Password or passphrase. |
| [555](tags/555-NoLegs.md) | [NoLegs](tags/555-NoLegs.md) | Number of <InstrumentLeg> repeating group instances. |
| [556](tags/556-LegCurrency.md) | [LegCurrency](tags/556-LegCurrency.md) | Currency associated with a particular Leg's quantity |
| [557](tags/557-TotNoSecurityTypes.md) | [TotNoSecurityTypes](tags/557-TotNoSecurityTypes.md) | Indicates total number of security types in the event that multiple Security Type messages are used to return results. |
| [558](tags/558-NoSecurityTypes.md) | [NoSecurityTypes](tags/558-NoSecurityTypes.md) | Number of SecurityType <167> repeating group instances. |
| [559](tags/559-SecurityListRequestType.md) | [SecurityListRequestType](tags/559-SecurityListRequestType.md) | Identifies the type/criteria of Security List Request <x>. |
| [560](tags/560-SecurityRequestResult.md) | [SecurityRequestResult](tags/560-SecurityRequestResult.md) | The results returned to a Security Request message. |
| [561](tags/561-RoundLot.md) | [RoundLot](tags/561-RoundLot.md) | The trading lot size of a security |
| [562](tags/562-MinTradeVol.md) | [MinTradeVol](tags/562-MinTradeVol.md) | The minimum trading volume for a security |
| [563](tags/563-MultiLegRptTypeReq.md) | [MultiLegRptTypeReq](tags/563-MultiLegRptTypeReq.md) | Indicates the method of execution reporting requested by issuer of the order. |
| [564](tags/564-LegPositionEffect.md) | [LegPositionEffect](tags/564-LegPositionEffect.md) | PositionEffect for leg of a multileg |
| [565](tags/565-LegCoveredOrUncovered.md) | [LegCoveredOrUncovered](tags/565-LegCoveredOrUncovered.md) | CoveredOrUncovered for leg of a multileg |
| [566](tags/566-LegPrice.md) | [LegPrice](tags/566-LegPrice.md) | Price for leg of a multileg |
| [567](tags/567-TradSesStatusRejReason.md) | [TradSesStatusRejReason](tags/567-TradSesStatusRejReason.md) | Indicates the reason a Trading Session Status Request <g> was rejected. |
| [568](tags/568-TradeRequestID.md) | [TradeRequestID](tags/568-TradeRequestID.md) | Trade Capture Report Request <AD> ID. |
| [569](tags/569-TradeRequestType.md) | [TradeRequestType](tags/569-TradeRequestType.md) | Type of Trade Capture Report <AE>. |
| [570](tags/570-PreviouslyReported.md) | [PreviouslyReported](tags/570-PreviouslyReported.md) | Indicates if the trade capture report was previously reported to the counterparty |
| [571](tags/571-TradeReportID.md) | [TradeReportID](tags/571-TradeReportID.md) | Unique identifier of trade capture report. |
| [572](tags/572-TradeReportRefID.md) | [TradeReportRefID](tags/572-TradeReportRefID.md) | Reference identifier used with CANCEL and REPLACE transaction types. |
| [573](tags/573-MatchStatus.md) | [MatchStatus](tags/573-MatchStatus.md) | The status of this trade with respect to matching or comparison. |
| [574](tags/574-MatchType.md) | [MatchType](tags/574-MatchType.md) | The point in the matching process at which this trade was matched. |
| [575](tags/575-OddLot.md) | [OddLot](tags/575-OddLot.md) | This trade is to be treated as an odd lot. If this field is not specified, the default will be "N" |
| [576](tags/576-NoClearingInstructions.md) | [NoClearingInstructions](tags/576-NoClearingInstructions.md) | Number of clearing instructions |
| [577](tags/577-ClearingInstruction.md) | [ClearingInstruction](tags/577-ClearingInstruction.md) | Eligibility of this trade for clearing and central counterparty processing. |
| [578](tags/578-TradeInputSource.md) | [TradeInputSource](tags/578-TradeInputSource.md) | Type of input device or system from which the trade was entered. |
| [579](tags/579-TradeInputDevice.md) | [TradeInputDevice](tags/579-TradeInputDevice.md) | Specific device number, terminal number or station where trade was entered |
| [580](tags/580-NoDates.md) | [NoDates](tags/580-NoDates.md) | Number of Date fields provided in date range |
| [581](tags/581-AccountType.md) | [AccountType](tags/581-AccountType.md) | Type of Account <1> associated with an order. |
| [582](tags/582-CustOrderCapacity.md) | [CustOrderCapacity](tags/582-CustOrderCapacity.md) | Capacity of customer placing the order. |
| [583](tags/583-ClOrdLinkID.md) | [ClOrdLinkID](tags/583-ClOrdLinkID.md) | Permits order originators to tie together groups of orders in which trades resulting from orders are associated for a specific purpose, for example the calculation of average execution price for a customer or to associate lists submitted to a broker as waves of a larger program trade. |
| [584](tags/584-MassStatusReqID.md) | [MassStatusReqID](tags/584-MassStatusReqID.md) | Value assigned by issuer of Mass Status Request <AF> to uniquely identify the request. |
| [585](tags/585-MassStatusReqType.md) | [MassStatusReqType](tags/585-MassStatusReqType.md) | Mass Status Request <AF> Type. |
| [586](tags/586-OrigOrdModTime.md) | [OrigOrdModTime](tags/586-OrigOrdModTime.md) | The most recent (or current) modification TransactTime (60) reported on an Execution Report (8) for the order. |
| [587](tags/587-LegSettlType.md) | [LegSettlType](tags/587-LegSettlType.md) | Refer to values for SettlType (63) |
| [588](tags/588-LegSettlDate.md) | [LegSettlDate](tags/588-LegSettlDate.md) | Refer to description for SettlDate (64) |
| [589](tags/589-DayBookingInst.md) | [DayBookingInst](tags/589-DayBookingInst.md) | Indicates whether or not automatic booking can occur. |
| [590](tags/590-BookingUnit.md) | [BookingUnit](tags/590-BookingUnit.md) | Indicates what constitutes a bookable unit. |
| [591](tags/591-PreallocMethod.md) | [PreallocMethod](tags/591-PreallocMethod.md) | Indicates the method of preallocation. |
| [592](tags/592-UnderlyingCountryOfIssue.md) | [UnderlyingCountryOfIssue](tags/592-UnderlyingCountryOfIssue.md) | Underlying security's CountryOfIssue. See CountryOfIssue (470) field for description |
| [593](tags/593-UnderlyingStateOrProvinceOfIssue.md) | [UnderlyingStateOrProvinceOfIssue](tags/593-UnderlyingStateOrProvinceOfIssue.md) | Underlying security's StateOrProvinceOfIssue. See StateOrProvinceOfIssue (471) field for description |
| [594](tags/594-UnderlyingLocaleOfIssue.md) | [UnderlyingLocaleOfIssue](tags/594-UnderlyingLocaleOfIssue.md) | Underlying security's LocaleOfIssue. See LocaleOfIssue (472) field for description |
| [595](tags/595-UnderlyingInstrRegistry.md) | [UnderlyingInstrRegistry](tags/595-UnderlyingInstrRegistry.md) | Underlying security's InstrRegistry. See InstrRegistry (543) field for description |
| [596](tags/596-LegCountryOfIssue.md) | [LegCountryOfIssue](tags/596-LegCountryOfIssue.md) | Multileg instrument's individual leg security's CountryOfIssue. See CountryOfIssue (470) field for description |
| [597](tags/597-LegStateOrProvinceOfIssue.md) | [LegStateOrProvinceOfIssue](tags/597-LegStateOrProvinceOfIssue.md) | Multileg instrument's individual leg security's StateOrProvinceOfIssue. See StateOrProvinceOfIssue (471) field for description |
| [598](tags/598-LegLocaleOfIssue.md) | [LegLocaleOfIssue](tags/598-LegLocaleOfIssue.md) | Multileg instrument's individual leg security's LocaleOfIssue. See LocaleOfIssue (472) field for description |
| [599](tags/599-LegInstrRegistry.md) | [LegInstrRegistry](tags/599-LegInstrRegistry.md) | Multileg instrument's individual leg security's InstrRegistry. See InstrRegistry (543) field for description |
| [600](tags/600-LegSymbol.md) | [LegSymbol](tags/600-LegSymbol.md) | Multileg instrument's individual security's Symbol. |
| [601](tags/601-LegSymbolSfx.md) | [LegSymbolSfx](tags/601-LegSymbolSfx.md) | Multileg instrument's individual security's SymbolSfx. See SymbolSfx (65) field for description |
| [602](tags/602-LegSecurityID.md) | [LegSecurityID](tags/602-LegSecurityID.md) | Multileg instrument's individual security's SecurityID. See SecurityID (48) field for description |
| [603](tags/603-LegSecurityIDSource.md) | [LegSecurityIDSource](tags/603-LegSecurityIDSource.md) | Multileg instrument's individual security's SecurityIDSource. See SecurityIDSource (22) field for description |
| [604](tags/604-NoLegSecurityAltID.md) | [NoLegSecurityAltID](tags/604-NoLegSecurityAltID.md) | Multileg instrument's individual security's NoSecurityAltID. See NoSecurityAltID (454) field for description |
| [605](tags/605-LegSecurityAltID.md) | [LegSecurityAltID](tags/605-LegSecurityAltID.md) | Multileg instrument's individual security's SecurityAltID. See SecurityAltID (455) field for description |
| [606](tags/606-LegSecurityAltIDSource.md) | [LegSecurityAltIDSource](tags/606-LegSecurityAltIDSource.md) | Multileg instrument's individual security's SecurityAltIDSource. See SecurityAltIDSource (456) field for description |
| [607](tags/607-LegProduct.md) | [LegProduct](tags/607-LegProduct.md) | Multileg instrument's individual security's Product. See Product (460) field for description |
| [608](tags/608-LegCFICode.md) | [LegCFICode](tags/608-LegCFICode.md) | Multileg instrument's individual security's CFICode. See CFICode (461) field for description |
| [609](tags/609-LegSecurityType.md) | [LegSecurityType](tags/609-LegSecurityType.md) | Multileg instrument's individual security's SecurityType. See SecurityType (167) field for description |
| [610](tags/610-LegMaturityMonthYear.md) | [LegMaturityMonthYear](tags/610-LegMaturityMonthYear.md) | Multileg instrument's individual security's MaturityMonthYear. See MaturityMonthYear (200) field for description |
| [611](tags/611-LegMaturityDate.md) | [LegMaturityDate](tags/611-LegMaturityDate.md) | Multileg instrument's individual security's MaturityDate. See MaturityDate (541) field for description |
| [612](tags/612-LegStrikePrice.md) | [LegStrikePrice](tags/612-LegStrikePrice.md) | Multileg instrument's individual security's StrikePrice. See StrikePrice (202) field for description |
| [613](tags/613-LegOptAttribute.md) | [LegOptAttribute](tags/613-LegOptAttribute.md) | Multileg instrument's individual security's OptAttribute. See OptAttribute (206) field for description |
| [614](tags/614-LegContractMultiplier.md) | [LegContractMultiplier](tags/614-LegContractMultiplier.md) | Multileg instrument's individual security's ContractMultiplier. See ContractMultiplier (231) field for description |
| [615](tags/615-LegCouponRate.md) | [LegCouponRate](tags/615-LegCouponRate.md) | Multileg instrument's individual security's CouponRate. See CouponRate (223) field for description |
| [616](tags/616-LegSecurityExchange.md) | [LegSecurityExchange](tags/616-LegSecurityExchange.md) | Multileg instrument's individual security's SecurityExchange. See SecurityExchange (207) field for description |
| [617](tags/617-LegIssuer.md) | [LegIssuer](tags/617-LegIssuer.md) | Multileg instrument's individual security's Issuer. |
| [618](tags/618-EncodedLegIssuerLen.md) | [EncodedLegIssuerLen](tags/618-EncodedLegIssuerLen.md) | Multileg instrument's individual security's EncodedIssuerLen. See EncodedIssuerLen (348) field for description |
| [619](tags/619-EncodedLegIssuer.md) | [EncodedLegIssuer](tags/619-EncodedLegIssuer.md) | Multileg instrument's individual security's EncodedIssuer. See EncodedIssuer (349) field for description |
| [620](tags/620-LegSecurityDesc.md) | [LegSecurityDesc](tags/620-LegSecurityDesc.md) | Multileg instrument's individual security's SecurityDesc. See SecurityDesc (107) field for description |
| [621](tags/621-EncodedLegSecurityDescLen.md) | [EncodedLegSecurityDescLen](tags/621-EncodedLegSecurityDescLen.md) | Multileg instrument's individual security's EncodedSecurityDescLen. See EncodedSecurityDescLen (350) field for description |
| [622](tags/622-EncodedLegSecurityDesc.md) | [EncodedLegSecurityDesc](tags/622-EncodedLegSecurityDesc.md) | Multileg instrument's individual security's EncodedSecurityDesc. See EncodedSecurityDesc (351) field for description |
| [623](tags/623-LegRatioQty.md) | [LegRatioQty](tags/623-LegRatioQty.md) | The ratio of quantity for this individual leg relative to the entire multileg security. |
| [624](tags/624-LegSide.md) | [LegSide](tags/624-LegSide.md) | The side of this individual leg (multileg security). See Side (54) field for description and values |
| [625](tags/625-TradingSessionSubID.md) | [TradingSessionSubID](tags/625-TradingSessionSubID.md) | Optional market assigned sub identifier for a trading session. Usage is determined by market or counterparties. |
| [626](tags/626-AllocType.md) | [AllocType](tags/626-AllocType.md) | Describes the specific type or purpose of an Allocation message (i.e. "Buyside Calculated"). |
| [627](tags/627-NoHops.md) | [NoHops](tags/627-NoHops.md) | Number of HopCompID (628) entries in repeating group. |
| [628](tags/628-HopCompID.md) | [HopCompID](tags/628-HopCompID.md) | Assigned value used to identify the third party firm which delivered a specific message either from the firm which originated the message or from another third party (if multiple "hops" are performed). It is recommended that this value be the SenderCompID (49) of the third party. |
| [629](tags/629-HopSendingTime.md) | [HopSendingTime](tags/629-HopSendingTime.md) | Time that HopCompID (628) sent the message. It is recommended that this value be the SendingTime (52) of the message sent by the third party. |
| [630](tags/630-HopRefID.md) | [HopRefID](tags/630-HopRefID.md) | Reference identifier assigned by HopCompID (628) associated with the message sent. It is recommended that this value be the MsgSeqNum (34) of the message sent by the third party. |
| [631](tags/631-MidPx.md) | [MidPx](tags/631-MidPx.md) | Mid price/rate |
| [632](tags/632-BidYield.md) | [BidYield](tags/632-BidYield.md) | Bid yield |
| [633](tags/633-MidYield.md) | [MidYield](tags/633-MidYield.md) | Mid yield |
| [634](tags/634-OfferYield.md) | [OfferYield](tags/634-OfferYield.md) | Offer yield |
| [635](tags/635-ClearingFeeIndicator.md) | [ClearingFeeIndicator](tags/635-ClearingFeeIndicator.md) | Indicates type of fee being assessed of the customer for trade executions at an exchange. Applicable for futures markets only at this time. |
| [636](tags/636-WorkingIndicator.md) | [WorkingIndicator](tags/636-WorkingIndicator.md) | Indicates if the order is currently being worked. Applicable only for OrdStatus <39> = 'New'. For open outcry markets this indicates that the order is being worked in the crowd. For electronic markets it indicates that the order has transitioned from a contingent order to a market order. |
| [637](tags/637-LegLastPx.md) | [LegLastPx](tags/637-LegLastPx.md) | Execution price assigned to a leg of a multileg instrument. See LastPx (31) field for description and values |
| [638](tags/638-PriorityIndicator.md) | [PriorityIndicator](tags/638-PriorityIndicator.md) | Indicates if a Cancel/Replace has caused an order to lose book priority. |
| [639](tags/639-PriceImprovement.md) | [PriceImprovement](tags/639-PriceImprovement.md) | Amount of price improvement. |
| [640](tags/640-Price2.md) | [Price2](tags/640-Price2.md) | Price of the future part of a F/X swap order. |
| [641](tags/641-LastForwardPoints2.md) | [LastForwardPoints2](tags/641-LastForwardPoints2.md) | F/X forward points of the future part of a F/X swap order added to LastSpotRate <194>. May be a negative value. |
| [642](tags/642-BidForwardPoints2.md) | [BidForwardPoints2](tags/642-BidForwardPoints2.md) | Bid F/X forward points of the future portion of a F/X swap quote added to spot rate. May be a negative value. |
| [643](tags/643-OfferForwardPoints2.md) | [OfferForwardPoints2](tags/643-OfferForwardPoints2.md) | Offer F/X forward points of the future portion of a F/X swap quote added to spot rate. May be a negative value. |
| [644](tags/644-RFQReqID.md) | [RFQReqID](tags/644-RFQReqID.md) | RFQ Request ID - used to identify an RFQ Request <AH>. |
| [645](tags/645-MktBidPx.md) | [MktBidPx](tags/645-MktBidPx.md) | Used to indicate the best bid in a market |
| [646](tags/646-MktOfferPx.md) | [MktOfferPx](tags/646-MktOfferPx.md) | Used to indicate the best offer in a market |
| [647](tags/647-MinBidSize.md) | [MinBidSize](tags/647-MinBidSize.md) | Used to indicate a minimum quantity for a bid. If this field is used the BidSize (134) field is interpreted as the maximum bid size |
| [648](tags/648-MinOfferSize.md) | [MinOfferSize](tags/648-MinOfferSize.md) | Used to indicate a minimum quantity for an offer. If this field is used the OfferSize (135) field is interpreted as the maximum offer size. |
| [649](tags/649-QuoteStatusReqID.md) | [QuoteStatusReqID](tags/649-QuoteStatusReqID.md) | Unique identifier for Quote Status Request <a>. |
| [650](tags/650-LegalConfirm.md) | [LegalConfirm](tags/650-LegalConfirm.md) | Indicates that this message is to serve as the final and legal confirmation. |
| [651](tags/651-UnderlyingLastPx.md) | [UnderlyingLastPx](tags/651-UnderlyingLastPx.md) | The calculated or traded price for the underlying instrument that corresponds to a derivative. Used for transactions that include the cash instrument and the derivative. |
| [652](tags/652-UnderlyingLastQty.md) | [UnderlyingLastQty](tags/652-UnderlyingLastQty.md) | The calculated or traded quantity for the underlying instrument that corresponds to a derivative. Used for transactions that include the cash instrument and the derivative. |
| [653](tags/653-SecDefStatus-replaced.md) | [SecDefStatus (replaced)](tags/653-SecDefStatus-replaced.md) | No longer used as of FIX 4.3. Included here for reference to prior versions. |
| [654](tags/654-LegRefID.md) | [LegRefID](tags/654-LegRefID.md) | Unique indicator for a specific leg. |
| [655](tags/655-ContraLegRefID.md) | [ContraLegRefID](tags/655-ContraLegRefID.md) | Unique indicator for a specific leg for the ContraBroker <375>. |
| [656](tags/656-SettlCurrBidFxRate.md) | [SettlCurrBidFxRate](tags/656-SettlCurrBidFxRate.md) | Foreign exchange rate used to compute the bid SettlCurrAmt (119) from Currency (15) to SettlCurrency (120) |
| [657](tags/657-SettlCurrOfferFxRate.md) | [SettlCurrOfferFxRate](tags/657-SettlCurrOfferFxRate.md) | Foreign exchange rate used to compute the offer SettlCurrAmt (119) from Currency (15) to SettlCurrency (120) |
| [658](tags/658-QuoteRequestRejectReason.md) | [QuoteRequestRejectReason](tags/658-QuoteRequestRejectReason.md) | Reason QuoteRequest <R> was rejected. |
| [659](tags/659-SideComplianceID.md) | [SideComplianceID](tags/659-SideComplianceID.md) | ID within repeating group of sides which is used to represent this transaction for compliance purposes (e.g. OATS reporting). |
| [660](tags/660-AcctIDSource.md) | [AcctIDSource](tags/660-AcctIDSource.md) | Used to identify the source of the Account (1) code. This is especially useful if the account is a new account that the Respondent may not have setup yet in their system. |
| [661](tags/661-AllocAcctIDSource.md) | [AllocAcctIDSource](tags/661-AllocAcctIDSource.md) | Used to identify the source of the AllocAccount <79> code. |
| [662](tags/662-BenchmarkPrice.md) | [BenchmarkPrice](tags/662-BenchmarkPrice.md) | Specifies the price of the benchmark. |
| [663](tags/663-BenchmarkPriceType.md) | [BenchmarkPriceType](tags/663-BenchmarkPriceType.md) | Identifies type of BenchmarkPrice <662>. |
| [664](tags/664-ConfirmID.md) | [ConfirmID](tags/664-ConfirmID.md) | Message reference for Confirmation <AK>. |
| [665](tags/665-ConfirmStatus.md) | [ConfirmStatus](tags/665-ConfirmStatus.md) | Identifies the status of the Confirmation <AK>. |
| [666](tags/666-ConfirmTransType.md) | [ConfirmTransType](tags/666-ConfirmTransType.md) | Identifies the Confirmation <AK> transaction type. |
| [667](tags/667-ContractSettlMonth.md) | [ContractSettlMonth](tags/667-ContractSettlMonth.md) | Specifies when the contract (i.e. MBS/TBA) will settle. |
| [668](tags/668-DeliveryForm.md) | [DeliveryForm](tags/668-DeliveryForm.md) | Identifies the form of delivery. |
| [669](tags/669-LastParPx.md) | [LastParPx](tags/669-LastParPx.md) | Last price expressed in percent-of-par. Conditionally required for Fixed Income trades when LastPx <31> is expressed in Yield, Spread, Discount or any other type (see PriceType <423>). |
| [670](tags/670-NoLegAllocs.md) | [NoLegAllocs](tags/670-NoLegAllocs.md) | Number of Allocations for the leg |
| [671](tags/671-LegAllocAccount.md) | [LegAllocAccount](tags/671-LegAllocAccount.md) | Allocation Account for the leg |
| [672](tags/672-LegIndividualAllocID.md) | [LegIndividualAllocID](tags/672-LegIndividualAllocID.md) | Reference for the individual allocation ticket |
| [673](tags/673-LegAllocQty.md) | [LegAllocQty](tags/673-LegAllocQty.md) | Leg allocation quantity. |
| [674](tags/674-LegAllocAcctIDSource.md) | [LegAllocAcctIDSource](tags/674-LegAllocAcctIDSource.md) | The source of the LegAllocAccount <671>. |
| [675](tags/675-LegSettlCurrency.md) | [LegSettlCurrency](tags/675-LegSettlCurrency.md) | Identifies settlement currency for the Leg. |
| [676](tags/676-LegBenchmarkCurveCurrency.md) | [LegBenchmarkCurveCurrency](tags/676-LegBenchmarkCurveCurrency.md) | LegBenchmarkPrice <679> currency. |
| [677](tags/677-LegBenchmarkCurveName.md) | [LegBenchmarkCurveName](tags/677-LegBenchmarkCurveName.md) | Name of the Leg Benchmark Curve. |
| [678](tags/678-LegBenchmarkCurvePoint.md) | [LegBenchmarkCurvePoint](tags/678-LegBenchmarkCurvePoint.md) | Identifies the point on the Leg Benchmark Curve. |
| [679](tags/679-LegBenchmarkPrice.md) | [LegBenchmarkPrice](tags/679-LegBenchmarkPrice.md) | Used to identify the price of the benchmark security. |
| [680](tags/680-LegBenchmarkPriceType.md) | [LegBenchmarkPriceType](tags/680-LegBenchmarkPriceType.md) | The price type of the LegBenchmarkPrice <679>. |
| [681](tags/681-LegBidPx.md) | [LegBidPx](tags/681-LegBidPx.md) | Bid price of this leg. |
| [682](tags/682-LegIOIQty.md) | [LegIOIQty](tags/682-LegIOIQty.md) | Leg-specific IOI <6> quantity. |
| [683](tags/683-NoLegStipulations.md) | [NoLegStipulations](tags/683-NoLegStipulations.md) | Number of leg stipulation entries. |
| [684](tags/684-LegOfferPx.md) | [LegOfferPx](tags/684-LegOfferPx.md) | Offer price of this leg. |
| [685](tags/685-LegOrderQty.md) | [LegOrderQty](tags/685-LegOrderQty.md) | Quantity ordered of this leg. |
| [686](tags/686-LegPriceType.md) | [LegPriceType](tags/686-LegPriceType.md) | The price type of the LegBidPx <681> and/or LegOfferPx <684>. |
| [687](tags/687-LegQty.md) | [LegQty](tags/687-LegQty.md) | Quantity of this leg, e.g. in Quote dialog. |
| [688](tags/688-LegStipulationType.md) | [LegStipulationType](tags/688-LegStipulationType.md) | For Fixed Income, type of Stipulation for this leg. |
| [689](tags/689-LegStipulationValue.md) | [LegStipulationValue](tags/689-LegStipulationValue.md) | For Fixed Income, value of stipulation. |
| [690](tags/690-LegSwapType.md) | [LegSwapType](tags/690-LegSwapType.md) | For Fixed Income, used instead of LegQty (687) or LegOrderQty (685) to requests the respondent to calculate the quantity based on the quantity on the opposite side of the swap. |
| [691](tags/691-Pool.md) | [Pool](tags/691-Pool.md) | For Fixed Income, identifies MBS / ABS pool. |
| [692](tags/692-QuotePriceType.md) | [QuotePriceType](tags/692-QuotePriceType.md) | Code to represent price type requested in Quote. |
| [693](tags/693-QuoteRespID.md) | [QuoteRespID](tags/693-QuoteRespID.md) | Message reference for Quote Response <AJ>. |
| [694](tags/694-QuoteRespType.md) | [QuoteRespType](tags/694-QuoteRespType.md) | Identifies the type of Quote Response <AJ>. |
| [695](tags/695-QuoteQualifier.md) | [QuoteQualifier](tags/695-QuoteQualifier.md) | Code to qualify Quote use |
| [696](tags/696-YieldRedemptionDate.md) | [YieldRedemptionDate](tags/696-YieldRedemptionDate.md) | Date to which the yield has been calculated (i.e. maturity, par call or current call, pre-refunded date). |
| [697](tags/697-RedemptionPrice.md) | [RedemptionPrice](tags/697-RedemptionPrice.md) | Price to which the yield has been calculated. |
| [698](tags/698-RedemptionPriceType.md) | [RedemptionPriceType](tags/698-RedemptionPriceType.md) | The price type of the YieldRedemptionPrice <697>. |
| [699](tags/699-BenchmarkSecurityID.md) | [BenchmarkSecurityID](tags/699-BenchmarkSecurityID.md) | The identifier of the benchmark security, e.g. Treasury against Corporate bond. |
| [700](tags/700-ReversalIndicator.md) | [ReversalIndicator](tags/700-ReversalIndicator.md) | Indicates a trade that reverses a previous trade. |
| [701](tags/701-YieldCalcDate.md) | [YieldCalcDate](tags/701-YieldCalcDate.md) | Include as needed to clarify yield irregularities associated with date, e.g. when it falls on a non-business day. |
| [702](tags/702-NoPositions.md) | [NoPositions](tags/702-NoPositions.md) | Number of position entries. |
| [703](tags/703-PosType.md) | [PosType](tags/703-PosType.md) | Used to identify the type of quantity that is being returned. |
| [704](tags/704-LongQty.md) | [LongQty](tags/704-LongQty.md) | Long Quantity |
| [705](tags/705-ShortQty.md) | [ShortQty](tags/705-ShortQty.md) | Short Quantity |
| [706](tags/706-PosQtyStatus.md) | [PosQtyStatus](tags/706-PosQtyStatus.md) | Status of this position. |
| [707](tags/707-PosAmtType.md) | [PosAmtType](tags/707-PosAmtType.md) | Type of Position amount. |
| [708](tags/708-PosAmt.md) | [PosAmt](tags/708-PosAmt.md) | Position amount. |
| [709](tags/709-PosTransType.md) | [PosTransType](tags/709-PosTransType.md) | Identifies the type of position transaction. |
| [710](tags/710-PosReqID.md) | [PosReqID](tags/710-PosReqID.md) | Unique identifier for the position maintenance request as assigned by the submitter. |
| [711](tags/711-NoUnderlyings.md) | [NoUnderlyings](tags/711-NoUnderlyings.md) | Number of underlying legs that make up the security. |
| [712](tags/712-PosMaintAction.md) | [PosMaintAction](tags/712-PosMaintAction.md) | Maintenance Action to be performed. |
| [713](tags/713-OrigPosReqRefID.md) | [OrigPosReqRefID](tags/713-OrigPosReqRefID.md) | Reference to the PosReqID (710) of a previous maintenance request that is being replaced or canceled. |
| [714](tags/714-PosMaintRptRefID.md) | [PosMaintRptRefID](tags/714-PosMaintRptRefID.md) | Reference to a PosMaintRptID <721> from a previous Position Maintenance Report <AM> that is being replaced or canceled. |
| [715](tags/715-ClearingBusinessDate.md) | [ClearingBusinessDate](tags/715-ClearingBusinessDate.md) | The "Clearing Business Date" referred to by this maintenance request. |
| [716](tags/716-SettlSessID.md) | [SettlSessID](tags/716-SettlSessID.md) | Identifies a specific settlement session. |
| [717](tags/717-SettlSessSubID.md) | [SettlSessSubID](tags/717-SettlSessSubID.md) | SubID value associated with SettlSessID <716>. |
| [718](tags/718-AdjustmentType.md) | [AdjustmentType](tags/718-AdjustmentType.md) | Type of adjustment to be applied, used for PCS & PAJ. |
| [719](tags/719-ContraryInstructionIndicator.md) | [ContraryInstructionIndicator](tags/719-ContraryInstructionIndicator.md) | Required to be set to true (Y) when a position maintenance request is being performed contrary to current money position. |
| [720](tags/720-PriorSpreadIndicator.md) | [PriorSpreadIndicator](tags/720-PriorSpreadIndicator.md) | Indicates if requesting a rollover of prior day's spread submissions. |
| [721](tags/721-PosMaintRptID.md) | [PosMaintRptID](tags/721-PosMaintRptID.md) | Unique identifier for this position report. |
| [722](tags/722-PosMaintStatus.md) | [PosMaintStatus](tags/722-PosMaintStatus.md) | Status of Position Maintenance Request <AL>. |
| [723](tags/723-PosMaintResult.md) | [PosMaintResult](tags/723-PosMaintResult.md) | Result of Position Maintenance Request <AL>. |
| [724](tags/724-PosReqType.md) | [PosReqType](tags/724-PosReqType.md) | Unique identifier for the position maintenance request as assigned by the submitter. |
| [725](tags/725-ResponseTransportType.md) | [ResponseTransportType](tags/725-ResponseTransportType.md) | Identifies how the response to the request should be transmitted. |
| [726](tags/726-ResponseDestination.md) | [ResponseDestination](tags/726-ResponseDestination.md) | URI (Uniform Resource Identifier) for details) or other pre-arranged value. Used in conjunction with ResponseTransportType (725) value of Out-of-Band to identify the out-of-band destination. |
| [727](tags/727-TotalNumPosReports.md) | [TotalNumPosReports](tags/727-TotalNumPosReports.md) | Total number of Position Reports being returned. |
| [728](tags/728-PosReqResult.md) | [PosReqResult](tags/728-PosReqResult.md) | Result of Request For Positions <AN>. |
| [729](tags/729-PosReqStatus.md) | [PosReqStatus](tags/729-PosReqStatus.md) | Status of Request For Positions <AN>. |
| [730](tags/730-SettlPrice.md) | [SettlPrice](tags/730-SettlPrice.md) | Settlement price. |
| [731](tags/731-SettlPriceType.md) | [SettlPriceType](tags/731-SettlPriceType.md) | Type of settlement price. |
| [732](tags/732-UnderlyingSettlPrice.md) | [UnderlyingSettlPrice](tags/732-UnderlyingSettlPrice.md) | Underlying security's SettlPrice. See SettlPrice (730) field for description |
| [733](tags/733-UnderlyingSettlPriceType.md) | [UnderlyingSettlPriceType](tags/733-UnderlyingSettlPriceType.md) | Underlying security's SettlPriceType. |
| [734](tags/734-PriorSettlPrice.md) | [PriorSettlPrice](tags/734-PriorSettlPrice.md) | Previous settlement price. |
| [735](tags/735-NoQuoteQualifiers.md) | [NoQuoteQualifiers](tags/735-NoQuoteQualifiers.md) | Number of repeating groups of QuoteQualifiers <695>. |
| [736](tags/736-AllocSettlCurrency.md) | [AllocSettlCurrency](tags/736-AllocSettlCurrency.md) | Currency code of settlement denomination for a specific AllocAccount <79>. |
| [737](tags/737-AllocSettlCurrAmt.md) | [AllocSettlCurrAmt](tags/737-AllocSettlCurrAmt.md) | Total amount due expressed in settlement currency (includes the effect of the forex transaction) for a specific AllocAccount <79>. |
| [738](tags/738-InterestAtMaturity.md) | [InterestAtMaturity](tags/738-InterestAtMaturity.md) | Amount of interest (i.e. lump-sum) at maturity. |
| [739](tags/739-LegDatedDate.md) | [LegDatedDate](tags/739-LegDatedDate.md) | The effective date of a new securities issue determined by its underwriters. Often but not always the same as the IssueDate <225> and the InterestAccrualDate <874>. |
| [740](tags/740-LegPool.md) | [LegPool](tags/740-LegPool.md) | For Fixed Income, identifies MBS / ABS pool for a specific leg of a multi-leg instrument. |
| [741](tags/741-AllocInterestAtMaturity.md) | [AllocInterestAtMaturity](tags/741-AllocInterestAtMaturity.md) | Amount of interest (i.e. lump-sum) at maturity at the account-level. |
| [742](tags/742-AllocAccruedInterestAmt.md) | [AllocAccruedInterestAmt](tags/742-AllocAccruedInterestAmt.md) | Amount of Accrued Interest for convertible bonds and fixed income at the allocation-level. |
| [743](tags/743-DeliveryDate.md) | [DeliveryDate](tags/743-DeliveryDate.md) | Date of delivery. |
| [744](tags/744-AssignmentMethod.md) | [AssignmentMethod](tags/744-AssignmentMethod.md) | Method under which assignment was conducted. |
| [745](tags/745-AssignmentUnit.md) | [AssignmentUnit](tags/745-AssignmentUnit.md) | Quantity Increment used in performing assignment. |
| [746](tags/746-OpenInterest.md) | [OpenInterest](tags/746-OpenInterest.md) | Open interest that was eligible for assignment. |
| [747](tags/747-ExerciseMethod.md) | [ExerciseMethod](tags/747-ExerciseMethod.md) | Exercise Method used to in performing assignment. |
| [748](tags/748-TotalNumTradeReports.md) | [TotalNumTradeReports](tags/748-TotalNumTradeReports.md) | Total number of trade reports returned. |
| [749](tags/749-TradeRequestResult.md) | [TradeRequestResult](tags/749-TradeRequestResult.md) | Result of Trade Request |
| [750](tags/750-TradeRequestStatus.md) | [TradeRequestStatus](tags/750-TradeRequestStatus.md) | Status of Trade Request. |
| [751](tags/751-TradeReportRejectReason.md) | [TradeReportRejectReason](tags/751-TradeReportRejectReason.md) | Reason Trade Capture Request was rejected. |
| [752](tags/752-SideMultiLegReportingType.md) | [SideMultiLegReportingType](tags/752-SideMultiLegReportingType.md) | Used to indicate if the side being reported on Trade Capture Report <AE> represents a leg of a multileg instrument or a single security. |
| [753](tags/753-NoPosAmt.md) | [NoPosAmt](tags/753-NoPosAmt.md) | Number of position amount entries. |
| [754](tags/754-AutoAcceptIndicator.md) | [AutoAcceptIndicator](tags/754-AutoAcceptIndicator.md) | Identifies whether or not an allocation has been automatically accepted on behalf of the Carry Firm by the Clearing House. |
| [755](tags/755-AllocReportID.md) | [AllocReportID](tags/755-AllocReportID.md) | Unique identifier for Allocation Report message. |
| [756](tags/756-NoNested2PartyIDs.md) | [NoNested2PartyIDs](tags/756-NoNested2PartyIDs.md) | Number of Nested2PartyID <757>, Nested2PartyIDSource <758>, and Nested2PartyRole <759> entries. |
| [757](tags/757-Nested2PartyID.md) | [Nested2PartyID](tags/757-Nested2PartyID.md) | PartyID value within a "second instance" Nested repeating group. |
| [758](tags/758-Nested2PartyIDSource.md) | [Nested2PartyIDSource](tags/758-Nested2PartyIDSource.md) | PartyIDSource value within a "second instance" Nested repeating group. |
| [759](tags/759-Nested2PartyRole.md) | [Nested2PartyRole](tags/759-Nested2PartyRole.md) | PartyRole value within a "second instance" Nested repeating group. |
| [760](tags/760-Nested2PartySubID.md) | [Nested2PartySubID](tags/760-Nested2PartySubID.md) | PartySubID value within a "second instance" Nested repeating group. |
| [761](tags/761-BenchmarkSecurityIDSource.md) | [BenchmarkSecurityIDSource](tags/761-BenchmarkSecurityIDSource.md) | Identifies class or source of the BenchmarkSecurityID <699> value. Required if BenchmarkSecurityID is specified. |
| [762](tags/762-SecuritySubType.md) | [SecuritySubType](tags/762-SecuritySubType.md) | Sub-type qualification/identification of the SecurityType <167> (e.g. for SecurityType="REPO"). |
| [763](tags/763-UnderlyingSecuritySubType.md) | [UnderlyingSecuritySubType](tags/763-UnderlyingSecuritySubType.md) | Underlying security's SecuritySubType. |
| [764](tags/764-LegSecuritySubType.md) | [LegSecuritySubType](tags/764-LegSecuritySubType.md) | SecuritySubType of the leg instrument. |
| [765](tags/765-AllowableOneSidednessPct.md) | [AllowableOneSidednessPct](tags/765-AllowableOneSidednessPct.md) | The maximum percentage that execution of one side of a program trade can exceed execution of the other. |
| [766](tags/766-AllowableOneSidednessValue.md) | [AllowableOneSidednessValue](tags/766-AllowableOneSidednessValue.md) | The maximum amount that execution of one side of a program trade can exceed execution of the other. |
| [767](tags/767-AllowableOneSidednessCurr.md) | [AllowableOneSidednessCurr](tags/767-AllowableOneSidednessCurr.md) | The currency that AllowableOneSidednessValue <766> is expressed in if AllowableOneSidednessValue is used. |
| [768](tags/768-NoTrdRegTimestamps.md) | [NoTrdRegTimestamps](tags/768-NoTrdRegTimestamps.md) | Number of TrdRegTimestamp (769) entries |
| [769](tags/769-TrdRegTimestamp.md) | [TrdRegTimestamp](tags/769-TrdRegTimestamp.md) | Traded / Regulatory timestamp value. Use to store time information required by government regulators or self regulatory organizations (such as an exchange or clearing house). |
| [770](tags/770-TrdRegTimestampType.md) | [TrdRegTimestampType](tags/770-TrdRegTimestampType.md) | Traded / Regulatory timestamp type. |
| [771](tags/771-TrdRegTimestampOrigin.md) | [TrdRegTimestampOrigin](tags/771-TrdRegTimestampOrigin.md) | Text which identifies the "origin" (i.e. system which was used to generate the time stamp) for the Traded / Regulatory timestamp value. |
| [772](tags/772-ConfirmRefID.md) | [ConfirmRefID](tags/772-ConfirmRefID.md) | Reference identifier to be used with ConfirmTransType <666> = "Replace" or "Cancel". |
| [773](tags/773-ConfirmType.md) | [ConfirmType](tags/773-ConfirmType.md) | Identifies the type of Confirmation <AK> message being sent. |
| [774](tags/774-ConfirmRejReason.md) | [ConfirmRejReason](tags/774-ConfirmRejReason.md) | Identifies the reason for rejecting a Confirmation <AK>. |
| [775](tags/775-BookingType.md) | [BookingType](tags/775-BookingType.md) | Method for booking out this order. Used when notifying a broker that an order to be settled by that broker is to be booked out as an OTC derivative (e.g. CFD or similar). |
| [776](tags/776-IndividualAllocRejCode.md) | [IndividualAllocRejCode](tags/776-IndividualAllocRejCode.md) | Identified reason for rejecting an individual AllocAccount (79) detail. |
| [777](tags/777-SettlInstMsgID.md) | [SettlInstMsgID](tags/777-SettlInstMsgID.md) | Unique identifier for Settlement Instruction message. |
| [778](tags/778-NoSettlInst.md) | [NoSettlInst](tags/778-NoSettlInst.md) | Number of settlement instructions within repeating group. |
| [779](tags/779-LastUpdateTime.md) | [LastUpdateTime](tags/779-LastUpdateTime.md) | Timestamp of last update to data item (or creation if no updates made since creation). |
| [780](tags/780-AllocSettlInstType.md) | [AllocSettlInstType](tags/780-AllocSettlInstType.md) | Used to indicate whether settlement instructions are provided on an Allocation Instruction <J> message, and if not, how they are to be derived. |
| [781](tags/781-NoSettlPartyIDs.md) | [NoSettlPartyIDs](tags/781-NoSettlPartyIDs.md) | Number of SettlPartyID <782>, SettlPartyIDSource <783>, and SettlPartyRole <784> entries. |
| [782](tags/782-SettlPartyID.md) | [SettlPartyID](tags/782-SettlPartyID.md) | PartyID value within a settlement parties component. Nested repeating group. |
| [783](tags/783-SettlPartyIDSource.md) | [SettlPartyIDSource](tags/783-SettlPartyIDSource.md) | PartyIDSource value within a settlement parties component. |
| [784](tags/784-SettlPartyRole.md) | [SettlPartyRole](tags/784-SettlPartyRole.md) | PartyRole value within a settlement parties component. |
| [785](tags/785-SettlPartySubID.md) | [SettlPartySubID](tags/785-SettlPartySubID.md) | PartySubID value within a settlement parties component. |
| [786](tags/786-SettlPartySubIDType.md) | [SettlPartySubIDType](tags/786-SettlPartySubIDType.md) | Type of SettlPartySubID <785> value. |
| [787](tags/787-DlvyInstType.md) | [DlvyInstType](tags/787-DlvyInstType.md) | Used to indicate whether a delivery instruction is used for securities or cash settlement. |
| [788](tags/788-TerminationType.md) | [TerminationType](tags/788-TerminationType.md) | Type of financing termination. |
| [789](tags/789-NextExpectedMsgSeqNum.md) | [NextExpectedMsgSeqNum](tags/789-NextExpectedMsgSeqNum.md) | Next expected MsgSeqNum (34) value to be received. |
| [790](tags/790-OrdStatusReqID.md) | [OrdStatusReqID](tags/790-OrdStatusReqID.md) | Can be used to uniquely identify a specific Order Status Request <H> message. |
| [791](tags/791-SettlInstReqID.md) | [SettlInstReqID](tags/791-SettlInstReqID.md) | Unique ID of Settlement Instruction Request <AV> message. |
| [792](tags/792-SettlInstReqRejCode.md) | [SettlInstReqRejCode](tags/792-SettlInstReqRejCode.md) | Identifies reason for rejection (of a Settlement Instruction Request <AV> message). |
| [793](tags/793-SecondaryAllocID.md) | [SecondaryAllocID](tags/793-SecondaryAllocID.md) | Secondary allocation identifier. Unlike the AllocID <70>, this can be shared across a number of allocation instruction or allocation report messages, thereby making it possible to pass an identifier for an original allocation message on multiple messages (e.g. from one party to a second to a third, across cancel and replace messages etc.). |
| [794](tags/794-AllocReportType.md) | [AllocReportType](tags/794-AllocReportType.md) | Describes the specific type or purpose of an Allocation Report <AS> message. |
| [795](tags/795-AllocReportRefID.md) | [AllocReportRefID](tags/795-AllocReportRefID.md) | Reference identifier to be used with AllocTransType <71> = 'Replace' or 'Cancel'. |
| [796](tags/796-AllocCancReplaceReason.md) | [AllocCancReplaceReason](tags/796-AllocCancReplaceReason.md) | Reason for cancelling or replacing an Allocation Instruction <J> or Allocation Report <AS> message. |
| [797](tags/797-CopyMsgIndicator.md) | [CopyMsgIndicator](tags/797-CopyMsgIndicator.md) | Indicates whether or not this message is a drop copy of another message. |
| [798](tags/798-AllocAccountType.md) | [AllocAccountType](tags/798-AllocAccountType.md) | Type of account associated with a confirmation or other trade-level message |
| [799](tags/799-OrderAvgPx.md) | [OrderAvgPx](tags/799-OrderAvgPx.md) | Average price for a specific order |
| [800](tags/800-OrderBookingQty.md) | [OrderBookingQty](tags/800-OrderBookingQty.md) | Quantity of the order that is being booked out as part of an Allocation Instruction <J> or Allocation Report <AS> message. |
| [801](tags/801-NoSettlPartySubIDs.md) | [NoSettlPartySubIDs](tags/801-NoSettlPartySubIDs.md) | Number of SettlPartySubID (785) and SettlPartySubIDType (786) entries |
| [802](tags/802-NoPartySubIDs.md) | [NoPartySubIDs](tags/802-NoPartySubIDs.md) | Number of PartySubID (523) and PartySubIDType (803) entries |
| [803](tags/803-PartySubIDType.md) | [PartySubIDType](tags/803-PartySubIDType.md) | Type of PartySubID (523) value |
| [804](tags/804-NoNestedPartySubIDs.md) | [NoNestedPartySubIDs](tags/804-NoNestedPartySubIDs.md) | Number of NestedPartySubID (545) and NestedPartySubIDType (805) entries |
| [805](tags/805-NestedPartySubIDType.md) | [NestedPartySubIDType](tags/805-NestedPartySubIDType.md) | Type of NestedPartySubID (545) value. |
| [806](tags/806-NoNested2PartySubIDs.md) | [NoNested2PartySubIDs](tags/806-NoNested2PartySubIDs.md) | Number of Nested2PartySubID <760> and Nested2PartySubIDType <807> entries. Second instance of <NestedParties>. |
| [807](tags/807-Nested2PartySubIDType.md) | [Nested2PartySubIDType](tags/807-Nested2PartySubIDType.md) | Type of Nested2PartySubID <760> value. Second instance of <NestedParties>. |
| [808](tags/808-AllocIntermedReqType.md) | [AllocIntermedReqType](tags/808-AllocIntermedReqType.md) | Response to allocation to be communicated to a counterparty through an intermediary, i.e. clearing house. Used in conjunction with AllocType (626) = "Request to Intermediary" and AllocReportType (794) = "Request to Intermediary" |
| [810](tags/810-UnderlyingPx.md) | [UnderlyingPx](tags/810-UnderlyingPx.md) | Underlying price associate with a derivative instrument. |
| [811](tags/811-PriceDelta.md) | [PriceDelta](tags/811-PriceDelta.md) | Delta calculated from theoretical price |
| [812](tags/812-ApplQueueMax.md) | [ApplQueueMax](tags/812-ApplQueueMax.md) | Used to specify the maximum number of application messages that can be queued before a corrective action needs to take place to resolve the queuing issue. |
| [813](tags/813-ApplQueueDepth.md) | [ApplQueueDepth](tags/813-ApplQueueDepth.md) | Current number of application messages that were queued at the time that the message was created by the counterparty. |
| [814](tags/814-ApplQueueResolution.md) | [ApplQueueResolution](tags/814-ApplQueueResolution.md) | Resolution taken when ApplQueueDepth (813) exceeds ApplQueueMax (812) or system specified maximum queue size. |
| [815](tags/815-ApplQueueAction.md) | [ApplQueueAction](tags/815-ApplQueueAction.md) | Action to take to resolve an application message queue (backlog). |
| [816](tags/816-NoAltMDSource.md) | [NoAltMDSource](tags/816-NoAltMDSource.md) | Number of alternative market data sources |
| [817](tags/817-AltMDSourceID.md) | [AltMDSourceID](tags/817-AltMDSourceID.md) | Session layer source for market data |
| [818](tags/818-SecondaryTradeReportID.md) | [SecondaryTradeReportID](tags/818-SecondaryTradeReportID.md) | Secondary trade report identifier - can be used to associate an additional identifier with a trade. |
| [819](tags/819-AvgPxIndicator.md) | [AvgPxIndicator](tags/819-AvgPxIndicator.md) | Average Pricing Indicator |
| [820](tags/820-TradeLinkID.md) | [TradeLinkID](tags/820-TradeLinkID.md) | Used to link a group of trades together. Useful for linking a group of trades together for average price calculations. |
| [821](tags/821-OrderInputDevice.md) | [OrderInputDevice](tags/821-OrderInputDevice.md) | Specific device number, terminal number or station where order was entered |
| [822](tags/822-UnderlyingTradingSessionID.md) | [UnderlyingTradingSessionID](tags/822-UnderlyingTradingSessionID.md) | Trading Session in which the underlying instrument trades |
| [823](tags/823-UnderlyingTradingSessionSubID.md) | [UnderlyingTradingSessionSubID](tags/823-UnderlyingTradingSessionSubID.md) | Trading Session sub identifier in which the underlying instrument trades |
| [824](tags/824-TradeLegRefID.md) | [TradeLegRefID](tags/824-TradeLegRefID.md) | Reference to the leg of a multileg instrument to which this trade refers |
| [825](tags/825-ExchangeRule.md) | [ExchangeRule](tags/825-ExchangeRule.md) | Used to report any exchange rules that apply to this trade. |
| [826](tags/826-TradeAllocIndicator.md) | [TradeAllocIndicator](tags/826-TradeAllocIndicator.md) | Identifies how the trade is to be allocated |
| [827](tags/827-ExpirationCycle.md) | [ExpirationCycle](tags/827-ExpirationCycle.md) | Part of trading cycle when an instrument expires. Field is applicable for derivatives. |
| [828](tags/828-TrdType.md) | [TrdType](tags/828-TrdType.md) | Type of Trade |
| [829](tags/829-TrdSubType.md) | [TrdSubType](tags/829-TrdSubType.md) | Further qualification to the trade type |
| [830](tags/830-TransferReason.md) | [TransferReason](tags/830-TransferReason.md) | Reason trade is being transferred |
| [831](tags/831-AsgnReqID.md) | [AsgnReqID](tags/831-AsgnReqID.md) | Deprecated in FIX 4.4 |
| [832](tags/832-TotNumAssignmentReports.md) | [TotNumAssignmentReports](tags/832-TotNumAssignmentReports.md) | Total Number of Assignment Reports being returned to a firm |
| [833](tags/833-AsgnRptID.md) | [AsgnRptID](tags/833-AsgnRptID.md) | Unique identifier for the Assignment Report. |
| [834](tags/834-ThresholdAmount.md) | [ThresholdAmount](tags/834-ThresholdAmount.md) | Amount that a position has to be in the money before it is exercised. |
| [835](tags/835-PegMoveType.md) | [PegMoveType](tags/835-PegMoveType.md) | Describes whether peg is static or floats |
| [836](tags/836-PegOffsetType.md) | [PegOffsetType](tags/836-PegOffsetType.md) | Type of Peg Offset value |
| [837](tags/837-PegLimitType.md) | [PegLimitType](tags/837-PegLimitType.md) | Type of Peg Limit |
| [838](tags/838-PegRoundDirection.md) | [PegRoundDirection](tags/838-PegRoundDirection.md) | If the calculated peg price is not a valid tick price, specifies whether to round the price to be more or less aggressive |
| [839](tags/839-PeggedPrice.md) | [PeggedPrice](tags/839-PeggedPrice.md) | The price the order is currently pegged at |
| [840](tags/840-PegScope.md) | [PegScope](tags/840-PegScope.md) | The scope of the peg |
| [841](tags/841-DiscretionMoveType.md) | [DiscretionMoveType](tags/841-DiscretionMoveType.md) | Describes whether discretionay price is static or floats |
| [842](tags/842-DiscretionOffsetType.md) | [DiscretionOffsetType](tags/842-DiscretionOffsetType.md) | Type of Discretion Offset value |
| [843](tags/843-DiscretionLimitType.md) | [DiscretionLimitType](tags/843-DiscretionLimitType.md) | Type of Discretion Limit |
| [844](tags/844-DiscretionRoundDirection.md) | [DiscretionRoundDirection](tags/844-DiscretionRoundDirection.md) | If the calculated discretionary price is not a valid tick price, specifies whether to round the price to be more or less aggressive |
| [845](tags/845-DiscretionPrice.md) | [DiscretionPrice](tags/845-DiscretionPrice.md) | The current discretionary price of the order |
| [846](tags/846-DiscretionScope.md) | [DiscretionScope](tags/846-DiscretionScope.md) | The scope of the discretion |
| [847](tags/847-TargetStrategy.md) | [TargetStrategy](tags/847-TargetStrategy.md) | The target strategy of the order |
| [848](tags/848-TargetStrategyParameters.md) | [TargetStrategyParameters](tags/848-TargetStrategyParameters.md) | Field to allow further specification of the TargetStrategy (847) - usage to be agreed between counterparties |
| [849](tags/849-ParticipationRate.md) | [ParticipationRate](tags/849-ParticipationRate.md) | For a TargetStrategy <847>="Participate" order specifies the target particpation rate. For other order types this is a volume limit (i.e. do not be more than this percent of the market volume). |
| [850](tags/850-TargetStrategyPerformance.md) | [TargetStrategyPerformance](tags/850-TargetStrategyPerformance.md) | For communication of the performance of the order versus the target strategy |
| [851](tags/851-LastLiquidityInd.md) | [LastLiquidityInd](tags/851-LastLiquidityInd.md) | Indicator to identify whether this fill was a result of a liquidity provider providing or liquidity taker taking the liquidity. Applicable only for OrdStatus <39> of 'Partial' or 'Filled'. |
| [852](tags/852-PublishTrdIndicator.md) | [PublishTrdIndicator](tags/852-PublishTrdIndicator.md) | Indicates if a trade should be reported via a market reporting service. |
| [853](tags/853-ShortSaleReason.md) | [ShortSaleReason](tags/853-ShortSaleReason.md) | Reason for short sale. |
| [854](tags/854-QtyType.md) | [QtyType](tags/854-QtyType.md) | Type of quantity specified in a Quantity <53> field:. |
| [855](tags/855-SecondaryTrdType.md) | [SecondaryTrdType](tags/855-SecondaryTrdType.md) | Additional TrdType assigned to a trade by trade match system. |
| [856](tags/856-TradeReportType.md) | [TradeReportType](tags/856-TradeReportType.md) | Type of Trade Report |
| [857](tags/857-AllocNoOrdersType.md) | [AllocNoOrdersType](tags/857-AllocNoOrdersType.md) | Indicates how the orders being booked and allocated by an Allocation Instruction <J> or Allocation Report <AS> message are identified, i.e. by explicit definition in the NoOrders <73> group or not. |
| [858](tags/858-SharedCommission.md) | [SharedCommission](tags/858-SharedCommission.md) | Commission to be shared with a third party, e.g. as part of a directed brokerage commission sharing arrangement. |
| [859](tags/859-ConfirmReqID.md) | [ConfirmReqID](tags/859-ConfirmReqID.md) | Unique identifier for a Confirmation Request message |
| [860](tags/860-AvgParPx.md) | [AvgParPx](tags/860-AvgParPx.md) | Used to express average price as percent of par (used where AvgPx (6) field is expressed in some other way) |
| [861](tags/861-ReportedPx.md) | [ReportedPx](tags/861-ReportedPx.md) | Reported price (used to differentiate from AvgPx (6) on a confirmation of a marked-up or marked-down principal trade) |
| [862](tags/862-NoCapacities.md) | [NoCapacities](tags/862-NoCapacities.md) | Number of repeating OrderCapacity <528> entries. |
| [863](tags/863-OrderCapacityQty.md) | [OrderCapacityQty](tags/863-OrderCapacityQty.md) | Quantity executed under a specific OrderCapacity <528> (e.g. quantity executed as agent, quantity executed as principal). |
| [864](tags/864-NoEvents.md) | [NoEvents](tags/864-NoEvents.md) | Number of repeating EventType (865) entries. |
| [865](tags/865-EventType.md) | [EventType](tags/865-EventType.md) | Code to represent the type of event |
| [866](tags/866-EventDate.md) | [EventDate](tags/866-EventDate.md) | Date of event |
| [867](tags/867-EventPx.md) | [EventPx](tags/867-EventPx.md) | Predetermined price of issue at event, if applicable |
| [868](tags/868-EventText.md) | [EventText](tags/868-EventText.md) | Comments related to the event. |
| [869](tags/869-PctAtRisk.md) | [PctAtRisk](tags/869-PctAtRisk.md) | Percent at risk due to lowest possible call. |
| [870](tags/870-NoInstrAttrib.md) | [NoInstrAttrib](tags/870-NoInstrAttrib.md) | Number of repeating InstrAttribType (871) entries. |
| [871](tags/871-InstrAttribType.md) | [InstrAttribType](tags/871-InstrAttribType.md) | Code to represent the type of instrument attribute |
| [872](tags/872-InstrAttribValue.md) | [InstrAttribValue](tags/872-InstrAttribValue.md) | Attribute value appropriate to the InstrAttribType (871) field. |
| [873](tags/873-DatedDate.md) | [DatedDate](tags/873-DatedDate.md) | The effective date of a new securities issue determined by its underwriters. Often but not always the same as the IssueDate (225) and the InterestAccrualDate (874) |
| [874](tags/874-InterestAccrualDate.md) | [InterestAccrualDate](tags/874-InterestAccrualDate.md) | The start date used for calculating accrued interest on debt instruments which are being sold between interest payment dates. Often but not always the same as the IssueDate (225) and the DatedDate (873) |
| [875](tags/875-CPProgram.md) | [CPProgram](tags/875-CPProgram.md) | The program under which a commercial paper is issued |
| [876](tags/876-CPRegType.md) | [CPRegType](tags/876-CPRegType.md) | The registration type of a commercial paper issuance |
| [877](tags/877-UnderlyingCPProgram.md) | [UnderlyingCPProgram](tags/877-UnderlyingCPProgram.md) | The program under which the underlying commercial paper is issued |
| [878](tags/878-UnderlyingCPRegType.md) | [UnderlyingCPRegType](tags/878-UnderlyingCPRegType.md) | The registration type of the underlying commercial paper issuance |
| [879](tags/879-UnderlyingQty.md) | [UnderlyingQty](tags/879-UnderlyingQty.md) | Unit amount of the underlying security (par, shares, currency, etc.) |
| [880](tags/880-TrdMatchID.md) | [TrdMatchID](tags/880-TrdMatchID.md) | Identifier assigned to a trade by a matching system. |
| [881](tags/881-SecondaryTradeReportRefID.md) | [SecondaryTradeReportRefID](tags/881-SecondaryTradeReportRefID.md) | Used to refer to a previous SecondaryTradeReportRefID (881) when amending the transaction (cancel, replace, release, or reversal). |
| [882](tags/882-UnderlyingDirtyPrice.md) | [UnderlyingDirtyPrice](tags/882-UnderlyingDirtyPrice.md) | Price (percent-of-par or per unit) of the underlying security or basket. "Dirty" means it includes accrued interest |
| [883](tags/883-UnderlyingEndPrice.md) | [UnderlyingEndPrice](tags/883-UnderlyingEndPrice.md) | Price (percent-of-par or per unit) of the underlying security or basket at the end of the agreement. |
| [884](tags/884-UnderlyingStartValue.md) | [UnderlyingStartValue](tags/884-UnderlyingStartValue.md) | Currency value attributed to this collateral at the start of the agreement |
| [885](tags/885-UnderlyingCurrentValue.md) | [UnderlyingCurrentValue](tags/885-UnderlyingCurrentValue.md) | Currency value currently attributed to this collateral |
| [886](tags/886-UnderlyingEndValue.md) | [UnderlyingEndValue](tags/886-UnderlyingEndValue.md) | Currency value attributed to this collateral at the end of the agreement |
| [887](tags/887-NoUnderlyingStips.md) | [NoUnderlyingStips](tags/887-NoUnderlyingStips.md) | Number of underlying stipulation entries |
| [888](tags/888-UnderlyingStipType.md) | [UnderlyingStipType](tags/888-UnderlyingStipType.md) | Type of stipulation. |
| [889](tags/889-UnderlyingStipValue.md) | [UnderlyingStipValue](tags/889-UnderlyingStipValue.md) | Value of stipulation. |
| [890](tags/890-MaturityNetMoney.md) | [MaturityNetMoney](tags/890-MaturityNetMoney.md) | Net Money at maturity if Zero Coupon and maturity value is different from par value |
| [891](tags/891-MiscFeeBasis.md) | [MiscFeeBasis](tags/891-MiscFeeBasis.md) | Defines the unit for a miscellaneous fee. |
| [892](tags/892-TotNoAllocs.md) | [TotNoAllocs](tags/892-TotNoAllocs.md) | Total number of NoAlloc entries across all messages. Should be the sum of all NoAllocs <78> in each message that has repeating NoAlloc entries related to the same AllocID <70> or AllocReportID <755>. Used to support fragmentation. |
| [893](tags/893-LastFragment.md) | [LastFragment](tags/893-LastFragment.md) | Indicates whether this message is the last in a sequence of messages for those messages that support fragmentation, such as Allocation Instruction <J>, Mass Quote <i>, Security List <y>, Derivative Security List <AA>. |
| [894](tags/894-CollReqID.md) | [CollReqID](tags/894-CollReqID.md) | Collateral Request Identifier. |
| [895](tags/895-CollAsgnReason.md) | [CollAsgnReason](tags/895-CollAsgnReason.md) | Reason for Collateral Assignment <AY>. |
| [896](tags/896-CollInquiryQualifier.md) | [CollInquiryQualifier](tags/896-CollInquiryQualifier.md) | Collateral inquiry qualifiers |
| [897](tags/897-NoTrades.md) | [NoTrades](tags/897-NoTrades.md) | Number of trades in repeating group. |
| [898](tags/898-MarginRatio.md) | [MarginRatio](tags/898-MarginRatio.md) | The fraction of the cash consideration that must be collateralized, expressed as a percent. A MarginRatio (898) of 102% indicates that the value of the collateral (after deducting for "haircut") must exceed the cash consideration by 2%. |
| [899](tags/899-MarginExcess.md) | [MarginExcess](tags/899-MarginExcess.md) | Excess margin amount (deficit if value is negative) |
| [900](tags/900-TotalNetValue.md) | [TotalNetValue](tags/900-TotalNetValue.md) | TotalNetValue is determined as follows:. |
| [901](tags/901-CashOutstanding.md) | [CashOutstanding](tags/901-CashOutstanding.md) | Starting consideration less repayments |
| [902](tags/902-CollAsgnID.md) | [CollAsgnID](tags/902-CollAsgnID.md) | Collateral Assignment Identifier. |
| [903](tags/903-CollAsgnTransType.md) | [CollAsgnTransType](tags/903-CollAsgnTransType.md) | Collateral Assignment <AY> Transaction Type. |
| [904](tags/904-CollRespID.md) | [CollRespID](tags/904-CollRespID.md) | Collateral Response Identifier. |
| [905](tags/905-CollAsgnRespType.md) | [CollAsgnRespType](tags/905-CollAsgnRespType.md) | Collateral Assignment <AY> Response Type. |
| [906](tags/906-CollAsgnRejectReason.md) | [CollAsgnRejectReason](tags/906-CollAsgnRejectReason.md) | Collateral Assignment <AY> Reject Reason. |
| [907](tags/907-CollAsgnRefID.md) | [CollAsgnRefID](tags/907-CollAsgnRefID.md) | Collateral Assignment Identifier to which a transaction refers. |
| [908](tags/908-CollRptID.md) | [CollRptID](tags/908-CollRptID.md) | Collateral Report Identifier. |
| [909](tags/909-CollInquiryID.md) | [CollInquiryID](tags/909-CollInquiryID.md) | Collateral Inquiry Identifier. |
| [910](tags/910-CollStatus.md) | [CollStatus](tags/910-CollStatus.md) | Collateral Status |
| [911](tags/911-TotNumReports.md) | [TotNumReports](tags/911-TotNumReports.md) | Total number or reports returned in response to a request |
| [912](tags/912-LastRptRequested.md) | [LastRptRequested](tags/912-LastRptRequested.md) | Indicates whether this message is that last report message in response to a request, such as Order Mass Status Request <AF>. |
| [913](tags/913-AgreementDesc.md) | [AgreementDesc](tags/913-AgreementDesc.md) | The full name of the base standard agreement, annexes and amendments in place between the principals applicable to a financing transaction. |
| [914](tags/914-AgreementID.md) | [AgreementID](tags/914-AgreementID.md) | A common reference to the applicable standing agreement between the counterparties to a financing transaction. |
| [915](tags/915-AgreementDate.md) | [AgreementDate](tags/915-AgreementDate.md) | A reference to the date the underlying agreement specified by AgreementID (914) and AgreementDesc (913) was executed. |
| [916](tags/916-StartDate.md) | [StartDate](tags/916-StartDate.md) | Start date of a financing deal, i.e. the date the buyer pays the seller cash and takes control of the collateral |
| [917](tags/917-EndDate.md) | [EndDate](tags/917-EndDate.md) | End date of a financing deal, i.e. the date the seller reimburses the buyer and takes back control of the collateral |
| [918](tags/918-AgreementCurrency.md) | [AgreementCurrency](tags/918-AgreementCurrency.md) | Contractual currency forming the basis of a financing agreement and associated transactions. Usually, but not always, the same as the trade currency. |
| [919](tags/919-DeliveryType.md) | [DeliveryType](tags/919-DeliveryType.md) | Identifies type of settlement |
| [920](tags/920-EndAccruedInterestAmt.md) | [EndAccruedInterestAmt](tags/920-EndAccruedInterestAmt.md) | Accrued Interest Amount applicable to a financing transaction on the EndDate <917>. |
| [921](tags/921-StartCash.md) | [StartCash](tags/921-StartCash.md) | Starting dirty cash consideration of a financing deal, i.e. paid to the seller on the StartDate <916>. |
| [922](tags/922-EndCash.md) | [EndCash](tags/922-EndCash.md) | Ending dirty cash consideration of a financing deal. i.e. reimbursed to the buyer on the EndDate <917>. |
| [923](tags/923-UserRequestID.md) | [UserRequestID](tags/923-UserRequestID.md) | Unique identifier for a User Request. |
| [924](tags/924-UserRequestType.md) | [UserRequestType](tags/924-UserRequestType.md) | Indicates the action required by a User Request <BE> Message. |
| [925](tags/925-NewPassword.md) | [NewPassword](tags/925-NewPassword.md) | New Password <554> or passphrase. |
| [926](tags/926-UserStatus.md) | [UserStatus](tags/926-UserStatus.md) | Indicates the status of a user |
| [927](tags/927-UserStatusText.md) | [UserStatusText](tags/927-UserStatusText.md) | A text description associated with a user status. |
| [928](tags/928-StatusValue.md) | [StatusValue](tags/928-StatusValue.md) | Indicates the status of a network connection |
| [929](tags/929-StatusText.md) | [StatusText](tags/929-StatusText.md) | A text description associated with a network status. |
| [930](tags/930-RefCompID.md) | [RefCompID](tags/930-RefCompID.md) | Assigned value used to identify a firm. |
| [931](tags/931-RefSubID.md) | [RefSubID](tags/931-RefSubID.md) | Assigned value used to identify specific elements within a firm. |
| [932](tags/932-NetworkResponseID.md) | [NetworkResponseID](tags/932-NetworkResponseID.md) | Unique identifier for a network response. |
| [933](tags/933-NetworkRequestID.md) | [NetworkRequestID](tags/933-NetworkRequestID.md) | Unique identifier for a network resquest. |
| [934](tags/934-LastNetworkResponseID.md) | [LastNetworkResponseID](tags/934-LastNetworkResponseID.md) | Identifier of the previous Network Response message sent to a counterparty, used to allow incremental updates. |
| [935](tags/935-NetworkRequestType.md) | [NetworkRequestType](tags/935-NetworkRequestType.md) | Indicates the type and level of details required for a Network Status Request Message. |
| [936](tags/936-NoCompIDs.md) | [NoCompIDs](tags/936-NoCompIDs.md) | Number of CompID entries in a repeating group. |
| [937](tags/937-NetworkStatusResponseType.md) | [NetworkStatusResponseType](tags/937-NetworkStatusResponseType.md) | Indicates the type of Network Response Message. |
| [938](tags/938-NoCollInquiryQualifier.md) | [NoCollInquiryQualifier](tags/938-NoCollInquiryQualifier.md) | Number of CollInquiryQualifier <896> entries in a repeating group. |
| [939](tags/939-TrdRptStatus.md) | [TrdRptStatus](tags/939-TrdRptStatus.md) | Trade Report Status |
| [940](tags/940-AffirmStatus.md) | [AffirmStatus](tags/940-AffirmStatus.md) | Identifies the status of the ConfirmationAck. |
| [941](tags/941-UnderlyingStrikeCurrency.md) | [UnderlyingStrikeCurrency](tags/941-UnderlyingStrikeCurrency.md) | Currency in which the strike price of an underlying instrument (UnderlyingStrikePrice <316>) is denominated. |
| [942](tags/942-LegStrikeCurrency.md) | [LegStrikeCurrency](tags/942-LegStrikeCurrency.md) | Currency in which the strike price of an instrument leg of a multileg instrument (LegStrikePrice <612>) is denominated. |
| [943](tags/943-TimeBracket.md) | [TimeBracket](tags/943-TimeBracket.md) | A code that represents a time interval in which a fill or trade occurred. |
| [944](tags/944-CollAction.md) | [CollAction](tags/944-CollAction.md) | Action proposed for an <UnderlyingInstrument> instance. |
| [945](tags/945-CollInquiryStatus.md) | [CollInquiryStatus](tags/945-CollInquiryStatus.md) | Status of Collateral Inquiry <BB>. |
| [946](tags/946-CollInquiryResult.md) | [CollInquiryResult](tags/946-CollInquiryResult.md) | Result returned in response to Collateral Inquiry <BB>. |
| [947](tags/947-StrikeCurrency.md) | [StrikeCurrency](tags/947-StrikeCurrency.md) | Currency in which the StrikePrice (202) is denominated. |
| [948](tags/948-NoNested3PartyIDs.md) | [NoNested3PartyIDs](tags/948-NoNested3PartyIDs.md) | Number of Nested3PartyID <949>, Nested3PartyIDSource <950>, and Nested3PartyRole <951> entries. |
| [949](tags/949-Nested3PartyID.md) | [Nested3PartyID](tags/949-Nested3PartyID.md) | PartyID value within a "third instance" Nested repeating group. |
| [950](tags/950-Nested3PartyIDSource.md) | [Nested3PartyIDSource](tags/950-Nested3PartyIDSource.md) | PartyIDSource value within a "third instance" Nested repeating group. |
| [951](tags/951-Nested3PartyRole.md) | [Nested3PartyRole](tags/951-Nested3PartyRole.md) | PartyRole value within a "third instance" Nested repeating group. |
| [952](tags/952-NoNested3PartySubIDs.md) | [NoNested3PartySubIDs](tags/952-NoNested3PartySubIDs.md) | Number of Nested3PartySubIDs <953> entries. |
| [953](tags/953-Nested3PartySubID.md) | [Nested3PartySubID](tags/953-Nested3PartySubID.md) | PartySubID value within a "third instance" Nested repeating group. |
| [954](tags/954-Nested3PartySubIDType.md) | [Nested3PartySubIDType](tags/954-Nested3PartySubIDType.md) | PartySubIDType value within a "third instance" Nested repeating group. |
| [955](tags/955-LegContractSettlMonth.md) | [LegContractSettlMonth](tags/955-LegContractSettlMonth.md) | Specifies when the contract (i.e. MBS/TBA) will settle. |
| [956](tags/956-LegInterestAccrualDate.md) | [LegInterestAccrualDate](tags/956-LegInterestAccrualDate.md) | The start date used for calculating accrued interest on debt instruments which are being sold between interest payment dates. Often but not always the same as the IssueDate (225) and the DatedDate (873) |
