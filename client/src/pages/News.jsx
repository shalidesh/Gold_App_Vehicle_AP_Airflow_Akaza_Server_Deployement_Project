import React from 'react'
import './news.css'
import TopBar from '../components/TopBar'
import Footer from '../components/Footer'
import LeftBar from '../components/LeftBar'
import NewsTitles from '../components/NewsTitles'

function News() {
  return (

    <div id="wrapper">

        <LeftBar/>

        <div id="content-wrapper" className="d-flex flex-column" style={{paddingLeft:'220px'}}>
            <div id="content">

                <TopBar/>

                <NewsTitles/>

                
            
            </div>
            
            <Footer/>
        </div>

    </div>
   
  )
}

export default News