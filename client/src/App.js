import { useContext, useRef } from "react";
import { Routes, Route } from "react-router-dom"
import Home from './pages/Home';
import Login from './pages/Login';
import { Context } from './context/Context';
import News from "./pages/News";
import Prophet from "./pages/Prophet";
import Lstm from "./pages/Lstm";
import Customer from "./pages/Customer";
import Register from "./pages/Register"
import Database from "./pages/Database";
import Validation from './pages/Validation';


function App() {

  const { user } = useContext(Context);

  console.log(user);

  return (
    <Routes>
        <Route path="/" element={ user ?  <Home /> : <Login /> } />
        <Route path="/news" element={user ? <News />: <Login />} />
        <Route path="/prophet" element={user ? <Prophet />: <Login />} />
        <Route path="/lstm" element={user ? <Lstm />: <Login />} />
        <Route path="/customer" element={user ? <Customer />: <Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/database" element={user ? <Database /> : <Login />} />
        <Route path="/comaparison" element={user ? <Validation /> : <Login />} />
    </Routes>
  );
 }

export default App;
