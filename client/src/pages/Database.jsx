import React from 'react'
import LeftBar from '../components/LeftBar'
import TopBar from '../components/TopBar'
import Footer from '../components/Footer'
import DatabasePage from '../components/DatabasePage'

function Database() {
  return (
    <div id="wrapper">

        <LeftBar/>

        <div id="content-wrapper" className="d-flex flex-column" style={{paddingLeft:'220px'}}>
            <div id="content">

                <TopBar/>
                <DatabasePage/>
            </div>
            <Footer/>
        </div>
    
    </div>
  )
}

export default Database