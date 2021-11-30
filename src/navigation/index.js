import React from 'react';
import { Image, StyleSheet, View, SafeAreaView, Platform } from 'react-native';
import { createAppContainer, createSwitchNavigator } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';

import {
  HomeScreen,
  AuthLoadingScreen,
  SigninScreen,
  EvaluationScreen,
  MapScreen,
  UsersScreen,
  CreateEditUser,
  QuizScreen
} from '../screens';

const defaultStackSettings = {
  defaultNavigationOptions: ({ navigation }) => ({ headerShown: false }),
}

const testStack = createStackNavigator({
  EvaluationScreen,
  MapScreen,
},
  defaultStackSettings
);

const usersStack = createStackNavigator({
  UsersScreen,
  CreateEditUser
},
  defaultStackSettings
);

const quizStack = createStackNavigator({
  QuizScreen
},
  defaultStackSettings
);


const authStack = createStackNavigator({
  SigninScreen,
},
  defaultStackSettings
)
//animated switch breaks on android
const homeSwitch = createSwitchNavigator({
  HomeScreen,
  testStack,
  usersStack,
  quizStack
},
  // {
  //   transition: (
  //     <Transition.Together>
  //       <Transition.Out
  //         type="slide-left"
  //         durationMs={250}
  //         interpolation="easeIn"
  //       />
  //       <Transition.In type="slide-right" durationMs={250} />
  //     </Transition.Together>
  //   ),
  // }
);

const switchScreens = {
  AuthLoadingScreen,
  authStack,
  homeSwitch,
};

const switchSettings = {
  // initialRouteName: 'EvaluationScreen',
  //backBehavior:'initialRoute'
};

const switchNavigator = createSwitchNavigator(switchScreens, switchSettings);

export default Nav = createAppContainer(switchNavigator);