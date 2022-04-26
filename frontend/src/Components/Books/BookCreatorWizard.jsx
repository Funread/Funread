import React from 'react' 
import Wizard from '../Shared/Wizard'
import TextField from '@mui/material/TextField';
 
import PageOneBookCreator from './PageOneBookCreator';
import PageTwoBookCreator from './PageTwoBookCreator';
import PageThreeBookCreator from './PageThreeBookCreator';
import BookCreatorBoard from './Template/BookCreatorBoard';
import UploadImage from '../Shared/UploadImage';
class BookCreatorWizard extends React.Component {
    constructor(props) {
        super(props)
        this.PageOneState = this.PageOneState.bind(this)
        this.state = {
            template: null,
            description: null,
            title: null,
            unitName: null,
            gradeNumber: null
        }
    }

    PageOneState(template) {
        this.setState({
            template: template
        })

    }

 
    render() {
        let TitleList = ['Book style', 'Name & clasification', 'Save and Create']
        let Fragment1 =
            <React.Fragment>
 
                step 1 here
            </React.Fragment>
        let Fragment2 =
            <React.Fragment>
                //Example of inputs here
                <TextField id="standard-basic" label="Standard" variant="standard" />
                <PageTwoBookCreator/>
                <UploadImage />
            </React.Fragment>

        // add <BookCreatorBoard/> in fragment to test    
        let Fragment3 = <React.Fragment> step 3  </React.Fragment>
 

        let stepListObjets = [Fragment1, Fragment2, Fragment3]
        return (
            <Wizard
                stepsTitleList={TitleList}
                stepList={stepListObjets}

            />

        )
    }
}

export default BookCreatorWizard
 
