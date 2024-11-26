import React from "react";
import "./LoginForm.css";

function LoginForm() {
  return (
    <div className="form-container">
      <form className="login-form">
        <input type="text" placeholder="USERNAME" className="input-field" />
        <input type="password" placeholder="PASSWORD" className="input-field" />
        <div className="toggle-container">
          <span className="toggle-label">NO</span>
          <span className="toggle-switch"></span>
          <label className="toggle-text">KEEP ME SIGNED IN</label>
        </div>
        <button type="submit" className="login-button">SIGN IN</button>
        <a href="#" className="forgot-password">Forgot your password?</a>
        <a href="/accounts/google/login/?next=/main" className="google-login">Login with Google</a>
      </form>
    </div>
  );
}

export default LoginForm;