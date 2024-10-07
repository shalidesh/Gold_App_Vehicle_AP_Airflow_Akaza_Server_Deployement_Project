import React from 'react'
import LeftBar from '../components/LeftBar'
import TopBar from '../components/TopBar'
import Footer from '../components/Footer'
import ProphetCharts from '../components/ProphetCharts'
import ProphetXgboostCharts from '../components/ProphetXgboostCharts'

function Lstm() {
    return (
        <div id="wrapper">
    
            <LeftBar/>
    
            <div id="content-wrapper" className="d-flex flex-column" style={{paddingLeft:'220px'}}>
                <div id="content">
    
                    <TopBar/>
                    <ProphetXgboostCharts />
    
                </div>
                
                <Footer/>
            </div>
        
        </div>
      )
}

export default Lstm