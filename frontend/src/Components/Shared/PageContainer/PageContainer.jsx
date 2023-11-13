import './PageContainer.sass'
import React, { useState, useEffect } from 'react'
import { useDrop } from 'react-dnd'
import Grids from '../Grids/Grids'
import { FullScreen, useFullScreenHandle } from 'react-full-screen'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { fa0, faExpandArrowsAlt, faTrash } from '@fortawesome/free-solid-svg-icons'
import html2canvas from 'html2canvas'
import { ToastContainer, toast } from 'react-toastify'
import AnswerQuiz from '../../Widgets/Quiz/UniqueSelection/AnswerQuiz'
import UniqueSelection from '../../Widgets/Quiz/UniqueSelection/UniqueSelection'
import Box from '../../Widgets/Text/TextBox'

//Objeto para nombrar todos los componentes que serán soltados en el contenedor
const widgetTypeToComponent = {
  Grids: Grids,
}

const PageContainer = ({
  pageNumber,
  onRemoveSlides,
  updateImage,
  addOrUpdatePage,
}) => {
  const [buttonVisible, setButtonVisible] = useState(true)
  const [droppedComponent, setDroppedComponent] = useState(null)
  //Se crea la constante
  const [selectedWidget, setSelectedWidget] = useState(null)
  const [isFullScreen, setIsFullScreen] = useState(false);
  const [originalContent, setOriginalContent] = useState(null);
  const [fullScreenButtonVisible, setFullScreenButtonVisible] = useState(false);


  useEffect(() => {
    captureImage()
  }, [droppedComponent, pageNumber])

  const captureImage = () => {
    // Captura el contenido del PageContainer
    html2canvas(document.getElementById(`pageContainer-${pageNumber}`)).then(
      (canvas) => {
        // Convierte el canvas en una imagen
        const image = new Image()
        image.src = canvas.toDataURL()

        // Llama a la función del BookCreator para pasar la imagen
        updateImage(pageNumber, image.src)
      }
    )
  }

  const [, drop] = useDrop(() => ({
    accept: Object.keys(widgetTypeToComponent),
    drop: (item) => {
      if (item.type === 'Grids') {
        const droppedComponentInfo = {
          type: item.type,
          direction: item.direction,
          rows: item.numRows,
        }
        addOrUpdatePage(
          pageNumber,
          droppedComponentInfo.direction,
          droppedComponentInfo.rows
        )
        setDroppedComponent(droppedComponentInfo)
      } else {
        toast.error('You must select a grid first')
      }
    },
    collect: (monitor) => ({
      isOver: !!monitor.isOver(),
    }),
  }))

  const remove = () => {
    onRemoveSlides(pageNumber)
    // setDroppedComponent(null)
  }

  const handle = useFullScreenHandle()

  const toggleButtonVisibility = (isVisible) => {
    setButtonVisible(isVisible)
  }

  const handleEnterFullScreen = () => {
    toggleButtonVisibility(false);
    handle.enter();
    setSelectedWidget(true);
    setIsFullScreen(true);
    setFullScreenButtonVisible(true);

  };
  console.log(FullScreen)
  return (
    <div className='container-fluid'>
      <div className='row'>
        <div className='col'>
          <FullScreen handle={handle}>
            <div className='card shadow mb-4 content_page shadow rounded'>
              <div className='card-header py-3 d-flex flex-row align-items-center justify-content-between'>
                <h6 className='m-0 font-weight-bold text-info'>
                  {'Activity ' + pageNumber}
                </h6>
                <div className='d-flex'>
                  {!handle.active && (
                    <div className='fullscreen-buttons'>
                      <button
                        id='btnDivs'
                        onClick={handleEnterFullScreen}
                        style={{ backgroundColor: 'rgb(182, 214, 242)' }}
                      >
                        <FontAwesomeIcon icon={faExpandArrowsAlt} />
                        <i className='fa fa-expand'></i>
                      </button>
                    </div>
                  )}
                  <button
                    onClick={remove}
                    id='btnDivs'
                    style={{ backgroundColor: 'rgb(255, 185, 204)' }}
                  >
                    <FontAwesomeIcon size='lg' icon={faTrash} />
                  </button>


                </div>
              </div>
              {isFullScreen ? (
                <div  id={`pageContainer-${pageNumber}`}
                className='card-body custom-card-body-page-container p-0'>
                  <Box Screen={isFullScreen} />

                </div>
              ) : (
                <div
                  id={`pageContainer-${pageNumber}`}
                  className='card-body custom-card-body-page-container p-0'
                  ref={drop}
                >
                  {droppedComponent &&
                    widgetTypeToComponent[droppedComponent.type] &&
                    React.createElement(
                      widgetTypeToComponent[droppedComponent.type],
                      {
                        direction: droppedComponent.direction,
                        numRows: droppedComponent.rows,
                      }
                    )}
                </div>

              )}
            </div>
          </FullScreen>
          <ToastContainer position='top-right' />
        </div>
      </div >
    </div >
  )
}

export default PageContainer


