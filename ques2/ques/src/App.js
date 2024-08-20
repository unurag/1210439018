import * as React from 'react'
import { ChakraProvider } from '@chakra-ui/react'
import Home from './Components/Home'


// using chakra ui library
// https://v2.chakra-ui.com/getting-started
export default function App() {
  return (
    <ChakraProvider>
      <Home />
    </ChakraProvider>
  )
}