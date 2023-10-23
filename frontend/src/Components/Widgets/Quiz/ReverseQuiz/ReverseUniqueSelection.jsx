import './ReverseUniqueSelection.css'
import React, { useState, useEffect } from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faMinus, faPlus } from '@fortawesome/free-solid-svg-icons'
import ReverseAnswerQuiz from './ReverseAnswerQuiz'

const MIN_RESPONSES = 2
const MAX_RESPONSES = 4

const ReverseUniqueSelection = () => {
  const [responses, setResponses] = useState(Array(MIN_RESPONSES).fill('')) // Inicia con dos respuestas mínimo
  const [isAddingResponses, setIsAddingResponses] = useState(true) // Estado inicial: agregar respuestas

  const addResponses = () => {
    if (responses.length < MAX_RESPONSES) {
      setResponses([...responses, '', ''])
    }
  }

  const removeResponses = () => {
    if (responses.length > MIN_RESPONSES) {
      const newResponses = responses.slice(0, -2)
      setResponses(newResponses)
    }
  }

  const toggleAddingResponses = () => {
    if (isAddingResponses) {
      addResponses()
    } else {
      removeResponses()
    }
  }

  const handleResponseChange = (index, value) => {
    setResponses((prevResponses) => {
      const newResponses = [...prevResponses]
      newResponses[index] = value
      return newResponses
    })
  }

  useEffect(() => {
    if (responses.length === MIN_RESPONSES) {
      setIsAddingResponses(true)
    } else if (responses.length === MAX_RESPONSES) {
      setIsAddingResponses(false)
    }
  }, [responses])

  return (
    <div className='custom-quiz-background'>
      <div className='container custom-quiz-container text-center'>
        <div className='row'>
          <div className='col'>
            <div id='cardQuestions'>
              <div className='row'>
                <input
                  type='text'
                  className='custom-input'
                  placeholder='Start typing your question'
                />
                {/* <div className="custom-add-image">
                  <div className="image-container">
                    <div>
                      <img src="/imagenes/quiz/addImage.png" alt="addimage" />
                      <p>Find and insert media</p>
                    </div>
                  </div>
                </div> */}
              </div>
            </div>

            <div className='responses-grid mx-auto mt-5'>
              {responses.map((response, index) => (
                <ReverseAnswerQuiz
                  key={index}
                  value={response}
                  onChange={(value) => handleResponseChange(index, value)}
                />
              ))}
            </div>
            <button
              className={`custom-button ${
                isAddingResponses ? 'adding' : 'removing'
              }`}
              onClick={toggleAddingResponses}
            >
              <div className='button-content'>
                <div className='button-icon'>
                  {isAddingResponses ? (
                    <FontAwesomeIcon size='lg' icon={faPlus} />
                  ) : (
                    <FontAwesomeIcon size='lg' icon={faMinus} />
                  )}
                </div>
                <div className='button-text'>
                  {isAddingResponses
                    ? 'Add more answers'
                    : 'Remove additional answers'}
                </div>
              </div>
            </button>
          </div>
        </div>
      </div>
    </div>
  )
}

export default ReverseUniqueSelection
