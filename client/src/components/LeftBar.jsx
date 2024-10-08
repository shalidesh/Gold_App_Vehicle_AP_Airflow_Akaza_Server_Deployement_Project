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
                        <Link to="/prophet1">
                            <a className="collapse-item" >Prophet+XgBoost</a>

                        </Link>
                        
                    </div>
                </div>
            </li>

            <li className="nav-item">
                <Link to="/news">
                    <li className="nav-item">
                        <a className="nav-link collapsed" href="#" data-toggle="collapse" data-target="#collapseUtilities"
                            aria-expanded="true" aria-controls="collapseUtilities">
                            <i className="fas fa-fw fa-wrench"></i>
                            <span>Gold News</span>
                        </a>
                        
                    </li>
                </Link>
            </li>
            
            <li className="nav-item">
                <a className="nav-link collapsed" href="#" data-toggle="collapse" data-target="#collapsePages_ai"
                    aria-expanded="true" aria-controls="collapsePages_ai">
                    <i className="fas fa-fw fa-chart-area"></i>
                    <span>AI Validation</span>
                </a>
                <div id="collapsePages_ai" className="collapse" aria-labelledby="headingPages" data-parent="#accordionSidebar">
                    <div className="bg-white py-2 collapse-inner rounded">
                        <h6 className="collapse-header">Validation Types:</h6>
                        <Link to="/database">
                            <a className="collapse-item" >Each Day Forecast</a>
                        </Link>
                        <Link to="/comaparison">
                            <a className="collapse-item" >Day Comparision</a>

                        </Link>
                        
                    </div>
                </div>
            </li>

            <li className="nav-item">
                <Link to="/customer">
                    <li className="nav-item">
                        <a className="nav-link collapsed" href="#" data-toggle="collapse" data-target="#collapseUtilities"
                            aria-expanded="true" aria-controls="collapseUtilities">
                            <i className="fas fa-fw fa-wrench"></i>
                            <span>Customer Identification</span>
                        </a>
                        
                    </li>
                </Link>

            </li>
            
            <li className="nav-item">
                <Link to="/model_training">
                    <li className="nav-item">
                        <a className="nav-link collapsed" href="#" data-toggle="collapse" data-target="#collapseUtilities"
                            aria-expanded="true" aria-controls="collapseUtilities">
                            <i className="fas fa-fw fa-cogs"></i>
                            <span>Model Traning</span>
                        </a>
                        
                    </li>
                </Link>
            </li>
            
            <div className="text-center d-none d-md-inline">
                <button className="rounded-circle border-0" id="sidebarToggle"></button>
            </div>


        </ul>
    </div>
  )
}

export default LeftBar