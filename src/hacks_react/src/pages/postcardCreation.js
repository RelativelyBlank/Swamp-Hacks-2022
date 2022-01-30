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
import tempSeal from '../assets/seal.png';
import tempImage from '../assets/temp_image_postcard.jpg';
import { Button, TextField } from '@mui/material';
import background from '../assets/postercards_back.jpg'
import settings_back from '../assets/settings_background.jpg'
import axios from 'axios';

export default function CreatePostcard() {
    const navigate = useNavigate();
    const [navigateBack, setNavigateBack] = React.useState();
    const isFirstRender = React.useRef(false);
    const [searched, setSearched] = React.useState(false);
    const [imgLink, setImgLink] = React.useState();
    const [review, setReview] = React.useState({text:"", author_name:""});
    const [email, setEmail] = React.useState();
    const [number, setNumber] = React.useState();
    const [location, setLocation] = React.useState('transparent_background');
    const [date, setDate] = React.useState();
    const refSelf = React.useRef();

    const getLocation = async() => {
        return await axios.get(`http://127.0.0.1:5000/location/${location}/image`).then((val)=> {
          // log the current directory
          setImgLink(val.data);
        })
    }

    const getReview = async() => {
      return await axios.get(`http://127.0.0.1:5000/location/${location}/best_review`).then((val)=> {
        if(val.data[0] === undefined) 
          setReview("");
        else
          setReview(val.data[0]);
      })
    }

    const submitPostcard = async() => {
      setSearched(true);
      await getLocation();
      await getReview();
    }
    const sendPostcard = async() => {
      //send postcard to server
      await axios.post(`http://127.0.0.1:5000/post/upload_file`,{image_location:location+'.png', email: localStorage.getItem('token')}).then(()=>navigate('/dashboard'));
    }
    const tryRequire = () => {
      try {
        if (searched === false) 
          throw new Error("Please search for a location before submitting");
        return require(`../assets/${location}.jpg`);
      } catch (e) {
        return require(`../assets/transparent_background.jpg`);
      }
    }
    React.useEffect(()=> {

    },[])
        
    
  return (
    <div style={{backgroundImage:`url(${background})`, minHeight:'100vh'}}>
      <AppBar color="transparent" position="static" >
        <Toolbar variant="dense">
          <IconButton onClick={()=>{navigate('/dashboard')}}edge="start" color="inherit" aria-label="menu" sx={{ mr: 2 }}>
            <ArrowCircleLeftIcon style={{
                color:'white',
                fontSize: '60px',
            }}/>
          </IconButton>
        </Toolbar>
      </AppBar>
      <div ref={refSelf} style={{display:"flex", alignItems:"center",textAlign:"center",justifyContent:"center",display:'inline-block' }}>
        <div style={{
            backgroundImage: `url(${postcardBackground})`,
            backgroundSize: 'cover',
            backgroundRepeat: 'no-repeat',
            width: '900px',
            marginTop: '50px',
            borderRadius: '10px',
        }}>
            <div style={{
                paddingLeft:'50px',
                paddingRight:'50px',
                paddingTop:'10px',
                paddingBottom:'100px',
                }}>
                    
                <div style={{display:'flex'}}>
                <p style={{float:'left',textAlign:'justify', width:'100%',marginLeft:'50px', fontSize:'20px', fontWeight:'bold'}}>{email}</p>
                <p style={{float:'left',textAlign:'justify', width:'100%',marginLeft:'50px', fontSize:'20px', fontWeight:'bold'}}>{date}</p>
                <p style={{float:'left',textAlign:'justify', width:'100%',marginLeft:'50px', fontSize:'20px', fontWeight:'bold'}}>{location!=='transparent_background' ? location : ""}</p>
                <img style={{maxHeight:'130px'}}src ={tempSeal} />
                </div>
            <div>
                <div style={{display:'flex'}}>
                  <img src={tryRequire(`../assets/${location}.jpg`)} 
                  style={{
                    height: '350px',
                    width: '600px',
                    borderRadius: '10px'}} />
                    <p style={{float:'right',textAlign:'justify', width:'100%',marginLeft:'50px'}}>{searched ? `"${review?.text}" -${review?.author_name}` : ""}</p>
                    </div>
                </div>
                <div style={{justifyContent:'right',textAlign:'right'}}>
                    Signed: {localStorage.getItem('token')}
                </div>
            </div>   
        </div>
        </div>
        <div style={{justifyContent:'center',textAlign:'center',display:'inline-block',marginLeft:'5%'}}>
        <div style={{
            backgroundImage: `url(${settings_back})`,
            backgroundSize: 'contain',
            backgroundRepeat: 'no-repeat',
            height: '900px',
            width: '500px',
            marginTop: '50px',
            borderRadius: '10px',
        }}>


        <Typography style={{textAlign:'center',paddingTop:'100px', fontSize:'30px'}}>Input Values</Typography>
        <div style={{paddingTop:'30px'}}>
        <TextField
            label='Recipient Email'
            onChange={(e)=>{setEmail(e.target.value)}}
            required
          />
          </div>
          <div style={{paddingTop:'30px'}}>
        <TextField
            label='Recipient Phone Number'
            onChange={(e)=>{setNumber(e.target.value)}}
            required
          />
          </div>
          <div style={{paddingTop:'30px'}}>
        <TextField
            label='Location'
            onChange={(e)=>{
              setSearched(false);
              setReview("");
              setLocation(e.target.value)}}
            required
          />
          </div>
          <div style={{paddingTop:'30px'}}>
        <TextField
            label='Date'
            onChange={(e)=>{setDate(e.target.value)}}
            required
          />
          </div>
          <Box sx={{height:'5vh'}}>

          </Box>
          <div style={{justifyContent:'space-between'}}>
            <Button variant="outlined" color="primary" style={{marginTop:'',marginRight:'30px',fontWeight:'bold', color:'black'}} onClick={submitPostcard}>
              Submit Edit 
            </Button>
            <Button variant="outlined" color="primary" style={{marginTop:'', marginLeft:'30px',fontWeight:'bold', color:'black'}} onClick={sendPostcard}>
              Send Postcard
            </Button>
          </div>
          </div>
        </div>
        </div>
  );
}