import React from "react";
import { Link, withRouter } from "react-router-dom";

function Navigation(props) {
    return(

        <ul>
            <li>
                <Link to="/">
                    Home
                </Link>
            </li>
            <li>
                <Link to="/bio">
                    Bio
                </Link>
            </li>
        </ul>

    );
}

export default withRouter(Navigation);
