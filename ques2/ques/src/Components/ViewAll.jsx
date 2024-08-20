import { Flex } from '@chakra-ui/react'
import React, {useEffect, useState} from 'react'

const ViewAll = () => {

    const [productData, setProductData] = useState()

    useEffect(() => {
        fetch('http://127.0.0.1:5000/categories/Laptop/products?n=5&min_price=30&max_price=4000&page=1&sort=None&order=None&company=AMZ').then(response => response.json()).then(data => {
          setProductData(data)
        })
      
      }, [])

  return (
    <Flex
        w='100vw'
        h='100vh'
        bg='gray.100'
    >
            
    </Flex>
  )
}

export default ViewAll