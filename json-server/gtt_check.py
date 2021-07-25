# USAGE: uvicorn gtt_check:api --reload --port 3000
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

    return failed_gtt

# Case query by tradeID

def query_tradeid(trade_id: str, trade_data: str, apis):
    
    trades_by_tradeid = []

    with open(f"{trade_data}", 'r') as f:
        for line in f.readlines():
            line_dict = json.loads(line)
            if line_dict.get("tradeID") == trade_id:
                trades_by_tradeid.append(line_dict)
    # print(trades_by_tradeid)
    
    failed_gtt = gtt_check(trades_by_tradeid, apis, "case_tradeid")

    return failed_gtt 

# Case query by clientID

def query_clientid(client_id: str, trade_data: str, apis):

    trades_by_clientid = []

    with open(f"{trade_data}", 'r') as f:
        for line in f.readlines():
            line_dict = json.loads(line)
            if line_dict.get("regulatoryReportingDetails").get("counterpartyID") == client_id:
                trades_by_clientid.append(line_dict)
    
    # print(trades_by_clientid)
    
    failed_gtt = gtt_check(trades_by_clientid, apis, "case_clientid")

    return failed_gtt

# GTT check based on given criteria

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
    # print(len(meet_criteria), meet_criteria)

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

    if query_case == "case_date": #to_add
        pass

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

if __name__ == "__main__":
    # app()
    pass
