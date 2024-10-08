import axios from "axios";
import { useContext, useRef,useState } from "react";
import { Link } from "react-router-dom";
import { Context } from "../context/Context";

function Register() {

    const [username, setUsername] = useState("");
    const [email, setEmail] = useState("");
    const [password, setPassword] = useState("");
    const [error, setError] = useState(false);
 

    const handleSubmit = async (e) => {
        e.preventDefault();
        setError(false);
        try {
          const res = await axios.post("/auth/register", {
            username,
            email,
            password,
          });

          !res.data && console.log("No responce data");
          console.log("---------responce recieved-----------");
          console.log(res.data);
          console.log("---------responce recieved-----------");
          res.data && window.location.replace("/");
        } catch (err) {
          setError(true);
        }
      };
    

  return (
    <section class="vh-100" style={{backgroundColor: '#508bfc'}}>
    <div class="container py-5 h-100">
        <div class="row d-flex justify-content-center align-items-center h-100">
        <div class="col-12 col-md-8 col-lg-6 col-xl-5">
            <div class="card shadow-2-strong" style={{borderRadius: '1rem'}}>
            <div class="card-body p-5 text-center">

                <h3 class="mb-5">Sign in</h3>

                <form  onSubmit={handleSubmit}>

                    <div class="form-outline mb-4">
                        <input type="text" id="typeUsernameX-2" class="form-control form-control-lg" placeholder='Username' onChange={(e) => setUsername(e.target.value)} />
                    </div>

                    <div class="form-outline mb-4">
                        <input type="email" id="typeEmailX-3" class="form-control form-control-lg" placeholder='Email' onChange={(e) => setEmail(e.target.value)} />
                    </div>

                    <div class="form-outline mb-4">
                        <input type="password" id="typePasswordX-2" class="form-control form-control-lg"  placeholder='Password' onChange={(e) => setPassword(e.target.value)}/>
                    </div>

                    <div class="form-check d-flex justify-content-start mb-4">
                        <input class="form-check-input" type="checkbox" value="" id="form1Example3" />
                        <label class="form-check-label" for="form1Example3"> Remember password </label>
                    </div>

                    {/* <Link className="link" to="/"> */}
                        <button class="btn btn-primary btn-lg btn-block" type="submit">Register</button>
                    {/* </Link> */}

                </form>

                <hr class="my-4"/>

                {error && <span style={{color:"red", marginTop:"10px"}}>Something went wrong!</span>}

            </div>
            </div>
        </div>
        </div>
    </div>
    </section>
  )
}

export default Register