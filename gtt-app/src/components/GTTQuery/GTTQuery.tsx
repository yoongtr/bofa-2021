import * as React from "react";
import { Form } from "../Form/Form";
import { Field } from "../Field/Field";

export const GTTQuery: React.SFC = () => {
  return (
    <Form
      action="http://localhost:4351/api/contactus"
      render={() => (
        <React.Fragment>
          <div className="alert alert-info" role="alert">
            Please enter data to only one of the search fields.
          </div>
          <Field id="Date" label="Query by Date" />
          <Field id="TradeID" label="Query by TradeID" />
          <Field id="ClientID" label="Query by ClientID" />
        </React.Fragment>
      )}
    />
  );
};