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
import { TextField } from '@mui/material';
import background from '../assets/postercards_back.jpg'

export default function Postcards() {
    /*
    const getPostercards = async() => {
        return await axios.get().then(()=> {

            }
        );
    }
    */
    const navigate = useNavigate();
    const [navigateBack, setNavigateBack] = React.useState();
    const isFirstRender = React.useRef(false);
  return (
    <div style={{backgroundImage:`url(${background})`, minHeight:'100vh'}}>
      <AppBar style={{borderBottom:'2px grey solid'}}color="transparent" position="static" >
        <Toolbar variant="dense">
          <IconButton onClick={()=>{navigate('/dashboard')}}edge="start" color="inherit" aria-label="menu" sx={{ mr: 2 }}>
            <ArrowCircleLeftIcon style={{
                color:'white',
                fontSize: '60px',
            }}/>
          </IconButton>
        </Toolbar>
      </AppBar>
      <div style={{justifyContent:'center',textAlign:'center'}}>
    </div>
    </div>
  );
}