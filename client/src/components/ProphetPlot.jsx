import React, { useState, useEffect } from 'react';
import Plot from 'react-plotly.js';
import axios from "axios";
import ForecastTable from './ForecastTable';

function ProphetPlot(startDate) {

  const [graphdata, setGraphData] = useState([]);
  const [graphdata2, setGraphData2] = useState([]);
  const [lastdata, setLastData] = useState({});
  const [spin, setSpin] = useState(false);

  const [isChecked, setIsChecked] = useState(false);

  useEffect(() => {

    const fetchData = async () => {

      console.log(startDate.startDate);
      setSpin(true)

      try {
        const response = await axios.post(`/api/forecast_prophet`,{
          "date":startDate.startDate
        });

        console.log("prophet Data is ");
        console.log(response.data)
        setGraphData(response.data); 
        setLastData(response.data[response.data.length - 1]);
        setSpin(false)

      } catch (error) {
        console.error('Error:', error);
      }
    };

    fetchData();
    
  }, [startDate]);

  const handleToggle = async (event) => {
    const checked = event.target.checked;
    setIsChecked(checked);

    try {
        const response = await axios.post('/api/real-data', {
            isChecked: checked
        });
        console.log('Response from backend:', response.data);
        setGraphData2(response.data); 
        
    } catch (error) {
        console.error('Error sending request to backend:', error);
    }
};

  const plotData = [
    {
      x: graphdata.map(data => data.ds),
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
    // },
    // ...(isChecked ? [{
    //   x: graphdata2.map(data => data.date),
    //   y: graphdata2.map(data => data.gld_price_lkr),
    //   type: 'scatter',
    //   mode: 'lines',
    //   name: 'Actual Data',
    //   line: {color: 'red', dash: 'dot'},
    // }] : [])
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
          {/* <h1 className='mt-5 mb-3'>Rs <span style={{ fontSize: '70px', fontWeight: 'bold',color: '#224abe' }}>205000</span> ({lastdata.ds})</h1> */}
            <h1 className='mt-5 mb-3'>Rs <span style={{ fontSize: '70px', fontWeight: 'bold',color: '#224abe' }}>{parseFloat(lastdata.yhat_manipulation_smooth).toFixed(2)}</span> ({lastdata.ds})</h1>
            {/* <p>Upper Bound - Rs <span style={{ fontSize: '20px', fontWeight: 'bold',color: '#224abe' }}>{parseFloat(lastdata.yhat_upper_manipulation_smooth).toFixed(2)}</span> </p>
            <p>Lower Bound - Rs  <span style={{ fontSize: '20px', fontWeight: 'bold',color: '#224abe' }}>{parseFloat(lastdata.yhat_lower_manipulation_smooth).toFixed(2)}</span></p> */}

            <div className="form-check form-switch">
            <input
                className="form-check-input bg-warning"
                type="checkbox"
                role="switch"
                id="flexSwitchCheckDefault"
                checked={isChecked}
                onChange={handleToggle}
            />
            <label className="form-check-label" htmlFor="flexSwitchCheckDefault">
                Actual Data
            </label>
        </div>

            <Plot
              data={plotData}
              layout={ {width: 1000, height: 600, title: 'Gold Price Forecast'} }
            />
            {/* {graphdata2} */}
            <ForecastTable data={graphdata.slice(-40)} />
          </>
        )}
      </div>
      
  )
  
}

export default ProphetPlot;
