import React, { useState } from "react";
import LoginForm from "../components/LoginForm";
import SignupForm from "../components/SignupForm";
import "./PlayerLoginSignup.css";

function PlayerLoginSignup() {
  const [isLogin, setIsLogin] = useState(true);

  return (
    <div className="login-signup-page">
      <div className="tabs">
        <span
          className={isLogin ? "active-tab" : "inactive-tab"}
          onClick={() => setIsLogin(true)}
        >
          SIGN IN
        </span>
        <span
          className={!isLogin ? "active-tab" : "inactive-tab"}
          onClick={() => setIsLogin(false)}
        >
          SIGN UP
        </span>
      </div>
      {isLogin ? <LoginForm /> : <SignupForm />}
    </div>
  );
}

export default PlayerLoginSignup;