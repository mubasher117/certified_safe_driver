import React, { memo, useRef } from "react"
import { Text, TouchableOpacity, ViewStyle, findNodeHandle, UIManager } from "react-native"
import styles from "./styles"
import { AdjustText } from "../adjustabletext"

interface IButtonProps {
  color: string
  label: string
  disabled?: boolean
  counter?: number
  containerStyle?: ViewStyle
  onPress?: () => void
  onLayout?: (nativeEvent) => void
}

export const Button = memo(function Button(props: IButtonProps) {
  const rootRef = useRef<TouchableOpacity>(null)
  return (
    <TouchableOpacity
      ref={rootRef}
      disabled={props.disabled == true}
      style={[styles.container, props.containerStyle, { backgroundColor: props.color }]}
      onPress={props.onPress}
      onLayout={({ nativeEvent }) => {
        let handle = findNodeHandle(rootRef.current) ?? 0
        UIManager.measure(handle, (x, y, width, height, pageX, pageY) => {
          if (props.onLayout != undefined) props.onLayout({ x: pageX, y: pageY, width, height })
        })
      }}>
      <AdjustText text={props.label} fontSize={14} numberOfLines={1} />
      {props.counter != undefined ? <Text style={styles.counter}>{props.counter}</Text> : undefined}
    </TouchableOpacity>
  )
})
