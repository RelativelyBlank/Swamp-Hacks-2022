// create a component that renders a login form

const Login = () => {
    return(
        <div>
            <h1>Login</h1>
            <form>
                <label>
                    Username:
                    <input type="text" name="username" />
                </label>
                <label>
                    Password:
                    <input type="password" name="password" />
                </label>
                <input type="submit" value="Login" />
            </form>
        </div>       
    )
}

export default Login;