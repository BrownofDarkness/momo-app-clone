import { Button, StyleSheet, Text, View } from 'react-native'
import React from 'react'

const Login = ({navigation,route}) => {
    // console.log(route.params.isAuthenticated);
  return (
    <View style={styles.screen}>
      <Text>Login Authenticated</Text>
      {/*<Button title='Back' onPress={()=>navigation.navigate('Home')}/>*/}
    </View>
  )
}

export default Login

const styles = StyleSheet.create({
    screen:{
        flex:1,
    }
})