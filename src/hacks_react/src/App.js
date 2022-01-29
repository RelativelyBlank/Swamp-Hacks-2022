import './App.css';
import {Routes,Route, BrowserRouter} from 'react-router-dom'
import Home from './pages/home';
import Login from './pages/login';
import ResponsiveAppBar from './components/appbar';
import knightsBackground from './assets/knights_background.jpg';
import Contacts from './pages/contacts';
import Dashboard from './pages/dashboard';

function App() {
  
  return (
    <BrowserRouter>
    <div style={{backgroundImage: `linear-gradient(to top, rgba(0, 0, 0, 0), rgba(0, 0, 0, 100)), 
      url(${knightsBackground})`,
          backgroundSize: 'cover',
          backgroundRepeat: 'no-repeat',
          }}>
        <div className="App">
          <ResponsiveAppBar />
          <Routes>
              <Route exact path="/" element={<Home />} />
              <Route  path="/login" element={<Login/>} />
              <Route  path="/contacts" element={<Contacts/>} />
              <Route  path="/dashboard" element={<Dashboard/>} />
          </Routes>
        </div>
    </div>
    </BrowserRouter>
  );
}

export default App;
