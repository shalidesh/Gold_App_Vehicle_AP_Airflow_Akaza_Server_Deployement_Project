import React, { useState, useEffect } from 'react';
import Plot from 'react-plotly.js';
import axios from "axios";
import ForecastTable from './ForecastTable';

function ForecastPlotDate(startDate) {

  const [graphdata, setGraphData] = useState([]);
  const [lastdata, setLastData] = useState({});
  const [spin, setSpin] = useState(false);


  useEffect(() => {

    const fetchData = async () => {

      console.log(startDate.startDate);
      setSpin(true)

      try {
        const response = await axios.post(`/comparison`,{
          "date":startDate.startDate
        });
        setGraphData(response.data); 
        setLastData(response.data[response.data.length - 1]);
        setSpin(false)

      } catch (error) {
        console.error('Error:', error);
      }
    };

    fetchData();
    
  }, [startDate]);

  const plotData = [
    {
      x: graphdata.map(data => data.date),
      y: graphdata.map(data => data.yhat_manipulation_smooth),
      type: 'scatter',
      mode: 'lines',
      name: 'Forecast',
      line: {color: 'blue'},
    },
    // {
    //   x: graphdata.map(data => data.ds),
    //   y: graphdata.map(data => data.yhat_lower_manipulation_smooth),
    //   type: 'scatter',
    //   mode: 'lines',
    //   name: 'Lower Bound',
    //   line: {color: 'red',dash: 'dot'},
    // },
    // {
    //   x: graphdata.map(data => data.ds),
    //   y: graphdata.map(data => data.yhat_upper_manipulation_smooth),
    //   type: 'scatter',
    //   mode: 'lines',
    //   name: 'Upper Bound',
    //   line: {color: 'green',dash: 'dot'},
    // }
  ];

  return (
      <div>
        {spin ? (
          <div className="d-flex justify-content-center">
          <div className="spinner-border text-primary" role="status" style={{width: '3rem', height: '3rem'}}>
            <span className="sr-only">Loading...</span>
          </div>
        </div>
        ) : (
          <>
            <Plot
              data={plotData}
              layout={ {width: 1000, height: 600, title: 'Gold Price Forecast'} }
            />
            <p><b>Date</b> - Forecast Price Captured Date</p>
            <p><b>Forecasted Price(Rs)</b> - Captured exact price on Selected Date</p>
            {/* <p><b>Upper Bound(Rs)</b> - Captured Upper bound Price on Selected Date</p>
            <p><b>Lower Bound(Rs)</b>  - Captured Lower bound Price on Selected Date</p> */}
            <ForecastTable data={graphdata.slice(-90)} />
          </>
        )}
      </div>
      
  )
  
}

export default ForecastPlotDate;
