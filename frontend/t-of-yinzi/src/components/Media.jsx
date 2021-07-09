import React from "react";
import ReactPlayer from 'react-player';
import './Media.css'

function Media() {
    return (

        <>
            <h1>Media</h1>
            <div className="media-container">

                <ReactPlayer
                    url="https://www.youtube.com/watch?v=UcgNYJeV_o8"
                    controls
                />
            </div>
        </>

    );
}

export default Media;


