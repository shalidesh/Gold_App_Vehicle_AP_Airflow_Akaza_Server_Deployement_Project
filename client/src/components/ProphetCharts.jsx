import { useState } from "react";
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import ProphetPlot from "./ProphetPlot";

function ProphetCharts() {


    const [startDate, setStartDate] = useState(new Date());
    

    return (
      <div className='container ml-5'>
        <div className="row">
           <div className="alert alert-danger mt-5" role="alert">
                Model is Updated Upto 2024-9-27 !
            </div>
            <div className="col-4">
            <DatePicker 
                selected={startDate} 
                onChange={date => setStartDate(date)} 
                className='form-control'
            />

            </div>
           
        </div>
        
        <ProphetPlot startDate={startDate}/>
        
      </div>
    );
}

export default ProphetCharts