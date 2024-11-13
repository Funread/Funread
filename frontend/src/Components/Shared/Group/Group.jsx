import './Group.sass'
import React, { useState, useEffect } from 'react'
import Button from 'react-bootstrap/Button'
import Form from 'react-bootstrap/Form'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
import { faPencilAlt, faSearch } from '@fortawesome/free-solid-svg-icons'
import SidebarBook from '../Shared/SidebarBook/SidebarBook'
import ListGroups from '../Shared/ListGroups/ListGroups'
import StudentCard from '../Shared/StudentCard/StudentCard'
import GroupCardProgress from '../Shared/GroupCardProgress/GroupCardProgress'
import GroupBuilder from '../Shared/GroupBuilder/GroupBuilder'
import { ToastContainer } from 'react-toastify'
import GroupView from '../Shared/GroupView/GroupView'
import Classes from '../Shared/Classes/Classes'
import ClassBuilder from '../Shared/ClassBuilder/ClassBuilder'
import { Tabs, Tab } from 'react-bootstrap'
import CustomMessage from '../Shared/CustomMessage/CustomMessage'



const Group = () => {
  const [groups, setGroups] = useState([])
  const [selectedStudent, setSelectedStudent] = useState(null)
  const [selectedGroup, setSelectedGroup] = useState(null)
  const [groupForm, setGroupForm] = useState(false)
  const [groupClasses, setGroupClasses] = useState(false)
  const [groupId, setGroupId] = useState(null)
  const [groupName, setGroupName] = useState(null)
  const [showClasses, setShowClasses] = useState(false)
  const [activities, setActivities] = useState([])
  const [key, setKey] = useState('group')

  const showGroupResume = (group) => {
    if (!selectedGroup || selectedGroup.id !== group.id) {
      setSelectedGroup(group)
    } else {
      setSelectedGroup(null)
    }

    setGroupForm(false)
    setSelectedStudent(null)
    setGroupClasses(false)
  }

  const toggleSidebar = (student) => {
    if (selectedStudent && selectedStudent.userid === student.userid) {
      setSelectedStudent(null)
    } else {
      setSelectedStudent(student)
    }

    setGroupClasses(false)
    setGroupForm(false)
    setSelectedGroup(null)
  }

  const toggleGroupForm = () => {
    setGroupClasses(false)
    setSelectedStudent(null)
    setSelectedGroup(null)
    setGroupForm(!groupForm || selectedGroup || selectedStudent)
  }

  const toggleGroupClasses = () => {
    setGroupClasses(!groupClasses)
    setGroupForm(false)
    setSelectedStudent(null)
    setSelectedGroup(null)
  }

  const handleGroupCreated = (newGroup) => {
    setGroups([...groups, newGroup])
  }

  const handleClassesComponent = (id, name) => {
    console.log("datos", id + " " + name)
    setGroupId(id)
    setGroupName(name)
    setShowClasses(true)
    setKey("classes")
  }
// ////////////////////////////////////////////////////////////////////////////
  const handleGroupsComponent = (id, name) => {
    console.log("datos")
    setGroupId(id)
    setGroupName(name)
    setShowGroups(true) //////////////////
    setKey("studentsGroup")
  }

  const handleActiviyCreated = (newActivity) => {
    setActivities([...activities, newActivity])
  }

  useEffect(() => {
    if (key == "group") {
      console.log("entre:", key);

      setShowClasses(false)
    }
   
  }, [key]);
  useEffect(() => {
        console.log("sali:", showClasses);
  }, [showClasses]);

  return (
    <div className='container-fluid text-center group'>
      <div className='row' style={{ height: 'auto' }}>
        <div className='col-1 p-0'>
          <SidebarBook />
        </div>
          <div>
            TEST
          </div>
        <div className='sidenav col-8'>
          <div style={{ maxWidth: '1100px' }} className='mx-auto content_group'>
            <div className='d-flex align-items-center justify-content-between mt-3'>
              <h4 className='custom-group-title'>My Groups</h4>
              <Button
                className='button-edit-library position-relative'
                variant='outline-success'
                onClick={toggleGroupForm}
                style={{ marginLeft: '10px' }} // Margen para separarlo del título
              >
                <FontAwesomeIcon icon={faPencilAlt} />
                <span className='position-absolute top-0 start-100 translate-middle badge rounded-pill bg-light text-dark' style={{ opacity: 0 }}>
                  New
                </span>
              </Button>
            </div>
            
            <Tabs
              className='section_group_Tap'
              id='controlled-tab'
              activeKey={key}
              onSelect={(k) => setKey(k)
              }
              fill
            >
              <Tab eventKey='group' title='My Groups' className='tab'>
              <div className='shadow p-3 bg-body rounded'>
                <ListGroups
                  toggleSidebar={toggleSidebar}
                  showGroupResume={showGroupResume}
                  newGroups={groups}
                  handleClassesComponent={handleClassesComponent}
                />
             </div>
              </Tab>
              <Tab eventKey='classes' title='Group Classes' className='tab'>
              <div className='shadow p-3 bg-body rounded'>
                {showClasses ? (
                  <Classes
                    groupId={groupId}
                    groudName={groupName}
                    toggleGroupClasses={toggleGroupClasses}
                    newActivities={activities}
                  />
                ):( 
                  <CustomMessage message={'You should assign tasks to the group'} />
                )
              }
               </div>
              </Tab>

              <Tab eventKey='studentsGroup' className='tab'>
              <div className='shadow p-3 bg-body rounded'>
                {showGroups ? (
                  <StudentGroups
                    groupId={groupId}
                    groudName={groupName}
                    toggleStudentsGroup={toggleStudentsGroup}
                    newActivities={activities}
                  />
                ):( 
                  <CustomMessage message={'You should assign students to the group'} />
                )
              }
               </div>
              </Tab>
            </Tabs>

            <GroupCardProgress></GroupCardProgress>
            <br />
          </div>
        </div>

        <div className='col-3 mobile-below-tap-group'>
          <div className='position_side shadow rounded'>
            {selectedStudent && (
              <StudentCard
                idStudent={selectedStudent?.userid}
                name={selectedStudent?.name}
                lastname={selectedStudent?.lastname}
                idGroup={selectedStudent?.groupscreateid}
              />
            )}
            {groupForm && <GroupBuilder updateGroup={handleGroupCreated} />}
            {selectedGroup && (
              <GroupView
                id={selectedGroup?.id}
                name={selectedGroup?.name}
                idimage={selectedGroup?.idimage}
              />
            )}

            {groupClasses && (
              <ClassBuilder
                groupId={groupId}
                updateActivity={handleActiviyCreated}
              />
            )}
          </div>
        </div>
      </div>
    </div>
  )
}

export default Group;

