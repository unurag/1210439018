import React, { useState } from 'react';
import { Flex, Button, Stack } from '@chakra-ui/react';
import ViewAll from './ViewAll';
import ViewWithId from './ViewWithId';

const ViewAllProducts = () => {
  return <ViewAll />;
};

const ViewProductsWithID = () => {
  return <ViewWithId />;
};

const Home = () => {
  const [view, setView] = useState('home');

  const renderComponent = () => {
    switch (view) {
      case 'viewAll':
        return <ViewAllProducts />;
      case 'viewByID':
        return <ViewProductsWithID />;
      default:
        return (
          <Flex
            w="100vw"
            h="100vh"
            bg="turquoise"
            justify="center"
            align="center"
          >
            <Stack direction="row" spacing={4} align="center">
              <Button colorScheme="teal" variant="solid" onClick={() => setView('viewAll')}>
                View all Products
              </Button>
              <Button colorScheme="teal" variant="outline" onClick={() => setView('viewByID')}>
                View Products with ID
              </Button>
            </Stack>
          </Flex>
        );
    }
  };

  return renderComponent();
};

export default Home;
