import { useState } from "react";

function ModelTraining() {

    const [alertMessage, setAlertMessage] = useState('');
    const [selectedFile, setSelectedFile] = useState(null);

    const handleFileChange = (event) => {

        const file = event.target.files[0];

        if (file && file.type === 'text/csv') {
          setSelectedFile(file);
          setAlertMessage('');
        } else {
          setSelectedFile(null);
          setAlertMessage('Please upload a CSV file.');
        }

      };

      const handleFileUpload = async () => {
        if (!selectedFile) {
          setAlertMessage('No file selected.');
          return;
        }
    
        const formData = new FormData();
        formData.append('file', selectedFile);
    
        try {
          const response = await fetch('/api/upload', {
            method: 'POST',
            body: formData,
          });
    
          const result = await response.json();
          setAlertMessage(result.message);
        } catch (error) {
          setAlertMessage('Error uploading file.');
        }
      };

  return (
    <div className='container ml-5 ' style={{paddingLeft:'220px',paddingRight:'220px',paddingTop:'150px',paddingBottom:'220px'}}>

        <div class="alert alert-primary" role="alert">
                Model is Updated Upto 2024-10-11 !
        </div>

        
        <label className="form-label mt-5" for="customFile">Upload Your Latest Dataset</label>
        <input type="file" className="form-control" id="customFile" onChange={handleFileChange} />

        <button type="button" className="mt-5 btn btn-primary" data-mdb-ripple-init onClick={handleFileUpload} disabled={!selectedFile}>Update Database</button>

        {alertMessage && (
            <div className="alert alert-danger mt-5" role="alert">
            {alertMessage}
            </div>
        )}


    </div>
  )
}

export default ModelTraining