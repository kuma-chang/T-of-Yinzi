import React from "react";
import { FaYoutube, FaInstagram, FaFacebook } from "react-icons/fa";
import { Row, Col } from "react-bootstrap";

function Footer() {
    return (

        <div className="footer">
            <footer class="py-2 fixed-bottom">
                <div class="container">
                    <Row className="justify-content-center">
                        <Col xs="auto">
                            <a href="https://www.youtube.com/channel/UC0-Tlkjzbib0cuBCIFscSrQ" target="_blank" rel="noreferrer">
                                <FaYoutube
                                    size="40"
                                    color='white'
                                />
                            </a>
                        </Col>
                        <Col xs="auto">
                            <a href="https://www.instagram.com/yinzizyz/" target="_blank" rel="noreferrer">
                                <FaInstagram
                                    size="40"
                                    color='white'
                                />
                            </a>
                        </Col>
                        <Col xs="auto">
                            <a href="https://www.facebook.com/yinzi.zhou" target="_blank" rel="noreferrer">
                                <FaFacebook
                                    size="40"
                                    color='white'
                                />
                            </a>
                        </Col>
                    </Row>
                </div>
            </footer>
        </div>

    );
}

export default Footer;

