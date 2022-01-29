// create a component that wraps an image with text 
//the image is to the left of the text
import { Typography } from '@mui/material';
import postcardBackground from '../assets/postcard_back.jpg';
import tempSeal from '../assets/seal_temp.jpg';
import tempImage from '../assets/temp_image_postcard.jpg';
const test = () => {
    return (
        <div>
            <img src={tempImage}/>
            <Typography style={{float:'right',textAlign:'justify'}}>dawnwadawdawdawdqwdnal kwdawdawdadndawndndn</Typography>
        </div>
    )
}
export default test;