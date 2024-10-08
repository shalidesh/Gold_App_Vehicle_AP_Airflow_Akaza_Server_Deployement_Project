import React, { useState, useEffect, useCallback } from "react";
import FusionCharts from "fusioncharts";
import TimeSeries from "fusioncharts/fusioncharts.timeseries";
import ReactFC from "react-fusioncharts";
import schema from "./schema";

ReactFC.fcRoot(FusionCharts, TimeSeries);

let currentDate = new Date();
let formattedDate = currentDate.getFullYear() + '-' + (currentDate.getMonth() + 1) + '-' + currentDate.getDate();

const chart_props = {
  timeseriesDs: {
    type: "timeseries",
    width: "100%",
    height: "600",
    dataEmptyMessage: "Fetching data...",
    dataSource: {
      caption: { text: `Gold Price Movement Untill ${formattedDate}`},
      data: null,
      yAxis: [
        {
          plot: [
            {
              value: "Price ($)"
            }
          ]
        }
      ]
    }
  }
};

  
function ChartViewer() {
  
  const [ds, setds] = useState(chart_props);

  const loadData = useCallback(async () => {
    try {
      const response = await fetch('/gold_price_history');
      const data = await response.json();
      const fusionTable = new FusionCharts.DataStore().createDataTable(
        data,
        schema
      );
      const options = { ...ds };
      options.timeseriesDs.dataSource.data = fusionTable;
      setds(options);
    } catch (err) {
      console.log(err);
    }
  }, []);

  useEffect(() => {
    console.log("render");
    loadData();
  }, [loadData]);

  return (
    <div style={{ marginTop: '10px', marginBottom: '10px', marginLeft: '0px', marginRight: '0px' }}>
      <ReactFC {...ds.timeseriesDs} />
    </div>
  );
}

export default ChartViewer;
