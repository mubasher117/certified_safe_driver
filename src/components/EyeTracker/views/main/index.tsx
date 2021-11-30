import React, { useState, memo, useRef, forwardRef, useImperativeHandle } from "react"
import { Image, View, findNodeHandle, UIManager } from "react-native"
import { IEmpty } from "../../utils"
import styles from "./styles"
import { R } from "../../res"
import { Button, AdjustText } from "../shared"
import Svg, { Polyline, Line, G, Path } from "react-native-svg"
import { isTablet } from "react-native-device-info"
import { getItem, storeItem } from "../../services/storage"
import _ from "lodash"

const KEY_ACTIONS = "actions"

interface IScreenAProps {
  counter: number
  clickButton: () => {}
}

type IMainState = IEmpty

enum ButtonType {
  FOLLOW_TIME = "follow_time",
  INTERSECTIONS = "intersections",
  PEDESTRIANS = "pedestrians",
  PARKED_CARS = "parkedCars",
  EYE_LEAD = "eye_lead",
  LEFT_MIRROR = "left_mirror",
  RIGHT_MIRROR = "right_mirror",
  GAUGES = "gauges",
}

type Point = {
  x: number
  y: number
}

type Layout = {
  x: number
  y: number
  height: number
  width: number
}

export const Main = memo(forwardRef((props: IMainState, ref) => {
  useImperativeHandle(
    ref,
    () => ({
      storeData() {
        // console.log('eye actions', JSON.stringify(actionsArray.current))
        // storeItem(KEY_ACTIONS, JSON.stringify(actionsArray.current))
        return actionsArray.current
      },
      loadData(actions) {
        try {
          console.log('actions', actions)
          lastClicked.current = undefined
          linesArray.current = []
          actionsArray.current = []
          // JSON.parse(actions ?? "[]").map((action) => onButtonClicked(action))
          // actions.map((action) => onButtonClicked(action))
          actions.forEach((action, index) => {
            // setTimeout(() => {
            onButtonClicked(action)
            // }, 100 * index);
          });
        } catch (err) {
          console.log('error loading ', err)
        }


      }

    }),
  )
  const rootRef = useRef<View>(null)
  const middleViewRef = useRef<View>(null)

  const lastClicked = useRef<ButtonType | undefined>(undefined)
  const actionsArray = useRef<Array<ButtonType>>([])
  const linesArray = useRef<Array<JSX.Element>>([])

  const headerHieight = useRef(0)
  const middleStartX = useRef(0)
  const followTimeLayout = useRef<Layout | undefined>(undefined)
  const intersectionsLayout = useRef<Layout | undefined>(undefined)
  const leftMirrorLayout = useRef<Layout | undefined>(undefined)
  const rightMirrorLayout = useRef<Layout | undefined>(undefined)
  const gaugesLayout = useRef<Layout | undefined>(undefined)
  const eyeLeadLayout = useRef<Layout | undefined>(undefined)
  const pedestriansLayout = useRef<Layout | undefined>(undefined)
  const parkedCarsLayout = useRef<Layout | undefined>(undefined)

  const [total, setTotal] = useState(0)
  // const [totalFront, setTotalFront] = useState(0)
  // const [totalRear, setTotalRear] = useState(0)


  const getMiddlePoint = (layout: Layout | undefined): Point | undefined => {
    if (layout == undefined) return undefined
    const midX = layout.x + layout.width / 2 - middleStartX.current
    const midY = layout.y + layout.height / 2 - headerHieight.current
    return { x: midX, y: midY }
  }

  const getLayout = (button: ButtonType | undefined): Layout | undefined => {
    switch (button) {
      case ButtonType.FOLLOW_TIME:
        return followTimeLayout.current
      case ButtonType.INTERSECTIONS:
        return intersectionsLayout.current
      case ButtonType.LEFT_MIRROR:
        return leftMirrorLayout.current
      case ButtonType.RIGHT_MIRROR:
        return rightMirrorLayout.current
      case ButtonType.GAUGES:
        return gaugesLayout.current
      case ButtonType.EYE_LEAD:
        return eyeLeadLayout.current
      case ButtonType.PEDESTRIANS:
        return pedestriansLayout.current
      case ButtonType.PARKED_CARS:
        return parkedCarsLayout.current
      default:
        return undefined
    }
  }

  const getRotation = (firstPoint: Point, secondPoint: Point, angel: number): number => {
    if (firstPoint.x < secondPoint.x && firstPoint.y == secondPoint.y)
      // R
      return 270
    else if (firstPoint.x > secondPoint.x && firstPoint.y == secondPoint.y)
      // L
      return 90
    else if (firstPoint.x == secondPoint.x && firstPoint.y < secondPoint.y)
      // U
      return 0
    else if (firstPoint.x == secondPoint.x && firstPoint.y > secondPoint.y)
      // D
      return 180
    else if (firstPoint.x < secondPoint.x && firstPoint.y > secondPoint.y)
      // RU
      return 270 - angel
    else if (firstPoint.x < secondPoint.x && firstPoint.y < secondPoint.y)
      // RD
      return 270 + angel
    else if (firstPoint.x > secondPoint.x && firstPoint.y > secondPoint.y)
      // LU
      return 90 + angel
    else return 90 - angel
  }

  const drawArrow = (firstPoint: Point, secondPoint: Point, angel: number, color: string) => {
    const distance = Math.sqrt(
      Math.pow(firstPoint.x - secondPoint.x, 2) + Math.pow(firstPoint.y - secondPoint.y, 2)
    )
    const deltaX = (Math.cos(angel * (Math.PI / 180)) * distance) / 2
    const deltaY = (Math.sin(angel * (Math.PI / 180)) * distance) / 2

    let originX = 0
    let originY = 0

    if (firstPoint.x > secondPoint.x) originX = firstPoint.x - deltaX
    else if (firstPoint.x < secondPoint.x) originX = secondPoint.x - deltaX
    else originX = firstPoint.x

    if (firstPoint.y > secondPoint.y) originY = firstPoint.y - deltaY
    else if (firstPoint.y < secondPoint.y) originY = secondPoint.y - deltaY
    else originY = firstPoint.y

    const margin = isTablet() ? 16 : 8
    return (
      <Polyline
        points={`${originX},${originY} ${originX + margin},${originY -
          margin} ${originX},${originY} ${originX - margin},${originY -
          margin} ${originX},${originY}`}
        fill="none"
        stroke={color}
        strokeWidth={`${isTablet() ? 4 : 2}`}
        origin={`${originX},${originY}`}
        rotation={`${getRotation(firstPoint, secondPoint, angel)}`}
      />
    )
  }

  const getColor = (firstBtn: ButtonType, secondBtn: ButtonType): string => {
    let color = "blue"
    if (
      (firstBtn == ButtonType.LEFT_MIRROR ||
        firstBtn == ButtonType.RIGHT_MIRROR ||
        firstBtn == ButtonType.GAUGES) &&
      (secondBtn == ButtonType.LEFT_MIRROR ||
        secondBtn == ButtonType.RIGHT_MIRROR ||
        secondBtn == ButtonType.GAUGES)
    ) {
      color = "red"
    }

    return color
  }

  const drawLine = (first: ButtonType | undefined, second: ButtonType) => {
    const firstMidPoint = getMiddlePoint(getLayout(first))
    const secondMidPoint = getMiddlePoint(getLayout(second))

    if (firstMidPoint != undefined && secondMidPoint != undefined) {
      const angel =
        (Math.atan2(
          Math.abs(secondMidPoint.y - firstMidPoint.y),
          Math.abs(secondMidPoint.x - firstMidPoint.x)
        ) *
          180) /
        Math.PI

      const color = getColor(first!!, second)

      linesArray.current.push(
        <Svg style={{ position: "absolute" }}>
          {drawArrow(firstMidPoint, secondMidPoint, angel, color)}
          <Line
            x1={`${firstMidPoint.x}`}
            y1={`${firstMidPoint.y}`}
            x2={`${secondMidPoint.x}`}
            y2={`${secondMidPoint.y}`}
            stroke={color}
            strokeWidth={`${isTablet() ? 4 : 2}`}
          />
        </Svg>
      )
    }
  }

  const onButtonClicked = (currentClicked: ButtonType) => {
    actionsArray.current.push(currentClicked)
    if (currentClicked != lastClicked.current) {
      drawLine(lastClicked.current, currentClicked)
      lastClicked.current = currentClicked
    }
    //HACK: it refreshed the screen after line draw, but it is not reliable as counter
    setTimeout(() => {
      setTotal(total + 1)
    }, 50);
    props.onUpdate(actionsArray.current)
  }

  // const store = () => {
  //   console.log('eye actions', JSON.stringify(actionsArray.current))
  //   // storeItem(KEY_ACTIONS, JSON.stringify(actionsArray.current))
  // }

  // const load = () => {
  //   getItem(KEY_ACTIONS).then((s) => {
  //     lastClicked.current = undefined
  //     linesArray.current = []
  //     actionsArray.current = []
  //     JSON.parse(s ?? "[]").map((action) => onButtonClicked(action))
  //   })
  // }

  return (
    <View style={{ flex: 1, }}>
      <View
        ref={rootRef}
        style={styles.container}
        onLayout={({ nativeEvent }) => {
          let handle = findNodeHandle(rootRef.current) ?? 0
          UIManager.measure(handle, (x, y, width, height, pageX, pageY) => {
            headerHieight.current = pageY
          })
        }}>
        <View style={styles.leftContainer}>
          <View style={{ flex: 1 }}>
            <Button
              color={R.colors.Blue}
              label={R.strings.Main.followTime}
              onPress={() => {
                onButtonClicked(ButtonType.FOLLOW_TIME)
              }}
            />
          </View>
          <View style={{ flex: 1 }}>
            <Button
              color={R.colors.Red}
              label={R.strings.Main.intersections}
              onPress={() => {
                onButtonClicked(ButtonType.INTERSECTIONS)
              }}
            />
          </View>
          <View style={{ flex: 1, paddingTop: 40 }}>
            <Button
              color={R.colors.Black}
              label={R.strings.Main.leftMirror}
              onPress={() => {
                onButtonClicked(ButtonType.LEFT_MIRROR)
              }}
            />
          </View>
          <View style={{ flex: 1, }}>
            <Button
              color={R.colors.Orange}
              label={R.strings.Main.gauges}
              onPress={() => {
                onButtonClicked(ButtonType.GAUGES)
              }}
            />
          </View>
        </View>
        <View
          ref={middleViewRef}
          style={styles.middleContainer}
          onLayout={({ nativeEvent }) => {
            let handle = findNodeHandle(middleViewRef.current) ?? 0
            UIManager.measure(handle, (x, y, width, height, pageX, pageY) => {
              middleStartX.current = pageX
            })
          }}>
          {linesArray.current.map((line) => (
            <>{line}</>
          ))}
          <View style={styles.upperContainer}>
            <View style={styles.firstUpperColumn}>
              <Button
                disabled
                counter={_.countBy(actionsArray.current)[ButtonType.FOLLOW_TIME] ?? 0}
                color={R.colors.Blue}
                label={R.strings.Main.followTime}
                onLayout={(layout) => {
                  followTimeLayout.current = layout
                }}
              />
            </View>
            <View style={styles.secondUpperColumn}>
              <View style={{ flex: 1 }} />
              <View style={{ flex: 1 }}>
                <Button
                  disabled
                  counter={_.countBy(actionsArray.current)[ButtonType.INTERSECTIONS] ?? 0}
                  color={R.colors.Red}
                  label={R.strings.Main.intersections}
                  onLayout={(layout) => {
                    intersectionsLayout.current = layout
                  }}
                />
              </View>
            </View>
            <View style={styles.thirdUpperColumn}>
              <View style={{ flex: 1 }} />
              <View style={{ flex: 1, paddingTop: 24, alignItems: "center" }}>
                <Image
                  resizeMode={"stretch"}
                  style={{ flex: 1, marginBottom: 8 }}
                  source={R.images.upperArrow}
                />
                <AdjustText
                  color={R.colors.Black}
                  fontSize={18}
                  numberOfLines={1}
                  text={R.strings.Main.front}
                />
              </View>
            </View>
            <View style={styles.forthUpperColumn}>
              <View style={{ flex: 1 }} />
              <View style={{ flex: 1, justifyContent: "space-between" }}>
                <Button
                  disabled
                  counter={_.countBy(actionsArray.current)[ButtonType.PEDESTRIANS] ?? 0}
                  color={R.colors.Green}
                  label={R.strings.Main.pedestrians}
                  onLayout={(layout) => {
                    pedestriansLayout.current = layout
                  }}
                />
                <View />
                <Button
                  disabled
                  counter={_.countBy(actionsArray.current)[ButtonType.PARKED_CARS] ?? 0}
                  color={R.colors.Green}
                  label={R.strings.Main.parkedCars}
                  onLayout={(layout) => {
                    parkedCarsLayout.current = layout
                  }}
                />
                <View />
              </View>
            </View>
            <View style={styles.fifthUpperColumn}>
              <Button
                disabled
                counter={_.countBy(actionsArray.current)[ButtonType.EYE_LEAD] ?? 0}
                color={R.colors.Blue}
                label={R.strings.Main.eyeLead}
                onLayout={(layout) => {
                  eyeLeadLayout.current = layout
                }}
              />
            </View>
          </View>
          <View style={styles.horizontalLine} />
          <View style={styles.lowerContainer}>
            <View style={styles.firstLowerColumn}>
              <Button
                disabled
                counter={_.countBy(actionsArray.current)[ButtonType.LEFT_MIRROR] ?? 0}
                color={R.colors.Black}
                label={R.strings.Main.leftMirror}
                onLayout={(layout) => {
                  leftMirrorLayout.current = layout
                }}
              />
              <AdjustText
                color={R.colors.Black}
                fontSize={14}
                numberOfLines={1}
                text={`Front ${(_.countBy(actionsArray.current)[ButtonType.FOLLOW_TIME] ?? 0) + (_.countBy(actionsArray.current)[ButtonType.INTERSECTIONS] ?? 0) + (_.countBy(actionsArray.current)[ButtonType.PEDESTRIANS] ?? 0) + (_.countBy(actionsArray.current)[ButtonType.PARKED_CARS] ?? 0) + (_.countBy(actionsArray.current)[ButtonType.EYE_LEAD] ?? 0)}`}
              />
            </View>
            <View style={styles.secondLowerColumn}>
              <View style={{ flex: 1, paddingBottom: 24, alignItems: "center" }}>
                <AdjustText
                  color={R.colors.Black}
                  fontSize={18}
                  numberOfLines={1}
                  text={R.strings.Main.rear}
                />
                <Image
                  resizeMode={"stretch"}
                  style={{ flex: 1, marginTop: 8 }}
                  source={R.images.lowerArrow}
                />
              </View>
              <View style={{ flex: 1, justifyContent: "flex-end" }}>
                <Button
                  disabled
                  counter={_.countBy(actionsArray.current)[ButtonType.GAUGES] ?? 0}
                  containerStyle={{ alignSelf: "center" }}
                  color={R.colors.Orange}
                  label={R.strings.Main.gauges}
                  onLayout={(layout) => {
                    gaugesLayout.current = layout
                  }}
                />
              </View>
            </View>
            <View style={styles.thirdLowerColumn}>
              <Button
                disabled
                counter={_.countBy(actionsArray.current)[ButtonType.RIGHT_MIRROR] ?? 0}
                color={R.colors.Black}
                label={R.strings.Main.rightMirror}
                onLayout={(layout) => {
                  rightMirrorLayout.current = layout
                }}
              />
              <AdjustText
                color={R.colors.Black}
                fontSize={14}
                numberOfLines={1}
                text={`Rear ${(_.countBy(actionsArray.current)[ButtonType.LEFT_MIRROR] ?? 0) + (_.countBy(actionsArray.current)[ButtonType.RIGHT_MIRROR] ?? 0) + (_.countBy(actionsArray.current)[ButtonType.GAUGES] ?? 0)}`}
              />
            </View>
          </View>
        </View>
        <View style={styles.rightContainer}>
          <View style={{ flex: 1 }}>
            <Button
              color={R.colors.Blue}
              label={R.strings.Main.eyeLead}
              onPress={() => {
                onButtonClicked(ButtonType.EYE_LEAD)
              }}
            />
          </View>
          <View style={{ flex: 1, justifyContent: "space-between" }}>
            <Button
              color={R.colors.Green}
              label={R.strings.Main.pedestrians}
              onPress={() => {
                onButtonClicked(ButtonType.PEDESTRIANS)
              }}
            />
            <Button
              containerStyle={{ marginBottom: 24 }}
              color={R.colors.Green}
              label={R.strings.Main.parkedCars}
              onPress={() => {
                onButtonClicked(ButtonType.PARKED_CARS)
              }}
            />
          </View>
          <View style={{ flex: 2, paddingTop: 40 }}>
            <Button
              color={R.colors.Black}
              label={R.strings.Main.rightMirror}
              onPress={() => {
                onButtonClicked(ButtonType.RIGHT_MIRROR)
              }}
            />
          </View>
        </View>
      </View>
      {/* <View
        style={{
          flexDirection: "row",
          justifyContent: "space-between",
          marginHorizontal: 24,
          marginBottom: 24,
        }}>
        <Button color={R.colors.Black} label={R.strings.Main.store} onPress={store} />
        <Button color={R.colors.Black} label={R.strings.Main.load} onPress={load} />
      </View> */}
    </View>
  )
}))
