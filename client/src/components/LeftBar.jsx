import React from 'react'
import { Link } from "react-router-dom";

function LeftBar() {
  return (
    <div>
        <ul className="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion fixed-top" id="accordionSidebar">

            <a className="sidebar-brand d-flex align-items-center justify-content-center" href="/">
                
                <div className="sidebar-brand-text mx-3">CDB GOLD</div>
            </a>

            <hr className="sidebar-divider my-0"/>

            <Link to="/">

                <li className="nav-item active">
                    <a className="nav-link">
                        <i className="fas fa-fw fa-tachometer-alt"></i>
                        <span>Dashboard</span></a>
                </li>

            </Link>

            <hr className="sidebar-divider"/>


            <div className="sidebar-heading">
                Features
            </div>

            <li className="nav-item">
                <a className="nav-link collapsed" href="#" data-toggle="collapse" data-target="#collapsePages"
                    aria-expanded="true" aria-controls="collapsePages">
                    <i className="fas fa-fw fa-chart-area"></i>
                    <span>Gold Forecast</span>
                </a>
                <div id="collapsePages" className="collapse" aria-labelledby="headingPages" data-parent="#accordionSidebar">
                    <div className="bg-white py-2 collapse-inner rounded">
                        <h6 className="collapse-header">Forecast Types:</h6>
                        <Link to="/prophet">
                            <a className="collapse-item" >Prophet</a>
                        </Link>
                        <Link to="/lstm">
                            <a className="collapse-item" >LSTM</a>

                        </Link>
                        
                    </div>
                </div>
            </li>

            <Link to="/customer">
                <li className="nav-item">
                    <a className="nav-link collapsed" href="#" data-toggle="collapse" data-target="#collapseUtilities"
                        aria-expanded="true" aria-controls="collapseUtilities">
                        <i className="fas fa-fw fa-wrench"></i>
                        <span>Customer Identification</span>
                    </a>
                    
                </li>
            </Link>

            <Link to="/news">
                <li className="nav-item">
                    <a className="nav-link collapsed" href="#" data-toggle="collapse" data-target="#collapseUtilities"
                        aria-expanded="true" aria-controls="collapseUtilities">
                        <i className="fas fa-fw fa-wrench"></i>
                        <span>Gold News</span>
                    </a>
                    
                </li>
            </Link>

            <hr className="sidebar-divider d-none d-md-block"/>

            <div className="text-center d-none d-md-inline">
                <button className="rounded-circle border-0" id="sidebarToggle"></button>
            </div>


        </ul>
    </div>
  )
}

export default LeftBar