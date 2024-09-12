import React, { useState,useEffect} from 'react';

function CustomerForm() {

  const [state, setStatus] = useState("Medical");
  const [gender, setGender] = useState("MALE");
  const [reason, setReason] = useState("Reason 1");

  const indistry_list=[
                  "Medicine",
                  "It",
                  "Engineering"]

    const gender_list=[
                      "MALE",
                      "FEMALE"
                      ]

    const reasons_list=[
                  "Reason 1",
                  "Reason 2"
                  ]
  
  return (

        <div style={{ marginTop: '50px', marginBottom: '100px', marginLeft: '200px', marginRight: '200px' }}>

          <div class="h2 text-primary" id="pageHeaderTitle">Customer Identification</div>

          <div className="row mt-5">
            <div className="col-6">

              <label>Customer Industry</label>

            </div>

            <div className="col-6">

              <div className="btn-group ">
                      <button type="button" className="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                      {state} 
                      </button>
                        <div className="dropdown-menu dropdown-menu-right"  style={{
                                      height: 'auto',
                                      maxHeight: '200px',
                                      overflowX: 'hidden',
                                      zIndex: 9999,
                                      top: '20%'
                                      
                            }}>
                              {indistry_list.map((item, index) => (
                                            <button  className="dropdown-item" type="button" onClick={() => setStatus(item)}>{item}</button>
                                            ))
                                }
                        </div>
                  </div>
              
            </div>


          </div>

          <div className="row mt-5">
            <div className="col-6">

              <label>Gender</label>

            </div>

            <div className="col-6">

              <div className="btn-group ">
                      <button type="button" className="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                      {gender} 
                      </button>
                        <div className="dropdown-menu dropdown-menu-right"  style={{
                                      height: 'auto',
                                      maxHeight: '200px',
                                      overflowX: 'hidden',
                                      zIndex: 9999,
                                      top: '20%'
                                      
                            }}>
                              {gender_list.map((item, index) => (
                                            <button  className="dropdown-item" type="button" onClick={() => setGender(item)}>{item}</button>
                                            ))
                                }
                        </div>
                  </div>
              
            </div>

          </div>

          <div className="row mt-5">
            <div className="col-6">

              <label>Pawning Reason</label>

            </div>

            <div className="col-6">

              <div className="btn-group ">
                      <button type="button" className="btn btn-secondary dropdown-toggle" data-toggle="dropdown" aria-haspopup="true" aria-expanded="false">
                      {reason} 
                      </button>
                        <div className="dropdown-menu dropdown-menu-right"  style={{
                                      height: 'auto',
                                      maxHeight: '200px',
                                      overflowX: 'hidden',
                                      zIndex: 9999,
                                      top: '20%'
                                      
                            }}>
                              {reasons_list.map((item, index) => (
                                            <button  className="dropdown-item" type="button" onClick={() => setReason(item)}>{item}</button>
                                            ))
                                }
                        </div>
                  </div>
              
            </div>

          </div>

          <button type="button" class="btn btn-primary mt-5">PREDICT</button>

          

    </div>

   
   
  )
}

export default CustomerForm