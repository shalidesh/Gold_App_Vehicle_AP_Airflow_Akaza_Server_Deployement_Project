import { useState } from "react";
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import ProphetXgboostPlot from "./ProphetXgboostPlot";

function ProphetXgboostCharts() {


    const [startDate, setStartDate] = useState(new Date());
    
    return (
      <div className='container ml-5'>
        <div className="row">
        <div className="alert alert-danger mt-5" role="alert">
                Model is Updated Upto 2024-10-21 !
            </div>
            <div className="col-4">
            <DatePicker 
                selected={startDate} 
                onChange={date => setStartDate(date)} 
                className='form-control'
            />

            </div>
           
        </div>
        
        <ProphetXgboostPlot startDate={startDate}/>
        
      </div>
    );
}

export default ProphetXgboostCharts