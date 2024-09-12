import React, { useEffect, useState } from 'react';
import axios from 'axios';
import Breadcrumbs from '../components/Breadcrumbs'
import ChartViewer from '../components/ChartViewer';

function Dashboard() {

    const [price, setPrice] = useState({

        'bid':"0",
        'ask':"0",
        'change':"0",
        'performance':"0"
    });

    useEffect(() => {
        // Fetch the gold price every 5 minute
        const interval = setInterval(async () => {  // Declare the function as async
            try {
                const response = await axios.get('/api/gold_price');
                console.log(response.data);
                setPrice(response.data);          
            } catch (error) {
                console.log("Error:", error);
            }
        }, 300000);  // 60000 milliseconds = 1 minute
    
        // Clear the interval when the component unmounts
        return () => clearInterval(interval);
    }, [price]);

    
    const breadcrumbs = [
        { label: 'Home', link: '/'},
        { label: 'Products', link: '/vehicle-price' },
        ];
    return (

    <div className="container-fluid"  style={{ marginTop: '10px', marginBottom: '10px', marginLeft: '20px', marginRight: '20px' }}>

        <Breadcrumbs breadcrumbs={breadcrumbs} />

    
        <div className="row" style={{ marginTop: '10px', marginBottom: '10px', marginLeft: '20px', marginRight: '20px' }}>

            <div className="col-xl-3 col-md-6 mb-4">
                <div className="card border-left-primary shadow h-100 py-2 bg-info">
                    <div className="card-body">
                        <div className="row no-gutters align-items-center">
                            <div className="col mr-2 ml-3">
                                <div className="text-xs font-weight-bold text-primary text-uppercase mb-1">
                                BID Gold Price(USD)</div>
                                <div className="h5 mb-0 font-weight-bold text-gray-800">{price.bid} per ounce</div>
                            </div>
                            <div className="col-auto">
                                <i className="fas fa-dollar-sign fa-2x text-gray-300"></i>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div className="col-xl-3 col-md-6 mb-4">
                <div className="card border-left-primary shadow h-100 py-2 bg-info">
                    <div className="card-body">
                        <div className="row no-gutters align-items-center">
                            <div className="col mr-2 ml-3">
                                <div className="text-xs font-weight-bold text-primary text-uppercase mb-1">
                                ASK Gold Price(USD)</div>
                                <div className="h5 mb-0 font-weight-bold text-gray-800">{price.ask} per ounce</div>
                            </div>
                            <div className="col-auto">
                                <i className="fas fa-dollar-sign fa-2x text-gray-300"></i>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div className="col-xl-3 col-md-6 mb-4">
                <div className="card border-left-primary shadow h-100 py-2 bg-info">
                    <div className="card-body">
                        <div className="row no-gutters align-items-center">
                            <div className="col mr-2 ml-3">
                                <div className="text-xs font-weight-bold text-primary text-uppercase mb-1">
                                    Change in the Price(+/-)</div>
                                <div className="h5 mb-0 font-weight-bold text-gray-800">{price.change}</div>
                            </div>
                            <div className="col-auto">
                                <i className="fas fa-dollar-sign fa-2x text-gray-300"></i>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

            <div className="col-xl-3 col-md-6 mb-4">
                <div className="card border-left-primary shadow h-100 py-2 bg-info">
                    <div className="card-body">
                        <div className="row no-gutters align-items-center">
                            <div className="col mr-2 ml-3">
                                <div className="text-xs font-weight-bold text-primary text-uppercase mb-1">
                                percentage change in the price</div>
                                <div className="h5 mb-0 font-weight-bold text-gray-800">{price.performance} %</div>
                            </div>
                            <div className="col-auto">
                                <i className="fas fa-dollar-sign fa-2x text-gray-300"></i>
                            </div>
                        </div>
                    </div>
                </div>
            </div>

        </div>

        <div className="row">
            <ChartViewer />
        </div>

    </div>   
  )
}

export default Dashboard