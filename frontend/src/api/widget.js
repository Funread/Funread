import { axiosAuth } from "../axiosInstances"


export async function newWidget(widgetitemid, value, type, pageid, widgetid) {
    return axiosAuth().post('widget/insertWidgetItem/', {
      widgetitemid: widgetitemid,
      value: value,
      type: type,
      pageid: pageid,
      widgetid: widgetid,
    }) 
  }
