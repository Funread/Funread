import React, { useState } from "react";
import "./BookView.sass";
import BookPreview from "../BookPreview/BookPreview";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faX } from "@fortawesome/free-solid-svg-icons";

const getImage = "http://localhost:8000";

const BookView = ({ title, description, portrait, author }) => {
  const bookImage = portrait
    ? `${getImage}${portrait}`
    : "./imagenes/no-image.png";

  const [modoPresentacion, setModoPresentacion] = useState(false);

  const activarModoPresentacion = () => {
    setModoPresentacion(true);
  };

  const desactivarModoPresentacion = () => {
    setModoPresentacion(false);
  };

  return (
    <div
      className="mx-auto pt-5 text-white justify-content-center"
      style={{ display: "flex", flexDirection: "column", height: "100%" }}
    >
      <div className="book-header">
        <div className="book-title">{title}</div>
        <div className="book-author">{author}</div>
      </div>

      <div className="book-image">
        <img src={bookImage} width={170} height={300} alt="portrait" />
      </div>

      <div className="book-description">
        <p>{description}</p>
      </div>

      <div
        className="button-section"
        style={{ marginTop: "auto", marginBottom: "30px" }}
      >
        <button className="button-preview" onClick={activarModoPresentacion}>
          Preview
        </button>

        {modoPresentacion && (
          <div className="modal-overlay-preview">
            <button
              className="close-button"
              onClick={desactivarModoPresentacion}
            >
              <FontAwesomeIcon size="lg" icon={faX} />
            </button>
            <BookPreview title={title} />
          </div>
        )}
        <button className="button">Botón 2</button>
      </div>
    </div>
  );
};

export default BookView;
