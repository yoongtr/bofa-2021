import * as React from "react";
import { useForm } from "react-hook-form";
import axios from 'axios';
import Headers from "./Header";
import "./styles.css";
import { first } from "lodash";

type FormValues = {
  date: string;
  tradeid: string;
  clientid: string;
};

function refresh(): void {
  window.location.reload();
}

export default function App() {
  const {
    register,
    handleSubmit,
    formState: { errors }
  } = useForm<FormValues>(); 


  return (
    <div>
    <form
      onSubmit={handleSubmit((data) => {
        console.log(data);
        
        if (data.date!="" && data.clientid=="" && data.tradeid=="") {
          console.log(data.date)
          
          axios({
            method: 'get',
            url: '/trades/date/' + data.date
          })
          .then(function (response) {
            if (response.data[0].date=="pass") {
              const results = document.getElementById("results")
              const query_label = document.createElement("p")
              query_label.id = "query-label"
              query_label.textContent = "No failed GTT results for " + data.date
              results?.appendChild(query_label);
            } 

            else if (response.data[0].date=="nonexist") {
              const results = document.getElementById("results")
              const query_label = document.createElement("p")
              query_label.id = "query-label"
              query_label.textContent = data.date + " does not exist in database."
              results?.appendChild(query_label);
            } 
            
            else {
              console.log(response.data)
              const results = document.getElementById("results")
              const query_label = document.createElement("p")
              query_label.id = "query-label"
              query_label.textContent = "Failed GTT details for Date " + data.date + ":"
              results?.appendChild(query_label);

              for(var i = 0; i < response.data.length; i++) {
                var obj = response.data[i];

                const date_client = document.createElement("p")
                date_client.id = "result-header"
                date_client.textContent = "Client ID: " + obj.clientid
                results?.appendChild(date_client)

                const date_entity = document.createElement("p")
                date_entity.id = "result-header"
                date_entity.textContent = "FNB Entity: " + obj.fnb_entity
                results?.appendChild(date_entity)

                const date_docs = document.createElement("p")
                date_docs.id = "result-box"
                date_docs.textContent = "Document(s): " + obj.docs
                results?.appendChild(date_docs)

                const date_trades = document.createElement("p")
                date_trades.id = "result-box"
                date_trades.textContent = "Failed Trade ID(s): " + obj.trades
                results?.appendChild(date_trades)
              }
            }
          })
          .catch(function (error) {
            // console.log(error);
            const results = document.getElementById("results")
            const query_label = document.createElement("p")
            query_label.id = "query-error"
            query_label.textContent = "An error has occurred as below. Please contact IT."
            results?.appendChild(query_label);

            const error_text = document.createElement("p")
            error_text.id = "result-box"
            error_text.textContent = error
            results?.appendChild(error_text);
          })
        }
        else if (data.date=="" && data.tradeid!="" && data.clientid=="") {
          axios({
            method: 'get',
            url: '/trades/tradeid/' + data.tradeid
          })
          .then(function (response) {
            const results = document.getElementById("results")
            
            // console.log(response.data[0].client_id)
            if (response.data[0].tradeid=="pass") {
              const results = document.getElementById("results")
              const query_label = document.createElement("p")
              query_label.id = "query-label"
              query_label.textContent = "No failed GTT results for " + data.tradeid
              results?.appendChild(query_label);
            } 

            else if (response.data[0].tradeid=="nonexist") {
              const results = document.getElementById("results")
              const query_label = document.createElement("p")
              query_label.id = "query-label"
              query_label.textContent = data.tradeid + " does not exist in database."
              results?.appendChild(query_label);
            } 

            else {
            const query_label = document.createElement("p")
            query_label.id = "query-label"
            query_label.textContent = "Failed GTT details for TradeID: " + data.tradeid
            results?.appendChild(query_label);

            var obj = response.data[0];

            const tradeid_client = document.createElement("p")
            tradeid_client.id = "result-header"
            tradeid_client.textContent = "Client ID: " + obj.client_id
            results?.appendChild(tradeid_client)

            const tradeid_entity = document.createElement("p")
            tradeid_entity.id = "result-header"
            tradeid_entity.textContent = "Entity: " + obj.fnb_entity
            results?.appendChild(tradeid_entity)

            const tradeid_docs = document.createElement("p")
            tradeid_docs.id = "result-box"
            tradeid_docs.textContent = "Document(s): " + obj.docs
            results?.appendChild(tradeid_docs)

            const tradeid_tradeid = document.createElement("p")
            tradeid_tradeid.id = "result-box"
            tradeid_tradeid.textContent = "Trade ID: " + obj.trade_id
            results?.appendChild(tradeid_tradeid)
            }
          })
          .catch(function (error) {
            const results = document.getElementById("results")
            const query_label = document.createElement("p")
            query_label.id = "query-error"
            query_label.textContent = "An error has occurred as below. Please contact IT."
            results?.appendChild(query_label);

            const error_text = document.createElement("p")
            error_text.id = "result-box"
            error_text.textContent = error
            results?.appendChild(error_text);
          })
        }
        else if (data.date=="" && data.tradeid=="" && data.clientid!="") {
          axios({
          method: 'get',
          url: '/trades/clientid/' + data.clientid
        })
          .then(function (response) {
            if (response.data[0].clientid == "pass") {
              const results = document.getElementById("results")
              const query_label = document.createElement("p")
              query_label.id = "query-label"
              query_label.textContent = "No failed GTT results for " + data.clientid
              results?.appendChild(query_label);
            } 
            
            else if (response.data[0].clientid=="nonexist") {
              const results = document.getElementById("results")
              const query_label = document.createElement("p")
              query_label.id = "query-label"
              query_label.textContent = data.clientid + " does not exist in database."
              results?.appendChild(query_label);
            } 

            else {
              const results = document.getElementById("results")
              
              const query_label = document.createElement("p")
              query_label.id = "query-label"
              query_label.textContent = "Failed GTT details for ClientID: " + data.clientid
              results?.appendChild(query_label);
              
              for(var i = 0; i < response.data.length; i++) {
                var obj = response.data[i];

                const clientid_entity = document.createElement("p")
                clientid_entity.id = "result-header"
                clientid_entity.textContent = "FNB Entity: " + obj.fnb_entity
                results?.appendChild(clientid_entity)

                const clientid_docs = document.createElement("p")
                clientid_docs.id = "result-box"
                clientid_docs.textContent = "Document(s): " + obj.docs
                results?.appendChild(clientid_docs)

                const clientid_trades = document.createElement("p")
                clientid_trades.id = "result-box"
                clientid_trades.textContent = "Failed Trade ID(s): " + obj.trades
                results?.appendChild(clientid_trades)
              }
            }
          })
          .catch(function (error) {
            const results = document.getElementById("results")
            const query_label = document.createElement("p")
            query_label.id = "query-error"
            query_label.textContent = "An error has occurred as below. Please contact IT."
            results?.appendChild(query_label);

            const error_text = document.createElement("p")
            error_text.id = "result-box"
            error_text.textContent = error
            results?.appendChild(error_text);
          })
        }
        else {
          const results = document.getElementById("results")
          const p = document.createElement("p")
          p.textContent = "Please enter data into ONE search field with the correct query format."
          results?.appendChild(p);
        }


      })}
    >
      <Headers
        description="Please enter data into only one of the search fields."
      />
      <label htmlFor="date">Query by Date:</label>
      <input
        {...register("date", { 
          maxLength: { value: 8, message: "Input date as YYYYMMDD." }
        })}
        id="date"
        placeholder="YYYYMMDD e.g. 20210607"
      />
      {errors.date && <p>{errors.date.message}</p>}

      <label htmlFor="tradeid">Query by TradeID:</label>
      <input
        id="tradeid"
        {...register("tradeid")}
        placeholder="e.g. P98ICK2EYR-10003"
      />

      <label htmlFor="clientid">Query by ClientID:</label>
      <input
        id="clientid"
        {...register("clientid")}
        placeholder="e.g. CLIENT-WXS14"
      />

      <input type="submit" />
      <div id="centered">
        <button onClick={refresh}>Clear Results</button>
      </div>
    </form>
    <div>
      <div id="results"> 
      </div>
    </div>
    </div>
  );
}
