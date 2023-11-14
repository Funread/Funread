import _ from 'lodash'
import './Slide.sass'
import PageContainer from '../PageContainer/PageContainer'

const Slide = ({
  slides,
  onRemoveSlides,
  updateImage,
  addOrUpdatePage,
  widgetChange,
}) => {
  return (
    <>
      {_.map(slides, (slide) => (
        <PageContainer
          key={slide.id}
          pageNumber={slide.id}
          onRemoveSlides={onRemoveSlides}
          updateImage={updateImage}
          addOrUpdatePage={addOrUpdatePage}
          widgetChange={widgetChange}
        />
      ))}
    </>
  )
}

export default Slide
