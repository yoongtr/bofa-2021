# USAGE: uvicorn gtt_check:api --reload --port 8000
import json
import typer
from fastapi import FastAPI

app = typer.Typer()
api = FastAPI()
trade_data = "gtt_trade_data.json"
api_data = "gtt_api_data.json"

# Case query by date
def query_date(input_date: str, trade_data: str, apis):
    
    trades_by_date = [] # All trades from the given date query

    with open(f"{trade_data}", 'r') as f:
        for line in f.readlines():
            line_dict = json.loads(line)
            if line_dict.get("date") == input_date:
                trades_by_date.append(line_dict)
    # print(len(trades_by_date), trades_by_date)
    
    failed_gtt = gtt_check(trades_by_date, apis, "case_date")
    if len(failed_gtt)==0:
        displayed_json = [{"client_id":"pass"}]
    else:
        displayed = {}
        for item in failed_gtt:
            displayed.update({item.get("client_id") : {item.get("trade_details").get("regulatoryReportingDetails").get("reportingCounterpartyID") : {"docs":set(), "trades":[]}}})
        
        for item in failed_gtt:
            entity = item.get("trade_details").get("regulatoryReportingDetails").get("reportingCounterpartyID")
            displayed[item.get("client_id")][entity]["docs"].add(item.get("api_details").get("documentId"))
            displayed[item.get("client_id")][entity]["trades"].append(item.get("trade_details").get("tradeID"))
        # print(displayed)
        
        displayed_json = []
        for key, val in displayed.items():
            for k,v in val.items():
                displayed_json.append({"clientid": key,
                                        "fnb_entity": k,
                                        "docs": v["docs"],
                                        "trades": v["trades"]})

    return displayed_json 

# Case query by tradeID
def query_tradeid(trade_id: str, trade_data: str, apis):
    
    trades_by_tradeid = []

    with open(f"{trade_data}", 'r') as f:
        for line in f.readlines():
            line_dict = json.loads(line)
            if line_dict.get("tradeID") == trade_id:
                trades_by_tradeid.append(line_dict)
    
    failed_gtt = gtt_check(trades_by_tradeid, apis, "case_tradeid")

    displayed = {}
    if len(failed_gtt)==0:
        displayed = [{"client_id":"pass"}]
    else:
        failed_trade = failed_gtt[0]
        displayed.update({"client_id" : failed_trade.get("client_id"),
                        "fnb_entity": failed_trade.get("trade_details").get("regulatoryReportingDetails").get("reportingCounterpartyID"), 
                        "docs": failed_trade.get("api_details").get("documentId"),
                        "trade_id": failed_trade.get("trade_details").get("tradeID")})
        displayed = [displayed]

    return displayed

# Case query by clientID
def query_clientid(client_id: str, trade_data: str, apis):

    trades_by_clientid = []

    with open(f"{trade_data}", 'r') as f:
        for line in f.readlines():
            line_dict = json.loads(line)
            if line_dict.get("regulatoryReportingDetails").get("counterpartyID") == client_id:
                trades_by_clientid.append(line_dict)
    
    failed_gtt = gtt_check(trades_by_clientid, apis, "case_clientid")

    if len(failed_gtt)==0:
        displayed_json = [{"fnb_entity":"pass"}]
    else:
        displayed = {}
        for item in failed_gtt:
            displayed.update({item.get("trade_details").get("regulatoryReportingDetails").get("reportingCounterpartyID"): {"docs": set(), "trades":[]}})
        
        for item in failed_gtt:
            displayed[item.get("trade_details").get("regulatoryReportingDetails").get("reportingCounterpartyID")]["docs"].add(item.get("api_details").get("documentId"))
            displayed[item.get("trade_details").get("regulatoryReportingDetails").get("reportingCounterpartyID")]["trades"].append(item.get("trade_details").get("tradeID"))
        
        displayed_json = []
        for key, val in displayed.items():
            displayed_json.append({"fnb_entity": key,
                                    "docs": val["docs"],
                                    "trades": val["trades"]})

    return displayed_json

# GTT check, return all details of trades and apis that failed GTT
def gtt_check(trades_to_check, apis, query_case):
    # Check only trades meeting criteria
    meet_criteria = []
    for item in trades_to_check:
        if (item["regulation"]=="SFT_REPORTING" 
            and item["reportingSide"]=="FIRM"
            and item["jurisdiction"] in ["UK","EU"]
            and item["securitiesFinancingTransactionType"] in ["SECURITIES_LENDING", "REPURCHASE", "MARGIN_LENDING", "BUY_BACK"]
            and item["regulatoryReportingDetails"]["reportingCounterpartyID"] in ["FNB-UK", "FNB-EU"]
            ):
            meet_criteria.append(item)

    failed_gtt = []
    for item in meet_criteria:
        item_clientid = item.get("regulatoryReportingDetails").get("counterpartyID")
        item_entityID = item.get("regulatoryReportingDetails").get("reportingCounterpartyID")
        for i in apis.get(item_clientid):
            if (i.get("entityId") == item_entityID
                and i.get("status") == "RED"):
                failed_gtt.append({"client_id" : item_clientid,
                                    "trade_details" : item,
                                    "api_details": i})

    return failed_gtt

# Main function
def run_app(query_case, query_key):
    data = {"apis": {},
            "trades": {}}

    # API data table unique key is clientid
    with open(f"{api_data}", 'r') as f:
        for line in f.readlines():
            line_dict = json.loads(line)
            data["apis"].update(line_dict)

    # Check which query case and call appropriate query function
    if query_case=="date":
        result = query_date(query_key, trade_data, data["apis"])
    elif query_case=="tradeid":
        result = query_tradeid(query_key, trade_data, data["apis"])
    elif query_case=="clientid":
        result = query_clientid(query_key, trade_data, data["apis"])

    return result

@api.get("/trades/{query_case}/{query_key}")
def api_integrate(query_case: str, query_key: str):
    return run_app(query_case, query_key)



@api.get("/trades")
def read_trades():
    trades = []
    with open(f"{trade_data}", 'r') as f:
        for line in f.readlines():
            line_dict = json.loads(line)
            trades.append(line_dict)
    return trades

@api.get("/apis")
def read_apis():
    apis = {}
    with open(f"{api_data}", 'r') as f:
        for line in f.readlines():
            line_dict = json.loads(line)
            apis.update(line_dict)
    return apis


if __name__ == "__main__":
    # app()
    # run_app("date","20210607")
    pass
