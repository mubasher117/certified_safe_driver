import { StyleSheet } from "react-native"
import { ViewStyleSheet, ImageStyleSheet, TextStyleSheet} from "../../../utils"
import { R } from "../../../res"

const viewStyles = ViewStyleSheet({
  container: {
    padding: 4,
    alignItems: "center"
  }
})

const imageStyles = ImageStyleSheet({})

const textStyles = TextStyleSheet({
  counter: {
    color: R.colors.White,
    fontSize: 12,
  }
})

const styles = StyleSheet.create({
  ...viewStyles,
  ...imageStyles,
  ...textStyles,
})

export default styles
