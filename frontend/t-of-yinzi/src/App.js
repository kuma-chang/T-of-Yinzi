import './App.css';
import React from "react";
import {Helmet} from "react-helmet";
import MovingBackground from './UI/Background';
import { BrowserRouter as Router, Route, Switch  } from "react-router-dom";
import { Navigation, Footer, Home, Bio, Gallery, Media, Schedule } from "./components";




function App() {
    return (
        <div>
            <Router>
                <MovingBackground/>
                <Navigation />
                <Switch>
                    <Route path="/" exact component={() => <Home />} />
                    <Route path="/bio" exact component={() => <Bio />} />
                    <Route path="/gallery" exact component={() => <Gallery />} />
                    <Route path="/media" exact component={() => <Media />} />
                    <Route path="/schedule" exact component={() => <Schedule />} />
                </Switch>
                <Footer />
            </Router>
            <Helmet>
                <title>Yinzi Zhou| Home</title>
            </Helmet>

        </div>
    );
}

export default App;
