import React from "react";
import "./SignupForm.css";

function SignupForm() {
  return (
    <div className="form-container">
      <form className="signup-form">
        <input type="text" placeholder="FULL NAME" className="input-field" />
        <input type="email" placeholder="EMAIL" className="input-field" />
        <input type="password" placeholder="PASSWORD" className="input-field" />
        <input
          type="password"
          placeholder="CONFIRM PASSWORD"
          className="input-field"
        />
        <button type="submit" className="signup-button">SIGN UP</button>
        <a href="/accounts/google/login/?next=/main" className="google-login">Sign up with Google</a>
      </form>
    </div>
  );
}

export default SignupForm;