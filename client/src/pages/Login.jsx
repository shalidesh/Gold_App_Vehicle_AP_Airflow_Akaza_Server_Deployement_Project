import axios from "axios";
import { useContext, useRef ,useState} from "react";
import { Link } from "react-router-dom";
import { Context } from "../context/Context";

function Login() {

    const userRef = useRef();
    const passwordRef = useRef();
    const { dispatch, isFetching } = useContext(Context);
    const [error, setError] = useState(null); 


    const handleSubmit = async (e) => {
        e.preventDefault();
        dispatch({ type: "LOGIN_START" });
        try {
          const res = await axios.post("/auth/login", {
            username: userRef.current.value,
            password: passwordRef.current.value,
          });
          console.log(res.data)
          dispatch({ type: "LOGIN_SUCCESS", payload: res.data });
        } catch (err) {
          dispatch({ type: "LOGIN_FAILURE" });
          setError("Invalid Username or Password, Please try again."); 
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
                        <input type="text" id="typeEmailX-2" class="form-control form-control-lg" placeholder='Username' ref={userRef} />
                    </div>

                    <div class="form-outline mb-4">
                        <input type="password" id="typePasswordX-2" class="form-control form-control-lg"  placeholder='Password' ref={passwordRef}/>
                    </div>

                    <div class="form-check d-flex justify-content-start mb-4">
                        <input class="form-check-input" type="checkbox" value="" id="form1Example3" />
                        <label class="form-check-label" for="form1Example3"> Remember password </label>
                    </div>

                    
                    <button class="btn btn-primary btn-lg btn-block" type="submit">Login</button>

                    {error && <p style={{ color: "red" }}>{error}</p>}
                    <Link className="link" to="/register">
                          <p>Already Have a Acoount?   <span>SIGNUP</span></p>                     
                    </Link>
                        
                 

                </form>

                <hr class="my-4"/>

            </div>
            </div>
        </div>
        </div>
    </div>
    </section>
  )
}

export default Login