import { useState } from "react";
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import ForecastPlotDate from "./ForecastPlotDate";

function ValidationPage() {

    const [startDate, setStartDate] = useState(new Date());

    // Define the minimum and maximum selectable dates
    const minDate = new Date('2024-09-09');
    const maxDate = new Date();
    
    return (
      <div className='container ml-5'>

            <div className="row">
              <div className="col-4">
                <h5>Select the Future Date</h5>
              </div>
                  
            </div>
            <div className="row">
            
                <div className="col-4">
                  <DatePicker 
                      selected={startDate} 
                      onChange={date => setStartDate(date)} 
                      minDate={minDate}
                      maxDate={maxDate}
                      className='form-control'
                  />

                </div>
            </div>

            <ForecastPlotDate startDate={startDate}/>
        
      </div>
    );
}

export default ValidationPage