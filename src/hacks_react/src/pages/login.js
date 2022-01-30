import dashboardBackground from '../assets/dashboard_background.jpg';
import knightsBackground from '../assets/knights_background.jpg';
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import ResponsiveAppBar from '../components/appbar';
import axios from 'axios';

const Login = () => {
    const [backgroundImage, setBackgroundImage] = useState(knightsBackground);
    const navigate = useNavigate();
    useEffect(()=> {
      if (window.location.pathname === '/') {
        setBackgroundImage(knightsBackground);
      }else if(window.location.pathname === '/dashboard') {
        setBackgroundImage(dashboardBackground);
      }
    },[navigate]);

    useEffect(()=> {
      window.open('http://localhost:5000/login')
      localStorage.setItem('token',"smhuerta26@gmail.com");
    },[])

    return(
        <div>
            <div style={{backgroundImage: `linear-gradient(to top, rgba(0, 0, 0, 0), rgba(0, 0, 0, 100)), 
            url(${backgroundImage})`,
                height:'100vh',
                backgroundSize: 'cover',
                backgroundRepeat: 'no-repeat',
                }}>
          <ResponsiveAppBar />
            <form>
                
            </form>
        </div>
        </div>      
    )
}

export default Login;