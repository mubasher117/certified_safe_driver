import { StyleSheet } from "react-native"
import { ViewStyleSheet, TextStyleSheet } from "../../utils"
import { R } from "../../res"

const viewStyles = ViewStyleSheet({
  container: {
    flex: 1,
    flexDirection: "row",
    marginVertical: 16
  },
  leftContainer: {
    flex: 1,
    paddingHorizontal: 8,
    marginTop: 10,
    backgroundColor: "#ffffff",
  },
  rightContainer: {
    flex: 1,
    paddingHorizontal: 8,
    marginTop: 10,
    backgroundColor: "#ffffff",
  },
  middleContainer: {
    flex: 5,
    backgroundColor: R.colors.Gray,
  },
  upperContainer: {
    flex: 1,
    flexDirection: "row",
    paddingHorizontal: 12,
    paddingTop: 10,
    paddingBottom: 8,
  },
  lowerContainer: {
    flex: 1,
    flexDirection: "row",
    paddingHorizontal: 8,
    paddingBottom: 32,
  },
  horizontalLine: {
    backgroundColor: R.colors.Black,
    height: 2,
    width: "100%",
  },
  firstUpperColumn: {
    flex: 1,
  },
  secondUpperColumn: {
    flex: 1,
    paddingBottom: 24,
  },
  thirdUpperColumn: {
    flex: 1,
    justifyContent: "flex-end",
  },
  forthUpperColumn: {
    flex: 1,
    paddingBottom: 24,
  },
  fifthUpperColumn: {
    flex: 1,
  },
  firstLowerColumn: {
    flex: 1,
    justifyContent:'space-between'
  },
  secondLowerColumn: {
    flex: 2,
    // paddingBottom: 32,
    marginTop: 8,
  },
  thirdLowerColumn: {
    flex: 1,
    justifyContent:'space-between'
  },
})

const textStyles = TextStyleSheet({
  text: {
    fontSize: 20,
    textAlign: "center",
    margin: 10,
  },
})

const styles = StyleSheet.create({
  ...viewStyles,
  ...textStyles,
})

export default styles
