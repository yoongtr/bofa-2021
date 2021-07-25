import * as React from "react";
import { useForm } from "react-hook-form";
import Headers from "./Header";
import "./styles.css";
import axios from 'axios';

let renderCount = 0;

type FormValues = {
  date: string;
  tradeid: string;
  clientid: string;
};

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
        var user_params = {};
        if (data.date!="" && data.clientid=="" && data.tradeid=="") {
          console.log(data.date)
          axios({
            method: 'get',
            url: '/trades/date/' + data.date
          })
          .then(
            function (response) {
              console.log(response.data)
            }
          );
        }
        else if (data.date=="" && data.tradeid!="" && data.clientid=="") {
          axios({
            method: 'get',
            url: '/trades/tradeid/' + data.tradeid
          })
          .then(
            function (response) {
              console.log(response.data)
            }
          );
        }
        else if (data.date=="" && data.tradeid=="" && data.clientid!="") {
          user_params = {
            "tradeID": data.tradeid,
          };
          axios({
          method: 'get',
          url: '/trades/clientid/' + data.clientid
        })
        .then(
          function (response) {
            console.log(response.data)
          }
        );
        }
        else {
          console.log("No data")
        }
      })}
    >
      <Headers
        renderCount={renderCount}
        description="Please enter data into only one of the search fields."
      />
      <label htmlFor="date">Query by Date:</label>
      <input
        {...register("date", { 
          maxLength: { value: 8, message: "Input date as YYYYMMDD." }
        })}
        id="date"
      />
      {errors.date && <p>{errors.date.message}</p>}

      <label htmlFor="tradeid">Query by TradeID:</label>
      <input
        id="tradeid"
        {...register("tradeid")}
      />

      <label htmlFor="clientid">Query by ClientID:</label>
      <input
        id="clientid"
        {...register("clientid")}
      />

      <input type="submit" />
    </form>
    <div>
        
    </div>
    </div>
  );
}
