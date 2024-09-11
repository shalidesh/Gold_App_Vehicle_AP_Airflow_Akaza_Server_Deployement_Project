import React from 'react'
import './news.css'
import TopBar from '../components/TopBar'
import Footer from '../components/Footer'
import LeftBar from '../components/LeftBar'
import CustomerForm from '../components/CustomerForm'

function Customer() {
  return (

    <div id="wrapper">

        <LeftBar/>

        <div id="content-wrapper" className="d-flex flex-column" style={{paddingLeft:'220px'}}>
            <div id="content">

                <TopBar/>
                <CustomerForm />
 
            
            </div>
            
            <Footer/>
        </div>

    </div>
   
  )
}

export default Customer