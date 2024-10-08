import React, { useState,useEffect} from 'react';
import Pagination from 'react-bootstrap/Pagination';

function ForecastTableXgBoost({ data}) {

    console.log(data);

    const [currentPage, setCurrentPage] = useState(1);
    const [itemsPerPage, setItemsPerPage] = useState(20);

    const reversedData = [...data].reverse();

    // Calculate the number of pages
    const pageCount = Math.ceil(reversedData.length / itemsPerPage);

    // Create an array of page numbers
    let pages = [];
    for (let i = 1; i <= pageCount; i++) {
        pages.push(i);
    }

    // Get the items for the current page
    const indexOfLastItem = currentPage * itemsPerPage;
    const indexOfFirstItem = indexOfLastItem - itemsPerPage;
    const currentItems = reversedData.slice(indexOfFirstItem, indexOfLastItem);

  

    return (
        <div>
            <div className="row mt-5">
                <table className="table">
                    <thead className="thead-dark">
                        <tr>
                            <th scope="col">Date</th>
                            <th scope="col">Forecasted Price(Rs)</th>
                            {/* <th scope="col">Upper Bound(Rs)</th>
                            <th scope="col">Lower Bound(Rs)</th>                     */}
                        </tr>
                    </thead>
                    <tbody>
                        {currentItems.map((row, index) => (
                            <tr key={index}>
                                <th scope="row">{row.ds ? row.ds : row.Date}</th>
                                <td>{parseFloat(row.Final_Prediction).toFixed(2)}</td>
                                {/* <td>{parseFloat(row.yhat_upper_manipulation_smooth).toFixed(2)}</td>
                                <td>{parseFloat(row.yhat_lower_manipulation_smooth).toFixed(2)}</td> */}
                            </tr>
                        ))}
                    </tbody>
                </table>
            </div>

            <Pagination>
            {pages.map(number => (
                <Pagination.Item key={number} active={number === currentPage} onClick={() => setCurrentPage(number)}>
                    {number}
                </Pagination.Item>
            ))}
            </Pagination>

        </div>  
        
    )
}

export default ForecastTableXgBoost