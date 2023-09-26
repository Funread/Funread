import React from "react";
import "../../App.css";
import Header from "../Shared/Header/Header";
import SignUp from "../SignUp/SignUp";
import Carousel from "../Shared/Carousel/Carousel";
import "./LandingPage.css";
import LogIn from "../LogIn/LogIn";
import JoinActivity from "../JoinActivity/JoinActivity"
import ButtonGroup from 'react-bootstrap/ButtonGroup';
import ToggleButton from 'react-bootstrap/ToggleButton';
import { useState } from "react";

import image1 from "./img/imagen1.webp"
import image2 from "./img/imagen2.webp"
import image3 from "./img/imagen3.webp"
import image4 from "./img/imagen4.webp"
import image5 from "./img/imagen5.webp"
import image6 from "./img/imagen6.webp"

// color de libro de logo funread = #A097F2

function LandingPage() {
  const [login, setLogin] = useState(true);
  const [join, setJoin] = useState(false);

  function changesLogin() {
    setLogin(!login)
  }

  function changesJoin() {
    setJoin(!join)
  }

  return (
    <div className="landing-page-container">
      <div className="landing-page-carousel">
        <Carousel Images={[image1,image2,image3,image4,image5,image6]} timeSlideInSeconds={6} controls={false}/>
        <div className="landing-page-carousel-bottom-gradient" />
      </div>
      <div className="landing-page-header">
        <Header />
      </div>
      <div className="landing-page-body">
          <div className="landing-page-options-section">
            <div className="landing-page-account-button-container">
              <button className={"landing-page-button-login" + (!join ? " landing-page-button-login-disable" : "")} onClick={changesJoin}>
                <div className={"landing-page-button-text" + (!login ? " landing-page-button-text-up" : "")}>
                  <span>Log In</span>
                  <span>Sing Up</span>
                </div>
              </button>
              <button className={"landing-page-button-singup" + (!join ? "" : " landing-page-button-singup-disable")} onClick={changesJoin}>Join</button>
            </div>
            <div className="landing-page-account-section">
              <div className={"landing-page-login-singup-div" + (!login ? " landing-page-login-singup-div-up" : "") + (join ? " landing-page-login-singup-div-right" : "")}>
                <LogIn/>
                <span className="landing-page-login-singup-span" onClick={changesLogin}>Don't you have a account?</span>
                <SignUp/>
                <span className="landing-page-login-singup-span" onClick={changesLogin}>you already have a account?</span>
              </div>
              <div className={"landing-page-join" + (join ? " landing-page-join-left" : "")}>
                <JoinActivity/>
              </div>
            </div>
          </div>
      </div>
    </div>
  );
}

export default LandingPage;