import { Linking, Alert, Platform } from 'react-native';
import * as Permissions from 'react-native-permissions';
import ImagePicker from 'react-native-image-crop-picker';
import ActionSheet from 'react-native-actionsheet'
import ImmersiveMode from 'react-native-immersive-mode';

async function askPermission(permission) {
  try {
    const status = await Permissions.check(permission);
    if (status !== Permissions.RESULTS.GRANTED) {
      //if not already granted then ask
      console.log('askPermission status', status, ' for permission', permission);
      const status = await Permissions.request(permission);
      if (status !== Permissions.RESULTS.GRANTED) {
        //user denied on ask
        return false;
      }
    }
    return true;
  } catch (err) {
    console.log('askPermission err', err, ' for permission', permission);
    return false;
  }
}

export async function getCameraGalleryPermissions() {
  //need both permisisons for camera, so ask both on galery and camera
  const { PERMISSIONS } = Permissions
  let permission = Platform.select({
    android: PERMISSIONS.ANDROID.CAMERA,
    ios: PERMISSIONS.IOS.CAMERA,
  })

  let cameraPermissions = await askPermission(permission);
  console.log('cameraPermissions ', cameraPermissions)
  permission = Platform.select({
    android: PERMISSIONS.ANDROID.READ_EXTERNAL_STORAGE,
    ios: PERMISSIONS.IOS.PHOTO_LIBRARY,
  })
  let storagePermissions = await askPermission(permission);
  console.log('storagePermissions ', storagePermissions)
  return cameraPermissions && storagePermissions
}



function permissionsAlert() {
  //console.log('alert');
  Alert.alert(
    'Permissions Required',
    'CSD requires Camera & Photos access to function properly. Please go to settings to enable manually.',
    [
      {
        text: 'Cancel',
        onPress: () => {
          ImmersiveMode.fullLayout(true)
          ImmersiveMode.setBarMode('BottomSticky')
          console.log('Cancel Pressed')
        }, style: 'cancel'
      },
      {
        text: 'Settings',
        onPress: () => {
          ImmersiveMode.fullLayout(true)
          ImmersiveMode.setBarMode('BottomSticky')
          Permissions.openSettings().catch(() => console.log('cannot open settings'))
        }
      },
    ]
  )
};

export const pickFromGallery = async () => {
  let havePermission = await getCameraGalleryPermissions();
  if (!havePermission) {
    permissionsAlert();
    return false;
  } else {
    try {
      let res = await ImagePicker.openPicker({ width: 300, height: 300, cropping: true, mediaType: 'photo', includeBase64: true });
      console.log('gallery res', res);
      return res
    } catch (err) {
      console.log('pickFromGallery err', err)
      return false;
    }

    // return await new Promise(function (resolve, reject) {
    //   ImagePicker.openPicker({ width: 300, height: 300, cropping: true, mediaType:'photo' }, (response) => {
    //     console.log('openPicker res', response)
    //     if (response.didCancel) {
    //       console.log('User cancelled image picker');
    //       resolve(false);
    //     } else if (response.error) {
    //       console.log('ImagePicker Error: ', response.error);
    //       resolve(false);
    //     } else {
    //       const source = response.uri;

    //       // You can also display the image using data:
    //       // const source = { uri: 'data:image/jpeg;base64,' + response.data };
    //       // console.log('response image', response)
    //       resolve(source);
    //     }
    //   });
    // })
  }
};

export const pickFromCamera = async () => {
  let havePermission = await getCameraGalleryPermissions();
  if (!havePermission) {
    permissionsAlert();
    return false;
  } else {
    try {
      let res = await ImagePicker.openCamera({ width: 300, height: 300, cropping: true, mediaType: 'photo', includeBase64: true });
      console.log('camera res', res);
      return res;
    } catch (err) {
      console.log('pickFromCamera err', err)
      return false;
    }

    // return await new Promise(function (resolve, reject) {
    //   ImagePicker.openCamera({width: 300, height: 300, cropping: true, mediaType:'photo'}, (response) => {
    //     console.log('openCamera res', response)
    //     if (response.didCancel) {
    //       console.log('User cancelled image picker');
    //       resolve(false);
    //     } else if (response.error) {
    //       console.log('ImagePicker Error: ', response.error);
    //       resolve(false);
    //     } else {
    //       const source = response.uri;

    //       // You can also display the image using data:
    //       // const source = { uri: 'data:image/jpeg;base64,' + response.data };
    //       console.log('image', source)
    //       resolve(source);
    //     }
    //   });
    // })
  }
};

const CropImagePicker = () => {
  const ImagePickerOptions = ['Take Photo', 'Choose from Images', 'Cancel'];
  return (
    <ActionSheet
      ref={CropImagePickerRef => this.CropImagePicker = CropImagePickerRef}
      title={'Update Profile Image'}
      options={ImagePickerOptions}
      cancelButtonIndex={2}
      // destructiveButtonIndex={1}
      onPress={(index) => {
        if (index != 2) {
          this.setState({ sex: ActionSheetOptions[index] })
        }
      }}
    />
  )
}
//for https://github.com/react-native-community/react-native-image-picker
// export const showImagePicker = async () => {
//   const options = {
//     title: 'Select Profile Image ',
//     cameraRoll: true,
//     waitUntilSaved: true,
//     cancelButtonTitle: 'Cancel',
//     takePhotoButtonTitle: 'Take photo',
//     chooseFromLibraryButtonTitle: 'Choose from Images',
//     storageOptions: {
//       skipBackup: true,
//       path: 'images',
//     },
//   };
//   let havePermission = await getCameraGalleryPermissions();
//   if (!havePermission) {
//     permissionsAlert();
//     return false;
//   } else {
//     return await new Promise(function (resolve, reject) {
//       ImagePicker.showImagePicker(options, (response) => {
//         if (response.didCancel) {
//           console.log('User cancelled image picker');
//           resolve(false);
//         } else if (response.error) {
//           console.log('ImagePicker Error: ', response.error);
//           resolve(false);
//         } else {
//           const source = response.uri;

//           // You can also display the image using data:
//           // const source = { uri: 'data:image/jpeg;base64,' + response.data };
//           console.log('image', source)
//           resolve(source);
//         }
//       });
//     })
//   }
// }

