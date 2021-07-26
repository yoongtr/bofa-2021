
# from itertools import groupby
# from operator import itemgetter

trades = [{'regulatoryReportingDetails': {'counterpartyID': 'CLIENT-TEQ17', 'reportingCounterpartyID': 'FNB-UK'}, 'date': '20210607', 'tradeID': 'YM76FS1AQT-10000', 'reportingSide': 'FIRM', 'regulation': 'SFT_REPORTING', 'jurisdiction': 'SG', 'securitiesFinancingTransactionType': 'SECURITIES_LENDING'}, 
{'regulatoryReportingDetails': {'counterpartyID': 'CLIENT-TEQ16', 'reportingCounterpartyID': 'FNB-EU'}, 'date': '20210607', 'tradeID': 'P98ICK2EYR-10001', 'reportingSide': 'FIRM', 'regulation': 'SFT_REPORTING', 'jurisdiction': 'UK', 'securitiesFinancingTransactionType': 'MARGIN_LENDING'}, 
{'regulatoryReportingDetails': {'counterpartyID': 'CLIENT-JHB19', 'reportingCounterpartyID': 'FNB-EU'}, 'date': '20210607', 'tradeID': 'OJKI63WE0Y-10002', 'reportingSide': 'FIRM', 'regulation': 'SFT_REPORTING', 'jurisdiction': 'EU', 'securitiesFinancingTransactionType': 'REPURCHASE'}, 
{'regulatoryReportingDetails': {'counterpartyID': 'CLIENT-WXS14', 'reportingCounterpartyID': 'FNB-EU'}, 'date': '20210607', 'tradeID': 'P98ICK2EYR-10003', 'reportingSide': 'FIRM', 'regulation': 'SFT_REPORTING', 'jurisdiction': 'UK', 'securitiesFinancingTransactionType': 'REPURCHASE'}, 
{'regulatoryReportingDetails': {'counterpartyID': 'CLIENT-MFC19', 'reportingCounterpartyID': 'FNB-UK'}, 'date': '20210608', 'tradeID': 'P98ICK2EYR-10004', 'reportingSide': 'FIRM', 'regulation': 'SFT_REPORTING', 'jurisdiction': 'EU', 'securitiesFinancingTransactionType': 'BUY_BACK'}, 
{'regulatoryReportingDetails': {'counterpartyID': 'CLIENT-9YL13', 'reportingCounterpartyID': 'FNB-EU'}, 'date': '20210608', 'tradeID': 'P98ICK2EYR-10005', 'reportingSide': 'FIRM', 'regulation': 'SFT_REPORTING', 'jurisdiction': 'EU', 'securitiesFinancingTransactionType': 'BUY_BACK'}, 
{'regulatoryReportingDetails': {'counterpartyID': 'CLIENT-TEQ15', 'reportingCounterpartyID': 'FNB-EU'}, 'date': '20210609', 'tradeID': 'RVC21ZSH5L-10006', 'reportingSide': 'FIRM', 'regulation': 'SFT_REPORTING', 'jurisdiction': 'EU', 'securitiesFinancingTransactionType': 'SECURITIES_LENDING'}, 
{'regulatoryReportingDetails': {'counterpartyID': 'CLIENT-9YL14', 'reportingCounterpartyID': 'FNB-UK'}, 'date': '20210609', 'tradeID': 'P4U28LL7BV-10007', 'reportingSide': 'FIRM', 'regulation': 'SFT_REPORTING', 'jurisdiction': 'SG', 'securitiesFinancingTransactionType': 'SECURITIES_LENDING'}, 
{'regulatoryReportingDetails': {'counterpartyID': 'CLIENT-WXS11', 'reportingCounterpartyID': 'FNB-EU'}, 'date': '20210610', 'tradeID': 'YM76FS1AQT-10008', 'reportingSide': 'CLIENT', 'regulation': 'SFT_REPORTING', 'jurisdiction': 'EU', 'securitiesFinancingTransactionType': 'MARGIN_LENDING'}, 
{'regulatoryReportingDetails': {'counterpartyID': 'CLIENT-MFC15', 'reportingCounterpartyID': 'FNB-UK'}, 'date': '20210610', 'tradeID': 'P98ICK2EYR-10009', 'reportingSide': 'FIRM', 'regulation': 'SFT_REPORTING', 'jurisdiction': 'SG', 'securitiesFinancingTransactionType': 'SECURITIES_LENDING'}]
# print(len(trades))
# trades_by_date = []

# for dt, k in groupby(sorted(trades,key=itemgetter('date')),key=itemgetter('date')):
#     maindict = {'date':dt}
#     # print(maindict)
#     for d in k:
#         print(d)
#         maindict.update(d)
#         print(maindict)
#     trades_by_date.append(d)

# print(trades_by_date)
# meet_criteria = []
# for item in trades:
#     if (item["regulation"]=="SFT_REPORTING" 
#         and item["reportingSide"]=="FIRM"
#         and item["jurisdiction"] in ["UK","EU"]
#         and item["securitiesFinancingTransactionType"] in ["SECURITIES_LENDING", "REPURCHASE", "MARGIN_LENDING", "BUY_BACK"]
#         and item["regulatoryReportingDetails"]["reportingCounterpartyID"] in ["FNB-UK", "FNB-EU"]
#         ):
#         meet_criteria.append(item)

# print(meet_criteria)
# print(len(meet_criteria))
import json
myd = {}
for i in trades:
    line_dict = i
    myd.add(line_dict)

print(myd)