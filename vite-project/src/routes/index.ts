import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';

// Import your pages here
import Home from '../pages/Home';
import About from '../pages/About';

const AppRoutes = () => {
  // this is a placeholder comment to indicate component structure
  // Add other page routes here as needed

  return (
    <Router>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/about' element={<About />} />
      </Routes>
    </Router>
  );
};

export default AppRoutes;