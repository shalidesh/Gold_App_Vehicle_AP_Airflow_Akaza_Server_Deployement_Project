import { useState } from "react";
import DatePicker from 'react-datepicker';
import 'react-datepicker/dist/react-datepicker.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import ForecastPlot from "./ForecastPlot";

function DatabasePage() {

    // Function to get the most recent Monday
    const getLastMonday = () => {
      const today = new Date();
      const dayOfWeek = today.getDay();
      const lastMonday = new Date(today);
      lastMonday.setDate(today.getDate() - ((dayOfWeek + 6) % 7));
      return lastMonday;
    };


    const [startDate, setStartDate] = useState(getLastMonday());

    // Function to check if the date is a Tuesday
    const isTuesday = (date) => {
      return date.getDay() === 1; // 0 = Sunday, 1 = Monday, 2 = Tuesday, etc.
    };

    // Define the minimum and maximum selectable dates
    const minDate = new Date('2024-09-09');
    const maxDate = new Date();
    
    return (
      <div className='container ml-5'>

            <div className="row">
              <div className="alert alert-danger mt-5" role="alert">
                      Model is Updated Upto 2024-10-11 !
                  </div>
            </div>

            <div className="row">
              <div className="col-4">
                <h5>Select the Forecast Start Date</h5>
              </div>
                  
            </div>
            <div className="row">
            
                <div className="col-4">
                  <DatePicker 
                      selected={startDate} 
                      onChange={date => setStartDate(date)} 
                      minDate={minDate}
                      maxDate={maxDate}
                      filterDate={isTuesday}
                      className='form-control'
                  />

                </div>
            </div>
        
        <ForecastPlot startDate={startDate}/>
        
      </div>
    );
}

export default DatabasePage