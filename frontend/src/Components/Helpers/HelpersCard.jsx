import React, { useState } from 'react';
import './HelpersCard.sass';

const getImage = 'http://localhost:8000'
const HelpersCard = ({
    id,
    imageUrl,
    photo,
    name,
    post,
    lugar,
    linke,

  }) => {
    const imageCard = imageUrl || photo
      ? `${getImage}${imageUrl || photo}`
      : './imagenes/no-image.png';
  
    return (
      <div
        className='HelpersCard'
        style={{
          width: '260px',
          borderRadius: '5px',
          backgroundColor: '#f5f5f5',
          border: '1px solid #ddd',
          marginTop: '200px',
          marginLeft: '35px',
          display: 'flex',
          flexwrap: 'wrap',
        }}
      >
        <div className='align-items'>
          <div style={{ padding: '20px 0 20px 20px' }}>
            <img
              className='card-im'
              src={"https://cdn-icons-png.flaticon.com/512/6596/6596121.png"}
              alt='Portrait'
              style={{ width: '90px', height: '80px',marginLeft: '50px', borderRadius: '0px' }}
            />
          </div>
          <div className='card-body d-flex flex-column justify-content-between'>
            <h5 className='card-title'>{name}</h5>
            <div>
              <h1 className='card-text'>{post}</h1>
            </div>
            <div>
              <h1 className='card-text '>{lugar}</h1>
            </div>
            <div>
              <h1 className='card-text'>{linke}</h1>
            </div>
          </div>
        </div>
      </div>
    );
  };
  
  export default HelpersCard;
  