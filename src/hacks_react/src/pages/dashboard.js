import { Button, Typography } from '@mui/material';
import { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import dashboardBackground from '../assets/dashboard_background.jpg';
import knightsBackground from '../assets/knights_background.jpg';
import woodBackground from '../assets/wood_background.jpg';
import ResponsiveAppBar from '../components/appbar';

const Dashboard = () => {
    const [backgroundImage, setBackgroundImage] = useState(knightsBackground);
    const navigate = useNavigate();
    useEffect(()=> {
      if (window.location.pathname === '/') {
        setBackgroundImage(knightsBackground);
      }else if(window.location.pathname === '/dashboard' || window.location.pathname === '/dashboard/#') {
        setBackgroundImage(dashboardBackground);
      }
    },[navigate]);
    return (
        <div>
            <div style={{backgroundImage: `linear-gradient(to top, rgba(0, 0, 0, 0), rgba(0, 0, 0, 100)), 
            url(${backgroundImage})`,
                backgroundSize: 'cover',
                backgroundRepeat: 'no-repeat',
                }}>
          <ResponsiveAppBar />
          <div style={{
              justifyContent:'center',
              display:'flex',
              textAlign: 'center',
              minHeight: '100vh',
              }}>
            <div>
                <h1 style={{fontWeight:'bold',color:'white'}}>Welcome Back,</h1>
                <h1 style={{fontWeight:'bold',color:'white'}}>{localStorage.getItem('token')}</h1>
                <div>
                    <Button style={{
                        margin: '5em',
                        width:'300px',
                        height: '80px',
                        borderRadius: '100px',
                        backgroundColor: '#aa6c39'
                    }} 
                    onClick={()=>{
                        navigate('/postcards')
                    }}
                    variant="contained">
                        <Typography style={{
                            fontSize: '25px',
                        }}>
                        My Postcards
                        </Typography></Button>
                    <Button style={{
                        margin: '5em',
                        width:'300px',
                        height: '80px',
                        borderRadius: '100px',
                        backgroundColor: '#aa6c39'
                    }} 
                    onClick={()=>{
                        navigate('/create')
                    }}
                    variant="contained">
                        <Typography style={{
                            fontSize: '25px',
                        }}>
                        + Create Something New
                    </Typography>
                    </Button>
                </div>
            </div>
          </div>
        </div>
        </div>
    );
}
export default Dashboard;