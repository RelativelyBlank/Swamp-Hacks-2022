const NavWrapper = ({children}) => {
    const [backgroundImage, setBackgroundImage] = useState(knightsBackground);
    const navigate = useNavigate();
    useEffect(()=> {
      if (window.location.pathname === '/') {
        setBackgroundImage(knightsBackground);
      }else if(window.location.pathname === '/dashboard') {
        setBackgroundImage(dashboardBackground);
      }
    },[navigate]);
    return(
        {children}
    )
}

export default NavWrapper;