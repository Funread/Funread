import { axiosAuth } from './axiosInstances'

export async function newWidgetItem(page, widget, type, value, elementorder) {
  return axiosAuth().post('widget/insertWidgetItem/', {
    pageid: page,
    widgetid: widget,
    type: type,
    value: value,
    elementorder: elementorder,
  })
}

export async function listedWidgets() {
  return axiosAuth().get('widget/listallWidgets/')
}

export async function listedWidgetItems() {
  return axiosAuth().get('widget/listallWidgetItems/')
}
