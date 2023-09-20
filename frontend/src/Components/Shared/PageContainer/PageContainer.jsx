import TemplateImage from '../../../POC-FR-312/TemplateImage';
import ContentImage from '../ContentImage/ContentImage'
import './PageContainer.css'

/*function Templatee({ children }) {
  return (
    <div >
      {children}
    </div>
  );
}*/

const PageContainer = ({ title, image, width, height, imageAlt, text }) => {
  return (
    <div className='container-fluid'>
      <div className='row'>
        <div className='col'>
          <div className='card shadow mb-4 content_page'>
            <div className='card-header py-3 d-flex flex-row align-items-center justify-content-between'>
              <h6 className='m-0 font-weight-bold text-primary'>{title}</h6>
            </div>

            <div className='card-body'>
              <div className='card shadow mb-4 centro'>
                <div className='card-body'>
                  <div className='d-flex flex-column align-items-center justify-content-center '>
                   
                    
                        <TemplateImage></TemplateImage>
                   
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default PageContainer
