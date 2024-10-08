import React, { useState, useEffect } from 'react';
import Plot from 'react-plotly.js';
import axios from "axios";
import ForecastTable from './ForecastTable';

function DatabaseTable(startDate) {

  const [graphdata, setGraphData] = useState([]);
  const [lastdata, setLastData] = useState({});
  const [spin, setSpin] = useState(false);


  useEffect(() => {

    const fetchData = async () => {

      console.log(startDate.startDate);
      setSpin(true)

      try {
        const response = await axios.post(`/database`,{
          "date":startDate.startDate
        });

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
            <ForecastTable data={graphdata.slice(-40)} />
          </>
        )}
      </div>
      
  )
  
}

export default DatabaseTable;
