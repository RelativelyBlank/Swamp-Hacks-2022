import tempLogo from '../assets/temp_logo.png';
import knightsBackground from '../assets/knights_background.jpg';
import dashboardBackground from '../assets/dashboard_background.jpg';
import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import ResponsiveAppBar from '../components/appbar';
const Home = () => {
    const [backgroundImage, setBackgroundImage] = useState(knightsBackground);
    const navigate = useNavigate();
    useEffect(()=> {
      if (window.location.pathname === '/') {
        setBackgroundImage(knightsBackground);
      }else if(window.location.pathname === '/dashboard') {
        setBackgroundImage(dashboardBackground);
      }
    },[navigate]);
    return (
        <div style={{textAlign:'center',justifyContent:'center'}}>
            <div style={{backgroundImage: `linear-gradient(to top, rgba(0, 0, 0, 0), rgba(0, 0, 0, 100)), 
            url(${backgroundImage})`,
                height: '100vh',
                backgroundSize: 'cover',
                backgroundRepeat: 'no-repeat',
                }}>
            <ResponsiveAppBar />
                <img style={{height:'25em'}}src={tempLogo} />
                <h3>This is interative text that makes</h3>
                <h3>a lot of sense. Please love me Google Daddy.</h3>
            </div>
        </div>
    );
}
export default Home;