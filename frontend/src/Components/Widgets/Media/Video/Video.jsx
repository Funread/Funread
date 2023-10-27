import "./Video.css";
import { Card, CardFooter } from "react-bootstrap";
import Tab from "react-bootstrap/Tab";
import Tabs from "react-bootstrap/Tabs";
import React from "react";
import WidgetVideoYou from "./WidgetVideoYou";
import WidgetVideo from "./WidgetVideo";
import { useState } from "react";
import Button from "react-bootstrap/Button";
import Modal from "react-bootstrap/Modal";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faDesktop } from "@fortawesome/free-solid-svg-icons";
import { faUpload } from "@fortawesome/free-solid-svg-icons";
import { faYoutube } from "@fortawesome/free-brands-svg-icons";
import { useDrag } from 'react-dnd'


const widgetType = 'widgetType'

function Video() {
  const [show, setShow] = useState(false);

  const handleClose = () => setShow(false);
  const handleShow = () => setShow(true);

  const [{ isDragging }, drag] = useDrag(() => ({
    type: widgetType, // identificador
    item: { type: 'Video' },
    //La funcion collect es opcional
    collect: (monitor) => ({
      isDragging: !!monitor.isDragging(), //Ayuda a saber si se está arrastrando o no
    }),
  }))
  return (

    <div
      ref={drag}
      
      style={{ border: isDragging ? '5px solid pink' : '0px' }}
    >
    <>
      <div>
        <h1>
          <br />
          <br />
        </h1>
        <Card className="custum-card-upload mx-auto">
          <Card.Header></Card.Header>
          <Card.Body className="custum-body-upload">
            <img
              className="custum-img-upload"
              src="/imagenes/Video/upload.jpg"
              alt="upload"
            />
            <Button
              className="custum-button-upload mx-auto mb-1"
              variant="success"
              onClick={handleShow}
            >
              <FontAwesomeIcon
                className="custum-icon-upload "
                size="lg"
                icon={faUpload}
              />
              Upload Video
            </Button>
          </Card.Body>
          <CardFooter></CardFooter>
        </Card>
      </div>

      <Modal className="" show={show} onHide={handleClose}>
        <Modal.Header className="bg bg-light" closeButton>
          <Modal.Title className="">Video Upload</Modal.Title>
        </Modal.Header>
        <Modal.Body>
          <Tabs
            defaultActiveKey="YouTube"
            className="custum-tabs mx-auto border border-secondary"
          >
            <Tab
              className="custum-tab-youtube mx-auto"
              eventKey="YouTube"
              title="YouTube"
            >
              <Card className="custum-video text-center bg-light border border-secondary">
                <Card.Header>
                  <Card.Body>
                    <Card.Title className="custum-icon-youtube">
                      <FontAwesomeIcon
                        className="custum-icon"
                        size="lg"
                        icon={faYoutube}
                        color="red"
                      />
                      <strong>YouTube</strong>
                    </Card.Title>
                    <Card.Text>
                      <WidgetVideoYou></WidgetVideoYou>
                    </Card.Text>
                  </Card.Body>
                </Card.Header>
              </Card>
            </Tab>
            <Tab className="mx-auto" eventKey="Desktop" title="Desktop">
              <Card className="custum-video  bg-light mx-auto border border-secondary">
                <Card.Header>
                  <Card.Body>
                    <Card.Title className="custum-title-desktop">
                      {""}
                      <FontAwesomeIcon
                        className="custum-icon"
                        size="lg"
                        icon={faDesktop}
                      />
                      <strong>Desktop</strong>
                    </Card.Title>
                    <Card.Text>
                      <WidgetVideo></WidgetVideo>
                    </Card.Text>
                  </Card.Body>
                </Card.Header>
              </Card>
            </Tab>
          </Tabs>
        </Modal.Body>
        <Modal.Footer className="bg bg-light">
          <Button variant="secondary" onClick={handleClose}>
            Close
          </Button>
          <Button variant="success" onClick={handleClose}>
            Save Changes
          </Button>
        </Modal.Footer>
      </Modal>
    </>
    </div>
  );
}

export default Video;
