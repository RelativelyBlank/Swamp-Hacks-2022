import * as React from 'react';
import AppBar from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import ArrowCircleLeftIcon from '@mui/icons-material/ArrowCircleLeft';
import { useNavigate } from 'react-router-dom';
import postcardBackground from '../assets/postcard_back.jpg';
import tempSeal from '../assets/seal_temp.jpg';
import tempImage from '../assets/temp_image_postcard.jpg';

export default function CreatePostcard() {
    const navigate = useNavigate();
    const [navigateBack, setNavigateBack] = React.useState();
    const isFirstRender = React.useRef(false);
  return (
    <Box backgroundColor="black" minHeight='100vh'sx={{ flexGrow: 1 }}>
      <AppBar color="transparent" elevation={0} position="static" >
        <Toolbar variant="dense">
          <IconButton onClick={()=>{navigate('/dashboard')}}edge="start" color="inherit" aria-label="menu" sx={{ mr: 2 }}>
            <ArrowCircleLeftIcon style={{
                color:'white',
                fontSize: '60px',
            }}/>
          </IconButton>
          <Typography style={{color:'white',fontWeight:'bold'}}variant="h6" color="inherit" component="div">
            Create a Postcard
          </Typography>
        </Toolbar>
      </AppBar>
      <div style={{display:"flex", alignItems:"center",textAlign:"center",justifyContent:"center" }}>
        <div style={{
            backgroundImage: `url(${postcardBackground})`,
            backgroundSize: 'cover',
            backgroundRepeat: 'no-repeat',
            height: '500px',
            width: '900px',
            borderRadius: '10px',
        }}>
            <div style={{
                paddingLeft:'50px',
                paddingRight:'50px',
                paddingTop:'10px',
                paddingBottom:'100px',
                }}>
                    
                <div style={{justifyContent:'right',textAlign:'right'}}>
                    <img style={{maxHeight:'130px'}}src ={tempSeal} />
                </div>
            <div>
                <div style={{display:'flex'}}>
                    <img src={tempImage} style={{
                        backgroundImage: `url(${tempImage})`,
                        backgroundSize: 'contain',
                        backgroundRepeat: 'no-repeat',
                        height: '300px',
                        width: '400px',
                        borderRadius: '10px'}} />
                    <Typography style={{float:'right',textAlign:'justify', width:'100%',marginLeft:'50px'}}>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.</Typography>
                    </div>
                </div>
                <div style={{justifyContent:'right',textAlign:'right'}}>
                    Signed: [User Name]
                </div>
            </div>   
        </div>
        </div>
    </Box>
  );
}