import _ from 'lodash';
import { apiGet } from './http';

export const dataParser = async (endpoint, typeKey) => {
  // let ignoreKey = 'btw';
  let res = await apiGet('/api/v1/btws/34/')
  // console.log('defaults ', request.defaults);
  console.log('res ', res);
  let normaldata = res.data;
  let modified = {};
  _.forEach(normaldata, (category, key) => {
    if (key == 'id' || key == typeKey || key == 'student') {
      modified[key] = category
    } else if (key == 'created' || key == 'updated') {
      // do not add these keys
    } else {
      let s = key.toString()
      let replaced = s.replace(/\s*_\s*|\s+, '*'/gm, ' ')
      replaced = replaced[0].toUpperCase() + replaced.substring(1)
      modified[key] = {
        key,
        // value: typeof (category) == 'object' ? {} : category,
        title: replaced
      };
      console.log('category', category, ':::type of:::', _.size(category))
      if (_.size(category) == 0) {
        modified[key].value = category
      } else {
        _.forEach(category, (fieldDefault, fieldKey) => {
          if (fieldKey == 'id' || fieldKey == typeKey) {
            modified[key][fieldKey] = fieldDefault
          } else if (fieldKey == 'created' || fieldKey == 'updated') {
            // do not add these keys
          } else {
            let s = fieldKey.toString()
            let replaced = s.replace(/\s*_\s*|\s+, '*'/gm, ' ')
            replaced = replaced[0].toUpperCase() + replaced.substring(1)
            // console.log('repalce', replaced)
            modified[key][fieldKey] = {
              key: fieldKey,
              value: fieldDefault,
              title: replaced
            }
          }
        })
      }
    }
  })
  console.log('modified ', modified);
  return modified;
}

export const dataModalMaker = async (endpoint, ignoreKey) => {
  // let ignoreKey = 'btw';
  // let res = await apiGet('/api/v1/swp-list/34/') // For swp-list section with id 70
  // let res = await apiGet('/api/v1/pas-list/70/') // For pas-list section with id 70
  // let res = await apiGet('/api/v1/pre-trips/81/') // For pre-trips section with id 81
  // let res = await apiGet('/api/v1/students/88/vrt/') // For Prods section with id 71
  let res = await apiGet(endpoint) // For Prods section with id 71
  // console.log('defaults ', request.defaults);
  console.log('res ', res);
  let normaldata = res.data;
  let modified = {};
  _.forEach(normaldata, (category, key) => {
    // console.log('category', category, 'key', key == "date" ? null : key);
    if (key == 'id' || key == 'test') {
      // modified[key] = category
    } else if (key == 'created' || key == 'updated' || key == 'student' || key == ignoreKey) {
      // do not add these keys
    } else {
      let s = key.toString()
      let replaced = s.replace(/\s*_\s*|\s+, '*'/gm, ' ')
      replaced = replaced[0].toUpperCase() + replaced.substring(1)
      modified[key] = {
        key,
        // value: typeof (category) == 'object' ? {} : category,
        title: replaced
      };
      console.log('category', category, ':::type of:::', _.size(category))
      if (_.size(category) == 0) {
        modified[key].value = category
      } else if (key == "date" || key == "start_time") {
        modified[key].value = null;
      } else {
        _.forEach(category, (fieldDefault, fieldKey) => {
          // console.log('fieldDefault', fieldDefault, 'fieldKey', fieldKey);
          if (fieldKey == 'id') {
            // modified[key][fieldKey] = fieldDefault
          } else if (fieldKey == 'created' || fieldKey == 'updated' || fieldKey == ignoreKey) {
            // do not add these keys
          } else {
            let s = fieldKey.toString()
            let replaced = s.replace(/\s*_\s*|\s+, '*'/gm, ' ')
            replaced = replaced[0].toUpperCase() + replaced.substring(1)
            // console.log('repalce', replaced)
            modified[key][fieldKey] = {
              key: fieldKey,
              value: fieldDefault,
              title: replaced
            }
          }
        })
      }
    }
  })
  console.log('modified ', modified);
  return modified;
}

export const prodsDataModalMaker = async (endpoint, ignoreKey) => {
  // let ignoreKey = 'btw';
  // let res = await apiGet('/api/v1/swp-list/34/') // For swp-list section with id 70
  // let res = await apiGet('/api/v1/pas-list/70/') // For pas-list section with id 70
  // let res = await apiGet('/api/v1/pre-trips/81/') // For pre-trips section with id 81
  let res = await apiGet('/api/v1/prods/71/') // For Prods section with id 71
  // console.log('defaults ', request.defaults);
  console.log('res ', res);
  let normaldata = res.data;
  let modified = {};
  _.forEach(normaldata, (category, key) => {
    // console.log('category', category, 'key', key == "date" ? null : key);
    if (key == 'id') {
      // modified[key] = category
    } else if (key == 'created' || key == 'updated' || key == 'student' || key == 'company' || key == 'instructor' || key == ignoreKey) {
      // do not add these keys
    } else {
      let s = key.toString()
      let replaced = s.replace(/\s*_\s*|\s+, '*'/gm, ' ')
      replaced = replaced[0].toUpperCase() + replaced.substring(1)
      modified[key] = {
        key,
        // value: typeof (category) == 'object' ? {} : category,
        title: replaced
      };
      console.log('category', category, ':::type of:::', _.size(category))
      if (_.size(category) == 0) {
        modified[key].value = category
      } else if (key == "date" || key == "start_time") {
        modified[key].value = null;
      }
      // else if (key == 'equipment_clean') {
      //   modified[key].value = category 
      // }
      else {
        _.forEach(category, (fieldDefault, fieldKey) => {
          // console.log('fieldDefault', fieldDefault, 'fieldKey', fieldKey);
          if (fieldKey == 'id') {
            // modified[key][fieldKey] = fieldDefault
          } else if (fieldKey == 'created' || fieldKey == 'updated' || fieldKey == ignoreKey) {
            // do not add these keys
          } else {
            let s = fieldKey.toString()
            let replaced = s.replace(/\s*_\s*|\s+, '*'/gm, ' ')
            replaced = replaced[0].toUpperCase() + replaced.substring(1)
            // console.log('repalce', replaced)
            modified[key][fieldKey] = {
              key: fieldKey,
              value: fieldDefault,
              title: replaced
            }
          }
        })
      }
    }
  })
  console.log('modified ', modified);
  return modified;
}


export const counterToAlpha = (count) => {
  let alphabetMap = [...'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz']
  return alphabetMap[count - 1]
}

export function getObjectDiff(obj1, obj2) {
  const diff = Object.keys(obj1).reduce((result, key) => {
    if (!obj2.hasOwnProperty(key)) {
      result.push(key);
    } else if (_.isEqual(obj1[key], obj2[key])) {
      const resultKeyIndex = result.indexOf(key);
      result.splice(resultKeyIndex, 1);
    }
    return result;
  }, Object.keys(obj2));

  return diff.length ? diff : false;
}


export function getDataDiff(obj1 = {}, obj2 = {}, debug) {
  //obj1 apidata, obj2 state
  let diff = []
  _.forEach(obj1, (data, key) => {
    if (obj2.hasOwnProperty(key)) {
      if (!_.isEqual(obj1[key], obj2[key])) {
        if(debug)
        console.log('not equal key', key, 'previous val:',obj1[key],' current val', obj2[key])
        diff.push(key)
      }
    }
  })
  return diff.length ? diff : false;
}