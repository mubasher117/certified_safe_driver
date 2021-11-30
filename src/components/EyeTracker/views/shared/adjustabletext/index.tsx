import { R } from "../../../res"
import React, { memo, useState } from "react"
import { Text } from "react-native"
import styles from "./styles"

interface IAdjustTextProps {
  fontSize: number
  text: string
  numberOfLines: number
  color?: string
}

export const AdjustText = memo(function AdjustText(props: IAdjustTextProps) {

  const [currentFont, setCurrentFont] = useState(props.fontSize)

  const onTextLayout = (e) => {
    const { lines } = e.nativeEvent;
    if (lines.length > props.numberOfLines) {
      setCurrentFont(currentFont - 1)
    }
  }

  return (
    <Text
      adjustsFontSizeToFit
      numberOfLines={ props.numberOfLines }
      style={{ fontSize: currentFont, color: props.color ?? R.colors.White }}
      onTextLayout={onTextLayout}
    >
      { props.text }
    </Text>
  )
})