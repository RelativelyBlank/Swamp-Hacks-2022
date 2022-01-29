import './App.css';
import {Routes,Route, BrowserRouter} from 'react-router-dom'
import Home from './pages/home';
import Login from './pages/login';
import ResponsiveAppBar from './components/appbar';

function App() {

  return (
    <BrowserRouter>
      <div className="App">
        <ResponsiveAppBar />
        <Routes>
            <Route exact path="/" element={<Home />} />
            <Route  path="/login" element={<Login/>} />
        </Routes>
      </div>
    </BrowserRouter>
  );
}

export default App;
