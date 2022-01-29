import dashboardBackground from '../assets/dashboard_background.jpg';
import knightsBackground from '../assets/knights_background.jpg';
import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";
import ResponsiveAppBar from '../components/appbar';

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
    return(
        <div>
            <div style={{backgroundImage: `linear-gradient(to top, rgba(0, 0, 0, 0), rgba(0, 0, 0, 100)), 
            url(${backgroundImage})`,
                backgroundSize: 'cover',
                backgroundRepeat: 'no-repeat',
                }}>
          <ResponsiveAppBar />
            <h1>Login</h1>
            <form>
                
                <input type="submit" value="Login" />
            </form>
        </div>
        </div>      
    )
}

export default Login;