import { NavigationActions, StackActions } from 'react-navigation';

let _navigator;

setTopLevelNavigator = (navigatorRef) => {
  _navigator = navigatorRef;
}

navigate = (routeName, params) => {
  _navigator.dispatch(
    NavigationActions.navigate({
      routeName,
      params,
    })
  );
}

goBack = () => {
  _navigator.dispatch(
    NavigationActions.back()
  );
}

resetStack = (routeName) => {
  const resetActions = StackActions.reset({
    index: 0,
    key: null,
    actions: [NavigationActions.navigate({ routeName })]
  });
  _navigator.dispatch(resetActions);
}
// add other navigation functions that you need and export them

export default {
  navigate,
  goBack,
  resetStack,
  setTopLevelNavigator,
};