import tempLogo from '../assets/seal.png';
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
                <h2 style={{color:'white'}}>This is a medieval postcard generator.</h2>
                <h2 style={{color:'white'}}>Our team made this :)</h2>
            </div>
        </div>
    );
}
export default Home;