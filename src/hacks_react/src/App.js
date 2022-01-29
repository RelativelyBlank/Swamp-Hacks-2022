import './App.css';
import {Routes,Route, BrowserRouter, useNavigate} from 'react-router-dom'
import Home from './pages/home';
import Login from './pages/login';
import ResponsiveAppBar from './components/appbar';
import knightsBackground from './assets/knights_background.jpg';
import Contacts from './pages/contacts';
import Dashboard from './pages/dashboard';
import dashboardBackground from './assets/dashboard_background.jpg';
import { useEffect, useState } from 'react';
import CreatePostcard from './pages/postcardCreation';
import Postcards from './pages/postcards';

function App() {
  return (
    <BrowserRouter>
          <Routes>
              <Route exact path="/" element={<Home />} />
              <Route  path="/login" element={<Login/>} />
              <Route  path="/contacts" element={<Contacts/>} />
              <Route  path="/dashboard" element={<Dashboard/>} />
              <Route path="/create" element ={<CreatePostcard />} />
              <Route path="/postcards" element ={<Postcards />} />
          </Routes>
    </BrowserRouter>
  );
}

export default App;
