import './App.css';
import React from "react";
import {Helmet} from "react-helmet";
import MovingBackground from './UI/Background';




function App() {
  return (
      <div>
      <Helmet>
          <title>Yinzi Zhou| Home</title>
      </Helmet>

      <MovingBackground/>
      </div>
  );
}

export default App;
