import React, { useState,useEffect } from 'react';
import { Chart, LineController, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend } from 'chart.js';
import { Line } from 'react-chartjs-2';
import Breadcrumbs from './Breadcrumbs';
import axios from "axios";

import { nissan_list } from '../constants/nissan';
import { suzuki_list } from '../constants/suzuki';
import { honda_list } from '../constants/honda';
import { toyota_list } from '../constants/toyota';
import { micro_list } from '../constants/micro';
import { yom_list } from '../constants/yom';


Chart.register(LineController, CategoryScale, LinearScale, PointElement, LineElement, Title, Tooltip, Legend);


function LineChart({id}) {

  const [year, setYear] = useState(2020);
  const [graphdata, setGraphData] = useState([]);
  const [regUnReg, setRegUnReg] = useState('REG');

  const models = {
    'Nissan':nissan_list ,
    'Suzuki':suzuki_list,
    'Toyota': toyota_list,
    'Honda': honda_list,
    'MICRO': micro_list
  };

  const [model, setModel] = useState('Nissan');
  const [subModel, setSubModel] = useState(models[model][0]);


  useEffect(() => {
    setSubModel(models[model][0]);
  }, [model]);

  useEffect(() => {

    const fetchData = async () => {

      try {
        const response = await axios.post(`/api/graphs/${id}`, {
          regUnReg,
          model,
          year,
          subModel,
        });

        setGraphData(response.data);
        console.log(graphdata);

      } catch (error) {
        console.error('Error:', error);
      }

    };

    fetchData();

    
  }, []);

     // Function to handle search button click
     const handleSubmit = async (e) => {

      e.preventDefault();
      try {
        const response = await axios.post(`/api/graphs/${id}`, {
          regUnReg,
          model,
          year,
          subModel,
        });

        setGraphData(response.data);
        console.log(graphdata);
      } catch (error) {
        console.error('Error:', error);
      }
    };

      const idMap = {
          'fastmoving': 'FAST MOVING',
          'minicar':'MINI CAR',
          'normalcar':'NORMAL CAR',
          'suvcar':' SUV CAR',
          'hybrid':'HYBRID'
      };


    const breadcrumbs = [
        { label: 'Home', link: '/'},
        { label: `${id}`, link: `/graphs/${id}`},
        ];

    const options = {
        responsive: true,
        plugins: {
          legend: {
            position: 'top',
          },
        },
      };

    let priceData = graphdata.map(item => item.PRICE);
      
    const labels = ['January', 'February', 'March', 'April', 'May', 'June', 'July','Auguest','Septhember','Octomber','November','December'];
      
    const data = {
        labels,
        datasets: [
          {
            label: '',
            data: priceData,
            borderColor: 'rgb(255, 99, 132)',
            backgroundColor: 'rgba(255, 99, 132, 0.5)',
          },
        ],
      };

      
  return (

    <div className="container">

        <h1 className='mt-2 mb-3'><strong style={{color: 'black'}}>{idMap[id]}</strong> VEHICLE PRICE MOVEMENT </h1>

        <Breadcrumbs breadcrumbs={breadcrumbs} />

        <div class="row">

            <div className="btn-group ml-0">
                <button type="button" className="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                {regUnReg} 
                </button>
                <div className="dropdown-menu dropdown-menu-right" style={{
                                      zIndex: 9999,           
                            }}>
                  <button className="dropdown-item" type="button" onClick={() => setRegUnReg('REG')}>Registered</button>
                  <button className="dropdown-item" type="button" onClick={() => setRegUnReg('UNREG')}>Un-Registered</button>
                </div>
              </div>

            <div className="btn-group ml-3">
              <button type="button" className="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                  {model}
              </button>
              <div className="dropdown-menu dropdown-menu-right"   style={{
                                      height: 'auto',
                                      maxHeight: '200px',
                                      overflowX: 'hidden',
                                      zIndex: 9999,           
                            }}>
                {Object.keys(models).map((model, index) => (
                  <button key={index} className="dropdown-item" type="button" onClick={() => setModel(model)}>{model}</button>
                ))}
              </div>
            </div>

            <div className="btn-group ml-3" >
            <button type="button" className="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                {year}
            </button>
            <div className="dropdown-menu dropdown-menu-right"   style={{
                                      height: 'auto',
                                      maxHeight: '200px',
                                      overflowX: 'hidden',
                                      zIndex: 9999,           
                            }}>
                         {yom_list.map((item, index) => (
                          <button className="dropdown-item" type="button" onClick={() => setYear(item)}>{item}</button>
                              
                          ))}   
            </div>
            </div>

            <div className="btn-group ml-3">
            <button type="button" className="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                {subModel}
            </button>
            <div className="dropdown-menu dropdown-menu-right"   style={{
                                      height: 'auto',
                                      maxHeight: '200px',
                                      overflowX: 'hidden',
                                      zIndex: 9999,
                                      
                            }}>
              {models[model].map((subModel, index) => (
                <button key={index} className="dropdown-item" type="button" onClick={() => setSubModel(subModel)}>{subModel}</button>
              ))}
            </div>
            </div>

            <button type="submit" class="btn btn-primary ml-5" onClick={handleSubmit}>SEARCH</button>

        </div>

        <div className="row mt-5">

            <Line options={options} data={data} />

        </div>

        

    </div>
    
  );
}

export default LineChart;
